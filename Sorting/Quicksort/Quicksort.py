# Create dataset
data = ["Gouda", "Red Leicester", "Double Gloucester", "Parmesan", "Cheddar", "Brie", "Blue"]


def quicksort(items):
    if len(items) <= 1:
        return items
    else:
        # Create necessary pointers and swap pivot to end
        pivot = (len(items) - 1) // 2
        items[-1], items[pivot] = items[pivot], items[-1]
        p1 = 0
        p2 = len(items) - 2
        pivot_value = items[-1]
        pointer_swap = False
        while not pointer_swap:
            # Set p1: it should increment until >= pivot
            while items[p1] < pivot_value:
                p1 += 1

            # Set p2: it should decrement until < pivot
            while items[p2] >= pivot_value and p2 >= 0:
                p2 -= 1

            # Find out if the pointers have swapped
            if p1 > p2:  # If the pointers have crossed, swap pivot and p1
                pointer_swap = True
                items[p1], items[-1] = pivot_value, items[p1]
            else:  # If not, swap p1 and p2
                items[p1], items[p2] = items[p2], items[p1]
    left_partition = items[:p1]
    right_partition = items[p1+1:]
    sorted_left = quicksort(left_partition)
    sorted_right = quicksort(right_partition)
    return sorted_left + [items[p1]] + sorted_right


sorted_data = quicksort(data)
print(sorted_data)
