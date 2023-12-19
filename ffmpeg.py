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
    
# add_audio_track("/Users/bhavyagiri/Developer/Vaani-ML/data/video/Everyone Can Be Rich_muted.mp4","/Users/bhavyagiri/Developer/Vaani-ML/data/audio/Everyone Can Be Rich_hi.wav")
    


