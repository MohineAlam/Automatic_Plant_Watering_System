## librairesdays_since_laste_watered2
import json
from decision_tree_ml import build_tree
from decision_tree_ml import predict
from test_sensor import read_sensor
from test_pump import run_pump
from datetime import datetime, timedelta
import explorerhat
import sys
import time
import numpy as np

if len(sys.argv) != 3:
        print("Correct usage: python ml_whentowater_custom.py diary.json volt_threshold")
        sys.exit(2)

# training data-set
x = [] # import data from plant diary
y = [] # has plant been watered in the last 24hrs? 1 = yes , 0 = no ** model will give prediction in 1 or 0

# load plant data - must be one plant at a time
plantdiary = json.load(open(sys.argv[1]))
volt_threshold = sys.argv[2]


# time parser
def time_parser(day):
        time = datetime.fromisoformat(day)
        return time

# watered days
watered_days = []

# loop through metrics of the plant (day, voltage, water_day, water_voltage)
for plant, metrics in plantdiary.items():
        # plant watered and voltage taken
        for index in range(len(metrics["water_day"])):
                wt = time_parser(metrics["water_day"][index])
                watered_days.append(wt)
        # plant voltage and day taken
        for index in range(len(metrics["day"])):
                 # parse_date creates = (2026, 01, 23, 21, 55, 09) date format
                time = datetime.fromisoformat(metrics["day"][index])
                # humidity of each day
                humidity = metrics["voltage"][index]
                # water_day that was recored before current time
                past_watering = [wt for wt in watered_days if wt < time]
                # how many days ago was the plant last watered comapred to current time
                days_since_last_watered = (time - max(past_watering)).days if past_watering else 1000
                # returns true or false if any water_day in list is within the next 24 hrs of the current time
                watered_soon = any(time < wt < time + timedelta(hours=24) for wt in watered_days)

                # append x and y values
                x.append([humidity, days_since_last_watered, time.hour])
                y.append(1 if watered_soon is True or humidity < 0.1 else 0)

# build a tree with plant diary
x = np.array(x)
y = np.array(y)
tree = build_tree(x,y)

# take measurement of plant and populate list
x2 = []
# voltage
#humidity = read_sensor()
humidity = 0.01
# date stamp
day = datetime.now().isoformat()
time2 = time_parser(day)
# days since last watered
days_since_laste_watered2 = ((time2 - max(watered_days)).days if watered_days else 1000)
# append to x2
x2.append([humidity, days_since_laste_watered2, time2.hour])
x2 = np.array(x2)
# create prediction
prediction = predict(x2, tree)

if prediction == 1:
	# activate pump
	print("Plant needs watering! :(")
	run_pump()
	print("Plant successfully watered! :)")
elif prediction == 0:
	# message to keep pump off
	print("No watering needed! :)")
	print(f"Humidity value: {humidity}")
else:
	# error message
	print("There was an error! :(")
	sys.exit(1)
