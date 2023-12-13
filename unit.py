import math

def convert_initial(unit):
    if unit.lower() in ["h", "hours"]:
        return 'hour'
    elif unit.lower() in ["min", "minutes"]:
        return 'minute'
    elif unit.lower() in ["sec", "seconds"]:
        return 'second'
    elif unit.lower() == "years":
        return 'year'
    else:
        return unit.lower()

def convert_SI(val, unit_in, unit_out):
    unit_in = convert_initial(unit_in)
    unit_out = convert_initial(unit_out)

    distance_units = {'mm': 0.001, 'cm': 0.01, 'm': 1.0, 'km': 1000., 'in': 0.0254, 'ft': 0.3048, 'yd': 0.9144, 'mile': 1609.344}
    temperature_units = ["c", "f", "k"]
    mass_units = ["kg", "g", "mg", 'oz', "lb"]
    date_units = ['day', 'hour', 'minute', 'second', 'year']
    speed_units = {'km/h': 1.0, 'km/s': 3600.0, 'm/s': 3.6, 'm/h': 0.001, 'kn': 1.852, 'mach': 1224}

    # Function to get the temperature symbol
    def get_temperature_symbol(unit):
        return "℃" if unit == "c" else "℉" if unit == "f" else "K"

    # Check if the units are temperature units
    if unit_in.lower() in temperature_units and unit_out.lower() in temperature_units:
        converted_val = convert_temperature(val, unit_in.lower(), unit_out.lower())
        return f"{val} {get_temperature_symbol(unit_in.lower())} is equal to {round(converted_val,6)} {get_temperature_symbol(unit_out.lower())}"
    elif unit_in.lower() in mass_units and unit_out.lower() in mass_units:
        converted_val = convert_mass(val, unit_in.lower(), unit_out.lower())
        return f"{val} {unit_in} is equal to {round(converted_val,5)} {unit_out}"
    elif unit_in.lower() in distance_units and unit_out.lower() in distance_units :
        unit_in = unit_in.lower()
        unit_out = unit_out.lower()
        converted_val = val * distance_units[unit_in] / distance_units[unit_out]
        return f"{val} {unit_in} is equal to {round(converted_val,5)} {unit_out}"
    elif unit_in.lower() in date_units and unit_out.lower() in date_units:
        unit_in = unit_in.lower()
        unit_out = unit_out.lower()
        converted_val = convert_date(val,unit_in,unit_out)
        return f"{val} {unit_in} is equal to {round(converted_val,5)} {unit_out}"
    elif unit_in.lower() in speed_units and unit_out.lower() in speed_units :
        unit_in = unit_in.lower()
        unit_out = unit_out.lower()
        converted_val = convert_speed(val,unit_in,unit_out)
        return f"{val} {unit_in} is equal to {round(converted_val,5)} {unit_out}"
    else:
        return print("please enter a valid units")

def convert_speed (val, unit_in, unit_out):
    speed = {'km/h':1.0, 'km/s':3600.0, 'm/s':3.6, 'm/h':0.001, 'kn':1.852,'mach':1224}
    return val * speed[unit_in]/speed[unit_out]

def convert_date (val, unit_in, unit_out):
    date = {'day':1.0,'hour':1/24,'minute':1/1440, 'second':1/86400 , 'year':365.0}
    return val * date[unit_in]/date[unit_out]

def convert_distance (val, unit_in, unit_out):
    distance = {'mm': 0.001, 'cm': 0.01, 'm': 1.0, 'km': 1000., 'in': 0.0254, 'ft': 0.3048, 'yd': 0.9144, 'mile': 1609.344}
    return val * distance[unit_in] /distance[unit_out]
def convert_mass(val, unit_in, unit_out):
    mass = {'kg': 1.0, 'g': 0.001, 'mg': 0.000001, 'oz': 0.0283495, 'lb': 0.453592}
    return val * mass[unit_in] / mass[unit_out]

def convert_temperature(val, unit_in, unit_out):
    # Convert temperature from unit_in to unit_out
    if unit_in == "c":
        if unit_out == "f":
            return (val * 9/5) + 32
        elif unit_out == "k":
            return val + 273.15
    elif unit_in == "f":
        if unit_out == "c":
            return (val - 32) * 5/9
        elif unit_out == "k":
            return (val - 32) * 5/9 + 273.15
    elif unit_in == "k":
        if unit_out == "c":
            return val - 273.15
        elif unit_out == "f":
            return (val - 273.15) * 9/5 + 32
    return val  # If same unit is input and output


start_script = input("If you want to see the unit list, please enter a \"list\" \n"
                     "if you want to use unit converter, enter a correct units :")
if start_script == "list":
    print("----------------------------------------------------------------------------------------------------------------\n"
          "distance_units = Millimeter (mm), Centimeter (cm), Meter (m), Kilometer (km), Inch (in), Feet (ft), Yard (yd), Mile (mile)\n"
          "----------------------------------------------------------------------------------------------------------------\n"
          "temperature_units = Celsius (c), Fahrenheit (f), Kelvin (k)\n"
          "----------------------------------------------------------------------------------------------------------------\n"
          "mass_units = Kilogram (kg), Gram (g), Milligram (mg), Ounce (oz), Pound (lb)\n"
          "----------------------------------------------------------------------------------------------------------------\n"
          "date_units = day, hour, minute, second, year\n"
          "----------------------------------------------------------------------------------------------------------------\n"
          "speed_units = km/h, km/s, m/s, m/h, kn, mach\n"
          "----------------------------------------------------------------------------------------------------------------\n")
    from_unit = input("Enter the unit you are converting from (e.g., 'm' for meters): ")
else:
    from_unit = start_script
    pass
to_unit = input("Enter the unit you are converting to (e.g., 'km' for kilometers): ")
value = float(input("Enter the value to convert: "))


# Convert the value
try:
    result_with_symbol = convert_SI(value, from_unit, to_unit)
    print(result_with_symbol)
except KeyError:
    print(f"Conversion from {from_unit} to {to_unit} is not available.")
except ValueError:
    print("Please enter a valid number.")