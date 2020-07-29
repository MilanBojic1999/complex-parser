from kivy.app import App
from kivy.uix.image import AsyncImage, Image
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.relativelayout import RelativeLayout
from kivy.loader import Loader

class Plot(Widget):
    pass


class PlotArea(RelativeLayout):

    def __init__(self, **kw):
        super().__init__(**kw)


class AppView(RelativeLayout):
    tinp = ObjectProperty(None)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)


    def funs(self):
        print('Kliknu sam ovo')

    def prt(self, inst, val):
        print('This sedngs:', inst, 'and its a', val)

    def ss(self, **args):
        print('Ja sam oved', args)


class ComplexApp(App):

    def build(self):
        v = AppView()
        return v


app = ComplexApp().run()

print(app)
