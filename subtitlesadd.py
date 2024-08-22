from moviepy.editor import *

# Load your video
clip = VideoFileClip("your_video.mp4")

# Create a text clip with the subtitle
txt_clip = TextClip("Your subtitle text", fontsize=24, color='white')

# Set the position and duration
txt_clip = txt_clip.set_pos('center').set_duration(10)

# Overlay the text clip on the video
final_clip = CompositeVideoClip([clip, txt_clip])

# Write the final video with subtitles
final_clip.write_videofile("output_with_subtitles.mp4")
