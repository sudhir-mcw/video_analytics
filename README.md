

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


## Installation
- Install OpenCV in system using the following command 
```
   sudo apt update
   sudo apt install libopencv-dev cmake make g++
```
- To download streamline UI, visit armDeveloper tools repository website (https://artifacts.tools.arm.com/arm-performance-studio/2024.0) and download the ARM Perfomance Studio 2024.0 which matches the host system OS and install it. 
For linux download use the link (https://artifacts.tools.arm.com/arm-performance-studio/2024.0/Arm_Performance_Studio_2024.0_linux_x86-64.tgz)

# Build 
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
./build-linux.sh 
```
Note: If the  installed version of ARM perfomance studio is 2024.1, copy the **gator** folder from host machine to the target and place it inside root of the project and build it using the steps given above, the gator folder can be found  in <path_to_ArmPerfomanceStudio_installation_directory>/streamline 

Build the libstreamline_annotate.so files
```
cd gator/annotate
make 
```
The above command will create a build-native-gcc-rel folder with **gatord** binaries.
- Build the project using 
```
    sh build.sh
``` 
# Run in Single Core 
Run the gator agent using any one method 1 or 2 in terminal 1 
*  Method 1: Remote capture via tcp on host machine \
Setup remote target machine in which the target device will stream data back to host machine which has streamline agent \
**Terminal 1**
```
    cd gator/build-native-gcc-rel/
    sudo ./gatord -S yes -a -p 5050
```
*  Method 2 Local capture on target machine \
Target Local capture which stores the capture to a folder in the target machine
```
    cd gator/build-native-gcc-rel/
    sudo ./gatord -S yes -o  <path_to_capture_folder.apc>
```
Example:\
`
sudo ./gatord -S yes -o ../capture.apc
`

Note : While running on local capture use ctrl+c to exit the capture and capture files to be dumped 

* **Terminal 2** 
```
    taskset -c <core_number> ./build/yolov8_ort <no_of_frames> <input_video_path> 
```
Example: to run the application for 100 frames on  core 0
```
    taskset -c 0 ./build/yolov8_ort 100 ./input/test_video_2.mp4
```
# Run in Multiple Cores
* Repeat the steps for running gator agent as mentioned in **Run in Single Core**
* **Terminal 2** 
```
    taskset -c <core_number>,<core_number>  ./build/yolov8_ort <no_of_frames> <input_video_path> 
```
Example: To run the application for 100 frames on  core 0 and 1
```
    taskset -c 0,1 ./build/yolov8_ort 100 ./input/test_video_2.mp4
```
# Report Generation
* To generate report on host machine 
```
    <path_to_ARMPerfomanceStudio_install_director>/streamline/bin/<os>/streamline -report -per_core --log --timeline <path_to_capture_folder.apc> -o <output_dir> 
```
Example:
`
<path_to_ARMPerfomanceStudio_install_director>/streamline/bin/<os>/streamline -report -per_core --log --timeline capture.apc -o capture 
` \ 
Note: The streamline cli launcher can be used to open terminal within the streamline folder, 
1. If local capture Method 2 was used to capture copy the files from remote target machine to host and generate report
2. If remote  capture Method 1 was used, the captured folder is usually found in ~/Documents/Streamline folder

# Analyze

Modify the start_core and  end_core value in analyze.py before running modify the script start_core, end_core based on the no of cores specified  for runnning the pipeline with taskset  
1. If the code ran with single  core i.e core number  0 set start_core and end_core to 0 
2. If the code ran with multiple cores i.e core numbers 0,1,2,3 set the start_core to 0 and end_core to 3

Move the <output_dir> to the root of the project and run the command
```    
    python analyze.py <output_dir>
```
Example:\
`
python analyze.py capture
`


