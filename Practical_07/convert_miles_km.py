"""
Practical 7: Question 3
convert_miles_km
"""

# modules
from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window

# CONSTANTS
MILES_TO_KILOMETERS = 1.60934


class MilesKilometersConversionApp(App):
    """
    MilesKilometersConversionApp is an App that converts a value in miles to kilometers
    """
    def build(self):
        """
        Build the Kivy app from the kv file
        """
        Window.size = (1000, 500)
        self.title = "Convert Miles to Kilometers"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

    def handle_increment(self, change):
        """
        Increment (Up) or Decrement (Down) the input value in miles when either Button `Up` or Button `Down` is pressed
        """
        value_in_mi = self.get_value_in_mi() + change
        self.root.ids.value_in_mi.text = str(value_in_mi)
        self.handle_calculate()

    def handle_calculate(self):
        """
        Calculate the distance from miles to kilometers
        """
        result = self.get_value_in_mi() * MILES_TO_KILOMETERS
        self.root.ids.value_in_km.text = str(result)

    def get_value_in_mi(self):
        """
        Get value in miles
        """
        try:
            value_in_mi = float(self.root.ids.value_in_mi.text)
            return value_in_mi
        except ValueError:
            return 0


MilesKilometersConversionApp().run()
