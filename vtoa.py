import moviepy.editor as mp
from tkinter.filedialog import askopenfilename

video_path = askopenfilename()
video = mp.VideoFileClip(video_path)

audio = video.audio
audio.write_audiofile("Sample_audio.mp3")

print("Code successfully completed")

