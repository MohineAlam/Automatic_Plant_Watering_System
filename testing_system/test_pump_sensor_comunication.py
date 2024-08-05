# import your libraries
import explorerhat
import time

# message to user
user_input = input("Place the screws (electrodes) into the soil of your plant, 5cm apart. Attach the pump tubing securely over the soil. Once you are ready press "y", otherwise press "n" to exit.")
print(user_input)

# sensor function
def sensor():
	if user_input == "y":
		print("Running water pump and sensor communication test...")
		explorerhat.output.one.on()
		time.sleep(1)
		read = explorerhat.analog.one.read()
		explorerhat.output.one.off()
		return read
	else:
		print("Test has been cancelled, run the script again if you want to test the communication between sensor and pump!")
		sys.exit()

# pump function with sensor function integrated
def pump():
	sensor_value = read
	saturated_soil = 0.4 # modify based on your plant
	dry_soil = 0.04 # modify based on your plant
	print(f"Your sensor value reads at: {sensor_value}V.")
	if sensor_value >= saturated_soil:
		print("Your plant is not thirsty! No watering is needed right now :)")
	elif sensor_value <= dry_soil:
		print("Your plant is thirsty! Watering your plant now :)")
		explorerhat.motor.one.forwards()
               	time.sleep(3)
               	explorerhat.motor.one.off()
		print("The thirst is quenched! Green love <3")
	elif dry_soil < sensor_value < saturated_soil: 
		print("Your plant will be due for a watering soon! No need to worry right now :)")

# call pump() to execute function
pump()
print("The pump and sensor communication was a success! You can now switch on the automatic watering system!")
