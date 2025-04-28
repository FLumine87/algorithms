#include "rclcpp/rclcpp.hpp"
#include "sensor_msgs/msg/image.hpp"
#include "cv_bridge/cv_bridge.h"
#include <opencv2/opencv.hpp>
#include <atomic>
#include <chrono>
#include <string>

using std::placeholders::_1;

class ImgNode_s : public rclcpp::Node
{
public:
    ImgNode_s(std::string name) : Node(name)
    {
        sub_novel = this->create_subscription<sensor_msgs::msg::Image>(
            "image_topic", 10, 
            std::bind(&ImgNode_s::topic_callback, this, _1));
    }
private:
    rclcpp::Subscription<sensor_msgs::msg::Image>::SharedPtr sub_novel;
    std::atomic<int> count = 1;

    void topic_callback(const sensor_msgs::msg::Image::SharedPtr msg)
    {
        // 将 ROS 2 的 Image 消息转换为 OpenCV 的 Mat
        cv::Mat image_d = cv_bridge::toCvCopy(msg, "bgr8")->image;
        RCLCPP_INFO(this->get_logger(), "binary image.Counts: %d",count++);

        // 显示图片
        cv::imshow("binary Image", image_d);
        cv::waitKey(3000);
        cv::destroyWindow("binary Image");
    } 
};

int main(int argc, char **argv)
{
    rclcpp::init(argc, argv);
    auto node = std::make_shared<ImgNode_s>("node2");
    RCLCPP_INFO(node->get_logger(),"Node2 is running");
    rclcpp::spin(node);
    rclcpp::shutdown();
    return 0;
}