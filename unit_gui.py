import tkinter as tk
from tkinter import ttk, messagebox
import math

class UnitConverterGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Unit Converter")

        # 입력을 위한 Entry 위젯
        self.from_unit_var = tk.StringVar()
        self.from_unit_var.set("m")  # 기본 값

        self.to_unit_var = tk.StringVar()
        self.to_unit_var.set("km")  # 기본 값



        self.entry = ttk.Entry(self.master, font=('Arial', 14), justify='right')
        self.entry.grid(row=0, column=0, columnspan=4, sticky='nsew')

        # 단위 선택을 위한 Listbox 위젯
        unit_list = ['mm', 'cm', 'm', 'km', 'in', 'ft', 'yd', 'mile', 'day', 'hour', 'minute', 'second', 'year', '°C', '°F', 'K', 'kg', 'g', 'mg', 'oz', 'km/h', 'km/s', 'm/s', 'm/h', 'kn', 'mach']
        self.from_listbox = tk.Listbox(self.master, selectmode=tk.SINGLE, exportselection=0, font=('Arial', 12))
        self.to_listbox = tk.Listbox(self.master, selectmode=tk.SINGLE, exportselection=0, font=('Arial', 12))

        for unit in unit_list:
            self.from_listbox.insert(tk.END, unit)
            self.to_listbox.insert(tk.END, unit)

        self.from_listbox.grid(row=1, column=0, rowspan=4, sticky='nsew')
        self.to_listbox.grid(row=1, column=3, rowspan=4, sticky='nsew')

        self.from_listbox.bind('<<ListboxSelect>>', lambda event: self.set_unit(event, self.from_unit_var))
        self.to_listbox.bind('<<ListboxSelect>>', lambda event: self.set_unit(event, self.to_unit_var))

        # 그리드를 조정하여 크기 조절 가능하도록 함
        for i in range(5):
            self.master.grid_rowconfigure(i, weight=1)
            self.master.grid_columnconfigure(i, weight=1)

        # 변환 버튼
        convert_btn = ttk.Button(self.master, text="Convert", command=self.convert_units)
        convert_btn.grid(row=5, column=0, columnspan=4, sticky='nsew')

        # 결과를 표시할 Label
        self.result_label = ttk.Label(self.master, text="")
        self.result_label.grid(row=6, column=0, columnspan=4, sticky='nsew')

    def set_unit(self, event, unit_var):
        selected_index = event.widget.curselection()
        if selected_index:
            selected_unit = event.widget.get(selected_index)
            unit_var.set(selected_unit)

    def convert_units(self):
        try:
            value = float(self.entry.get())
            from_unit = self.from_unit_var.get()
            to_unit = self.to_unit_var.get()

            if from_unit in ('°C', '°F', 'K') and to_unit in ('°C', '°F', 'K'):
                converted_value = self.convert_temperature(value, from_unit, to_unit)
            elif from_unit in ('kg', 'g', 'mg', 'oz') and to_unit in ('kg', 'g', 'mg', 'oz'):
                converted_value = self.convert_mass(value, from_unit, to_unit)
            elif from_unit in ('mm', 'cm', 'm', 'km', 'in', 'ft', 'yd', 'mile') and to_unit in ('mm', 'cm', 'm', 'km', 'in', 'ft', 'yd', 'mile'):
                converted_value = self.convert_distance(value, from_unit, to_unit)
            elif from_unit in ('day', 'hour', 'minute', 'second', 'year') and to_unit in ('day', 'hour', 'minute', 'second', 'year'):
                converted_value = self.convert_date(value, from_unit, to_unit)
            elif from_unit in ('km/h', 'km/s', 'm/s', 'm/h', 'kn', 'mach') and to_unit in ('km/h', 'km/s', 'm/s', 'm/h', 'kn', 'mach'):
                converted_value = self.convert_speed(value, from_unit, to_unit)
            else:
                raise ValueError("변환할 수 없는 단위입니다.")

            result_text = f"{value} {from_unit} is equal to {round(converted_value, 6)} {to_unit}"
            self.result_label.config(text=result_text)

        except ValueError as e:
            messagebox.showerror("오류", str(e))

    def convert_temperature(self, val, unit_in, unit_out):
        # 온도를 unit_in에서 unit_out으로 변환
        if unit_in == "°C":
            if unit_out == "°F":
                return (val * 9/5) + 32
            elif unit_out == "K":
                return val + 273.15
        elif unit_in == "°F":
            if unit_out == "°C":
                return (val - 32) * 5/9
            elif unit_out == "K":
                return (val - 32) * 5/9 + 273.15
        elif unit_in == "K":
            if unit_out == "°C":
                return val - 273.15
            elif unit_out == "°F":
                return (val - 273.15) * 9/5 + 32
        return val  # 같은 단위를 입력 및 출력하는 경우

    def convert_mass(self, val, unit_in, unit_out):
        mass = {'kg': 1.0, 'g': 0.001, 'mg': 0.000001, 'oz': 0.0283495}
        return val * mass[unit_in] / mass[unit_out]

    def convert_distance(self, val, unit_in, unit_out):
        distance_units = {'mm': 0.001, 'cm': 0.01, 'm': 1.0, 'km': 1000., 'in': 0.0254, 'ft': 0.3048, 'yd': 0.9144, 'mile': 1609.344}
        return val * distance_units[unit_in] / distance_units[unit_out]

    def convert_date(self, val, unit_in, unit_out):
        date_units = {'day': 1.0, 'hour': 1/24, 'minute': 1/1440, 'second': 1/86400, 'year': 365.0}
        return val * date_units[unit_in] / date_units[unit_out]

    def convert_speed(self, val, unit_in, unit_out):
        speed_units = {'km/h': 1.0, 'km/s': 3600.0, 'm/s': 3.6, 'm/h': 0.001, 'kn': 1.852, 'mach': 1224}
        return val * speed_units[unit_in] / speed_units[unit_out]

if __name__ == "__main__":
    root = tk.Tk()
    app = UnitConverterGUI(root)
    root.mainloop()
