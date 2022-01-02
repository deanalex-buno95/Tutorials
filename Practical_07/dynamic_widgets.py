"""
Practical 7: Question 4
dynamic_widgets
"""

# modules
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.properties import StringProperty


class DynamicWidgetsApp(App):
    """
    DynamicWidgetsApp is an App to create dynamic widgets for a dictionary of store items with their prices
    """
    status_text = StringProperty()

    def __init__(self):
        """
        Constructor for the Kivy app
        """
        super().__init__()
        self.item_to_price = {}  # dictionary to store items bought from a store with their prices

    def build(self):
        """
        Build the Kivy GUI
        """
        self.title = "Dynamic Widgets"
        self.root = Builder.load_file("dynamic_widgets.kv")
        return self.root


DynamicWidgetsApp().run()
