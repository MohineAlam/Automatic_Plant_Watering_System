#!/usr/bin/python
# libraries
import json
import matplotlib.pyplot as plt
import sys
import os

# plot line graph: x = humidity, y = plant

#===============================#
# read json file
#===============================#
input = json.load(open(sys.argv[1]))

#===============================#
# create figure to populate
#===============================#
plt.figure(figsize=(12,8))
# colours for samples
colours = "tab10"
colour_palette = plt.get_cmap(colours)
index = 0

#===============================#
# unpack json
#===============================#
for plant, metrics in input.items():
	# create plant index
	index += 1
	# colour by index
	colour = colour_palette(index % 10)
	# order by days
	days = metrics["day"]
	volts = metrics["voltage"]
	paired = list(zip(days, volts)) # creates tupple list = [(day,volt), (day,volt), (day,volt)]
	paired_ordered = sorted(paired, key=lambda x: x[0]) # sort based on first value of each tuple (day=0, volt=1)
	days_sorted, voltage_sorted = zip(*paired_ordered) # unpack again to plot and zip = (day, day, day), (volt, volt, volt)

	# plot x and y values
	plt.plot(days_sorted,voltage_sorted,lw=2, color=colour)
	# annotate samples
	label = f"{plant}"
	x = days_sorted[-1]
	y = voltage_sorted[-1]
	plt.annotate(label,(x, y))

	# annotate watetered value
	days_watered = metrics["water_day"]
	volts_watered = metrics["water_voltage"]
	paired2 = list(zip(days_watered, volts_watered))
	paired2_ordered = sorted(paired2, key=lambda x: x[0])
	days_sorted2, voltage_sorted2 = zip(*paired2_ordered)
	plt.plot(days_sorted2, voltage_sorted2, marker='o', linestyle='None' , color="blue")
	label2 = f"{plant} watered"
	for x in days_sorted2:
		for y in voltage_sorted2:
			plt.annotate(label2, (x, y))

# label axis and show plot
plt.xlabel("Day")
plt.ylabel("Humidity")
plt.title("Plant humidity diary")
plt.grid(True)
plt.tight_layout()
plt.show()

outputpath = os.path.dirname(sys.argv[1])
outfile = os.path.join(outputpath, "plant_diary.png")
plt.savefig(outfile, dpi=300, bbox_inches="tight")











































