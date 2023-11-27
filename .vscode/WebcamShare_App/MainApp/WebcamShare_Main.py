from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder

Builder.load_file('frontend.kv')


class CameraScreen(Screen):
    
    def start(self):
        pass

    def stop(self):
        pass

    def capture(self):
        pass


class FileSharer: # I need to go back into the last module of the Flatmates Bill Sharing App to find this code explanation.

    def __init__(self, filepath, api_key="AViVqp7suSQWWEdrl6hf9z"):
        self.filepath = filepath
        self.api_key = api_key

    # def share(self):
    #     client = Client(self.api_key)
    #     new_filelink = client.upload(filepath=self.filepath)
    #     return new_filelink.url


class ImageScren(Screen):
    pass


class RootWidget(ScreenManager):
    pass

class MainApp(App):

    def build(self):
        return RootWidget()

MainApp().run()