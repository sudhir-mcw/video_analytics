if [ -z "$1" ]
    then
    ./build/yolov8_ort 50
else
    ./build/yolov8_ort $1
fi




