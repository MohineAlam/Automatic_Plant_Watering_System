# import libraries
import explorerhat
import sys

user_input = input("Do you want to run the explorer hat test? If so press (y), if not press anything else to exit: ").strip().lower()

# switch on all four explorer hat pro LEDs 
def explorerhat_test(question):
	print("Explorer hat pro test run in progress...")
	if question == "y":
		explorerhat.light.yellow.on()
		explorerhat.light.blue.on()
		explorerhat.light.red.on()
		explorerhat.light.green.on()
		print("Did you see the flash? If so, the explorer hat pro is working fine!")
	else:
		print("You have exited the test. Run the script again to test the Explorer hat pro.")

# call the function and exit system
explorerhat_test(user_input)
sys.exit()
