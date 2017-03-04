from kivy.app import App
from kivy.clock import Clock
from kivy.properties import ObjectProperty, StringProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.core.audio import SoundLoader
from kivy.core.text import LabelBase
from kivy.uix.popup import Popup

class Timer(BoxLayout):
    nap_time = ObjectProperty
    nap = StringProperty
    nap_button = StringProperty
    recommend = StringProperty
    audio_btn = ObjectProperty
    cd_seconds = 0
    start = False

    sound1 = SoundLoader.load('sounds/annoying_alarm.wav')
    sound1.volume = 1.0

    def countdown_time(self, nap):

        if self.cd_seconds <= 1:
            if self.sound1:
                self.sound1.play()

            self.start = False
            self.recommend.x -= 2000
            self.nap_button.x -= self.width * 0.25
            self.clock(self.start)

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
        self.cd_seconds = 10 * 60

        if self.start:
            self.start = False
            self.recommend.x -= 2000
            self.nap_button.x -= self.width * 0.25
        else:
            self.start = True
            self.recommend.x += 2000
            self.nap_button.x += self.width * 0.25

        self.clock(self.start)

    def change_audio(self):
        popup = Popup(title='Test popup',
                      content=self.box,
                      size_hint=(None, None), size=(400, 400))
        popup.open()

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

        config = NapTimerApp.get_running_app().config
        sound = config.getdefault("Sound", "Alarms", "Annoying Alarm")
        if sound == "Annoying Alarm":
            self.sound1 = SoundLoader.load('sounds/annoying_alarm.wav')
        elif sound == "Sunday Mass":
            self.sound1 = SoundLoader.load('sounds/sunday_church.wav')

        try:

            if self.cd_seconds <= 0:
                self.cd_seconds = self.track_time()
        except:
            print("You fucking broke something!")
            return

        if self.start:
            self.start = False
            self.recommend.x -= 2000
            self.nap_button.x -= self.width * 0.25
        else:
            self.start = True
            self.recommend.x += 2000
            self.nap_button.x += self.width * 0.25

        self.clock(self.start)

    def set_alarm(self):
        config = NapTimerApp.get_running_app().config
        sound = config.getdefault("Sound", "Alarms", "Annoying Alarm")
        if sound == "Annoying Alarm":
            self.sound1 = SoundLoader.load('sounds/annoying_alarm.wav')
        elif sound == "Sunday Mass":
            self.sound1 = SoundLoader.load('sounds/annoying_alarm.wav')


class NapTimerApp(App):

    #use_kivy_settings = False

    def on_start(self):
        print("Oh fuck, it started up!")

    def build_config(self, config):
        config.setdefaults('Sound', {'Alarms': 'Annoying Alarm'})

    def build_settings(self, settings):
        settings.add_json_panel("Settings", self.config, data="""
    [
    {"type": "options",
    "title": "Alarm",
    "section": "Sound",
    "key": "Alarms",
    "options": ["Annoying Alarm", "Sunday Mass", "Dulcet Tones"]
    }
    ]"""
                                )

if __name__ == "__main__":
    from kivy.core.window import Window
    from kivy.utils import get_color_from_hex

    LabelBase.register(name='Lato',
                       fn_regular='fonts/Lato/Lato-Regular.ttf')
    Window.clearcolor = get_color_from_hex('#E6DEDC')
    NapTimerApp().run()