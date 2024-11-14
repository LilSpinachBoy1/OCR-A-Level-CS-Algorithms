# Create dataset
data = ["Gouda", "Red Leicester", "Double Gloucester", "Parmesan", "Cheddar", "Brie", "Blue"]


def quicksort(items):                                                                               # Create a quicksort function, in order to allow recursion
    if len(items) <= 1:                                                                             # If there is only one item in the list, return the list itself, as the item must be sorted
        return items
    else:                                                                                           # If the list is longer than one item
        pivot = (len(items) - 1) // 2                                                               # Store the index of the pivot item (in this algorithm, the midpoint)
        items[-1], items[pivot] = items[pivot], items[-1]                                           # Swap the pivot and the last item of the list
        p1 = 0                                                                                      # Set the low pointer to zero, the first item in the partitioned range
        p2 = len(items) - 2                                                                         # Set the upper pointer to the highest value, not including the pivot (hence -2 not -1)
        pivot_value = items[-1]                                                                     # Create a variable to store the pivot, for easy comparison (without needing to use the len function)
        pointer_swap = False                                                                        # Flag to check if the pointers have crossed, and thus the pivot needs to be moved
        while not pointer_swap:                                                                     # Loop until the pointers cross each other
            while items[p1] < pivot_value:                                                          # Increment p1 until it is greater than or equal to the pivot
                p1 += 1
            while items[p2] >= pivot_value and p2 >= 0:                                             # Decrement p2 until it is less than the pivot, or it reaches the bottom of the list (resolves issue with the same item being the only in a partition)
                p2 -= 1
            if p1 > p2:                                                                             # If p1 is greater than p2, and thus the pointers have crossed
                pointer_swap = True                                                                 # Set the flag to end this partition's run
                items[p1], items[-1] = pivot_value, items[p1]                                       # Swap the low pointer and pivot
            else:                                                                                   # If not, swap p1 and p2
                items[p1], items[p2] = items[p2], items[p1]
    left_partition = items[:p1]                                                                     # Partition the list to the left of the pivot (sorted item)
    right_partition = items[p1+1:]                                                                  # Partition the list to the right of the pivot (sorted item)
    sorted_left = quicksort(left_partition)                                                         # Sort the left partition
    sorted_right = quicksort(right_partition)                                                       # Sort the right partition
    return sorted_left + [items[p1]] + sorted_right                                                 # Combine the sorted sections and return a sorted list


sorted_data = quicksort(data)
print(sorted_data)
