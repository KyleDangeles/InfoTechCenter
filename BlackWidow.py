print("\n************************************************\n")
print("Gasoline Branch - Developer: Kyle Delos Angeles\n")

import random
from time import sleep

def gasLevelGauge():
    gasLevelList = ["Empty", "Low", "Quarter Tank", "Half Tank", "Three Quarter Tank", "Full Tank"]
    return random.choice(gasLevelList)

def gasStations():
    gasStationsList = ["Shell", "Marathon", "Speedway", "Circle K", "Wesco", "Meijer", "Buc-ees", "Costco", "Sam's Club"]
    return random.choice(gasStationsList)

def gasLevelAlert():
    milesToGasStationLow = round(random.uniform(1,25),1)
    milesToGasStationQuarterTank = round(random.uniform(25.1,50),1)    
    gasLevelindicator = gasLevelGauge()
    if gasLevelindicator == "Empty":
        print("******WARNING - YOU ARE OUT OF GAS*****\n")
        sleep(1.25)
        print("Calling AAA")
    elif gasLevelindicator == "Low":
        print("Your gas tank is extremely low, checking GPS for the closest gas")
        sleep(1.25)
        print("The closest gas station is", gasStations(), "which is", milesToGasStationLow, "miles" )
    elif gasLevelindicator == "Quarter Tank":
        print("Your gas tank is on a Quarter Tank, checking GPS for the closest gas")
        sleep(1.25)
        print("The closest gas station is", gasStations(), "which is", milesToGasStationQuarterTank, "miles" )
        
gasLevelAlert()