from youtube_transcript_api import YouTubeTranscriptApi

def get_youtube_video_captions_with_timeline(video_id):
    try:
        # Fetch the transcript (captions) for the given video ID
        transcript = YouTubeTranscriptApi.get_transcript(video_id)
        
        # Format the captions with timeline
        captions_with_timeline = []
        for item in transcript:
            start_time = item['start']
            duration = item['duration']
            text = item['text']
            captions_with_timeline.append((start_time, duration, text))

        return captions_with_timeline
    except Exception as e:
        return str(e)


