import time
import youtube_dl as yt_dlp
import argparse
from pytube import YouTube 
import os

def convert(link, name):
    URLS = [str(link)]
    ydl_opts = {
        'format': 'm4a/bestaudio/best',
        'outtmpl': str(name)+'.%(ext)s',
        'postprocessors': [{  # Extract audio using ffmpeg
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3'
        }]
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        error_code = ydl.download(URLS)

def convert_video():
    # where to save 
    SAVE_PATH = r"C:\Users\plytn\Downloads\YTConverter"

    # link of the video to be downloaded 
    link = "https://www.youtube.com/watch?v=kJQP7kiw5Fk"

    try: 
        # object creation using YouTube 
        yt = YouTube(link) 
    except: 
        #to handle exception 
        print("Connection Error") 

    # Get all streams and filter for mp4 files
    mp4_streams = yt.streams.filter(file_extension='mp4').all()

    # get the video with the highest resolution
    d_video = mp4_streams[-1]

    try: 
        # downloading the video 
        d_video.download(output_path=SAVE_PATH)
        print('Video downloaded successfully!')
    except: 
        print("Some Error!")

def convert_audio(link):
    # where to save 
    SAVE_PATH = r"C:\Users\plytn\Downloads\YTConverter"
    SAVE_PATH = os.path.join(SAVE_PATH, str(count_folders(SAVE_PATH)))
    try:
        yt = YouTube(link) 
    except: 
        print("Connection Error")
    audio_streams = yt.streams.filter(only_audio=True).first()
    try: 
        # downloading the audio stream
        out_file = audio_streams.download(output_path=SAVE_PATH)
  
        # save the file 
        base, ext = os.path.splitext(out_file) 
        new_file = base + '.mp3'
        os.rename(out_file, new_file) 

        print('Audio downloaded successfully!')
    except Exception as e: 
        
        print("Some Error!: ", e)
    # print(new_file)
    return new_file
    

def count_folders(path):
    return len([f for f in os.listdir(path) if os.path.isdir(os.path.join(path, f))])


if __name__ == '__main__':
    # name = input("Enter the name of the file: ")
    # link = input("Enter the link of the video: ")
    # convert(link, name)
    convert_audio("https://www.youtube.comx/watch?v=kJQP7kiw5Fk")
