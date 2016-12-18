import kivy
kivy.require('1.9.1')
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import NumericProperty, ObjectProperty

class SetTimer(BoxLayout):

    nap_time = NumericProperty

class NapTimerApp(App):

    def build(self):
        return SetTimer()

napApp = NapTimerApp()

if __name__ == "__main__":
    napApp.run()