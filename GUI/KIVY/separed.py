#coding:utf-8
import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty

class MyGrid(Widget):
    name = ObjectProperty(None)
    last = ObjectProperty(None)
    email = ObjectProperty(None)

    def btn(self):
        print(f"Name:\t\t{self.name.text}\nLastName:\t{self.last.text}\nEmail:\t\t{self.email.text}\n")
        self.name.text = ""
        self.last.text = ""
        self.email.text = ""
"""
le fichier .kv est nommer "my.kv" parceque:
- la class ci-dessous s'appelle MyApp, on enleve le "App"
- lower case

donc si la classe s'appelais:   MaPutainDApplicationQuiVaToutDechirerApp
le fichier .kv s'appelera:      maputaindapplicationquivatoutdechirer.kv
"""
class separatedApp (App):
    def build(self):
        return MyGrid()

if __name__ == "__main__":
    separatedApp().run()
