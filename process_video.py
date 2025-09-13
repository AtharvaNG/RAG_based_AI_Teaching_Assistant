#Converts the videos to mp3

import os
import subprocess
files=os.listdir("videos")

for file in files:
    tutorial_name=file.split("｜")[0]
    tutorial_number=file.split("#")[1].split(" [")[0]
    print(tutorial_number,tutorial_name)
    
    subprocess.run(["ffmpeg","-i",f"videos/{file}",f"audios/{tutorial_number}_{tutorial_name}.mp3"])