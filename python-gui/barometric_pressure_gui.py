import tkinter as tk
from tkinter import ttk
import serial
import time
import threading
import csv
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# ==== CONFIGURATION ====
arduino_port = 'COM3'  # Change this to your actual COM port
baud_rate = 9600
ser = serial.Serial(arduino_port, baud_rate)

data_queue = []

# ==== READ FROM SERIAL ====
def read_data():
    while True:
        if ser.in_waiting > 0:
            line = ser.readline().decode('utf-8').strip()
            if "Altitude" in line:
                try:
                    altitude = float(line.split('=')[1].split('m')[0].strip())
                    timestamp = time.time()
                    data_queue.append((timestamp, altitude))
                    update_gui(timestamp, altitude)
                except:
                    pass

# ==== GUI UPDATER ====
def update_gui(timestamp, altitude):
    timestamp_label.config(text=f"Timestamp: {timestamp:.2f}")
    altitude_label.config(text=f"Altitude: {altitude:.2f} m")
    save_button.config(state=tk.NORMAL)

# ==== SAVE TO CSV ====
def save_data():
    with open('sensor_data.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Timestamp", "Altitude(m)"])
        writer.writerows(data_queue)
    save_button.config(state=tk.DISABLED)

# ==== PLOT ====
def plot_data():
    df = pd.DataFrame(data_queue, columns=["Timestamp", "Altitude(m)"])
    fig, ax = plt.subplots(figsize=(8, 6))
    ax.plot(df["Timestamp"], df["Altitude(m)"], label='Altitude over Time')
    ax.set_xlabel('Timestamp')
    ax.set_ylabel('Altitude (m)')
    ax.set_title('Altitude Data over Time')
    ax.legend()

    canvas = FigureCanvasTkAgg(fig, master=plot_frame)
    canvas.draw()
    canvas.get_tk_widget().pack()

# ==== GUI SETUP ====
root = tk.Tk()
root.title("Barometric Altitude Monitor")
root.geometry("800x600")

data_frame = ttk.Frame(root, padding="10")
data_frame.pack(pady=20)

timestamp_label = ttk.Label(data_frame, text="Timestamp: ", font=("Arial", 12))
timestamp_label.grid(row=0, column=0, sticky=tk.W, padx=10)

altitude_label = ttk.Label(data_frame, text="Altitude: ", font=("Arial", 12))
altitude_label.grid(row=1, column=0, sticky=tk.W, padx=10)

control_frame = ttk.Frame(root, padding="10")
control_frame.pack(pady=20)

save_button = ttk.Button(control_frame, text="Save Data", command=save_data, state=tk.DISABLED)
save_button.grid(row=0, column=0, padx=10)

plot_button = ttk.Button(control_frame, text="Plot Data", command=plot_data)
plot_button.grid(row=0, column=1, padx=10)

plot_frame = ttk.Frame(root, padding="10")
plot_frame.pack(pady=20)

# ==== START THREAD ====
threading.Thread(target=read_data, daemon=True).start()
root.mainloop()
