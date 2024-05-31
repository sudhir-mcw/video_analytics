

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
- To download streamline UI, visit armDeveloper website (https://developer.arm.com/Tools%20and%20Software/Streamline%20Performance%20Analyzer) and download the ARM Perfomance Studio 2024.0 which matches the host system OS and install it. 
For linux download use the link (https://artifacts.tools.arm.com/arm-performance-studio/2024.0/Arm_Performance_Studio_2024.0_linux_x86-64.tgz)

# Build and Run in Linux
- Clone the repo and switch to cpp_streamline
```
    git clone https://github.com/sudhir-mcw/video_analytics.git
    cd  video_analytics
    git checkout cpp_streamline
```
-  Download the model file and save it in models/ folder if not present already.
```
wget https://github.com/lindevs/yolov8-face/releases/latest/download/yolov8n-face-lindevs.onnx
mkdir models
mv yolov8n-face-lindevs.onnx models
```
Download the onnxruntime from the releases or use the command inside source of the repo 
```
cd video_analytics
wget https://github.com/microsoft/onnxruntime/releases/download/v1.18.0/onnxruntime-linux-aarch64-1.18.0.tgz
tar -xvf onnxruntime-linux-aarch64-1.18.0.tgz
```
- Download the streamline gator agent and build the linux gator agent
```
cd  video_analytics
git clone https://github.com/ARM-software/gator.git
cd gator
chmod +x ./build-linux.sh
./build-linux.sh -l off
```
Followed by that build the libstreamline_annotate.so files
```
cd gator/annotate
make 
```
The above command will create a build-native-gcc-rel folder with **gatord** binaries.
- Build the project using 
```
    sh build.sh
``` 
- To run the project  
Run the gator agent using any one method 1 or 2 in terminal 1 
*  Setup remote target machine in which the target device will stream data back to host machine which has streamline agent
```
    cd gator/build-native-gcc-rel/
    sudo ./gatord -S yes -a -p 5050
```
*  Setup on target capture which stores the capture to a folder
```
    cd gator/build-native-gcc-rel/
    sudo ./gatord -S yes -o  ../capture.apc
```
Note : While running on local capture use ctrl+c to exit the capture and capture files to be dumped 

* Run the application in terminal 2
```
    sh run <no_of_frames>
```
Example: to limit the no of frames from the video 
```
    sh run.sh 50 
```
* Run the analyzation
```
    <path_to_streamline>/bin/<os>/streamline -report -per_core --all capture.apc -o output_dir 
```
Note: The streamline cli can be used to open terminal within the streamline folder 

Move the output_dir to the root of the project and run the command
```    
    python analyze.py output_dir
```
