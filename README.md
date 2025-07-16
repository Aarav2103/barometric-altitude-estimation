# Barometric Altitude Estimation with ML Correction

This project estimates altitude using barometric pressure data from the Arduino Nano 33 BLE Sense and enhances its accuracy using Python visualization and future-ready ML techniques.

## 🧠 Features

- Real-time altitude calculation using onboard LPS22HB pressure sensor.
- GUI built with Tkinter to display, log, and visualize altitude data.
- CSV export for later ML model training or regression analysis.
- Designed for applications in drones, mountaineering, and aerospace systems.

## 🛠 Tech Stack

- **Hardware:** Arduino Nano 33 BLE Sense (LPS22HB sensor)
- **Arduino:** C++ (Barometric pressure reading and altitude computation)
- **Python:** Tkinter, matplotlib, pandas, serial
- **Optional ML Models:** Regression, Neural Nets (planned or ongoing)

## 📂 Files

- `/arduino/atmos_pressure.ino` – Reads and prints altitude from pressure.
- `/python-gui/barometric_pressure_gui.py` – Tkinter-based GUI to read and plot data.
- `/sample-data/sensor_data.csv` – Example CSV with timestamped altitude readings.


## 🚀 Getting Started

1. Upload the Arduino sketch to your Nano 33 BLE Sense.
2. Run the Python GUI script (`barometric_pressure_gui.py`).
3. Connect Arduino via USB (update `COM3` to your port).
4. Start collecting and visualizing altitude in real-time!

## 📘 Future Work

- Add ML-based altitude correction using weather conditions.
- Train regression models on exported CSV data to refine estimations.
