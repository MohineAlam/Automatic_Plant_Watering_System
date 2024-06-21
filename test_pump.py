# import libraries
import explorerhat
import time

print("Running water pump test...")
# Switch on water pump from motor1
speed = 50 # this can be edited for individual needs
def water_pump_test():
 explorerhat.motor.one.forwards(speed)
 time.sleep(5) # switch on for 5 seconds
 explorerhat.motor.one.stop()
 print("Pump test was a success!")

water_pump_test()
