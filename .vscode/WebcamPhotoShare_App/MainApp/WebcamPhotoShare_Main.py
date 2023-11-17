from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
import wikipedia
import requests
import urllib.request

Builder.load_string("""
<FirstScreen>:
    GridLayout:
        cols: 1
        padding: 10
        spacing: 10
        Image:
            id: img
            size_hint_y: 0.8
        TextInput:
            id: user_query
            size_hint_y: 0.1
        Button:
            text: 'Search Image'
            size_hint_y: 0.1
            on_press: root.search_image()

<RootWidget>:
    FirstScreen:
        id: first_screen
        name: 'first_screen'
""")

# Because we are only utilizing one screen at this point in our app, we only require one screen class.
class FirstScreen(Screen):

    # When the user uses the search bar to search for an image, we need a method that will fulfill the request.
    def search_image(self):
        # Allows for users to query from the search bar.
        query = self.manager.current_screen.ids.user_query.text
        # Creates an instance for the user query to run through wikipedia URLS (essentially a wikipedia search).
        page = wikipedia.page(query)
        # Declaring [0] forces the function to run on the first URL in the search.
        image_link = page.images[0]
        # Download the queried image.
        req = requests.get(image_link)
        # Create file from the download.
        urllib.request.urlretrieve(image_link, 'query_image.jpg')
        # Set the image into the Image widget
        self.manager.current_screen.ids.img.source = 'query_image.jpg'

class RootWidget(ScreenManager):
    pass

class MainApp(App):

    def build(self):
        return RootWidget()

MainApp().run()