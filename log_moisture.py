import explorerhat
import time
import datetime
import csv

# convert reading into humidity
def convert_to_humidity(analogue_value):
	min_analogue = 0.04 #dry soil read
	max_analogue = 0.40 #saturated soil read
	min_humidity = 0
	max_humidity = 100
	humidity = (analogue_value - min_analogue) * (max_humidity - min_humidity) / (max_analogue - min_analogue) + min_humidity
	return humidity

log_file = 'mositure_log.csv'
threshold = 10 # set a threshold
# create log file nd set up csv writer
with open(log_file, mode='w', newline='') as file:
	writer = csv.writer(file)
	writer.writerow(["Time Stamp", "Analogue Value", "Humidity", "Pump Status"])

# Pump control
while True:
# switch on humidity sensor
	explorerhat.output.one.on()
	time.sleep(2)
	analogue_value =  explorerhat.analog.one.read()
	humidity = convert_to_humidity(analogue_value)
	if humidity < threshold:
		explorerhat.output.two.on()
		time.sleep(3)
		explorerhat.output.two.off()
		pump_status = "ON"
	timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
	else:
		print("Your plant is not thirsty! :)")
		pump_status = "OFF"
	timestap = datetime.datetime.now()strftime("%Y-%m-%d %H:%M:%S")

	# log data in .csv file
	with open(log_file, mode = 'a', newline =  '') as file:
		writer = csv.writer(file)
		writer.writerow([timestamp,analogue_value,humidity,pump_status])
	time.sleep(604800) # 1 week
