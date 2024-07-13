# import libraries
import explorerhat
import time
import sys

# ask if user is ready
user_ready = input("Place pump into container full of water (make sure it is submerged) and place the pump tube into an empty container. Press (y) if you are ready or (n) to exit...").strip.lower()
print(user_ready)

# Switch on water pump from motor1
def water_pump_test(user_ready):
	print("Running water pump test...")
	speed = 50 # this can be edited for individual needs
	if user_ready == "y":
	 	explorerhat.motor.one.forwards(speed)
	 	time.sleep(5) # switch on for 5 seconds
 		explorerhat.motor.one.stop()
 		print("Pump test was a success!")
	else:
		print("Pump test has been cancelled, run the pipeline again if you would like to test the pump.")


water_pump_test(user_ready)
sys.exit()
