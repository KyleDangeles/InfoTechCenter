print("\n*************************************\n")

print("Weather Branch - Developer: Mr. Lange\n")

#Import Libraries Here!
import random
from time import sleep

#Weather Function to determine the weather
def weather():
    weatherForecastList = ["snowy", "blizzard", "icy", "rainy", "windy", "sunny"]
    weatherCondition = random.choice(weatherForecastList)
    return weatherCondition

weatherAlert = weather()

def vehicleResponseSystem():
    if weatherAlert == "snowy":
        print("\nThe National Weather Service has updated our alarm by 30 minutes because"
        " it is", weatherAlert, "outside.")
    elif weatherAlert == "blizzard":
        print("\nThe National Weather Service has updated our alarm by 60 minutes because"
        " it is a", weatherAlert, "outside!")
    elif weatherAlert == "icy":
        print("\nThe National Weather Service has updated our alarm by 90 minutes because"
        " it is", weatherAlert, "outside.")
    elif weatherAlert == "rainy":
        print("\nThe National Weather Service has updated our alarm by 10 minutes because"
        " it is", weatherAlert, "outside.")
    elif weatherAlert == "windy":
        print("\nThe National Weather Service has updated our alarm by 5 minutes because"
        " it is", weatherAlert, "outside.")
    else:
        print("\nThe National Weather Service is calling for", weatherAlert, "skys outside, drive safe!")
        
vehicleResponseSystem()