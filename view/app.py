from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.label import Label


class ComplexApp(App):

    def build(self):
        return Label(text='Pozdrav')


app = ComplexApp().run()
