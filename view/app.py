from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty, StringProperty
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.dropdown import DropDown

from Controler import *
import time

zooms = [10, 50, 100, 150, 200]


class ZoomDD(Button):
    btnnm = StringProperty("Zoom")

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.drop = DropDown()
        # self.text = 'Zoom'
        for i in zooms:
            strr: str = str(i) + '%'
            #print(strr)
            btn = Button(text=strr, size_hint_y=None, height=25)

            btn.bind(on_press=lambda bt: self.drop.select(bt.text))

            self.drop.add_widget(btn)

        self.bind(on_release=self.drop.open)
        self.drop.bind(on_select=self.change)

    def change(self, instance, x: str):
        # print(x, instance)
        self.btnnm = x


class Plot(Widget):
    src = StringProperty("view/plot.png")

    def relode(self):
        self.canvas.ask_update()


class PlotArea(RelativeLayout):
    src = StringProperty("view/plot.png")

    def __init__(self, **kw):
        super().__init__(**kw)
        #time.sleep(10)
        self.input_str = 'x'
        self.output_str = 'sqrt(x*i)'
        self.arr = input_function(self.input_str)
        print(self.arr)
        transformation(self.output_str, self.arr)

    def relode(self):
        self.canvas.ask_update()


class AppView(Widget):
    tinp = ObjectProperty(None)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def what_fun(self, string):
        print(string)

    def input_read(self, string):
        print('Posia je', string)


class ComplexApp(App):

    def build(self):
        v = AppView()
        print(v.ids)
        return v


app = ComplexApp().run()

print(app)
