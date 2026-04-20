# library
from flask import Flask, render_template
import json
import sys
import os
import requests
import subprocess
from datetime import datetime
from gui.get_outside_temp import get_outside_temp
from gui.test_sensor import read_sensor
from ml_prediction.ml_whentowater_custom import run_model
# graphs function
from dashboard.plotly_graphs import multi_line_graph, multi_boxplot


# plant diary input:
input_data = json.load(open(sys.argv[1]))
h_threshold = sys.argv[2]

#============#
# create app
#============#
app = Flask(__name__)

@app.route("/")
# graph input - load graphs
def dashboard():

	# line graph

	# multi line graph
	m_line_graph = multi_line_graph(input_data)
	m_line_html = m_line_graph.to_html(full_html = False)

	# multi boxplot
	m_boxplot = multi_boxplot(input_data)
	m_boxplot_html = m_boxplot.to_html(full_html = False)

	# current data
	day = str(datetime.now())
	moisture = read_sensor()
	temperature = get_outside_temp()

	# ml prediction
	ml_output = run_model(input_data,h_threshold)

	return render_template("dashboard_template.html",
		multi_line_graph=m_line_html,
		multi_boxplot=m_boxplot_html,
		moisture=moisture,
		temperature=temperature,
		ml_answer=ml_output["message"])
#=========#
# run app
#=========#
app.run(host = "0.0.0.0", port=5000)

