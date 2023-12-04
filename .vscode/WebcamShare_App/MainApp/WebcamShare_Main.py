from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder

Builder.load_string("""
<CameraScreen>:
    GridLayout:
        cols: 1
        Camera: # Kivy has it's own inherent camera widget
            id: camera
            resolution: (640, 480)
            play: False # Stating False here will make it so that the camera will not start automatically when the code is run.
        Button:
            id: camera_button
            text: 'Start Camera'
            on_press: root.start() if root.ids.camera.play == False else root.stop()
        Button:
            text: 'Capture Image'

<RootWidget>:
    CameraScreen:
        id: camera_screen
        name: 'camera_screen'
""")


class CameraScreen(Screen):
    
    def start(self):
        self.ids.camera.play = True
        self.ids.camera_button.text = "Stop Camera"
        self.ids.camera.texture = self.ids.camera._camera.texture

    def stop(self):
        self.ids.camera.play = True
        self.ids.camera_button.text = "Start Camera"
        self.ids.camera.texture = None

    def capture(self):
        current_time = time.strftime('%Y%m%d - $H$H$S')
        filename = current_time + '.png'
        self.ids.camera.export_to_png(filename)


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