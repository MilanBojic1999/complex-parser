from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.properties import ObjectProperty


class AppView(Widget):
    tinp = ObjectProperty(None)

    def funs(self):
        print('Kliknu sam ovo')

    def prt(self,inst,val):
        print('This sedngs:',inst,'and its a',val)


class ComplexApp(App):



    def build(self):
        v = AppView()
        return v


app = ComplexApp().run()

print(app)
