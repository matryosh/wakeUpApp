import kivy
import time as tm
import winsound
Freq = 2500 # Set Frequency To 2500 Hertz
Dur = 1000 # Set Duration To 1000 ms == 1 second
kivy.require('1.9.1')

from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.properties import NumericProperty

class NapFloatLayout(FloatLayout):

    minute_label = "15:00"

    def numberInput(self, sleepAmt):
        pass

    def napButton(self, sleepAmt):
        sleep_minutes = float(sleepAmt)*60

        if sleepAmt:
            tm.sleep(float(sleepAmt))
            winsound.Beep(Freq, Dur)
            print "Wake UP!"

class NapTimerApp(App):

    def build(self):
        return NapFloatLayout()

napApp = NapTimerApp()
napApp.run()