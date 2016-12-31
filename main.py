import kivy
kivy.require('1.9.1')
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import NumericProperty, ObjectProperty
from time import sleep
class SetTimer(BoxLayout):

    nap_time = NumericProperty

    def check_time(self):
        if 12 <= int(self.nap_time.text) <= 20:
            #print(self.nap_time.text)
            return True
        else:
            print("Pick a number between 12 and 20.")
            return False

    def countdown(self):
        time = int(self.nap_time.text)
        if self.check_time():
            i = time * 60
            while i >= 0:
                count_label = str(i/60)+":00" if i % 60 == 0 else str(i/60)+":"+str(i%60)
                print count_label
                i -= 1


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