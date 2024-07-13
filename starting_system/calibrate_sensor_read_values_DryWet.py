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
	user_prompt = input("Ready? Place the electrodes (screws) into the dry soil of your plant, once you're ready press (y) to continue or (n) to exit.")
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
	else:
		print("Run script again to re-start")
		return False


# method for measuring wet soil
def sensor_switch_wet():
	user_prompt = input("Now lets measure the wet soil! Pour water into the soil until its saturated. Press (y) once you're ready or (n) to exit.")
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
	else:
               	print("Run script again to re-start")
               	return False


# execution of functions:
if sensor_switch_dry() is not False:
	if sensor_switch_wet() is not False:
		print("Measurements completed successfully!")
	else:
		print("Wet soil measurement was not performed!")
else:
	print("Dry soil measurement was not performed!")
sys.exit()
