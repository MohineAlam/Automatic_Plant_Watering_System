import explorerhat
import time
import datetime
import csv

# convert reading into humidity
def convert_to_humidity(analogue_value):
	while True:
        	user_prompt = input("Place the pump in the water container (with the tube ontop of the soil of your plant). Place the electrodes (screws) 5cm apart in the soil of your plant. Once you are ready to continue press (y) or (n) to exit").strip().lower()
		if user_prompt == "y":
			min_analogue = "/watering_system/Automatic-Plant-Watering-System/starting_system/.csv" #dry soil read (write the path to the csv document you make from calibrate_sensor_read_values_DryWet.py)
			max_analogue = "/watering_system/Automatic-Plant-Watering-System/starting_system/.csv"  #wet soil read (write the path to the csv document you make from calibrate_sensor_read_values_DryWet.py)
			min_humidity = 0
			max_humidity = 100
			humidity = (analogue_value - min_analogue) * (max_humidity - min_humidity) / (max_analogue - min_analogue) + min_humidity
			return humidity
		elif user_prompt == "n":
			print("Run the script again to restart!")
			return False
		else:
			print("Invalid input... Press (y) to continue or (n) to exit.")

# create log file and set up csv writer
log_file = 'mositure_log.csv'
with open(log_file, mode='w', newline='') as file:
	writer = csv.writer(file)
	writer.writerow(["Time Stamp", "Analogue Value", "Humidity", "Pump Status"])

# Pump control
threshold = 10 # set a threshold
while True:
# switch on humidity sensor
	explorerhat.output.one.on()
	time.sleep(2)
	analogue_value = explorerhat.analog.one.read()
	humidity = convert_to_humidity(analogue_value)
	explorerhat.output.one.off()
	if humidity < threshold:
		print("Your plant is thirsty!!! Watering now...")
		explorerhat.output.two.on()
		time.sleep(3)
		explorerhat.output.two.off()
		print("Finished watering! Your plant is no longer thirsty :D")
		pump_status = "ON"
	else:
		print("Your plant is not thirsty! No need to water right now :)")
		pump_status = "OFF"
	timestamp = datetime.datetime.now()strftime("%Y-%m-%d %H:%M:%S")

	# log data in .csv file
	with open(log_file, mode = 'a', newline =  '') as file:
		writer = csv.writer(file)
		writer.writerow([timestamp,analogue_value,humidity,pump_status])
	time.sleep(10) # 10 seconds - just for testing, change after you have tested
