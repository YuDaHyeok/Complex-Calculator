import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import math


class CalculatorGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Calculator")

        # Entry for input
        self.entry_var = tk.StringVar()
        self.entry = ttk.Entry(self.master, font=('Arial', 14), justify='right', textvariable=self.entry_var)
        self.entry.grid(row=0, column=0, columnspan=4, sticky='nsew')

        # Buttons for numbers
        buttons = [
            '7', '8', '9', '+',
            '4', '5', '6', '-',
            '1', '2', '3', '*',
            '0', '.', '=', '/'
        ]
        row_val = 1
        col_val = 0
        for button in buttons:
            ttk.Button(self.master, text=button, command=lambda b=button: self.button_click(b)).grid(row=row_val, column=col_val, sticky='nsew')
            col_val += 1
            if col_val > 3:
                col_val = 0
                row_val += 1

        # Configure grid to make it resizable
        for i in range(1, 5):
            self.master.grid_rowconfigure(i, weight=1)
            self.master.grid_columnconfigure(i, weight=1)

        # Combo box for advanced functions
        self.advanced_var = tk.StringVar()
        advanced_options = [
            'Square', 'Cube', 'Square root', 'Cube root',
            'Factorial', 'Sin', 'Cos', 'Tan'
        ]
        self.advanced_combo = ttk.Combobox(self.master, values=advanced_options, textvariable=self.advanced_var)
        self.advanced_combo.grid(row=5, column=0, columnspan=2, sticky='nsew')

        # Button for clearing input
        ttk.Button(self.master, text='C', command=self.clear_input).grid(row=5, column=2, sticky='nsew')

        # Label for result
        self.result_label = ttk.Label(self.master, text="")
        self.result_label.grid(row=6, column=0, columnspan=4, sticky='nsew')

    def button_click(self, value):
        current = self.entry_var.get()
        if value == '=':
            try:
                if self.advanced_var.get():
                    self.calculate_advanced(self.advanced_var.get())
                else:
                    result = eval(current)
                    self.entry_var.set(result)
                    self.result_label.config(text=f"Result: {result}")
            except Exception as e:
                messagebox.showerror("Error", "Invalid Expression")
        else:
            current += str(value)
            self.entry_var.set(current)

    def clear_input(self):
        self.entry_var.set("")
        self.result_label.config(text="")
        self.advanced_var.set("")

    def calculate_advanced(self, option):
        try:
            value = float(self.entry_var.get())
            result = 0

            if option == 'Square':
                result = value ** 2
            elif option == 'Cube':
                result = value ** 3
            elif option == 'Square root':
                result = math.sqrt(value)
            elif option == 'Cube root':
                result = value ** (1/3)
            elif option == 'Factorial':
                result = math.factorial(int(value))
            elif option == 'Sin':
                result = math.sin(math.radians(value))
            elif option == 'Cos':
                result = math.cos(math.radians(value))
            elif option == 'Tan':
                result = math.tan(math.radians(value))

            self.result_label.config(text=f"Result: {result}")
        except ValueError:
            messagebox.showerror("Error", "Invalid Input")

if __name__ == "__main__":
    root = tk.Tk()
    app = CalculatorGUI(root)
    root.mainloop()
