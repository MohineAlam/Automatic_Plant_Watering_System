# library
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# mult line graph
def multi_line_graph(input_data):

	# empty row variable to store data frame vaules
	rows = []

	# flatten json file
	for plant, metrics in input_data.items():

		for d, v in zip(metrics["day"], metrics["voltage"]):
			rows.append({
				"plant" : plant,
				"day" : d,
				"voltage" : v,
				"type" : "measurement"
			})

		for d, v in zip(metrics["water_day"], metrics["water_voltage"]):
			rows.append({
				"plant" : plant,
				"day" : d,
				"voltage" : v,
				"type" : "watered"
			})

		# create data frame
		df = pd.DataFrame(rows)

		# create line graph
		fig = px.line(
			df[df["type"] == "measurement" ],
			x = "day",
			y = "voltage",
			color = "plant",
			title = "Humidity vs Day"
		)

		# add water points
		watered_df = df[df["type"] == "watered"]
		fig.add_scatter(
			x = watered_df["day"],
			y = watered_df["voltage"],
			mode = "markers",
			marker = dict(size=10),
			name = "watered"
		)

		return fig


# multi plant box plot of voltage/moisture
def multi_boxplot(input_data):
	# empty list to store df
	rows = []
	# parse json file
	for plant, metrics in input_data.items():
		# extract dry voltage
		for v in metrics["voltage"]:
			rows.append({
				"plant" : plant,
				"voltage" : v,
				"type" : "not watered"
			})
		for v in metrics["water_voltage"]:
			rows.append({
				"plant" : plant,
				"voltage" : v,
				"type" : "watered"
			})
	# create data frame from list
	df = pd.DataFrame(rows)

	# create box plot
	fig = px.box(
		df,
		x = "plant",
		y = "voltage",
		points = "all",
		color = "type",
		title = "Watered vs Not Watered"
	)

	return fig

