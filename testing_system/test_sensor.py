# import your libraries
import explorerhat
import time
import sys

# ask if user is ready
user_ready = input("Place the electrodes (screws) into the soil of your plant, 5cm apart. When you are ready press (y) to continue or (n) to exit: ").strip().lower()

# read humidity from sensor - this should be attached to analogue (analog) one
def read_sensor(user_ready):
	if user_ready == "y":
		explorerhat.output.one.on()
		time.sleep(1)
		read = explorerhat.analog.one.read()
		explorerhat.output.one.off()
		return read
	else:
		print("The sensor test has been halted and exited. Run the script again to test the sensor.")
		return None
# return read
sensor_value = read_sensor(user_ready)

if sensor_value is not None:
	print(f"The voltage from your sensor is: {sensor_value:.2f}V.")
	print("Your sensor is functioning as normal. Remember to test both dry and wet soil! Use the sensor_read_output.py script :)")
else:
	print("Sensor value could not be read, ensure set up is correct and try again!")

sys.exit()
