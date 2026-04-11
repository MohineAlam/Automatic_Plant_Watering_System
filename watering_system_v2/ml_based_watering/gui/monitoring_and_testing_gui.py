import tkinter as tk
import subprocess
import csv
import os
import json
import sys
from collections import defaultdict
from test_sensor import read_sensor
from tkcalendar import DateEntry
from datetime import datetime

# error handling for usage
if len(sys.argv) < 2:
        print("Usage: automatic_watering_launcher.py json_file/none")
        print("If you do not have a json file, write 'none'")
        sys.exit(2)

#===================================#
# Open json file
#===================================#
plant_monitor_diary = sys.argv[1]
basename = os.path.basename(plant_monitor_diary)

if os.path.exists(plant_monitor_diary):
	with open(plant_monitor_diary, "r") as f:
		diary = json.load(f)
elif plant_monitor_diary == "none":
	print("You do not have a json file to store your plant diary, let's create one.")
	filename = input("Enter the name you want to save your diary as e.g. 'diary' : ")
	if filename != "":
		with open(filename + ".json", "w") as f:
			json.dump({}, f)
		with open(filename + ".json", "r") as f:
			diary = json.load(f)
	else:
		print("You have exited")
		print("(Your need to enter a name)")
		sys.exit(1)
elif plant_monitor_diary == "test":
	print("You are in testing mode")
else:
	print("Usage: automatic_watering_launcher.py json_file/none")
	print("If you do not have a json file write 'none'")
	sys.exit(1)

#======================================#
# functions for GUI and diary addition
#======================================#

# test soil sensor
def test_sen():
        result = subprocess.run(["python3", "test_sensor.py"],
        capture_output=True,
        text=True
        )
        print(result.stdout)
        voltage_label.config(text=read_sensor())
        return result

# test water pump
def test_pump():
        result = subprocess.run(["python3", "test_pump.py"])
        print(result.stdout)
        return result

# print keys if requested
def request_names():
	if diary.keys():
		print(f"These are the plant names found in {basename}: ")
		for plant in diary.keys():
			print(f"{plant}")
	else:
		print("There are no plants recorded in your diary.")

# date time format convert
def get_time_stamp(day_entry):
	date_string = day_entry # get day entry which is in this format: day - month - year
	# tell datetime your format and then convert it to (y, m, d, h=0, s=0, m=0)
	date_object = datetime.strptime(date_string, "%d-%m-%Y")
	# current time
	now = datetime.now()
	# replace h, m, s with actual time
	timestamp = date_object.replace(
		hour=now.hour,
		minute=now.minute,
		second=now.second
	)

	# return string "y-m-d T h-m-s"
	return timestamp.isoformat()

# create dictionary key
plant_dict = lambda : {"day" : [], "voltage": [], "water_day": [], "water_voltage": []}

def save_humidity_data():
	# retrieve input values
	day = get_time_stamp(day_entry.get())
	plant = plant_entry.get()
	volts = read_sensor()

	# store data
	if day != "" and plant != "":
		if plant not in diary:
			diary[plant] = plant_dict()
		diary[plant]["day"].append(day)
		diary[plant]["voltage"].append(volts)

		tmp = plant_monitor_diary + ".tmp"
		with open(tmp, "a") as file:
			json.dump(diary, file, indent=4)
		os.replace(tmp, plant_monitor_diary)

		print(f"Entry added - {plant}: ({day}, {volts})")
		day_entry.delete(0, tk.END)

	else:
		print("You have not entered a day / plant name")

def save_watered_humidity_data():
	# activate pump
	test_pump()

	# measure voltage
	while True:
		answer = input("Ready to measure voltage? (enter: y (yes) / w (wait) / anything else to exit)")
		if answer == "y":
			volts = read_sensor()

			break
		elif asnwer == "w":
			continue
		else:
			print("You have exited the measurment.")
			volts = 0

	# retrieve input
	plant = plant_entry.get()
	day = get_time_stamp(day_entry.get())
	if plant != "" and day != "":
		if plant not in diary:
			diary[plant] = plant_dict()
		diary[plant]["water_day"].append(day)
		diary[plant]["water_voltage"].append(volts)

		tmp = plant_monitor_diary + ".tmp"
		with open(tmp, "w") as f:
			json.dump(diary, f, indent=4)
		os.replace(tmp, plant_monitor_diary)
		print(f"Entry added - {plant} : ({day}, {volts})")
	else:
		print("You have not entered a day / plant name")

#########################
# create the main window
#########################
root = tk.Tk()
root.title("Automatic Watering System")
root.geometry("600x600") # width x height

#=======================#
# add buttons and labels
#=======================#

########## TEST BUTTONS ##########

# soil sensor
btn2 = tk.Button(root, text="Test Soil Sensor", command=test_sen, height=2, width=20)
btn2.grid(row=2, column=0, pady=10, padx=10)
voltage_label = tk.Label(root, text="Voltage: N/A", font=("Arial",14))
voltage_label.grid(row=2, column=1,pady=10, padx=10)

# water pump
btn3 = tk.Button(root, text="Test Water Pump", command=test_pump, height=2, width=20)
btn3.grid(row=3, column=0, pady=10, padx=10)

########## DATA COLLECTION BUTTONS ##########

#============= create new frame
#frame = tk.Frame(root, width=600, height=600)
#frame.pack(padx=10, pady=10)
#nested_frame = tk.Frame(frame, width=600, height=)

# enter which plant you want to monitor humidity
tk.Label(root, text="Enter Plant Name: ").grid(row=5, column=0, padx=10, pady=10)
#plant_menu = tk.OptionMenu(root, plant_var, "Plant 1", "Plant 2")
plant_entry = tk.Entry(root)
plant_entry.grid(row=5, column=1, padx=10, pady=10)

# saving voltage button
save_button = tk.Button(root, text="Save Voltage", command=save_humidity_data)
save_button.grid(row=7, column=0, pady=10, padx=10 )

# record wet soil voltage
record_wet_soil_button = tk.Button(root, text="Record Wet Soil Voltage", command=save_watered_humidity_data)
record_wet_soil_button.grid(row=8, column=0, padx=10, pady=10)

#Day input
tk.Label(root, text="Select Day:").grid(row=4, column=0, padx=10, pady=10)
day_entry = DateEntry(root, width=12, date_pattern="dd-mm-yyyy")
day_entry.grid(row=4, column=1, padx=10, pady=10)

# request plant names if the json file
name_button = tk.Button(root, text="Current Plants in Diary", command=request_names)
name_button.grid(row=6, column=0, padx=10, pady=10)

#=============================#
# data storage and graphing
#=============================#


# Run GUI loop
root.mainloop()
