#!/usr/bin/bash
source /home/Mohin3/myenv/bin/activate

# json input or "none"
input="$1"

if [[ -n "$1" ]]; then
	# run script to launch GUI
	python3 monitoring_and_testing_gui.py "$input"
else
	echo "You need an input json file or enter 'none'"
fi
