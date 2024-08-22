import flet as ft
from gemini_api import generateJson
import json

path = None
_path = None
_url = None
_instructions = None
_shortsCounts = None

def _main(page: ft.Page):
    def on_file_uploaded(e: ft.FilePickerResultEvent):
        if e.files:
            global path
            path = e.files[0].path
            transcription.value = f"Video uploaded: {path}"
            # print(transcription.value)
            page.update()

    
    def goButton(e):
        global path
        global _path, _url, _instructions, _shortsCounts
        _url = url.value
        _instructions = instructions.value
        _shortsCounts = shortsCount.value
        _path = path
        print('url is provided')
        json_data = generateJson(_url, _shortsCounts, _instructions, _path)
        # print(json_data)
        # with open('data.json', 'w') as file:
        #     json.dump(json_data, file)
        # with open('data.json', 'r') as file:
        #     data = json.load(file)
        #     print(data)
        # return _url, _instructions, _shortsCounts, _path
    
    # Define dropdown options
    numbersList = [
        ft.dropdown.Option("1"),
        ft.dropdown.Option("2"),
        ft.dropdown.Option("3"),
        ft.dropdown.Option("4"),
        ft.dropdown.Option("5"),
    ]
    
    # Create the components
    welcome_text = ft.Text("Welcome to ShortZP", style="headlineMedium", color=ft.colors.BLUE_900, weight="bold")
    description_text = ft.Text(
        'Transform your cherished memories and epic moments into captivating shorts and reels effortlessly',
        style="bodyMedium",
        italic=True,
        color=ft.colors.BLUE_GREY_600,
    )
    
    page.title = 'shortZ'
    
    url = ft.TextField(label='YouTube Video URL', width=400, border_color=ft.colors.BLUE_400, border_radius=8)
    button = ft.ElevatedButton(text='Click', icon=ft.icons.PLAY_ARROW, bgcolor=ft.colors.GREEN_400, on_click=goButton)
    instructions = ft.TextField(label='What do you want to extract', width=400, border_color=ft.colors.BLUE_400, border_radius=8)
    shortsCount = ft.Dropdown(label='Shorts', width=100, options=numbersList, border_color=ft.colors.BLUE_400)
    file_picker = ft.FilePicker(on_result=on_file_uploaded)
    upload_button = ft.ElevatedButton("Upload Video", icon=ft.icons.UPLOAD_FILE, bgcolor=ft.colors.ORANGE_400, on_click=lambda _: file_picker.pick_files(allow_multiple=False))
    
    # Add the FilePicker to the page overlay
    page.overlay.append(file_picker)
    
    # Create card sections
    card1 = ft.Container(
        content=ft.Column(
            [
                welcome_text,
                description_text,
                ft.Divider(height=10, color=ft.colors.BLACK)
            ],
            spacing=10,
            alignment="center",
            horizontal_alignment="center",
        ),
        padding=20,
        border_radius=10,
        bgcolor=ft.colors.BROWN_900,
        shadow=ft.BoxShadow(
            offset=ft.Offset(2, 2),
            blur_radius=8,
            spread_radius=2,
            color=ft.colors.BLACK12
        )
    )
    
    card2 = ft.Container(
        content=ft.Row(
            [
                url, 
                shortsCount,
                upload_button
            ],
            spacing=10,
            alignment="center",
        ),
        padding=20,
        border_radius=10,
        bgcolor=ft.colors.BROWN_900,
        shadow=ft.BoxShadow(
            offset=ft.Offset(2, 2),
            blur_radius=8,
            spread_radius=2,
            color=ft.colors.BLACK12
        )
    )
    free = ft.Text('')
    transcription = ft.Text('''Transcription will appear here...''', color=ft.colors.BLACK54)
    emptyContainer = ft.Container(content=ft.Column(
        [free,free,free,free]
    ))
    card3 = ft.Card(
        content=ft.Container(
            content=ft.Column(
                [
                    card1,
                    card2,
                    instructions,
                    button,
                    transcription,
                    emptyContainer
                ],
                spacing=20,
                alignment="center",
                horizontal_alignment="center",
            ),
            padding=20,
            border_radius=10,
            bgcolor=ft.colors.BLACK,
            shadow=ft.BoxShadow(
                offset=ft.Offset(2, 2),
                blur_radius=8,
                spread_radius=2,
                color=ft.colors.BLACK12
            )
        )
    )
    
    # Add the main card to the page
    page.add(card3)
    
    
ft.app(_main)