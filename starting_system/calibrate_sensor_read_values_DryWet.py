import explorerhat
import time
import datetime
import csv
import sys

# make csv file
log_file = "humidity_calibration_log.csv"
with open(log_file, mode = "w", newline = "") as file:
        writer = csv.writer(file)
        writer.writerow(["Condition","Value"])


# method for measuring dry soil
def sensor_switch_dry():
	while True:
		user_prompt = input("Ready? Place the electrodes (screws) into the dry soil of your plant, once you're ready press (y) to continue or (n) to exit.").strip().lower()
		if user_prompt == "y":
			condition = "Dry Soil"
			explorerhat.output.one.on()
			time.sleep(2)
			value = explorerhat.analog.one.read()
			explorerhat.output.one.off()
			print("The dry soil value has been recorded in the humidity_log file as: {}V.".format(value))
			with open(log_file, mode = "a", newline = "") as file:
	                	writer = csv.writer(file)
        	        	writer.writerow([condition,value])
			break
		elif user_prompt == "n":
			print("Run script again to re-start")
			return False
		else:
			print("Invalid input... press (y) to continue or (n) to exit.").strip().lower()

# method for measuring wet soil
def sensor_switch_wet():
	while True:
		user_prompt = input("Now lets measure the wet soil! Pour water into the soil until its saturated. Press (y) once you're ready or (n) to exit.").strip().lower()
		if user_prompt == "y":
                	condition = "Wet Soil"
                	explorerhat.output.one.on()
                	time.sleep(2)
                	value = explorerhat.analog.one.read()
                	explorerhat.output.one.off()
                	print("The wet soil value has been recorded in the humidity_log file as: {}V.".format(value))
			with open(log_file, mode = "a", newline = "") as file:
                        	writer = csv.writer(file)
                        	writer.writerow([condition,value])
			break
		elif user_prompt == "n":
               		print("Run script again to re-start")
               		return False
		else:
			print("Invalid input... Press (y) to continue or (n) to exit")

# execution of functions:
if sensor_switch_dry() is not False: # call sensor_switch_dry() function
	if sensor_switch_wet() is not False: # calls sensor_swtich_wet() function if first function is called
		print("Measurements completed successfully! Make sure the .csv file has correctly recorded the soil measurements.")
	else:
		print("Wet soil measurement was not performed!")
else:
	print("Dry soil measurement was not performed!")
sys.exit()
