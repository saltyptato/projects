# Imports
import json, os, requests

# Set secrets
WEATHER_API_KEY = os.getenv("WEATHER_API_KEY") #grabbing from system variables


# Inputs
lat = input("Enter your latitude: ")
lon = input("Enter your longitute: ")
# TODO: make input validation

# API calls
response = requests.get(f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={WEATHER_API_KEY}").json() #Turning response into a json object

# Outputs

#Checking if the response code is 200
if response["cod"] == 200:
    print(response)
else:
    print("Something went wrong")
