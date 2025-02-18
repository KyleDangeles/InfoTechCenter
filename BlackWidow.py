print("\n************************************************\n")
print("Gasoline Branch - Developer: Kyle Delos Angeles\n")

import random
from time import sleep

def gasLevelGauge():
    # Predefined list of gas levels
    gasLevelList = ["Empty", "Low", "Quarter Tank", "Half Tank", "Three Quarter Tank", "Full Tank"]
    return random.choice(gasLevelList)

def gasStations():
    # Predefined list of gas stations
    gasStationsList = ["Shell", "Marathon", "Speedway", "Circle K", "Wesco", "Meijer", "Buc-ees", "Costco", "Sam's Club"]
    return random.choice(gasStationsList)

def gasLevelAlert():
    # Get a random gas level and station
    gasLevelindicator = gasLevelGauge()
    gasStation = gasStations()

    # Define miles for different fuel levels
    milesToGasStation = {
        "Low": round(random.uniform(1, 25), 1),
        "Quarter Tank": round(random.uniform(25.1, 50), 1)
    }

    # Print based on the gas level
    if gasLevelindicator == "Empty":
        print("******WARNING - YOU ARE OUT OF GAS*****\n")
        sleep(1.25)
        print("Calling AAA")
    elif gasLevelindicator == "Low" or gasLevelindicator == "Quarter Tank":
        print(f"Your gas tank is on {gasLevelindicator}, checking GPS for the closest gas station.\n")
        sleep(1.25)
        print(f"The closest gas station is {gasStation} which is {milesToGasStation.get(gasLevelindicator, 0)} miles away.")
    elif gasLevelindicator == "Half Tank":
        print("Your gas tank is half full, which is plenty to get to your destination!\n")
    elif gasLevelindicator == "Three Quarter Tank":
        print("Your gas tank is at three-quarters. You're good to go!")
    else:
        print("Your gas tank is FULL, Vroom Vroom!")

# Call the alert function
gasLevelAlert()
