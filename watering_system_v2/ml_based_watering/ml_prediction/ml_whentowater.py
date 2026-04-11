# import ml library
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
import sys
import json
from datetime import datetime, timedelta

# training data-set
x = [] # import data from plant diary
y = [] # has plant been watered in the last 24hrs? 1 = yes , 0 = no ** model will give prediction in 1 or 0

# load plant data - must be one plant at a time
plantdiary = json.load(open(sys.argv[1]))

# time parser
def time_parser(day):
	time = datetime.strptime(day, "%Y-%m-%dT%H:%M:%S")
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
		time = datetime.strptime(metrics["day"][index], "%Y-%m-%dT%H:%M:%S")
		# humidity of each day
		humidity = metrics["voltage"][index]
		# water_day that was recored before current time
		past_watering = [wt for wt in watered_days if wt < time]
		# how many days ago was the plant last watered comapred to current time
		days_since_last_watered = (time - max(past_watering)).days if past_watering else 1000
		# returns true or false if any water_day in list is within the next 24 hrs of the current time
		watered_soon = any(time < wt < time + timedelta(hour=24) for wt in watered_days)

		# append x and y values
		x.append([humidity, days_since_water, time.hours])
		y.append(1 if  watered_soon is True else 0 )

# train test split
xtrain, xtest, ytrain, ytest = train_test_split(
	x,
	y,
	test_size=0.2,
	random_state=42) # less than 100 rows, so 20% of data being tested

#=============#
# train model
#=============#
# set model foundation
clf = RandomForestClassifier(
	n_estimators=100,
	random_state=42,
	max_depth=5
	) ## nestimators = number of decision trees, each tree sees a random subset of data and makes predictions
	## maxdepth = how deep decision tree is allowed to grow - dont want too big as it overfits and memorises data

# train with data set
clf.fit(xtrain, ytrain)

# use x test data set on model to predict y (1 or 0)
ypredict = clf.predict(xtest)

# evaluate model - how correct was it?
print(classification_report(ytest, ypredict))
