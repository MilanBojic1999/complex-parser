from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty, StringProperty
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.dropdown import DropDown

from Controler import *

zooms = [10, 50, 100, 150, 200]

input_str = 'x'
output_str = 'sin(x)+cos(x)'





class ZoomDD(Button):
    btnnm = StringProperty("Zoom")

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.drop = DropDown()
        # self.text = 'Zoom'
        for i in zooms:
            strr: str = str(i) + '%'
            # print(strr)
            btn = Button(text=strr, size_hint_y=None, height=25)

            btn.bind(on_press=lambda bt: self.drop.select(bt.text))

            self.drop.add_widget(btn)

        self.bind(on_release=self.drop.open)
        self.drop.bind(on_select=self.change)

    def change(self, x: str):
        # print(x, instance)
        self.btnnm = x


class Plot(Widget):
    src = StringProperty("view/plot.png")

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # self.area = area

    def relode(self):
        self.ids.aimg.reload()


class PlotArea(RelativeLayout):
    src = StringProperty("view/plot.png")

    def __init__(self, **kw):
        super().__init__(**kw)

    def relode(self):
        self.canvas.ask_update()
        self.ids.inputplt.relode()


class AppView(Widget):
    tinp = ObjectProperty(None)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.input_str = '5'
        self.output_str = 'sin(x)+cos(x)'
        self.create_plots()

    def what_fun(self, string):
        print(string)

    def input_read(self, string):
        print('Posia je', string)

    def get_ifun(self, string):
        if len(string) == 0:
            return
        self.output_str = string
        self.create_plots()

    def get_ofun(self, string):
        if len(string) == 0:
            return
        self.input_str = string
        self.create_plots()

    def create_plots(self):
        arr = input_function(self.input_str)
        transformation(self.output_str, arr)
        self.canvas.ask_update()
        self.ids.plot1.relode()
        self.ids.plot2.relode()


class ComplexApp(App):

    def build(self):
        v = AppView()
        print(v.ids)
        return v


app = ComplexApp().run()

print(app)
