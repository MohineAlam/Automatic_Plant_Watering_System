# Automatic-Plant-Watering-System with Raspberry Pi

## Material you will need:
 - Raspberry Pi
 - Explorer hat pro
 - jumper wires
 - submersible water pump
 - tubing for the water pump
 - humidity sensor

## Software Set up Steps:
### - encrypt MicroSD card with Raspberry Pi OS
  - You can do this from the Raspberry Pi official webstie - download the imager
### - install Docker and Docker Compose
 - set up a virtual environment for docker compose - import and use yaml in Python scripts within "myenv" (source myenv/bin/activate). Avoiding virtual environment interfering with the system Pyhon or other environments
### - install explorer hat pro
 - install the explorer hat pro library in the virtual environment - (pip install explorerhat)

## Test runs
### - To check that the explorer hat has been connected to the 40 pin GPIO connector on the Raspberry Pi correctly:
 - Make sure you have placed the hat with the bread board ontop of the Pi before the next step
 - run the command: python test_explorerhat.py
 - you should see all three LED colours flash
## - To check that the water pump has been connected to the motor port correctly:
 - place the water pump inside a container with water and the plastic tubing inside a recipient container 
 - run the command: python test_pump.py
 - the water pump should pump water into the empty container for 5 seconds
