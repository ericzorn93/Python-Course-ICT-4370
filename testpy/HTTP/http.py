import requests
import json

# Simple Get Request to the Open Weather API
r = requests.get('http://samples.openweathermap.org/data/2.5/weather?q=London&appid=b6907d289e10d714a6e88b30761fae22')

# Parses Text Response from JSON data in the Open Weather API
j = json.loads(r.text)

# Retrieved clouds key from JSON dictionary and value of clouds dictionary
amt_clouds = j['clouds']['all']

# Prints a formatted string of cloud information from the API that is dynamically updated
print("There are {0} clouds outside right now".format(amt_clouds))


