from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder

# As long as the file we are loading is in the same directory as the MainApp file, we only need to input the name of the file alone.
Builder.load_file('frontend.kv')

# Because we are only utilizing one screen at this point in our app, we only require one screen class.
class FirstScreen(Screen):

    # When the user uses the search bar to search for an image, we need a method that will fulfill the request.
    def search_image(self):
        pass

class RootWidget(ScreenManager):
    pass

class MainApp(App):

    def build(self):
        return RootWidget()

MainApp().run()