cmake_minimum_required(VERSION 3.0.0)
project(yolov8_ort)

find_package(OpenCV REQUIRED)
find_package(Threads)
include_directories("include/")

add_executable(yolov8_ort
               src/utils.cpp
               src/yolov8_predictor.cpp
               src/main.cpp)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_CXX_FLAGS_RELEASE "-g")

target_include_directories(yolov8_ort PRIVATE ${CMAKE_SOURCE_DIR}/onnxruntime-linux-aarch64-1.18.0/include)
target_compile_features(yolov8_ort PRIVATE cxx_std_17)
target_link_libraries(yolov8_ort  ${CMAKE_SOURCE_DIR}/onnxruntime-linux-aarch64-1.18.0/lib/libonnxruntime.so  ${OpenCV_LIBS} pthread)
