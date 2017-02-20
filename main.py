from kivy.app import App
from kivy.clock import Clock
from kivy.properties import ObjectProperty, StringProperty
from kivy.uix.boxlayout import BoxLayout


class Timer(BoxLayout):
    nap_time = ObjectProperty
    nap = StringProperty
    nap_button = StringProperty
    cd_seconds = 0
    start = False

    def countdown_time(self, nap):

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

    def reset(self):
        self.cd_seconds = self.track_time()
        minutes, seconds = divmod(self.cd_seconds, 60)
        self.ids.nap_label.text = (
            '%02d:%02d' %
            (int(minutes), int(seconds)))

    def clock(self, stop_start):
        event = Clock.schedule_interval(self.countdown_time, 0)
        if stop_start:
            Clock.unschedule(self.countdown_time)
            event()
        else:
            self.reset()

    def start_countdown(self):

        # this checks to see if cd_seconds is zero. If so, it calls track time

        if self.cd_seconds == 0:
            self.cd_seconds = self.track_time()

        if self.start:
            self.start = False
        else:
            self.start = True

        self.clock(self.start)


class NapTimerApp(App):
    def build(self):
        return Timer()


if __name__ == "__main__":
    NapTimerApp().run()