// #include "rclcpp/rclcpp.hpp"
// #include "std_msgs/msg/string.hpp"
// #include "std_msgs/msg/u_int32.hpp"
#include "rclcpp/rclcpp.hpp"
#include "sensor_msgs/msg/image.hpp"
#include "cv_bridge/cv_bridge.h"
#include <opencv2/opencv.hpp>

#include "test2/armor.hpp"

#include <chrono>
#include <string>
#include <vector>

// #include <opencv2/core.hpp>
// #include <opencv2/core/base.hpp>
// #include <opencv2/highgui.hpp>
// #include <opencv2/imgcodecs.hpp>


class ImgNode: public rclcpp::Node
{
public:
    ImgNode(std::string name) : Node(name){
        // 创建一个 image_transport 发布者
        publisher_i = this->create_publisher<sensor_msgs::msg::Image>("image_topic", 10);

        // 定时器，每秒发布一次图片
        timer_i = this->create_wall_timer(
            std::chrono::seconds(3),
            std::bind(&ImgNode::publish_image, this));

        // 读取图片
        gbr_img = cv::imread("/home/flumine/ROS2_test/ws1/src/test2/image/test_image4.jpg", cv::IMREAD_COLOR);
        if (gbr_img.empty())
        {
            RCLCPP_ERROR(this->get_logger(), "Failed to read image");
            rclcpp::shutdown();
        }
    }

    std::vector<rm_auto_aim::Light> lights;
    cv::Mat gbr_img;
    cv::Mat b_img;

    //静态参数
    int binary_thres = 26;
    double min_fill_ratio = 0.65;
    double max_fill_ratio = 0.90;
    double min_ratio=0.075;
    double max_ratio=0.250;
    double max_angle=10.0;
    
    //绝对参数
    // double min_fill_ratio = 0.82;
    // double max_fill_ratio = 0.84;
    // double min_ratio=0.150;
    // double max_ratio=0.175;
    //double max_angle=4.0;

private:
    void publish_image(){
        // // 读取图片

        b_img = preprocessImage(gbr_img);
        // 转换为 ROS 2 的 Image 消息
        // auto msg = cv_bridge::CvImage(std_msgs::msg::Header(), "mono8", b_img).toImageMsg();
        // publisher_i->publish(*msg);

        //test
        // cv::imshow("binary Image", b_img);
        // cv::waitKey(0);
        // cv::destroyWindow("binary Image");

        lights = findLights(gbr_img, b_img);

        prit_lights();

        RCLCPP_INFO(this->get_logger(), "Published an image");
    }

    cv::Mat preprocessImage(const cv::Mat & rgb_img){
        cv::Mat gray_img;
        cv::cvtColor(rgb_img, gray_img, cv::COLOR_RGB2GRAY);
    
        cv::Mat binary_img;
        cv::threshold(gray_img, binary_img, binary_thres , 255, cv::THRESH_BINARY);
    
        return binary_img;
    }

    std::vector<rm_auto_aim::Light> findLights(const cv::Mat & rgb_img, const cv::Mat & binary_img){
        using std::vector;
        //初步拟合轮廓
        vector<vector<cv::Point>> contours;
        vector<cv::Vec4i> hierarchy;
        cv::findContours(binary_img, contours, hierarchy, cv::RETR_EXTERNAL, cv::CHAIN_APPROX_SIMPLE);

        vector<rm_auto_aim::Light> lights;
        for (const auto & contour : contours) {
            if (contour.size() < 5) continue;//这5不知道要不要修改

            auto b_rect = cv::boundingRect(contour);
            auto r_rect = cv::minAreaRect(contour);
            cv::Mat mask = cv::Mat::zeros(b_rect.size(), CV_8UC1);
            std::vector<cv::Point> mask_contour;
            for (const auto & p : contour) {
                mask_contour.emplace_back(p - cv::Point(b_rect.x, b_rect.y));
            }
            cv::fillPoly(mask, {mask_contour}, 255);//这里右边会出现一个小白条，还不清楚是什么原因
            std::vector<cv::Point> points;
            cv::findNonZero(mask, points);

            auto is_fill_rotated_rect =[&]()->bool{
                float fill_ratio = points.size() / (r_rect.size.width * r_rect.size.height);
                return (fill_ratio > min_fill_ratio && fill_ratio < max_fill_ratio);
            };

            if(!is_fill_rotated_rect())continue;

            cv::Vec4f return_param;
            cv::fitLine(points, return_param, cv::DIST_L2, 0, 0.01, 0.01);
            cv::Point2f top, bottom;
            double angle_k;
            if (int(return_param[0] * 100) == 100 || int(return_param[1] * 100) == 0) { 
                top = cv::Point2f(b_rect.x + b_rect.width / 2, b_rect.y);
                bottom = cv::Point2f(b_rect.x + b_rect.width / 2, b_rect.y + b_rect.height);
                angle_k = 0;
            } else {
                auto k = return_param[1] / return_param[0];
                auto b = (return_param[3] + b_rect.y) - k * (return_param[2] + b_rect.x);
                top = cv::Point2f((b_rect.y - b) / k, b_rect.y);
                bottom = cv::Point2f((b_rect.y + b_rect.height - b) / k, b_rect.y + b_rect.height);
                angle_k = std::atan(k) / CV_PI * 180 - 90;
                if (angle_k > 90) {
                    angle_k = 180 - angle_k;
                }
            }

            rm_auto_aim::Light light = rm_auto_aim::Light(b_rect, top, bottom, points.size(), angle_k);

            auto isLight=[&]()->bool{
                // The ratio of light (short side / long side)
                float ratio = light.width / light.length;
                bool ratio_ok = min_ratio < ratio && ratio < max_ratio;
                bool angle_ok = (max_angle - light.tilt_angle > 180 || max_angle + light.tilt_angle > 0);
                bool is_light = ratio_ok && angle_ok; 
              
                // // Fill in debug information
                // auto_aim_interfaces::msg::DebugLight light_data;
                // light_data.center_x = light.center.x;
                // light_data.ratio = ratio;
                // light_data.angle = light.tilt_angle;
                // light_data.is_light = is_light;
                // this->debug_lights.data.emplace_back(light_data);
              
                return is_light;
            };

            if (isLight()) {
                rm_auto_aim::Light rect = light;
                if (  // Avoid assertion failed
                    0 <= rect.x && 0 <= rect.width && rect.x + rect.width <= rgb_img.cols && 0 <= rect.y &&
                    0 <= rect.height && rect.y + rect.height <= rgb_img.rows) {
                    int sum_r = 0, sum_b = 0;
                    auto roi = rgb_img(rect);
                    // Iterate through the ROI
                    for (int i = 0; i < roi.rows; i++) {
                        for (int j = 0; j < roi.cols; j++) {
                            if (cv::pointPolygonTest(contour, cv::Point2f(j + rect.x, i + rect.y), false) >= 0) {
                                // if point is inside contour
                                sum_r += roi.at<cv::Vec3b>(i, j)[2];
                                sum_b += roi.at<cv::Vec3b>(i, j)[0];
                            }
                        }
                    }
                // Sum of red pixels > sum of blue pixels ?
                light.color = sum_r > sum_b ? rm_auto_aim::Light::Color::RED : rm_auto_aim::Light::Color::BLUE;
                lights.emplace_back(light);
                }
            }
        }

        //test
        // cv::imshow("binary Image", image_d);
        // cv::waitKey(3000);
        // cv::destroyWindow("binary Image");
        return lights;
    }

