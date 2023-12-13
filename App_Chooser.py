import tkinter as tk
from tkinter import ttk

# Importing the UnitConverterGUI and Calculator functions from your code
from unit_gui import UnitConverterGUI
from cal_gui import CalculatorGUI

class AppChooser(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("App Chooser")

        # Label
        label = ttk.Label(self, text="Choose an App:")
        label.pack(pady=10)

        # Button to open Unit Converter
        unit_convert_btn = ttk.Button(self, text="Unit Converter", command=self.open_unit_converter)
        unit_convert_btn.pack(pady=5)

        # Button to open Calculator
        calculator_btn = ttk.Button(self, text="Calculator", command=self.open_calculator)
        calculator_btn.pack(pady=5)

    def open_unit_converter(self):
        # Create a new window for Unit Converter
        unit_converter_window = tk.Toplevel(self)
        unit_converter_app = UnitConverterGUI(unit_converter_window)

    def open_calculator(self):
        # Run the Calculator function
        calculator_window = tk.Toplevel(self)
        calculator_app = CalculatorGUI(calculator_window)
        
if __name__ == "__main__":
    app_chooser = AppChooser()
    app_chooser.mainloop()
