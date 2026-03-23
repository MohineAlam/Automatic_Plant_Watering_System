import time
import explorerhat
import sys

def run_pump():

	print("Turning pump ON.")
	explorerhat.motor.one.forward(50)
	time.sleep(5)
	explorerhat.motor.one.stop()
	print("Pump OFF.")

if __name__ == "__main__":
	run_pump()
	sys.exit()
