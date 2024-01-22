# #            __      ___       __          ___ 
# #  /\  \  / |__)    |__  |\ | / _` | |\ | |__  
# # /--\  \/  |       |___ | \| \__> | | \| |___ 
# #                                                 

# # Automated Short Video Production Engine
# # Bao Bui-Quang

# ============================== LIBRARIES IMPORT ==============================
from moviepy.editor import *
import random
import shutil
import os

# ============================== DIRECTORY SETUP ==============================

dir_visual = "assets/video_for_visual/"
dir_audio = "assets/video_for_audio/"
dir_output = "assets/output/"

assets_audio = os.listdir(dir_audio)
assets_visual_group = os.listdir(dir_visual)
assets_visual = []
for g in assets_visual_group:
    dir_g = dir_visual + g
    assets_visual.append([g + '/' + e for e in os.listdir(dir_g)])




for audio_file in assets_audio:

    # ============================== RESOURCES PICK ==============================
    video_files_1 = []
    video_files_2 = []
    for v in assets_visual:
        r = random.sample(v, 2) # 🎲
        video_files_1.append(r[0])
        video_files_2.append(r[1])
    video_files_1_A = [item for item in video_files_1 if not item.startswith('7')]     # Just a filter that don't add the video from unwanted folder
    video_files_2_A = [item for item in video_files_2 if item.startswith('5')]         # Just a filter that don't add the video from unwanted folder
    video_files_2_B = [item for item in video_files_2 if not item.startswith('5')]     # Just a filter that don't add the video from unwanted folder
    random.shuffle(video_files_1_A) # 🎲
    random.shuffle(video_files_2_A) # 🎲
    random.shuffle(video_files_2_B) # 🎲
    video_files = video_files_1_A + video_files_2_A + video_files_2_B
    # print(video_files)
    video_files = [dir_visual + e for e in video_files]

    # audio_file = random.sample(assets_audio, 1)[0] # 🎲
    # print(audio_file)
    audio_name_in_output = audio_file
    audio_file = dir_audio + audio_file

    # ============================== VIDEO GENERATION ==============================

    # Audio of video
    audio_clip = AudioFileClip(audio_file)

    # Visual of video
    video_clips = []
    for video_file in video_files:
        video_clip = VideoFileClip(video_file)
        video_clip = video_clip.set_audio(None)
        video_clips.append(video_clip)

    # Final Video
    final_video = concatenate_videoclips(video_clips, method="compose")
    final_video = final_video.set_audio(audio_clip)
    final_video = final_video.set_duration(audio_clip.duration - 1.0)

    # Extra: Fade out audio effect
    final_video = final_video.audio_fadeout(1.0)

    # ============================== EXPORT 0 ==============================

    output_file = audio_name_in_output[16:-4] + '_ALTER.mp4'
    output_file = dir_output + output_file

    # Export
    final_video.write_videofile(output_file, codec="libx264", audio_codec="aac")

    # # ============================== EXPORT 1 ==============================

    # output_file = audio_name_in_output[16:-4] + '-A.mp4'
    # output_file = dir_output + output_file

    # # Extra: Watermark
    # watermark_text = "@bryanverlice"
    # font = "assets/font/BaiJamjuree-Medium.ttf"
    # font_size = 40
    # font_color = "#555555"
    # margin_top = 1496

    # text_clip = TextClip(watermark_text, fontsize=font_size, font=font, color=font_color)
    # text_position = (video_clip.size[0] / 2 - text_clip.size[0] / 2, margin_top)
    # text_clip = text_clip.set_duration(final_video.duration)
    # text_clip = text_clip.set_position(text_position)
    # final_video_1 = CompositeVideoClip([final_video, text_clip])

    # # Export
    # final_video_1.write_videofile(output_file, codec="libx264", audio_codec="aac")

    # # ============================== EXPORT 2 ==============================

    # output_file = audio_name_in_output[16:-4] + '-B.mp4'
    # output_file = dir_output + output_file

    # # Extra: Watermark
    # watermark_text = "@dailylifeofbao"
    # font = "assets/font/BaiJamjuree-Medium.ttf"
    # font_size = 40
    # font_color = "#555555"
    # margin_top = 1496

    # text_clip = TextClip(watermark_text, fontsize=font_size, font=font, color=font_color)
    # text_position = (video_clip.size[0] / 2 - text_clip.size[0] / 2, margin_top)
    # text_clip = text_clip.set_duration(final_video.duration)
    # text_clip = text_clip.set_position(text_position)
    # final_video_2 = CompositeVideoClip([final_video, text_clip])

    # # Export
    # final_video_2.write_videofile(output_file, codec="libx264", audio_codec="aac")