# Automatic-Plant-Watering-System with Raspberry Pi
 (In this tutorial the moisture sensor will be made from scratch and the water pump will be modified to make it safer. The sensor will be more robust compared to a lot of commercial sensors that tend to oxidise! Although you can alternatively purchase a ready made sensor as well as a ready made pump:))

## Material you will need:
### Single board computer and expansions
 - Raspberry Pi
 - Explorer hat pro
 - Micro SD card and Micro SD adapter
### Water pump materials
 - Submersible water pump (no more than 5V)
 - Tubing for the water pump
 - 1K ohm resistor
 - Diode 1N400
 - Transitor
 - Jumper wires
 - Container/pot to hold wter and store the water pump
### Moisture sensor materials
 - Galvanised screws (2x)
 - 10k ohm resistor
 - Jumper wires
 
## Software Set Up Steps (for Linux systems - Ubuntu/Debian-based):
### Set up the Raspberry Pi
### - Encrypt MicroSD card with Raspberry Pi OS
  - You can do this from the Raspberry Pi official website using the micro SD adapter - download the imager
  - You can now set up the Raspberry Pi hardware - in the hardware set up steps
### - Install python
 - open up the terminal and run the following commands in your virtual environment:
	sudo apt update
	sudo apt install python3
	sudo apt install python3-pip
	python3 --version
 - if the python version is shown, python has successfully been installed
        sudo apt install python3
### - Install R - optional, you can also parse data in python
 - follow this website to download the correct version of R for you:
        https://cran.r-project.org/
### - Install virtual environment
 - Set up a virtual environment to set up your automatic watering system, following the commands:
	sudo apt install python3-venv
	mkdir Automatic_Watering_System
	cd Automatic_Watering_System
	python -m venv myenv
 - within "myenv" (source myenv/bin/activate) you avoid virtual environment interfering with the system Python or other environments
### - Install Explorer Hat Pro
 - Install the explorer hat pro library in the virtual environment:
        pip install explorerhat

## Hardware Set Up Steps - Set up the Raspberry Pi
### - MicroSD
 - insert the SD card into the Raspberry Pi SD slot
### - Explorer Hat Pro
 - insert the 40 pin GPIO connector ontop of the pins on the Raspberry Pi
 - stick the bread board ontop of the Explorer Hat Pro
### - Wires, monitor, keyboard, and mouse
 - connect the power supply to the Raspberry Pi power port
 - connect the HDMI cable to the Raspberry Pi HDMI port and the other end to the computer monitor port
 - connect the keyboard and mouse to the Raspberry Pi using the USB port 
 - your Raspberry Pi can now be accessed
#### find the rest of the hardware steps to make the sensor, modify the pump, and set up the parts on the Raspberry Pi in the wiki tutorial!

## Test Runs Using Repository Scripts (after complete hardware set up)
 - Copy the github repository into your virtual enviornment using the clone link
### - To check that the explorer hat has been connected to the 40 pin GPIO connector on the Raspberry Pi correctly:
 - Make sure you have placed the hat with the bread board ontop of the Pi before the next step
 - Run the command: 
	python test_explorerhat.py
 - You should see all three LED colours flash and a message to you
### - To check that the water pump has been connected to the motor port correctly:
 - Place the water pump inside a container with water and the plastic tubing inside a recipient container 
 - Run the command: 
	python test_pump.py
 - The terminal should show you two messages and water should be pumped into the empty container for 5 seconds
### - To check that the moisture sensor has been made correctly and connected to the analog one, output one and ground correctly
 - Make sure all the jumper wires are in the correct terminals and the screws are inside the soil of your plant
 - Run the command:
	python test_sensor.py 
 - The terminal should show you a message and the voltage from your sensor
### - To check that the sensor and pump communicate correctly
 - Run the command:
	python test_pump_sensor_communication.py
 - If the pump and sensor communicate successfully, you should see messages on the terminal, the voltage unit, and (if the plant needs watering) the pump switched on
