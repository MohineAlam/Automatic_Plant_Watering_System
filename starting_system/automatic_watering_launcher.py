import tkinter as tk
from tkinter import messagebox
import pandas as pd
import matplotlib.pyplot as plt
import random
import os

# Simulated script1: Replace with actual voltage-reading code
def run_script1():
    return round(random.uniform(3.0, 5.0), 2)

# File paths
file_plant1 = 'plant1_data.csv'
file_plant2 = 'plant2_data.csv'

# Data storage
days_plant1, voltages_plant1 = [], []
days_plant2, voltages_plant2 = [], []

# Load existing data
def load_data():
    global days_plant1, voltages_plant1, days_plant2, voltages_plant2
    if os.path.exists(file_plant1):
        df1 = pd.read_csv(file_plant1)
        days_plant1 = df1['Day'].tolist()
        voltages_plant1 = df1['Voltage'].tolist()
    if os.path.exists(file_plant2):
        df2 = pd.read_csv(file_plant2)
        days_plant2 = df2['Day'].tolist()
        voltages_plant2 = df2['Voltage'].tolist()

# Save data to CSV
def save_to_csv():
    pd.DataFrame({'Day': days_plant1, 'Voltage': voltages_plant1}).to_csv(file_plant1, index=False)
    pd.DataFrame({'Day': days_plant2, 'Voltage': voltages_plant2}).to_csv(file_plant2, index=False)

# Save new entry
def save_data():
    day = day_entry.get()
    plant = plant_var.get()
    
    if not day:
        messagebox.showerror("Input Error", "Please enter a day.")
        return

    voltage = run_script1()

    if plant == "Plant 1":
        days_plant1.append(day)
        voltages_plant1.append(voltage)
    elif plant == "Plant 2":
        days_plant2.append(day)
        voltages_plant2.append(voltage)

    save_to_csv()  # Save to file immediately

    messagebox.showinfo("Data Saved", f"{plant}: Day {day}, Voltage {voltage}V saved.")
    day_entry.delete(0, tk.END)

# Plot data
def show_plot():
    plant = plant_var.get()

    if plant == "Plant 1":
        if not days_plant1:
            messagebox.showerror("No Data", "No data for Plant 1.")
            return
        df = pd.DataFrame({'Day': days_plant1, 'Voltage': voltages_plant1})
    elif plant == "Plant 2":
        if not days_plant2:
            messagebox.showerror("No Data", "No data for Plant 2.")
            return
        df = pd.DataFrame({'Day': days_plant2, 'Voltage': voltages_plant2})
    
    # Plot
    plt.figure(figsize=(8, 5))
    plt.plot(df['Day'], df['Voltage'], marker='o', linestyle='-')
    plt.xlabel("Day")
    plt.ylabel("Voltage (V)")
    plt.title(f"Voltage vs Day - {plant}")
    plt.grid(True)
    plt.tight_layout()
    plt.show()

# GUI setup
root = tk.Tk()
root.title("Plant Voltage Logger")

# Load any existing data
load_data()

tk.Label(root, text="Enter Day:").grid(row=0, column=0, padx=10, pady=10)
day_entry = tk.Entry(root)
day_entry.grid(row=0, column=1, padx=10, pady=10)

plant_var = tk.StringVar(value="Plant 1")
tk.Label(root, text="Select Plant:").grid(row=1, column=0, padx=10, pady=10)
plant_menu = tk.OptionMenu(root, plant_var, "Plant 1", "Plant 2")
plant_menu.grid(row=1, column=1, padx=10, pady=10)

save_button = tk.Button(root, text="Save Voltage", command=save_data)
save_button.grid(row=2, column=0, columnspan=2, pady=10)

plot_button = tk.Button(root, text="Show Plot", command=show_plot)
plot_button.grid(row=3, column=0, columnspan=2, pady=10)

root.mainloop()
