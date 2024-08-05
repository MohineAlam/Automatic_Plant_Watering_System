# import libraries
import explorerhat

print("Explorer hat pro test run in progress...")

# switch on all four explorer hat pro LEDs 
def explorerhat_test(): 
 explorerhat.light.yellow.on()
 explorerhat.light.blue.on()
 explorerhat.light.red.on()
 explorerhat.light.green.on()
 print("Did you see the flash? If so, the explorer hat pro is working fine!")

explorerhat_test()
