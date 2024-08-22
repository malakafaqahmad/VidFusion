from moviepy.editor import VideoFileClip

def cut_video(input_file, output_file, start_time, end_time):


    # Load the video
    video = VideoFileClip(input_file).subclip(start_time, end_time)
    
    video.write_videofile(output_file, codec='libx264')

# Example usage
    
input_file = "mrbeast.mp4"
output_file = "edited.mp4"
start_time = 10  # start time in seconds
end_time = 20    # end time in seconds

cut_video(input_file, output_file, start_time, end_time)
