// #include "rclcpp/rclcpp.hpp"
// #include "std_msgs/msg/string.hpp"
// #include "std_msgs/msg/u_int32.hpp"
#include "rclcpp/rclcpp.hpp"
#include "sensor_msgs/msg/image.hpp"
#include "cv_bridge/cv_bridge.h"
#include <opencv2/opencv.hpp>

#include "armor_detector/armor.hpp"

#include <chrono>
#include <string>
#include <vector>

// #include <opencv2/core.hpp>
// #include <opencv2/core/base.hpp>
// #include <opencv2/highgui.hpp>
// #include <opencv2/imgcodecs.hpp>

// class Light {
//     public:
//         // 构造函数
//         Light(const cv::Rect &b_rect, const cv::Point2f &top, const cv::Point2f &bottom, 
//               int point_count, double tilt_angle)
//             : bounding_rect(b_rect), top(top), bottom(bottom), 
//               point_count(point_count), tilt_angle(tilt_angle), color(UNKNOWN) {
//             // 计算中心点
//             center = cv::Point2f(
//                 (top.x + bottom.x) / 2.0,
//                 (top.y + bottom.y) / 2.0
//             );
//             // 计算灯条的长度和宽度
//             length = cv::norm(top - bottom);
//             width = static_cast<float>(b_rect.width);
//         }
    
//         // 灯条颜色枚举
//         enum Color {
//             UNKNOWN,
//             RED,
//             BLUE
//         };
    
//         // 成员变量
//         cv::Rect bounding_rect;  // 最小外接矩形
//         cv::Point2f top;         // 灯条顶部坐标
//         cv::Point2f bottom;      // 灯条底部坐标
//         cv::Point2f center;      // 灯条中心点
//         float length;            // 灯条长度
//         float width;             // 灯条宽度
//         int point_count;         // 灯条内部像素点数量
//         double tilt_angle;       // 灯条倾斜角度
//         Color color;             // 灯条颜色
// };


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
    double min_fill_ratio = 0.5;
    double min_ratio=0.001;
    double max_ratio=0.750;

private:
    void publish_image(){
        // // 读取图片

        b_img = preprocessImage(gbr_img);
        // 转换为 ROS 2 的 Image 消息
        // auto msg = cv_bridge::CvImage(std_msgs::msg::Header(), "mono8", b_img).toImageMsg();
        // publisher_i->publish(*msg);

        //test
        // cv::imshow("binary Image", b_img);
        // cv::waitKey(3000);
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
            bool is_fill_rotated_rect =
                points.size() / (r_rect.size.width * r_rect.size.height) > min_fill_ratio;
            if(!is_fill_rotated_rect)continue;

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

            rm_auto_aim::Light light = Light(b_rect, top, bottom, points.size(), angle_k);

            auto isLight=[&]()->bool{
                // The ratio of light (short side / long side)
                float ratio = light.width / light.length;
                bool ratio_ok = min_ratio < ratio && ratio < max_ratio;
                // bool angle_ok = light.tilt_angle < max_angle;
                bool is_light = ratio_ok ; //&& angle_ok
              
                // // Fill in debug information
                // auto_aim_interfaces::msg::DebugLight light_data;
                // light_data.center_x = light.center.x;
                // light_data.ratio = ratio;
                // light_data.angle = light.tilt_angle;
                // light_data.is_light = is_light;
                // this->debug_lights.data.emplace_back(light_data);
              
                return is_light;
            };

            if (isLight(light)) {
                vector<rm_auto_aim::Light> rect = light;
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
                                sum_r += roi.at<cv::Vec3b>(i, j)[0];
                                sum_b += roi.at<cv::Vec3b>(i, j)[2];
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

    void prit_lights(){
        for (size_t i = 0; i < lights.size(); ++i) {
            const auto& light = lights[i];
            RCLCPP_INFO(this->get_logger(), "Light %zu:", i + 1);
            RCLCPP_INFO(this->get_logger(), "  Top: (%f, %f)", light.top.x, light.top.y);
            RCLCPP_INFO(this->get_logger(), "  Bottom: (%f, %f)", light.bottom.x, light.bottom.y);
            RCLCPP_INFO(this->get_logger(), "  Center: (%f, %f)", light.center.x, light.center.y);
            RCLCPP_INFO(this->get_logger(), "  Length: %f", light.length);
            RCLCPP_INFO(this->get_logger(), "  Width: %f", light.width);
            RCLCPP_INFO(this->get_logger(), "  Tilt Angle: %f", light.tilt_angle);
            RCLCPP_INFO(this->get_logger(), "  Color: %s", 
                light.color == rm_auto_aim::Light::Color::RED ? "RED" : 
                light.color == rm_auto_aim::Light::Color::BLUE ? "BLUE" : "UNKNOWN");
        }

        std::string input;
        do {
            std::cout << "输入 'y' 后继续: ";
            std::cin >> input;
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