    void prit_lights() {
        // 创建一个副本以避免修改原始图像
        cv::Mat display_img;
        cv::cvtColor(b_img, display_img, cv::COLOR_GRAY2BGR);
    
        for (size_t i = 0; i < lights.size(); ++i) {
            const auto& light = lights[i];
    
            // 打印灯条信息
            RCLCPP_INFO(this->get_logger(), "Light %zu:", i + 1);
            // RCLCPP_INFO(this->get_logger(), "  Top: (%f, %f)", light.top.x, light.top.y);
            // RCLCPP_INFO(this->get_logger(), "  Bottom: (%f, %f)", light.bottom.x, light.bottom.y);
            RCLCPP_INFO(this->get_logger(), "  Center: (%f, %f)", light.center.x, light.center.y);
            RCLCPP_INFO(this->get_logger(), "  Length: %f", light.length);
            RCLCPP_INFO(this->get_logger(), "  Width: %f", light.width);
            RCLCPP_INFO(this->get_logger(), "  Tilt Angle: %f", light.tilt_angle);
            RCLCPP_INFO(this->get_logger(), "  Color: %s", 
                light.color == rm_auto_aim::Light::Color::RED ? "RED" : 
                light.color == rm_auto_aim::Light::Color::BLUE ? "BLUE" : "UNKNOWN");
            RCLCPP_INFO(this->get_logger(), "  bizhi: %f", light.width / light.length);
            // RCLCPP_INFO(this->get_logger(), "  fill_ratio: %f", static_cast<float>(light.area) / (light.width * light.length));//算不出来
    
            // 绘制外接矩形
            if (light.color == rm_auto_aim::Light::Color::RED) {
                cv::rectangle(display_img, light, cv::Scalar(0, 0, 255), 2); // 红色矩形，线宽为 2
            }else{
                cv::rectangle(display_img, light, cv::Scalar(255, 0, 0), 2); // 蓝色矩形，线宽为 2
            }

            // 绘制拟合直线（直接使用 top 和 bottom）
            cv::line(display_img, light.top, light.bottom, cv::Scalar(0, 255, 0), 2);
        }
    
        // 显示带有外接矩形的图像
        cv::imshow("Lights Bounding Rectangles", display_img);
        cv::waitKey(0); // 等待用户按键
        cv::destroyWindow("Lights Bounding Rectangles");
    
        // 用户交互
        std::string input;
        do {
            std::cout << "输入 'y' 后继续，输入 'n' 退出程序: ";
            std::cin >> input;
            if (input == "n") {
                RCLCPP_INFO(this->get_logger(), "Terminating program...");
                rclcpp::shutdown();  // 停止 ROS 2 节点
                return;
            }
        } while (input != "y");
    }

    rclcpp::Publisher<sensor_msgs::msg::Image>::SharedPtr publisher_i;
    rclcpp::TimerBase::SharedPtr timer_i;

};

int main(int argc, char **argv){
    rclcpp::init(argc, argv);
    auto node = std::make_shared<ImgNode>("image_node");
    RCLCPP_INFO(node->get_logger(), "Image Node is running");
    rclcpp::spin(node);
    rclcpp::shutdown();
    return 0;

}