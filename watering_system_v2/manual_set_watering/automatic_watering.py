# libraries
import json
import os
import explorerhat
import sys
import subprocess
import time
from datetime import datetime
from run_sensor import read_sensor_one, read_sensor_two


# scripts
pump = "run_pump.py"

# function to run scripts
def run_script(script):
	'''
	calls input scripts
	e.g. python3 run_pump.py
	'''
        cmd = ["python3", script ]
        result = run.subprocess(cmd, capture_output=True, text=True)
        return result

# time stamp
def time_stamp():
	'''
	creates current time stamp in format:
	2026-01-17 19:59:59
	'''
	timestamp = datetime.strftime("Y%-M%-D% H%:M%:S%")
	return timestamp

#==============================#
# input plants - load json files
#==============================#
plants_config = json.load(open("$HOME/watering_system/automatic_watering/settings/plants_config.json"))
plant_tracker = json.load(open("$HOME/watering_system/automatic_watering/plant_tracking/plant_tracker.json"))

#==============================#
# load thresholds and plants
#==============================#
plant1thresh = plants_config["plant1"]["threshold"]
plant2thresh = plants_config["plant2"]["threshold"]

plant1id = plants_config["plant1"]["id"]
plant2id = plants_config["plant2"]["id"]


# create key values for plant dict
tracking_template = lambda : { "timestamp": [], "humidity": [], "action": [] }

#==============================#
# run automatic watering
#==============================#
while True:

	if plant1id:
		# run sensor
		humidity1 = read_sensor_one()
		# if soil is below "dry" threshold - water
		if humidity1 < plant1thresh:
			run_pump = run_script(pump)
			print(f"Low humidty detected for {plant1id} ! Plant soil is dry !")
			print(f"Humidty value of soil: {humidity1}")
			# write results into json plant_tracker
			if plant1id not in plant_tracker:
				plant_tracker[plant1id] = tracking_template()
			plant_tracker[plant1id]["timestamp"].append(time_stamp())
			plant_tracker[plant1id]["humidity"].append(humidity1)
			plant_tracker[plant1id]["action"].append("watered")

		# if soil is above "dry" threshold - don't water
		elif humidity1 > plant1thresh:
			print("No need to water today! :)")
			# write results into json plant_tracker
			if plant1id not in plant_tracker:
				plant_tracker[plant1id] = tracking_template()
			plant_tracker[plant1id]["timestamp"].append(time_stamp())
			plant_tracker[plant1id]["humidity"].append(humidity1)
			plant_tracker[plant1id]["action"].append("none")

	if plant2id:
		# run sensor
		humidity2 = read_sensor_two()
		# if soild is below "dry" threshold - water
		if humidity2 < plant2thresh:
			run_pump = run_script(pump)
			print(f"Low humidity detected for {plant2id} ! Plant soil is dry !")
			print(f"Humidity value of {humidity2}")
			# write results into json plant_tracker
			if plant2id not in plant_tracker:
				plant_tracker[plant2id] = tracking_template()
			plant_tracker[plant2id]["timestamp"].append(time_stamp())
			plant_tracker[plant2id]["humidty"].append(humidity2)
			plant_tracker[plant2id]["action"].append("watered")

		elif humidity2 > plant2thresh:
			print("No need to water today! :)")
			# write results into json plant_tracker
			if plant2id not in plant_tracker:
				plant_tracker[plant2id] = tracking_template()
			plant_tracker[plant2id]["timestamp"].append(time_stamp())
			plant_tracker[plant2id]["humidty"].append(humidity2)
			plant_tracker[plant2id]["action"].append("none")


	# write to json plant tracker
	# write temp file
	tmp = plant_tracker + ".tmp"
	with open(tmp, "w") as file:
		json.dump(plant_tracker, file, indent=4)

	# replace tmp file with plant_tracker
	os.replace(tmp, plant_tracker)

	# exit system
	sys.exit()
