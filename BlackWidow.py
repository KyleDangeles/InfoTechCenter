print("\n******************************************************\n")
print("Gasoline Branch - Developer: Kyle Delos Angeles\n")

import random
from time import sleep

def gasLevelGauge():
  gasLevelList = ["Empty", "Low", "Quarter Tank", "Half Tank", "Three Quarter Tank", "Full Tank"]
  return random.choice(gasLevelList)
  
