# import your libraries
import explorerhat
import time

# read humidity from sensor - this should be attached to analogue one
def read_sensor():
	explorerhat.output.one.on()
	time.sleep(1)
	read = explorerhat.analog.one.read()
	explorerhat.output.one.off()
	return read

# return read
if __name__ == "__main__":
	print("Running sensor test...")
	sensor_value = read_sensor()
	print(f"The voltage from your sensor is: {sensor_value}")
