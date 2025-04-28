// #include "rclcpp/rclcpp.hpp"
// #include "std_msgs/msg/string.hpp"
// #include "std_msgs/msg/u_int32.hpp"
#include "rclcpp/rclcpp.hpp"
#include "sensor_msgs/msg/image.hpp"
#include "cv_bridge/cv_bridge.h"
#include <opencv2/opencv.hpp>

#include <chrono>
#include <string>

// #include <opencv2/core.hpp>
// #include <opencv2/core/base.hpp>
// #include <opencv2/highgui.hpp>
// #include <opencv2/imgcodecs.hpp>

class ImgNode: public rclcpp::Node
{
public:
    ImgNode(std::string name) : Node(name)
    {
        // 创建一个 image_transport 发布者
        publisher_i = this->create_publisher<sensor_msgs::msg::Image>("image_topic", 10);

        // 定时器，每秒发布一次图片
        timer_i = this->create_wall_timer(
            std::chrono::seconds(5),
            std::bind(&ImgNode::publish_image, this));

        // 读取图片
        gbr_img = cv::imread("/home/flumine/ROS2_test/ws1/src/test2/image/test_image.jpg", cv::IMREAD_COLOR);
        if (gbr_img.empty())
        {
            RCLCPP_ERROR(this->get_logger(), "Failed to read image");
            rclcpp::shutdown();
        }
        // cv::imshow("RGB Image", gbr_img);
        // cv::waitKey(0);
        // cv::destroyAllWindows();
    }

    cv::Mat gbr_img;
    cv::Mat b_img;

private:
    void publish_image()
    {
        // // 读取图片

        b_img = preprocessImage(gbr_img);
        // 转换为 ROS 2 的 Image 消息
        // auto msg = cv_bridge::CvImage(std_msgs::msg::Header(), "bgr8", b_img).toImageMsg();
        // publisher_i->publish(*msg);

        //test
        // cv::imshow("binary Image", b_img);
        // cv::waitKey(3000);
        // cv::destroyWindow("binary Image");

        RCLCPP_INFO(this->get_logger(), "Published an image");
    }

    // cv::Mat preprocessImage(const cv::Mat & rgb_img)
    // {
    //   cv::Mat gray_img;
    //   cv::cvtColor(rgb_img, gray_img, cv::COLOR_RGB2GRAY);
    
    //   cv::Mat binary_img;
    //   cv::threshold(gray_img, binary_img, 55, 255, cv::THRESH_BINARY);
    
    //   return binary_img;
    // }

    //用颜色进行初步筛
    cv::Mat preprocessImage(const cv::Mat & rgb_img)
    {
        // 转换到HSV颜色空间
        cv::Mat hsvImage;
        cv::cvtColor(rgb_img, hsvImage, cv::COLOR_BGR2HSV);
    
        // 定义红色的两个HSV区间
        cv::Mat lower_red1 = (cv::Mat_<uchar>(1, 3) << 0, 100, 100);
        cv::Mat upper_red1 = (cv::Mat_<uchar>(1, 3) << 10, 255, 255);
        cv::Mat lower_red2 = (cv::Mat_<uchar>(1, 3) << 160, 100, 100);
        cv::Mat upper_red2 = (cv::Mat_<uchar>(1, 3) << 180, 255, 255);
    
        // 创建掩码
        cv::Mat mask1, mask2, redMask;
        inRange(hsvImage, lower_red1, upper_red1, mask1);
        inRange(hsvImage, lower_red2, upper_red2, mask2);
        bitwise_or(mask1, mask2, redMask);

        cv::imshow("binary Image", redMask);
        cv::waitKey(3000);
        cv::destroyWindow("binary Image");
    
    //   cv::Mat binary_img;
    //   cv::threshold(gray_img, binary_img, 55, 255, cv::THRESH_BINARY);
    
      return rgb_img;
    }

    rclcpp::Publisher<sensor_msgs::msg::Image>::SharedPtr publisher_i;
    rclcpp::TimerBase::SharedPtr timer_i;
};

int main(int argc, char **argv)
{
    rclcpp::init(argc, argv);
    auto node = std::make_shared<ImgNode>("image_node");
    RCLCPP_INFO(node->get_logger(), "Image Node is running");
    // gbr_img = cv::imread("/home/flumine/ROS2_test/ws1/src/test2/image/test_image.jpg", cv::IMREAD_COLOR);
    // if (gbr_img.empty())
    // {
    //     RCLCPP_ERROR(node->get_logger(), "Failed to read image");
    //     return -1;
    // }
    // cv::imshow("RGB Image", gbr_img);
    // cv::waitKey(0);
    // cv::destroyAllWindows();
    rclcpp::spin(node);
    rclcpp::shutdown();
    return 0;

}