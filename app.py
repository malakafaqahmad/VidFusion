import flet as ft
from gui import _main, _instructions, _path, _shortsCounts, _url
from gemini_api import generateJson
# from movie import cut_video
import json

def main(page:ft.Page):
    _main(page)
    if _url is not None:
        print('url is provided')
        json_data = generateJson(_url, _shortsCounts, _instructions, _path)
        with open('data.json', 'w') as file:
            json.dump(json_data, file)
        with open('data.json', 'r') as file:
            data = json.load(file)
            print(data)
    else:
        print("URL is None. Please provide a valid URL.")
