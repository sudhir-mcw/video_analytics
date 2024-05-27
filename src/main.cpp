



#include <regex>
#include <iostream>
#include <opencv2/opencv.hpp>
#include <filesystem>
#include <ctime>


#include <sys/time.h>
#include <sys/resource.h>


#include "streamline_annotate.h"
#include "utils.h"
#include "yolov8Predictor.h"





int main(int argc, char *argv[]) {
  gator_annotate_setup();
  float confThreshold = 0.4f;
    float iouThreshold = 0.4f;

    float maskThreshold = 0.5f;

    
    bool isGPU    = false;

    const std::string modelPath      = "./models/yolov8n-face-lindevs.onnx";


   
    if (!std::filesystem::exists(modelPath))
    {
        return -1;
    }
   

    YOLOPredictor predictor{nullptr};
    try
    {
        predictor = YOLOPredictor(modelPath, isGPU,
                                  confThreshold,
                                  iouThreshold,
                                  maskThreshold);
    }
    catch (const std::exception &e)
    {
        std::cerr << "unable to load model " << e.what() << std::endl;
        return -1;
    }
 
    assert(argc==2);
    
  

    cv::VideoCapture cap("./Input/test_video_2.mp4");

    if (!cap.isOpened())
    {
        std::cerr << "Error: Cannot open video." << std::endl;
        return -1;
    }
    cv::Mat frame; 
    int frame_count = 0;
    int MAX_FRAMES= std::stoi(argv[1]);
    while (true)
    {
        // printf("frame count : %d\n",frame_count);

        if(frame_count>=MAX_FRAMES){
            printf("No fo frames computed : %d\n",frame_count);
            break;
        }
        
        cap >> frame;
        if (frame.empty())
        {
            std::cerr << "Error: Cannot get frame." << std::endl;
            break;
        }
        try
        {
            cv::Mat image = frame.clone();
            std::vector<Yolov8Result> result = predictor.predict(image);
           
        }
        catch (const std::exception &e)
        {
            std::cerr << e.what() << std::endl;
            break;
        }
        frame_count+=1;
        
    }
 
    cap.release();
  return 1;
}


