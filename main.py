from kivy.app import App
from kivy.clock import Clock
from kivy.properties import ObjectProperty, StringProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.core.audio import SoundLoader
from kivy.core.text import LabelBase
from kivy.storage.jsonstore import JsonStore
from kivy.uix.popup import Popup
from kivy.uix.button import Button
import collections as clt


class Timer(BoxLayout):
    nap_time = ObjectProperty
    nap = StringProperty
    nap_button = StringProperty
    recommend = StringProperty
    cd_seconds = 0
    start = False

    sound1 = SoundLoader.load('sounds/annoying_alarm.wav')
    sound1.volume = 1.0

    store = JsonStore('store.json')
    num_of_rec = JsonStore('amount_storage.json') #used for adding keys into the store variable e.g. {0: time}, {1:time}

    if num_of_rec.exists('amount'):
        rec_number = num_of_rec.get('amount')['times']
        print rec_number
    else:
        num_of_rec.put('amount', times=0)
        rec_number = 0

    def store_recommendation(self, rating):

        self.store.put(self.rec_number, time=self.cd_seconds / 60, rating=rating)
        self.rec_number += 1

        self.num_of_rec.put('amount', times=self.rec_number)


    def rating_popup(self):
        """rating popup asks user how their nap was using a popup"""
        layout = BoxLayout(orientation='vertical', padding=20,
        spacing=20)
        btn1 = Button(text='bad')
        btn2 = Button(text='good')
        btn3 = Button(text='great')
        layout.add_widget(btn1)
        layout.add_widget(btn2)
        layout.add_widget(btn3)

        popup = Popup(title='How did you sleep?', content=layout, size_hint=(None, None), size=(400, 400))

        def bad_rating():
            self.store_recommendation(0)
            popup.dismiss()

        def good_rating():
            self.store_recommendation(1)
            popup.dismiss()

        def great_rating():
            self.store_recommendation(2)
            popup.dismiss()

        btn1.bind(on_press=lambda x: bad_rating())
        btn2.bind(on_press=lambda x: good_rating())
        btn3.bind(on_press=lambda x: great_rating())

        popup.open()

    def create_recommendation(self):
        listz = [self.store.get(i[1])['time']
                 for i in enumerate(self.store.keys()) if self.store.get(i[1])['rating'] > 1]

        rec_num = clt.Counter(listz)

        return rec_num.most_common()[0][0]



    def start_var(self):
        """used to change the global start variable"""
        self.start = True

    def stop_var(self):
        """used to change the global start variable"""
        self.start = False

    def countdown_time(self, nap):

        if self.cd_seconds <= 1:
            if self.sound1:
                self.sound1.play()

            self.stop_var()
            self.rating_popup()
            self.clock(self.start)

        if self.start:
            self.cd_seconds -= nap

        minutes, seconds = divmod(self.cd_seconds, 60)
        self.ids.nap_label.text = (
            '%02d:%02d' %
            (int(minutes), int(seconds)))

    def track_time(self):
        """This functions initializes the time to seconds from minutes"""
        cd_seconds = int(self.ids.nap_minutes.text) * 60
        return cd_seconds

    def recommend_time(self):
        """this function displays the created recommendation to the screen"""
        rec_num = self.create_recommendation()
        self.ids.nap_minutes.text = str(rec_num)

    def reset(self):
        """resets the look of the screen back"""
        self.cd_seconds = self.track_time()
        minutes, seconds = divmod(self.cd_seconds, 60)
        self.ids.nap_label.text = (
            '%02d:%02d' %
            (int(minutes), int(seconds)))



    def clock(self, stop_start):
        """this resets kivy's clock function and changes the nap button"""
        event = Clock.schedule_interval(self.countdown_time, 0)
        if stop_start or self.cd_seconds <= 0:
            self.set_alarm()
            Clock.unschedule(self.countdown_time)
            self.nap_button.text = "I woke up early"
            event()
        else:
            Clock.unschedule(self.countdown_time)
            self.nap_button.text = "Time For A Nap"
            self.reset()

    def start_countdown(self):
        "this function starts the other functions"
        self.cd_seconds = 0 #makes the app countdown from the user sets on the first try

        try:
            self.cd_seconds = self.track_time()
        except:
            print("You fucking broke something!")
            return

        if self.start:
            self.stop_var()
        else:
            self.start_var()

        self.clock(self.start)

    def set_alarm(self):    #this function sets the sound1 variable to whatever is in the naptimer.ini

        config = NapTimerApp.get_running_app().config
        sound = config.getdefault("Sound", "Alarms", "Annoying Alarm")
        if sound == "Annoying Alarm":
            self.sound1 = SoundLoader.load('sounds/annoying_alarm.wav')
        elif sound == "Sunday Mass":
            self.sound1 = SoundLoader.load('sounds/sunday_church.wav')
        elif sound == "Dulcet Tones":
            self.sound1 = SoundLoader.load('sounds/Dulcet Tones.m4a')


class NapTimerApp(App):

    use_kivy_settings = False

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
    Window.clearcolor = get_color_from_hex('#000000')
    NapTimerApp().run()