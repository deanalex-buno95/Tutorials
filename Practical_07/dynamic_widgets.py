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

    def add_new_item(self, item_name, item_price):
        """
        Add a new item widget from user input
        :param item_name: Name of item (str)
        :param item_price: Price of item (float)
        """
        try:  # Ensure the price is a number
            name = item_name.title()  # name convention
            price = float(item_price)  # `try` condition
            if price < 0:  # Invalid price
                self.status_text = "Invalid price!"
            elif name in self.item_to_price:  # Item already existed
                self.status_text = "Item already existed!"
            elif name == "":  # Item name is empty
                self.status_text = "Item name is empty!"
            else:  # Valid price and a new item
                self.item_to_price[name] = price
                new_button = Button(text=name)
                new_button.bind(on_release=self.press_item_button)
                self.root.ids.item_list.add_widget(new_button)
                self.status_text = f"{name} (${price:.2f}) added!"
        except ValueError:  # Price is either empty or NaN
            self.status_text = "Invalid price value!"

    def press_item_button(self, instance):
        """
        Handle the clicking of items in the item list
        :param instance: Instance of button clicked
        """
        name = instance.text  # item name
        price = self.item_to_price[name]  # item price
        self.status_text = f"{name} costs ${price:.2f}."

    def clear_all_items(self):
        """
        Clear out all of the items in the dictionary and the Kivy app
        """
        self.root.ids.item_list.clear_widgets()
        self.item_to_price = {}


DynamicWidgetsApp().run()
