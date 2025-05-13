#ifndef ARMOR_DETECTOR__ARMOR_HPP_
#define ARMOR_DETECTOR__ARMOR_HPP_

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

struct Light : public cv::Rect
{
  enum class Color {
    UNKNOWN,
    RED,
    BLUE
  };
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
}

#endif  // ARMOR_DETECTOR__ARMOR_HPP_