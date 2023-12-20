import subprocess



# Convert video to audio
def audio_extraction(video_path, audio_path):
    subprocess.run([
        'ffmpeg', '-i', video_path, '-q:a', '0', audio_path
    ])

# Mute original video
def mute(video_path, muted_video_path):
    
    subprocess.run([
        'ffmpeg', '-i', video_path, 
        '-an', muted_video_path
    ])

# Combine muted video and audio files


def add_audio_track(muted_video_path, audio_path):
    output = 'output.mp4'
    ffmpeg_cmd = [
        "ffmpeg", 
        "-i", muted_video_path,
        "-i", audio_path,
        "-c:v", "copy", 
        "-c:a", "aac",
        "-map", "0:v:0",
        "-map", "1:a:0",  
        output  
    ]

    subprocess.run(ffmpeg_cmd)

import os
import subprocess

def get_duration(file_path):
    ffprobe_cmd = [
        "ffprobe",
        "-v", "error",
        "-show_entries", "format=duration",
        "-of", "default=noprint_wrappers=1:nokey=1",
        file_path
    ]
    result = subprocess.run(ffprobe_cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    return float(result.stdout.strip())

import os
import subprocess

def adjust_audio_speed(input_audio_path, output_audio_path, speed=1.0):
    ffmpeg_cmd = [
        "ffmpeg",
        "-i", input_audio_path,
        "-filter:a", f"atempo={speed}",
        output_audio_path
    ]
    subprocess.run(ffmpeg_cmd)

def get_duration(file_path):
    ffprobe_cmd = [
        "ffprobe",
        "-v", "error",
        "-show_entries", "format=duration",
        "-of", "default=noprint_wrappers=1:nokey=1",
        file_path
    ]
    result = subprocess.run(ffprobe_cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    return float(result.stdout.strip())

# def stitch_audio_to_video(video_path, audio_path, output_path):
#     ffmpeg_cmd = [
#         "ffmpeg", 
#         "-i", video_path,
#         "-i", audio_path,
#         "-c:v", "copy", 
#         "-c:a", "aac",
#         "-map", "0:v:0",
#         "-map", "1:a:0",  
#         output_path   
#     ]
#     subprocess.run(ffmpeg_cmd)

def stitch_audio_to_video_with_subtitles(video_path, audio_path, subtitle_path, output_path):
    ffmpeg_cmd = [
        "ffmpeg", 
        "-i", video_path,
        "-i", audio_path,
        "-i", subtitle_path,
        "-c:v", "copy", 
        "-c:a", "aac",
        "-c:s", "mov_text",
        "-map", "0:v:0",
        "-map", "1:a:0",
        "-map", "2:s:0",
        output_path   
    ]
    subprocess.run(ffmpeg_cmd)

def adjust_audio_and_stitch(video_path, input_audio_path,subtitle_path):
    output_path = "output.mp4"
    video_duration = get_duration(video_path)
    audio_duration = get_duration(input_audio_path)
    
    speed =  audio_duration/video_duration

    adjusted_audio_path = "adjusted_audio.wav"
    adjust_audio_speed(input_audio_path, adjusted_audio_path, speed)
    stitch_audio_to_video_with_subtitles(video_path, adjusted_audio_path,subtitle_path,output_path)
    os.remove(adjusted_audio_path)  # Remove temporary adjusted audio file

# Example usage:
# adjust_audio_and_stitch("longer_video.mp4", "original_audio.wav", "output_combined.mp4")


# Example usage:
# adjust_audio_and_stitch("longer_video.mp4", "original_audio.wav", "output_combined.mp4")


# adjust_audio_and_stitch("/Users/bhavyagiri/Developer/Vaani-ML/data/video/Everyone Can Be Rich_muted.mp4","/Users/bhavyagiri/Developer/Vaani-ML/data/audio/Everyone Can Be Rich_hi.wav","/Users/bhavyagiri/Developer/Vaani-ML/data/subtitle/Everyone Can Be Rich_hi.srt")

    
    


