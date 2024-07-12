#import explorerhat
#import time
#import datetime
import csv





# make csv file
log_file = "humidity_log.csv"
with open(log_file, mode = "w", newline = "") as file:
        writer = csv.writer(file)
        writer.writerow(["Condition","Value"])


# ask user if they're ready
user_prompt = input("Ready? Place the electrodes (screws) into the dry soil of your plant, once you're ready press (y) to continue or (n) to exit.")

def sensor_switch(user_prompt):
	if user_prompt == "y":
		condition = "Dry"
		explorerhat.output.one.on()
		time.sleep(2)
		value = explorerhat.analog.one.read()
		explorerhat.output.one.off()
		print("Your dry soil value has been recorded in the humidity_log file as: {}V.".format(value))
	else:
		print("Run script again to start")

	# add to csv file
	with open(log_file, mode = "a", newline = "") as file:
		writer = csv.writer(file)
		writer.writerow([condition,value])

sensor_switch()
