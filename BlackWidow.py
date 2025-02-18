print("\n************************************************\n")
print("Gasoline Branch - Developer: Kyle Delos Angeles\n")

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
        print("Your gas tank is half full, which is plenty to get to your destination!\n")
    # Check if the gas level is 'Three Quarter Tank'
    elif gasLevelindicator == "Three Quarter Tank":
        print("Your gas tank is at three-quarters. You're good to go!")
    # If the gas level is 'Full Tank'
    else:
        print("Your gas tank is FULL, Vroom Vroom!")

# Call the function to simulate the gas level alert
gasLevelAlert()
