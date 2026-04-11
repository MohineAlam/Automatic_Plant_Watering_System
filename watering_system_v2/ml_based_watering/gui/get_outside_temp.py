# library
import requests
from dotenv import load_dotenv
import os

# function to retrieve temperature outside
def get_outside_temp():
	# location variable
	load_dotenv()
	LAT = os.getenv("LATITUDE")
	LONG = os.getenv("LONGITUDE")

	# params
	url = "https://api.open-meteo.com/v1/forecast"
	params = {
		"latitude" : LAT,
		"longitude" : LONG,
		"current_weather" : True
	}
	# make requests
	r = requests.get(url=url, params=params)
	data = r.json()

	return data["current_weather"]["temperature"]

if __name__ == "__main__":
	temp = get_outside_temp()
	print(temp, "*C")
