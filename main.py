from kivy.app import App
from kivy.clock import Clock
from kivy.properties import ObjectProperty, StringProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.core.audio import SoundLoader
from kivy.core.text import LabelBase


class Timer(BoxLayout):
    nap_time = ObjectProperty
    nap = StringProperty
    nap_button = StringProperty
    recommend = StringProperty
    cd_seconds = 0
    start = False
    sound1 = SoundLoader.load('sounds/annoying_alarm.wav')
    sound1.volume = 1.0

    def countdown_time(self, nap):

        if self.cd_seconds <= 1:
            if self.sound1:
                self.sound1.play()

            self.clock(False)
            self.start = False

        if self.start:
            self.cd_seconds -= nap

        minutes, seconds = divmod(self.cd_seconds, 60)
        self.ids.nap_label.text = (
            '%02d:%02d' %
            (int(minutes), int(seconds)))

    def track_time(self):
        # This functions initializes the time to seconds from minutes
        cd_seconds = int(self.ids.nap_minutes.text) * 60
        return cd_seconds

    def recommend_time(self):
        print("This is a placeholder for a recommendation button")

    def reset(self):
        self.cd_seconds = self.track_time()
        minutes, seconds = divmod(self.cd_seconds, 60)
        self.ids.nap_label.text = (
            '%02d:%02d' %
            (int(minutes), int(seconds)))

    def clock(self, stop_start):
        event = Clock.schedule_interval(self.countdown_time, 0)
        if stop_start or self.cd_seconds <= 0:
            Clock.unschedule(self.countdown_time)
            self.nap_button.text = "I woke up early"
            event()
        else:
            Clock.unschedule(self.countdown_time)
            self.nap_button.text = "Time For A Nap"
            self.reset()

    def start_countdown(self):

        # this checks to see if cd_seconds is zero. If so, it calls track time

        if self.cd_seconds <= 0:
            self.cd_seconds = self.track_time()

        if self.start:
            self.start = False
            self.recommend.x -= 2000
            self.nap_button.x -= self.width * 0.25
        else:
            self.start = True
            self.recommend.x += 2000
            self.nap_button.x += self.width * 0.25

        self.clock(self.start)


class NapTimerApp(App):
    def build(self):
        return Timer()

    def on_start(self):
        print("Oh fuck, it started up!")


if __name__ == "__main__":
    from kivy.core.window import Window
    from kivy.utils import get_color_from_hex

    LabelBase.register(name='Lato',
                       fn_regular='fonts/Lato/Lato-Regular.ttf')
    Window.clearcolor = get_color_from_hex('#E6DEDC')
    NapTimerApp().run()