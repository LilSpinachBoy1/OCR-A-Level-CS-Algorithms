# Create dataset
data = ["Gouda", "Red Leicester", "Double Gloucester", "Parmesan", "Cheddar", "Brie", "Blue"]
data = [4, 5, 2, 1, 3]

def quicksort(items):
    if len(items) <= 1:
        return items
    else:
        # Create neccesary pointers and swap pivot to end
        pivot = (len(items) - 1) // 2
        data[-1], data[pivot] = data[pivot], data[-1]
        p1 = 0
        p2 = len(items) - 2
        pivot_value = data[-1]
        pointer_swap = False
        while not pointer_swap:
            # Set p1: it should increment until >= pivot
            while data[p1] < pivot_value:
                p1 += 1

            # Set p2: it should decrement until < pivot
            while data[p2] >= pivot_value:
                p2 -= 1

            # Find out if the pointers have swapped
            if p1 > p2:  # If the pointers have crossed, swap pivot and p1
                pointer_swap = True
                data[p1], data[-1] = pivot_value, data[p1]
            else:  # If not, swap p1 and p2
                data[p1], data[p2] = data[p2], data[p1]
    left_partition = data[:p1]
    right_partition = data[p1+1:]
    sorted_left = quicksort(left_partition)
    sorted_right = quicksort(right_partition)
    return sorted_left + data[p1] + sorted_right

print(quicksort(data))