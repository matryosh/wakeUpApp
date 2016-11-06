import kivy
import time as tm
import winsound
Freq = 2500 # Set Frequency To 2500 Hertz
Dur = 1000 # Set Duration To 1000 ms == 1 second
kivy.require('1.9.1')

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout

class NapBoxLayout(BoxLayout):
    def timah(self):
        tm.sleep(10)
        winsound.Beep(Freq, Dur)
        print "Wake UP!"

class NapTimerApp(App):

    def build(self):
        return NapBoxLayout()

napApp = NapTimerApp()
napApp.run()