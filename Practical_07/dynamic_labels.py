"""
Practical 7: Question 4
dynamic_labels
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label
from kivy.properties import StringProperty


class DynamicNameListApp(App):
    """
    DynamicNameListApp is an App for Dynamic Name Labels
    """
    status_text = StringProperty()

    def __init__(self):
        """
        Construct DynamicNameListApp
        """
        super().__init__()
        self.name_list = []

    def build(self):
        """
        Build the Kivy GUI
        :return: self.root
        """
        self.root = Builder.load_file("dynamic_labels.kv")
        self.title = "Dynamic Name List"
        self.status_text = "Add a name to the list or clear out all names!"
        return self.root

    def add_name(self, new_name):
        """
        Add new name as a label into the GUI
        """
        name = new_name.title()
        if name in self.name_list:  # Name already existed
            self.status_text = "This name already existed!"
        else:
            self.name_list.append(name)
            new_label = Label(text=name, font_size=48)
            self.root.ids.name_list.add_widget(new_label)
            self.status_text = f"{name} added!"
            self.root.ids.new_name.text = ""

    def clear_names(self):
        """
        Clear all names in the GUI and the list
        """
        self.root.ids.name_list.clear_widgets()
        self.name_list = []
        self.status_text = "All names are cleared!"
        self.root.ids.new_name.text = ""


DynamicNameListApp().run()
