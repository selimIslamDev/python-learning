# Goal:
# Print a countdown before something "exciting" happens (like "Launching..."
# "Happy New Year!").


import time

count = int(input("Enter a number to start the countdown: "))

print("\nStarting the countdown...")

for i in range(count, 0, -1):
    print(i)
    time.sleep(1)

print("\n happy new year")