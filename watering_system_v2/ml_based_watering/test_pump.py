import time
import explorerhat
import sys


def run_pump():
	print("Connect your pump to the explorerhat, submerge the pump in water, and place the pump tube inside an empty container.")
	user_input = input("Once you are ready press (y), or (n) to exit.").strip().lower()
	if user_input == "y":
		print("Pump ON.")
		explorerhat.motor.one.forward(50)
		time.sleep(5)
		explorerhat.motor.one.stop()
		print("Pump OFF.")

	elif user_input == "n":
		print("You have terminated the test.")
	else:
		print("Invalid input.")
		sys.exit()

if __name__ == "__main__":
	run_pump()
	sys.exit()
