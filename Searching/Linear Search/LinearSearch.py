# Set up data
data = ["Reese", "Advin", "Ralfs", "Josh", "Sam"]
target = "Josh"

length = len(data)                                  # Store the length of the data to use as an endpoint
found = False                                       # Flag to improve efficiency
i = 0                                               # Acts as a pointer to the position in the list
while not found and i < length:                     # Keep looping while the target has not been found, and while the pointer is within the range of the list
    if data[i] == target:                           # If the current item is the one to find
        found = True                                # Set flag to true, so the loop ends
    else:
        i += 1                                      # Move to the next item if not found yet

if found:                                           # If the item was found, output a suitable message
    print("Item found at position " + str(i))
else:
    print("Item not found!")
