# Import the Python SDK
import google.generativeai as genai
from ytcaptions import get_youtube_video_captions_with_timeline
import re
from role import Role

def extract_video_id(url):
    # Define the regular expression pattern for YouTube video URLs
    pattern = re.compile(
        r'(?:https?://)?(?:www\.)?'
        r'(?:youtube\.com/(?:[^/]+/.+/|(?:v|e(?:mbed)?)|.*[?&]v=)|youtu\.be/)'
        r'([^"&?/ ]{11})'
    )

    # Search for the pattern in the URL
    match = pattern.search(url)
    
    # If a match is found, return the video ID
    if match:
        return match.group(1)
    else:
        return None



def generateJson(_url,_shortsCounts,_instructions,_path):
    
    api_key = ''
    videoid = extract_video_id(_url)
    print('vidoe id extracted', videoid)
    captions = get_youtube_video_captions_with_timeline(video_id= videoid)
    print('captions generated', captions)


    genai.configure(api_key=api_key)

    model = genai.GenerativeModel('gemini-pro')

    response = model.generate_content(f'{Role} {captions}')
    print('responce generated from gemini', response.text)
    return response.text
