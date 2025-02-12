# Print a decorative header
print("\n*************************************\n")
print("Weather Branch - Developer: Kyle Delos Angeles")

# Import necessary libraries
import random  # Used for generating random weather conditions

# Weather Function to determine the weather
def weather():
    # List of possible weather conditions
    weatherForecastList = ["snowy", "blizzard", "icy", "rainy", "windy", "sunny"]

    # Randomly select a weather condition from the list
    return random.choice(weatherForecastList)

# Vehicle Response System function to determine what action to take based on the weather
def vehicleResponseSystem(weatherAlert):
    # Mapping of weather condition to delay and speed
    weather_conditions = {
        "snowy": {"delay": 30, "speed": 55},
        "blizzard": {"delay": 60, "speed": 50},
        "icy": {"delay": 90, "speed": 40},
        "rainy": {"delay": 10, "speed": 55},
        "windy": {"delay": 5, "speed": 60},
        "sunny": {"delay": 0, "speed": 0, "message": "VRS has been disengaged"}
    }

    # Get the relevant weather info
    weather_info = weather_conditions.get(weatherAlert, {"delay": 0, "speed": 0, "message": "Drive safe!"})

    # Handle specific weather conditions
    if weatherAlert != "sunny":
        print(f"\nThe National Weather Service has updated our alarm by {weather_info['delay']} minutes because it is {weatherAlert} outside.")
        print(f"VRS has been engaged only allowing us to drive {weather_info['speed']}mph")
    else:
        print(f"\nThe National Weather Service is calling for {weatherAlert} skies outside, {weather_info['message']}")

# Call the weather function to get the weather alert
weatherAlert = weather()

# Call the vehicle response system to update the alarm based on the weather
vehicleResponseSystem(weatherAlert)
