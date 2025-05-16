# 🌡️ Temperature Converter

A simple and user-friendly desktop application to convert temperatures between Celsius, Fahrenheit, and Kelvin scales. Built with Python’s `tkinter` GUI library for easy usage and quick conversions.

---

## ⚙️ Features

- Convert temperatures between:
  - Celsius (°C)
  - Fahrenheit (°F)
  - Kelvin (K)
- Clean and intuitive GUI interface
- Input validation with error messages
- Results displayed clearly and formatted to two decimal places
- Lightweight and dependency-managed

---

## 📦 Requirements

- Python 3.11  
- `tkinter` (auto-installed if missing on some platforms)

---

## 🚀 How to Run

```bash
python temperature_converter.py
```

This will open a window where you can enter a temperature value, select the input unit, and convert it to the other two scales.

---

## 🖼️ Screenshot (Conceptual)

```
+-------------------------------------+
|         Temperature Converter       |
|-------------------------------------|
| Enter Temperature: [ 25.0       ]   |
| Select Unit:       [ Celsius ▼ ]    |
|                                     |
|           [ Convert ]               |
|                                     |
| Fahrenheit: 77.00                   |
| Kelvin:     298.15                  |
+-------------------------------------+
```

---

## 🔍 How It Works

1. Enter a numeric temperature value.
2. Choose the unit of the input temperature.
3. Click the "Convert" button.
4. The converted temperature values in the other two units will display below.

---

## 📋 Tech Stack

| Component      | Purpose                |
|----------------|------------------------|
| `tkinter`      | GUI interface          |
| `ttk.Combobox` | Unit selection dropdown|
| Python core    | Conversion logic       |
