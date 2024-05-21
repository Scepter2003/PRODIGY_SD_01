import tkinter as tk
from tkinter import messagebox

def convert_temperature():
    try:
        temp_value = float(temp_entry.get())
        original_unit = original_unit_var.get()
        
        if original_unit == "Celsius":
            fahrenheit = temp_value * 9/5 + 32
            kelvin = temp_value + 273.15
            result_label.config(text=f"Result:\n\n {temp_value} Celcius is equal to: \n\n {fahrenheit:.2f} Fahrenheit\n\n {kelvin:.2f}  Kelvin")
        elif original_unit == "Fahrenheit":
            celsius = (temp_value - 32) * 5/9
            kelvin = celsius + 273.15
            result_label.config(text=f"Result:\n\n {temp_value} Fahrenheit is equal to:\n\n {celsius:.2f} Celsius\n\n {kelvin:.2f} Kelvin")
        elif original_unit == "Kelvin":
            celsius = temp_value - 273.15
            fahrenheit = celsius * 9/5 + 32
            result_label.config(text=f"Result:\n\n {temp_value} Kelvin is equal to:\n\n {celsius:.2f} Celsius\n\n  {fahrenheit:.2f} Fahrenheit")
    
    except ValueError:
        messagebox.showerror("Error", "Invalid temperature value")

root = tk.Tk()
root.title("Temperature Conversion Program")

temp_label = tk.Label(root, text="Enter temperature value:")
temp_label.pack()

temp_entry = tk.Entry(root, width=20)
temp_entry.pack()

original_unit_var = tk.StringVar()
original_unit_var.set("Celsius")

original_unit_label = tk.Label(root, text="Original unit:")
original_unit_label.pack()

original_unit_menu = tk.OptionMenu(root, original_unit_var, "Celsius", "Fahrenheit", "Kelvin")
original_unit_menu.pack()

convert_button = tk.Button(root, text="Convert", command=convert_temperature)
convert_button.pack()

result_label = tk.Label(root, text="Result:")
result_label.pack()

root.mainloop()
