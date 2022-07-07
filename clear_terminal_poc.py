import os
from time import sleep

# Printing the os name
print("os name is :", os.name)

# Waiting for 2 seconds to clear the screen
sleep(2)

# Clearing the Screen
# posix is os name for linux or mac
if os.name == "posix":
    os.system("clear")
# else screen will be cleared for windows
else:
    os.system("cls")
