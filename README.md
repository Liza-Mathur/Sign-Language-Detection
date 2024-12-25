# Sign-Language-Detection
This repo contains my sign language detection project

# About Files - 
1. CheckingMediaPipe.py - 
  - Run the file and it will open a window which captures live camera and shows tracks and features on your hands even when they move. 
  - My observation - Mediapipe does not track very fast hand movements nicely. But its fine for my code for now. 
2. DeleteExtraFiles.py - 
  - This file is used to clean the data I am using.
  - After downloading data I observed few videos (maximum 1 or 2) in all the folders had video with more than 1 word's sign.
  - To delete that I used its patter. If video is more than 30 seconds long that means it has more than 1 word sign and it should be delted.
3. DownloadVideos.py - 
  - This was the actual file I ran for downloading my data in correct format. 
  - This takes all the words and their URLs as dict from GetVideoLinks.py and download the videos is correct folder structure.
  - I used yt-dlp library to download youtube videos and normal requests and response libraries to download videos from other sites.
  - You can download yt-dlp just by pip install yt-dlp command. 
4. GetVideoLinks.py -
  - This file reads my main data file - WLASL_v0.3.json which I got from Kaggle
  - It reads and stores only words and their URLs in a dict called as all_urls and returns all_urls in its method. 
5. SaveHandFeatures.py - 
  - This file has script which uses mediapipe to track the hand movements in each video.
  - It tracks hand features (21 hand features) per frame [25 frames per second for each video].
  - It stores hand features and file name with its path in pkl file - hand_features.pkl
  - I have removed logging from this file because the logging was making it hard for me to read the output in console.

# Few things - 
- I downloaded data on local storage becuase keras use folder structure for image processing and video processing
- Downloading data took around 4-5 hours to download all the videos
- Currently SaveHandFeatures.py is running. My estimation - Its gonna take around 19-20 hours to finish running.