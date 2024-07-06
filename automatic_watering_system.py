import explorerhat
import time


# method to convert sensor read to humidity
def convert_to_humidity(analog_value):


# define a threshold of humidity
threshold = **

# method to siwtch pump on based on humidity sensor 
while True: #continuous loop
	explorerhat.output.one.on()
	time.sleep(0.5) # wait for voltage to stabalise
	analog_value = explorerhat.analog.one.read()
	humidity = convert_to_humidity(analog_value)
	print("Your analogue value is: {}, and you humidity value is: {}".format(analog_value,humidity))
	explorerhat.output.one.off()
	if humidity < threshold:
		explorerhat.output.two.on()
	else:
		explorerhat.output.two.off()
	time.sleep(604800) # check again in a week
