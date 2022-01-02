"""
Practical 7: Question 3
convert_miles_km
"""

# modules
from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window


class MilesKilometersConversionApp(App):
    """ MilesKilometersConversionApp is an App that converts a value in miles to kilometers """
    def build(self):
        """ Build the Kivy app from the kv file """
        Window.size = (1000, 500)
        self.title = "Convert Miles to Kilometers"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root
