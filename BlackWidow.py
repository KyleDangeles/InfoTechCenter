# Print a decorative header
print("\n*************************************\n")
print("Weather Branch - Developer: Mr. Lange")

# Import necessary libraries
import random  # Used for generating random weather conditions
from time import sleep  # Sleep function can be used if delays are needed

# Weather Function to determine the weather
def weather():
    # List of possible weather conditions
    weatherForecastList = ["snowy", "blizzard", "icy", "rainy", "windy", "sunny"]

    # Randomly select a weather condition from the list
    weatherCondition = random.choice(weatherForecastList)

    # Return the selected weather condition
    return weatherCondition

# Call the weather function to get the weather alert
weatherAlert = weather()

# Vehicle Response System function to determine what action to take based on the weather
def vehicleResponseSystem():
    # Check if the weather is snowy and update the alarm accordingly
    if weatherAlert == "snowy":
        print("\nThe National Weather Service has updated our alarm by 30 minutes because"
              " it is", weatherAlert, "outside.")
        sleep(1)
        print("VRS has been engaged only allowing us to drive 55mph")
    # Check if the weather is a blizzard and update the alarm accordingly
    elif weatherAlert == "blizzard":
        print("\nThe National Weather Service has updated our alarm by 60 minutes because"
              " it is a", weatherAlert, "outside!")
        sleep(1)
        print("VRS has been engaged only allowing us to drive 50mph")
    # Check if the weather is icy and update the alarm accordingly
    elif weatherAlert == "icy":
        print("\nThe National Weather Service has updated our alarm by 90 minutes because"
              " it is", weatherAlert, "outside.")
        sleep(1)
        print("VRS has been engaged only allowing us to drive 40mph")
    # Check if the weather is rainy and update the alarm accordingly
    elif weatherAlert == "rainy":
        print("\nThe National Weather Service has updated our alarm by 10 minutes because"
              " it is", weatherAlert, "outside.")
        sleep(1)
        print("VRS has been engaged only allowing us to drive 55mph")
    # Check if the weather is windy and update the alarm accordingly
    elif weatherAlert == "windy":
        print("\nThe National Weather Service has updated our alarm by 5 minutes because"
              " it is", weatherAlert, "outside.")
        sleep(1)
        print("VRS has been engaged only allowing us to drive 60mph")
    # If the weather is sunny, print a safety message
    else:
        print("\nThe National Weather Service is calling for", weatherAlert, "skies outside, drive safe!")
        sleep(1)
        print("VRS has been disengaged")

# Call the vehicle response system to update the alarm based on the weather
vehicleResponseSystem()
