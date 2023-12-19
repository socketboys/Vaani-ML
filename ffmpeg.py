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
    output_path = 'output.mp4'
    subprocess.run([
        'ffmpeg', 
        '-i', muted_video_path,
        '-i', audio_path,
        '-c', 'copy',
        output_path
    ])


