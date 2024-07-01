# Automatic-Plant-Watering-System with Raspberry Pi
 (In this tutorial the moisture sensor will be made from scratch as it is more robust compared to a lot of commercial sensors that tend to oxidise! Although you can alternatively purchase a ready made sensor :))

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
 
## Software Set Up Steps:
### - Encrypt MicroSD card with Raspberry Pi OS
  - You can do this from the Raspberry Pi official website using the micro SD adapter - download the imager
### - Install Docker and Docker Compose
 - Set up a virtual environment for docker compose - import and use yaml in Python scripts within "myenv" (source myenv/bin/activate). Avoiding virtual environment interfering with the system Pyhon or other environments
### - Install Explorer Hat Pro
 - Install the explorer hat pro library in the virtual environment - (pip install explorerhat)

## Test Runs Using Repository Scripts
### - To check that the explorer hat has been connected to the 40 pin GPIO connector on the Raspberry Pi correctly:
 - Make sure you have placed the hat with the bread board ontop of the Pi before the next step
 - Run the command: 
   python test_explorerhat.py
 - You should see all three LED colours flash
## - To check that the water pump has been connected to the motor port correctly:
 - Place the water pump inside a container with water and the plastic tubing inside a recipient container 
 - Run the command: python test_pump.py
 - The terminal should show the message "Running water pump test...", following water pumped into the empty container for 5 seconds, then you should see the message "Pump test was a success!"
## - To check that the moisture sensore has been made correctly and connected to the analog one, output one and ground correctly
 - Make sure all the jumper wires are in the correct terminals and the screws are inside the soil of your plant, you will do this twice for dry and wet soil
 - Run the command:
   python test_sensor.py 
 - The terminal should show the message "Running sensor test..." and "The voltage from your sensor is: (your voltage)"

### - Install python dependencies 

