# Create dataset
data = ["Paddington", "Red One", "Wicked", "Piece By Piece", "Mufassa", "Moana 2"]
print(data)                                                   # Print unsorted data

swap_made = True                                              # Flag to check if any swaps are made, if False, the list must be in order, as no items have been moved
high = 0                                                      # Used to reduce swap area as top will be sorted after each pass
while swap_made:                                              # Keep making passes until the list is in order
    swap_made = False                                         # Set swaps flag to False at the start of each pass
    for i in range(len(data) - high - 1):                     # Loop through each item of data, -1 to prevent checking outside the list
        if data[i] > data[i+1]:                               # If the current item is greater than the next, swap them
            data[i], data[i+1] = data[i+1], data[i]           # Shorthand method of swapping two items
            swap_made = True                                  # Set swap to true, as a swap has been made
    high += 1

print(data)                                                   # Print the (hopefully) sorted data!
