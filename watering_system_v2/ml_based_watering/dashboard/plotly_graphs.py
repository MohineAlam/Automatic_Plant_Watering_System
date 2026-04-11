import pandas as pd
import plotly.express as px

def multi_line_graph(input_data):

	# empty row variable to store data frame vaules
	rows = []

	# flatten json file
	for plant, metrics in input_data.items():

		for d, v in zip(metrics["days"], metrics["voltage"]):
			rows.append({
				"plant" : plant,
				"days" : d,
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
			title = "Plant humidity diary"
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
