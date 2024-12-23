from GetVideoLinks import getVideoLinks
import os
import requests
import yt_dlp
import multiprocessing

download_folder = "L:/SignLanguageData"
os.makedirs(download_folder, exist_ok=True)

def getVideos(url, fileName):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }
    try:
        response = requests.get(url ,headers=headers, stream=True)
        if response.status_code == 200:
            with open(fileName , "wb") as file:
                file.write(response.content)
            print(f"Downloaded: {fileName}")
        else:
            print(f"Failed to download {url}")
    except Exception as e:
        print("Ho gaya kaand   " , url , e)


def getYTVideos(url, fileName):
    try:
        ydl_opts = {
            'format': 'bestvideo',  
            'outtmpl': f'{fileName}.%(ext)s', 
            'noplaylist': True,  
            # 'merge_output_format': 'mp4', 
            'quiet': True,  
            'headers': {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
            }
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
            print(f"Downloaded: {fileName}.mp4")
    except Exception as e:
        print(f"Error downloading YouTube video {url}: {e}")

def process_video(word, url, idx):
    word_folder = download_folder +"/"+word
    os.makedirs(os.path.join(download_folder,f"{word}") , exist_ok=True)
    fileName = os.path.join(word_folder, f"{idx}.mp4")  

    if "youtube.com" in url:
        getYTVideos(url, fileName)
    else:
        getVideos(url, fileName)


if __name__ == "__main__":
    all_urls = getVideoLinks()
    pool = multiprocessing.Pool(processes=multiprocessing.cpu_count())
    for word in all_urls.keys():
        print(f"Processing videos for: {word}")
        pool.starmap(process_video, [(word, url, idx) for idx, url in enumerate(all_urls[word])])  
    pool.close()
    pool.join()