# --- Standard queue ---
queue_length = 5
queue = ["" for i in range(queue_length)]  # Simulate an array, which stores the data of our queue
front_pointer = 0  # Set the front pointer to 0, as this is the front item of the empty list
rear_pointer = 0  # Set the rear pointer to 0, as this is the end item of the empty list

# Enqueing an item
data = "CrazyDave"
if rear_pointer == queue_length:  # Check to make sure there is room to add an item
    print("Queue overflow!")
else:
    queue[rear_pointer] = data  # Set the data at the rear pointer to be equal to the data we want
    rear_pointer += 1  # Increment our rear pointer, as there is now extra data

# Peeking at an item
print(queue[front_pointer])  # Look at the item at the front of the queue

# Dequeing an item
if front_pointer == rear_pointer:  # Check to make sure that there is data in the queue
    print("Queue underflow!")
else:
    queue[front_pointer] = ""  # Remove the data at the front of the queue
    front_pointer += 1  # Increment the front pointer by one, as it no longer points to an item
    