# import your libraries
import explorerhat
# read humidity from sensor - this should be attached to analogue (analog) one
print("Running sensor test...")
def read_sensor():
 read = input.input.one.read()
 return read

# Add voltage values to dry_voltage (completely dry soil) and wet_voltage (completey saturated soil) variables:
dry_voltage = pass
wet_voltage = pass
def read_soil_moisture():
 current_voltage = read_sensor()
 percentage_moisture = ((current_voltage - dry_voltage) / (current_voltage - wet_voltage)) * 100
 return "The current humidity for your plant is: {percentage_moisture}%"

print(read_soil_moisiture())
