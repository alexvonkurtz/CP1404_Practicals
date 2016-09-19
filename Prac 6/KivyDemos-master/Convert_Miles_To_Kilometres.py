"""
CP1404/CP5632 Practical
Kivy GUI program to Convert a number from Miles to Kilometres
Alex Von Kurtz, IT@JCU
Started 17/09/2016
"""

from kivy.app import App
from kivy.lang import Builder

__author__ = 'Alex Von Kurtz'

MILES_TO_KM = 1.60934

class Miles_To_Kilometres(App):
    """ Miles to Kilometres is a Kivy App for converting a number from miles to kilometres """
    def build(self):
        """ build the Kivy app from the kv file """
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file('Convert_Miles_To_Kilometres.kv')
        return self.root

    def handle_calculate(self):
        """ gets value from inputted number, multiplies that number by MILES_TO_KM then outputs """
        value = self.get_validated_miles()
        result = value * MILES_TO_KM
        self.root.ids.output_label.text = str(result)

    def handle_increment(self, change):
        """
        when the up/down button is pressed the value is increased or decreased and updated
        :param change: the amount to change
        """
        value = self.get_validated_miles() + change
        self.root.ids.input_number.text = str(value)
        self.handle_calculate()

    def get_validated_miles(self):
        """
        get text input from text entry widget, convert to float
        :return: 0 if error, float version of text if valid
        """
        try:
            value = float(self.root.ids.input_number.text)
            return value
        except ValueError:
            return 0

Miles_To_Kilometres().run()