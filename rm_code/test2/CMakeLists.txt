cmake_minimum_required(VERSION 3.8)
project(test2)

if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
  add_compile_options(-Wall -Wextra -Wpedantic)
endif()

# find dependencies
find_package(ament_cmake REQUIRED)
find_package(rclcpp REQUIRED)
find_package(rclpy REQUIRED)
find_package(std_msgs REQUIRED)

find_package(OpenCV REQUIRED)

find_package(image_transport REQUIRED)
find_package(cv_bridge REQUIRED)

if(BUILD_TESTING)
  find_package(ament_lint_auto REQUIRED)
  # the following line skips the linter which checks for copyrights
  # comment the line when a copyright and license is added to all source files
  set(ament_cmake_copyright_FOUND TRUE)
  # the following line skips cpplint (only works in a git repo)
  # comment the line when this package is in a git repo and when
  # a copyright and license is added to all source files
  set(ament_cmake_cpplint_FOUND TRUE)
  ament_lint_auto_find_test_dependencies()
endif()

ament_package()

add_executable(node1 src/node_p.cpp)
ament_target_dependencies(node1
  rclcpp
  sensor_msgs
  image_transport
  cv_bridge
  OpenCV
)
target_include_directories(node1 PUBLIC ${OpenCV_INCLUDE_DIRS})
target_link_libraries(node1 ${OpenCV_LIBRARIES})

add_executable(node2 src/node_s.cpp)
ament_target_dependencies(node2
  rclcpp
  sensor_msgs
  image_transport
  cv_bridge
  OpenCV
)
target_include_directories(node2 PUBLIC ${OpenCV_INCLUDE_DIRS})
target_link_libraries(node2 ${OpenCV_LIBRARIES})

add_executable(nodet src/test.cpp)
ament_target_dependencies(nodet
  rclcpp
  sensor_msgs
  image_transport
  cv_bridge
  OpenCV
)
target_include_directories(nodet PUBLIC ${OpenCV_INCLUDE_DIRS})
target_link_libraries(nodet ${OpenCV_LIBRARIES})

add_executable(nodet2 src/test2.cpp)
ament_target_dependencies(nodet2
  rclcpp
  sensor_msgs
  image_transport
  cv_bridge
  OpenCV
)
target_include_directories(nodet2 PUBLIC 
  ${OpenCV_INCLUDE_DIRS}
  ${CMAKE_CURRENT_SOURCE_DIR}/include
)
target_link_libraries(nodet2 ${OpenCV_LIBRARIES})

install(TARGETS
  node1
  node2
  nodet
  nodet2
  DESTINATION lib/${PROJECT_NAME}
)