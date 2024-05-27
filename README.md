

**C++ YOLOv8 ONNXRuntime** inference code for *Object Detection* 






## Prequisites:
- OpenCV 4
- ONNXRuntime 
- Perfetto 
- CMake version 3.13+
- Make version 4.2.1+





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

- Download the perfetto binaries from the github repo 
```
    mkdir perfetto 
    cd perfetto 
    wget https://github.com/google/perfetto/releases/download/v45.0/linux-arm64.zip
    unzip linux-arm64.zip
    cd linux-arm64
    chmod +x *
    
```

# Build and Run in Linux

- Clone the repo and switch to cpp_perfetto
```
    git clone https://github.com/sudhir-mcw/face-analytics-pipeline.git
    cd face-analytics-pipeline
    git checkout cpp_perfetto
```
- Build the project using 
```
    sh build.sh
``` 

- To run the project 
open three terminal  and follow the steps in individual windows,
Navigate to previosly extracted linux-arm64/ folder in all the terminals
Example 
```
cd face-analytics-pipeline/perfetto/linux-arm64
```
Terminal 1 
```
sudo ./tracebox traced
```
Terminal 2 
```
sudo ./traced_probes
```
Terminal 3
```
sudo ./tracebox perfetto -c <path_to_config_file> --txt -o trace_file 
```
Here path to config is root_of_the_project/system_wide_trace_cfg.pbtxt \
Example Usage
```
sudo ./tracebox perfetto -c ../../system_wide_trace_cfg.pbtxt --txt -o ../output/trace_file 
``` 
Once you see enabled ftrace in the Terminal 2 window run the command
Terminal 4 
```
   cd face-analytics-pipeline
   sudo  sh run.sh <no_of_frames> 
```
Example: to limit the no of frames from the video 
```
   sudo sh run.sh 50 
```

Note: Inorder to collect the trace for 100 frames increase the duration in system_wide_trace_cfg.pbtxt file from  to 10000  ms or more

Once the trace is completed run the following in Terminal 3 in location face-analytics-pipeline/perfetto/linux-arm64
```
sudo ./traceconv json ../../output/trace_file ../../output/trace_file.json
``` 
The command will generate a json file from the trace file obtained which can be viewed in https://ui.perfetto.dev

Run the measure_trace.py with trace_file.json location as argument

```
python3 measure_trace.py ./output/trace_file.json 
```





