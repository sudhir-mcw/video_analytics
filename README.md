**C++ YOLOv8 ONNXRuntime** inference code for *Face Detection* 
## Machine Requirements:
- Processor Architecture: ARM64
- RAM: Minimum 8GB
- OS: Ubuntu 20.04 
- Storage: Minimum 64GB

## Prequisites:
- OpenCV 4
- ONNXRuntime 
- cmake 
- make
- g++ 

## OpenCV Installation
- Install OpenCV in system using the following command 
```
   sudo apt update
   sudo apt install libopencv-dev cmake make g++
```
# Build 
- Clone the repo 
```
    git clone https://github.com/sudhir-mcw/video_analytics.git
    cd video_analytics
    git checkout main
```
-  Download the model file and save it in models/ folder within the repo if not present already
```
cd video_analytics
wget https://github.com/lindevs/yolov8-face/releases/latest/download/yolov8n-face-lindevs.onnx
mkdir models
mv yolov8n-face-lindevs.onnx models
```
Download the onnxruntime from the releases or use the command inside the repo 
```
cd video_analytics
wget https://github.com/microsoft/onnxruntime/releases/download/v1.18.0/onnxruntime-linux-aarch64-1.18.0.tgz
tar -xvf onnxruntime-linux-aarch64-1.18.0.tgz
```
- Build the project using 
```
    sh build.sh
``` 
# Run in Single Core
-  To limit the number of cores while running use taskset utility
```
    taskset -c <core> ./build/yolov8_ort <no_of_frames> <input_video_path>
```
- Example: to run the application on core 0 \
`
    taskset -c 0 ./build/yolov8_ort 50 ./input/test_video_2.mp4
`
# Run in Multiple  Cores
- To limit the number of cores while running use taskset utility
```
    taskset -c <core>,<core> ./build/yolov8_ort <no_of_frames> <input_video_path>
```
- Example: to run the application for 50 frames on core 0 and 1 \
`
    taskset -c 0,1 ./build/yolov8_ort 50 ./input/test_video_2.mp4
`