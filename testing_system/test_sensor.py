# import your libraries
import explorerhat
import time
# message to user
print("Running sensor test...")
# read humidity from sensor - this should be attached to analogue (analog) one
def read_sensor():
	explorerhat.output.one.on()
	time.sleep(1)
	read = explorerhat.analog.one.read()
	explorerhat.output.one.off()
	return read

# return read
sensor_value = read_sensor()
print(f"The voltage from you sensor is: {sensor_value}V.")
print("Your sensor is functioning as normal. Remember to test both dry and wet soil! Use the sensor_read_output.py script :)")
