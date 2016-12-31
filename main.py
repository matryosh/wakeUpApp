import kivy
kivy.require('1.9.1')
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import NumericProperty, ObjectProperty
from time import sleep
class SetTimer(BoxLayout):

    nap_time = NumericProperty


class Countdown(BoxLayout):

    nap_timer = NumericProperty

    def startTime(self):
        time = int(self.nap_timer.text[:2])*60
        print(time)

class TimerRoot(BoxLayout):
    startTimer = ObjectProperty()

    def startTimer(self):
        self.clear_widgets()
        self.add_widget(Countdown())
        Countdown().startTime()

    def setTimer(self):
        self.clear_widgets()
        self.add_widget(SetTimer())

class NapTimerApp(App):
    def build(self):
        return TimerRoot()

napApp = NapTimerApp()

if __name__ == "__main__":
    napApp.run()