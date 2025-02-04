# Libraries HERE
import sys  # Import the sys module to interact with system-specific parameters and functions
import time  # Import the time module to use time-related functions, such as sleep()

# Print a welcome message to the console
print("Welcome Branch - Developer:Kyle Delos Angeles")

# Print a version message to the console
print("Welcome to InfoTechCenter V1.0\n")

# Initialize variables
x = 0  # A counter variable that will track the number of iterations in the loop
ellipsis = 0  # Variable used to control the number of dots in the message for the "booting" process

# Start a while loop that runs until x reaches 20
while x != 20:
    x += 1  # Increment the value of x by 1 in each loop iteration
    message = ("Infotech Center System Booting" + "." * ellipsis)  # Create the message, adding dots based on ellipsis
    ellipsis += 1  # Increment the ellipsis counter to add more dots
    sys.stdout.write("\r" + message)  # Write the message to stdout, overwriting the previous output
    time.sleep(.5)  # Pause the program for half a second to create a delay for the booting effect
    if ellipsis == 4:  # When ellipsis reaches 4, reset it to 0 to loop through 1 to 3 dots
        ellipsis = 0
    if x == 20:  # Once the counter reaches 20, print the final boot-up message
        print("\n\nperating System Booted Up - Retina Scanned - Access Granted\n")
