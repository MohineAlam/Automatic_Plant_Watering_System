from flask import Flask, render_template
import json
import sys
# graphs function
from plotly_graphs import multi_line_graph


# plant diary input:
input_data = json.load(open(sys.argv[1]))

# create app
app = Flask(__name__)

@app.route("/")
# graph input - load graphs
def dashboard():

	# line graph - import and call line graph using imput

	# multi line graph - import and call graph using input
	m_line_graph = multi_line_graph(input_data)
	m_line_html = m_line_graph.to_html(full_html = False)
	# box graph -

	# other grah -


	return render_template("dashboard_template.html", graph=m_line_html)
# run app
app.run(host = "0.0.0.0", port=5000)

