from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty, StringProperty
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.dropdown import DropDown

zooms = [10, 50, 100, 150, 200]


class ZoomDD(Button):
    btnnm = StringProperty("Zoom")

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.drop = DropDown()
        # self.text = 'Zoom'
        for i in zooms:
            strr: str = str(i) + '%'
            print(strr)
            btn = Button(text=strr, size_hint_y=None, height=20)

            btn.bind(on_press=lambda bt: self.drop.select(bt.text))

            self.drop.add_widget(btn)

        self.bind(on_release=self.drop.open)
        self.drop.bind(on_select=self.change)

    def change(self, instance, x: str):
        print(x, instance)
        self.btnnm = x


class Plot(Widget):
    src = StringProperty("view/plot.png")


class PlotArea(RelativeLayout):
    idk = ObjectProperty(None)

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
