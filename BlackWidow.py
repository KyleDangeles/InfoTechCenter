# Libraries HERE
import sys  # Import the sys module to interact with system-specific parameters and functions
import time  # Import the time module to use time-related functions, such as sleep()
import random  # Used for generating random weather conditions



# Define color constants using ANSI escape sequences
RESET = "\033[0m"  # Reset to default text color
CYAN = "\033[96m"  # Cyan color for the welcome message
YELLOW = "\033[93m"  # Yellow color for the version message
GREEN = "\033[92m"  # Green color for the final success message
MAGENTA = "\033[95m"  # Magenta color for the booting message

# Print a welcome message to the console in cyan
#print(f"{CYAN}\nWelcome Branch - Developer: Kyle Delos Angeles\n{RESET}")

# Print a version message to the console in yellow
print(f"{YELLOW}Welcome to InfoTechCenter V1.0\n{RESET}")

# Initialize variables for the booting process
x = 0  # A counter variable that tracks the number of iterations in the loop
ellipsis = 0  # Variable that controls the number of dots in the booting message

# Start a while loop that runs until x reaches 20
while x != 20:
    x += 1  # Increment x by 1 with each loop iteration
    # Create the message with an increasing number of dots (controlled by the ellipsis variable)
    message = f"{MAGENTA}Infotech Center System Booting{RESET}{'.' * ellipsis}"  
    ellipsis += 1  # Increment the ellipsis counter to add more dots
    sys.stdout.write("\r" + message)  # Overwrite the previous output on the same line
    time.sleep(0.5)  # Pause the program for 0.5 seconds to create a delay for the booting effect
    # When ellipsis reaches 4, reset it to 0 to loop through 1 to 3 dots
    if ellipsis == 4:
        ellipsis = 0
    # Once the counter x reaches 20, print the final boot-up message
    if x == 20:
        print(f"\n\n{GREEN}Operating System Booted Up - Retina Scanned - Access Granted{RESET}\n")


print("************************************************\n")
#print("Gasoline Branch - Developer: Kyle Delos Angeles\n")

import random
from time import sleep

def gasLevelGauge():
    # Define a list of possible gas levels
    gasLevelList = ["Empty", "Low", "Quarter Tank", "Half Tank", "Three Quarter Tank", "Full Tank"]
    # Randomly select and return a gas level
    return random.choice(gasLevelList)

def gasStations():
    # Define a list of possible gas stations
    gasStationsList = ["Shell", "Marathon", "Speedway", "Circle K", "Wesco", "Meijer", "Buc-ees", "Costco", "Sam's Club"]
    # Randomly select and return a gas station
    return random.choice(gasStationsList)

def gasLevelAlert():
    # Get a random gas level and gas station
    gasLevelindicator = gasLevelGauge()
    gasStation = gasStations()

    # Define miles to nearest gas station based on gas level
    milesToGasStation = {
        "Low": round(random.uniform(1, 25), 1),  # Miles for Low gas level
        "Quarter Tank": round(random.uniform(25.1, 50), 1)  # Miles for Quarter Tank gas level
    }

    # Check if the gas level is 'Empty'
    if gasLevelindicator == "Empty":
        print("******WARNING - YOU ARE OUT OF GAS*****\n")
        sleep(1.25)  # Simulate a pause for effect
        print("Calling AAA")  # Simulate calling AAA for help
    # Check if the gas level is 'Low' or 'Quarter Tank'
    elif gasLevelindicator == "Low" or gasLevelindicator == "Quarter Tank":
        print(f"Your gas tank is on {gasLevelindicator}, checking GPS for the closest gas station.\n")
        sleep(1.25)  # Simulate a pause for effect
        # Get the distance to the nearest gas station based on the gas level
        print(f"The closest gas station is {gasStation} which is {milesToGasStation.get(gasLevelindicator, 0)} miles away.")
    # Check if the gas level is 'Half Tank'
    elif gasLevelindicator == "Half Tank":
        print("Your gas tank is half full, which is plenty to get to your destination!")
    # Check if the gas level is 'Three Quarter Tank'
    elif gasLevelindicator == "Three Quarter Tank":
        print("Your gas tank is at three-quarters. You're good to go!")
    # If the gas level is 'Full Tank'
    else:
        print("Your gas tank is FULL, Vroom Vroom!")

# Call the function to simulate the gas level alert
gasLevelAlert()


# Print a decorative header
print("\n*************************************")


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

