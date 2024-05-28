

**C++ YOLOv8 ONNXRuntime** inference code for *Object Detection* 


## Prequisites:
- OpenCV 4
- ONNXRuntime 



## Installation
- Install OpenCV in system using the following command 
```
   sudo apt update
   sudo apt install libopencv-dev 
```

-  Download the model file and save it in models/ folder if not present already.
```
wget https://github.com/lindevs/yolov8-face/releases/latest/download/yolov8n-face-lindevs.onnx
mv yolov8n-face-lindevs.onnx models
```

Download the onnxruntime from the releases or use the command inside source of the repo 
```
wget https://github.com/microsoft/onnxruntime/releases/download/v1.18.0/onnxruntime-linux-aarch64-1.18.0.tgz

tar -xvf onnxruntime-linux-aarch64-1.18.0.tgz
```

# Build and Run in Linux

- Clone the repo 
```
    git clone https://github.com/sudhir-mcw/video_analytics.git
    cd video_analytics
```
- Build the project using 
```
    sh build.sh
``` 
- To run the project use
```
    rm output.log
    sh run.sh <no_of_frames> 
```
Example: to limit the no of frames from the video 
```
    sh run.sh 100 
```
