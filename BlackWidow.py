# Libraries HERE
import sys  # Import the sys module to interact with system-specific parameters and functions
import time  # Import the time module to use time-related functions, such as sleep()

# Define color constants using ANSI escape sequences
RESET = "\033[0m"  # Reset to default text color
CYAN = "\033[96m"  # Cyan color for the welcome message
YELLOW = "\033[93m"  # Yellow color for the version message
GREEN = "\033[92m"  # Green color for the final success message
MAGENTA = "\033[95m"  # Magenta color for the booting message

# Print a welcome message to the console in cyan
print(f"{CYAN}Welcome Branch - Developer: Kyle Delos Angeles{RESET}")

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

