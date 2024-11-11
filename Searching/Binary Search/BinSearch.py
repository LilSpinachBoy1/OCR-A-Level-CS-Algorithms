data = ["Advin's Love", "Bye", "Goron Rmy", "Hey"]
item_to_find = "Bye"
found = False
low_p = 0
high_p = len(data) - 1
item_index = -1

while not found:                                # NotEquals, as if they are equal on next iteration, the item is not in list
    mid = (low_p + high_p) // 2                 # Use integer division to ensure midpoint is an integer
    if data[mid] == item_to_find:               # If the midpoint is the item (convenient!)
        item_index = mid
        found = True
    elif item_to_find > data[mid]:              # If the item is later in the list than the current midpoint
        low_p = mid + 1                         # Make the lower pointer the next item above the midpoint
    elif item_to_find < data[mid]:              # If the item is earlier in the list than the current midpoint
        high_p = mid - 1                        # Make the higher pointer the item before the midpoint
    elif low_p == high_p:                       # If the pointers are the same at this point, the item is not in the list
        break

if found:                                       # If the item was found, produce an appropriate message
    print("The item is at index " + str(item_index))
else:                                           # If the item wasn't found, produce a message
    print("The item is not in the list!")
