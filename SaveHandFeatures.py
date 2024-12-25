import os
import cv2
import mediapipe as mp
import pickle
import logging
from absl import logging as abslLog

abslLog.set_verbosity(logging.ERROR)
logging.getLogger("mediapipe").setLevel(logging.ERROR)
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'  # For suppressing the warning and INFO messages 

mp_hands = mp.solutions.hands
hands = mp_hands.Hands(static_image_mode=False, max_num_hands=2, min_detection_confidence=0.5)


def process_video(video_path):
    cap = cv2.VideoCapture(video_path)
    print(f"Processing for Video: {video_path}")
    frame_features = []
    frame_count = 0
    while True:
        ret, frame = cap.read()
        if not ret:
            break

        frame_count += 1
        if frame_count % 5 == 0 :
            print(f"frame count : {frame_count}")
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        result = hands.process(rgb_frame)

        if result.multi_hand_landmarks:
            for hand_landmarks in result.multi_hand_landmarks:
                landmarks = [[lm.x, lm.y, lm.z] for lm in hand_landmarks.landmark]
                frame_features.append(landmarks)
    
    cap.release()
    return frame_features


if __name__ == "__main__":
    print("Started the prog")
    main_folder = "L:/SignLanguageData"
    all_data = []
    all_labels = []
    
    folder_paths = [os.path.join(main_folder, folder) for folder in os.listdir(main_folder) if os.path.isdir(os.path.join(main_folder, folder))]
        
    for folder_path in folder_paths:
        label = os.path.basename(folder_path)  
        for video_file in os.listdir(folder_path):
            if video_file.endswith(".mp4"):
                video_path = os.path.join(folder_path, video_file)
                features = process_video(video_path)
                if features:
                    all_data.append(features)
                    all_labels.append(label)
    
    with open("hand_features.pkl", "wb") as f:
        pickle.dump((all_data, all_labels), f)

    print("Data preprocessing complete. Features saved to 'hand_features.pkl'")
