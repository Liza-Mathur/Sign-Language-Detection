import os
import cv2

DEFAULT_FPS = 25

def check_video_duration(video_path):

    cap = cv2.VideoCapture(video_path)

    total_frames = cap.get(cv2.CAP_PROP_FRAME_COUNT)

    duration = total_frames / DEFAULT_FPS

    cap.release()

    return duration

def delete_long_videos(folder_path, max_duration=30):
    for subfolder in os.listdir(folder_path):
        subfolder_path = os.path.join(folder_path, subfolder)
        
        if os.path.isdir(subfolder_path):
            print(f"Checking folder: {subfolder_path}")
            
            for file_name in os.listdir(subfolder_path):
                file_path = os.path.join(subfolder_path, file_name)
                
                if file_name.endswith(".mp4"):
                    duration = check_video_duration(file_path)
                    print(f"Video: {file_name}, Duration: {duration:.2f} seconds")

                    if duration > max_duration:
                        os.remove(file_path)
                        print(f"Deleted {file_name} (Duration: {duration:.2f} seconds)")

if __name__ == "__main__":
    folder_path = "L:/SignLanguageData"
    delete_long_videos(folder_path)
