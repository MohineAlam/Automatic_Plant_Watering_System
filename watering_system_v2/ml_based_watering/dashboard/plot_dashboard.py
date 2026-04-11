from flask import Flask, render_template
import json
import sys
import os
import requests
import subprocess
from datetime import datetime
#from gui.get_outside_temp import get_outside_temp
#from gui.test_sensor import read_sensor

# graphs function
from plotly_graphs import multi_line_graph


# plant diary input:
input_data = json.load(open(sys.argv[1]))

def read_sensor():
	path = os.path.expanduser("~/Automatic_Plant_Watering_System/watering_system_v2/ml_based_watering/gui/test_sensor.py")
	cmd = subprocess.run(["python3", path], capture_output=True, text=True)
	result = cmd.stdout.strip()
	return result

def get_outside_temp():
	path = os.path.expanduser("~/Automatic_Plant_Watering_System/watering_system_v2/ml_based_watering/gui/get_outside_temp.py")
	cmd = subprocess.run(["python3", path], capture_output=True, text=True)
	result = cmd.stdout.strip()
	return result
#============#
# create app
#============#
app = Flask(__name__)

@app.route("/")
# graph input - load graphs
def dashboard():

	# line graph - import and call line graph using imput

	# multi line graph - import and call graph using input
	m_line_graph = multi_line_graph(input_data)
	m_line_html = m_line_graph.to_html(full_html = False)
	# current data
	day = str(datetime.now())
	moisture = read_sensor()
	temperature = get_outside_temp()
	note = None

	return render_template("dashboard_template.html",
		multi_line_graph=m_line_html,
		moisture=moisture,
		temperature=temperature,
		note=note)
#=========#
# run app
#=========#
app.run(host = "0.0.0.0", port=5000)

