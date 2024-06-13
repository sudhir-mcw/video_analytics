**C++ YOLOv8 ONNXRuntime** inference code for *Object Detection* 

## Prequisites:
- OpenCV 4
- ONNXRuntime 
- cmake 
- make
- g++ 

## Installation
- Install OpenCV in system using the following command 
```
   sudo apt update
   sudo apt install libopencv-dev cmake make g++
```
# Build and Run in Linux

- Clone the repo 
```
    git clone https://github.com/sudhir-mcw/video_analytics.git
    cd video_analytics
```
-  Download the model file and save it in models/ folder within the repo if not present already.
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
- To run the project use
```
    sh run.sh <no_of_frames> 
```
Example: to limit the no of frames from the video 
```
    sh run.sh 100 
```
* To limit the number of cores while running use taskset utility
```
    taskset -c <core>,<core> ./build/yolov8_ort <no_of_frames>
```
Example: to run the application on core 0 and 1
```
    taskset -c 0,1 ./build/yolov8_ort 50
```
