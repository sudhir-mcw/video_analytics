
cmake_minimum_required(VERSION 3.13)
project(yolov8_ort)
set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

find_package(Threads)
find_package(OpenCV REQUIRED)
include_directories(sdk)
include_directories(include)
include_directories(${CMAKE_SOURCE_DIR}/gator/annotate)

add_executable(yolov8_ort
               src/utils.cpp
               src/yolov8Predictor.cpp
               src/main.cpp
               )
               
set(CMAKE_CXX_FLAGS_RELEASE "-O3")
target_include_directories(yolov8_ort PRIVATE ${CMAKE_SOURCE_DIR}/onnxruntime-linux-aarch64-1.18.0/include)
target_compile_features(yolov8_ort PRIVATE cxx_std_17)
target_link_libraries(yolov8_ort ${CMAKE_SOURCE_DIR}/onnxruntime-linux-aarch64-1.18.0/lib/libonnxruntime.so ${CMAKE_SOURCE_DIR}/gator/annotate/libstreamline_annotate.so  ${OpenCV_LIBS} pthread)

