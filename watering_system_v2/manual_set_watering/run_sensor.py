# import your libraries
import explorerhat
import time

# read humidity from sensor - this should be attached to analogue one
def read_sensor_one():
	explorerhat.output.one.on()
	time.sleep(1)
	read = explorerhat.analog.one.read()
	explorerhat.output.one.off()
	return read

# read humidty sensor two
def read_sensor_two():
	explorer.output.two.on()
	time.sleep(1)
	read = explorerhat.analog.two.read()
	explorerhat.output.two.off()
	return read

# return read
if __name__ == "__main__":
	print("Running sensor one test...")
	sensor_value_one = read_sensor_one()
	print(f"The voltage from your sensor is: {sensor_value_one}")

	print("Running sensor two test...")
	sensor_value_two = read_sensor_two()
	print(f"The voltage from your sensor is: {sensor_value_two}")
