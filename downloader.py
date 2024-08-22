import pytube as YouTube


def download_video(short, download_path):
    video_url = short["url"]
    try:
        yt = YouTube(video_url)
        stream = yt.streams.filter(file_extension='mp4', only_video=True).first()
        if stream is not None:
            stream.download(output_path=download_path)
            print(f"Downloaded: {yt.title}")
        else:
            print(f"No compatible video found for URL: {video_url}")
    except Exception as e:
        print(f"An error occurred while downloading video {video_url}: {e}")


