
# optional GUI usage - For now only testing scripts are in GUI
import tkinter as tk
import subprocess

# test explorer hat
def test_eh():
  subprocess.run(["python3","/path/to/test_explorerhat.py"])

# test soil sensor
def test_sen():
  result = subprocess.run(["python3","/path/to/test_sensor.py"],
                         stdout=subprocess.PIPE,
                          text=True
                         )
  output = result.stdout.strip()
  voltage_label.config(text=output)

# test water pump
def test_pump():
  subprocess.run(["python3","/path/to/test_pump.py"])

# create the main window
root = tk.Tk()
root.title("Automatic Watering System")
root.geometry("600x300") # width x height

#==============#
# add buttons and labels
#=======================#

# explorer hat
btn1 = tk.Button(root, text="Test Explorer Hat", command=test_eh, height=2, width=20)
btn1.pack(pady=10)

# soil sensor
btn2 = tk.Button(root, text="Test Soil Sensor", command=test_sen, height=2, width=20)
btn2.pack(pady=10)
voltage_label = tk.Label(root, text="Voltage: N/A", font=("Arial",14))
voltage_label.pack(pady=10)

# water pump
btn3 = tk.Button(root, text="Test Water Pump", command=test_pump, height=2, width=20)
btn3.pack(pady=10)

# Rrun GUI loop
root.mainloop()
