from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty, StringProperty
from kivy.uix.relativelayout import RelativeLayout

zooms = [10, 50, 100, 150, 200]


class Plot(Widget):
    src = StringProperty("view/plot.png")


class PlotArea(RelativeLayout):

    def __init__(self, **kw):
        super().__init__(**kw)


class AppView(Widget):
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
