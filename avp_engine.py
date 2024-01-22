#            __      ___       __          ___ 
#  /\  \  / |__)    |__  |\ | / _` | |\ | |__  
# /--\  \/  |       |___ | \| \__> | | \| |___ 
#                                                 

# Automated Video Production Engine
# Bao Bui-Quang


NUM_OF_TRACKS = 15
VIDEO_FPS     = 24


# ============================== LIBRARIES IMPORT ==============================
from moviepy.editor import *
import random
import shutil
import os

# ============================== DIRECTORY SETUP ==============================

dir_image = "assets/image/"
dir_audio = "assets/audio/"
dir_output = "assets/output/"
dir_used_image = "assets/image_used/"

assets_image = os.listdir(dir_image)
assets_audio = os.listdir(dir_audio)

# ============================== RESOURCES PICK ==============================

# image_path  = "image.png"
# audio_paths = ["audio1.mp3", "audio2.mp3", "audio3.mp3"]
image_path  = random.sample(assets_image, 1)[0]          # 🎲
audio_paths = random.sample(assets_audio, NUM_OF_TRACKS) # 🎲

# ============================== VIDEO GENERATION ==============================

# Preprocess
image_path = dir_image + image_path
audio_paths = [dir_audio + e for e in audio_paths]

# Image
image = ImageClip(image_path)

# Audio
order = list(range(len(audio_paths)))
random.shuffle(order) # 🎲
audios = []
for i in range(len(audio_paths)):
    audios.append(AudioFileClip(audio_paths[order[i]]))
audio = concatenate_audioclips(audios)

# SFX
audio = audio.audio_fadein(2.5)
audio = audio.audio_fadeout(5.0)

# Video
output_path = dir_output + "V_" + image_path[:-4].split('/')[-1] + "_" + "{:05d}".format(random.randint(0, 99999)) + ".mp4"
video = image.set_duration(audio.duration)
video = video.set_audio(audio)

# VFX
video = video.fadein(5.0)
video = video.fadeout(5.0)

# Export
print("================== EXPORTING ==================")
video.write_videofile(output_path, fps=VIDEO_FPS, codec="libx264", audio_codec="aac")
# Archive the used image
shutil.move(image_path, dir_used_image)

# ============================== INFORMATION DISPLAY ==============================

# Info
print("================= INFORMATION =================")
print("-------------------- IMAGE --------------------")
print(f"Image: {image_path.split('/')[-1]}")
print("-------------------- AUDIO --------------------")
print(f"Audios order: {order}")
for i in range(len(audio_paths)):
    print(f"{audio_paths[order[i]].split('/')[-1]} ({audios[i].duration}s)")
print("-------------------- VIDEO --------------------")
print(f"Video: {output_path.split('/')[-1]}")
print(f"Length: {round(audio.duration)}s ({round(audio.duration // 60)}:{'{:02d}'.format(round(audio.duration % 60))})")

print("================= DESCRIPTION =================")
# txtf = open("assets/output/test.txt","w+") # test
txtf = open(output_path[:-4]+".txt","w+")
timestamp = 0.0
for i in range(len(audio_paths)):
    print(f"{'{:02d}'.format(round(timestamp // 60))}:{'{:02d}'.format(round(timestamp % 60))} {audio_paths[order[i]].split('/')[-1][:-4]}")
    txtf.write(f"{'{:02d}'.format(round(timestamp // 60))}:{'{:02d}'.format(round(timestamp % 60))} {audio_paths[order[i]].split('/')[-1][:-4]}\n")
    timestamp += audios[i].duration
txtf.close()