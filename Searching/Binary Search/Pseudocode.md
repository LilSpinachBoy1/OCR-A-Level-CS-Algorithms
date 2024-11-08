# Pseudocode for a Binary Search
// Create data and pointers/flags
data = ["Some data here..."]
item_to_find = "Advin's Love"
found = False
low_p = 0
high_p = data.length - 1

while found == False and low_p != high_p         // NotEquals, as if they are equal on next iteration, the item is not in list
    mid = (low_p + high_p) DIV 2                 // Use integer division to ensure midpoint is an integer
    if data[mid] == item_to_find then            // If the midpoint is the item (convenient!)
        item_index = mid
        found = True
    else if item_to_find > data[mid] then        // If the item is later in the list than the current midpoint
        low_p = mid + 1                          // Make the lower pointer the next item above the midpoint
    else if item_to_find < data[mid] then        // If the item is earlier in the list than the current midpoint
        high_p = mid - 1                         // Make the higher pointer the item before the midpoint
    endif
endwhile                                         // Repeat until the item is found, or is understood to not be in the list

if found == True then                            // If the item was found, produce an appropriate message
    print("The item is at index " + item_index)
else                                             // If the item wasn't found, produce a message
    print("The item is not in the list!")
