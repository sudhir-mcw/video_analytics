if [ -z "$1" ]
    then
    ./build/yolov8_ort 50 ./input/test_video_2.mp4
else
    
    ./build/yolov8_ort $1 $2
fi
