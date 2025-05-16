import sys
import os
import subprocess

# --- Auto-install missing dependencies ---
try:
    import tkinter as tk
    from tkinter import ttk, messagebox
except ImportError:
    subprocess.check_call([sys.executable, "-m", "pip", "install", "tk"])
    os.execv(sys.executable, [sys.executable] + sys.argv)

# --- Temperature conversion logic ---
def convert_temperature(value, from_unit):
    value = float(value)
    conversions = {}

    if from_unit == "Celsius":
        conversions["Fahrenheit"] = value * 9 / 5 + 32
        conversions["Kelvin"] = value + 273.15
    elif from_unit == "Fahrenheit":
        conversions["Celsius"] = (value - 32) * 5 / 9
        conversions["Kelvin"] = (value - 32) * 5 / 9 + 273.15
    elif from_unit == "Kelvin":
        conversions["Celsius"] = value - 273.15
        conversions["Fahrenheit"] = (value - 273.15) * 9 / 5 + 32

    return conversions

# --- GUI Setup ---
class TempConverterApp:
    def __init__(self, root):
        self.root = root
        root.title("Temperature Converter")
        root.geometry("300x280")
        root.resizable(False, False)

        tk.Label(root, text="Enter Temperature:").pack(pady=10)
        self.entry = tk.Entry(root, justify="center")
        self.entry.pack()

        tk.Label(root, text="Select Unit:").pack(pady=10)
        self.unit_var = tk.StringVar(value="Celsius")
        self.unit_menu = ttk.Combobox(root, textvariable=self.unit_var, values=["Celsius", "Fahrenheit", "Kelvin"], state="readonly")
        self.unit_menu.pack()

        tk.Button(root, text="Convert", command=self.convert).pack(pady=10)
        self.result_text = tk.Text(root, height=5, width=35, state="disabled")
        self.result_text.pack(pady=10)

    def convert(self):
        try:
            value = float(self.entry.get())
            from_unit = self.unit_var.get()
            results = convert_temperature(value, from_unit)

            self.result_text.config(state="normal")
            self.result_text.delete("1.0", tk.END)
            for unit, val in results.items():
                self.result_text.insert(tk.END, f"{unit}: {val:.2f}\n")
            self.result_text.config(state="disabled")
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid number.")

# --- Main ---
if __name__ == "__main__":
    root = tk.Tk()
    app = TempConverterApp(root)
    root.mainloop()
