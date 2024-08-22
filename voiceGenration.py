from gtts import gTTS
import os

def text_to_speech_urdu(text, output_file="output.mp3"):
    tts = gTTS(text=text, lang='ur')
    tts.save(output_file)
    print("Speech file generated successfully:", output_file)
    # Play the speech file (optional)
    os.system("mpg321 " + output_file)  # You can replace "mpg321" with any audio player installed on your system

# Example Urdu text
urdu_text = '''you are an expert in extracting a 3 number of unique short captions from long captions provided below in the formate [(starttime, duration, 'text')].
you are supposed to go through all the captions and find facts from all these captions. your task is to return 
a json format of the starttime,duration and text withing '''

# Convert Urdu text to speech
text_to_speech_urdu(urdu_text)
