#ifndef TEST2_ARMOR_HPP_
#define TEST2_ARMOR_HPP_

#include <opencv2/core.hpp>

// STL
#include <algorithm>
#include <string>

namespace rm_auto_aim
{
// const int RED = 0;
// const int BLUE = 1;

// enum class ArmorType { SMALL, LARGE, INVALID };
// const std::string ARMOR_TYPE_STR[3] = {"small", "large", "invalid"};

enum class Color {
  UNKNOWN,
  RED,
  BLUE
};

enum class ArmorType { 
  SMALL, 
  LARGE, 
  INVALID 
};

struct Light : public cv::Rect
{
  Light() = default;
  explicit Light(cv::Rect box, cv::Point2f top, cv::Point2f bottom, int area, float tilt_angle)
  : cv::Rect(box), top(top), bottom(bottom), tilt_angle(tilt_angle)
  {
    length = cv::norm(top - bottom);
    width = area / length;
    center = (top + bottom) / 2;
  }

  Color color;
  cv::Point2f top, bottom;
  cv::Point2f center;
  double length;
  double width;
  float tilt_angle;
  // int area;
};

struct Armor
{
  Armor() = default;
  Armor(const Light & l1, const Light & l2)
  {
    if (l1.center.x < l2.center.x) {
      left_light = l1, right_light = l2;
    } else {
      left_light = l2, right_light = l1;
    }
    center = (left_light.center + right_light.center) / 2;
  }

  // Light pairs part
  Light left_light, right_light;
  cv::Point2f center;
  ArmorType type;

  // Number part
  cv::Mat number_img;
  std::string number;
  float confidence;
  std::string classfication_result;
};
}

#endif  // ARMOR_DETECTOR__ARMOR_HPP_