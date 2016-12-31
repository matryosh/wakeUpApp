import kivy
kivy.require('1.9.1')
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import NumericProperty, ObjectProperty
from time import sleep
class SetTimer(BoxLayout):

    nap_time = NumericProperty

    def testButton(self):
        print("Just seeing if the button works.")

class TimerRoot(BoxLayout):
    startTimer = ObjectProperty()

    def setTimer(self):
        self.clear_widgets()
        self.add_widget(SetTimer())

class NapTimerApp(App):
    def build(self):
        return TimerRoot()

napApp = NapTimerApp()

if __name__ == "__main__":
    napApp.run()