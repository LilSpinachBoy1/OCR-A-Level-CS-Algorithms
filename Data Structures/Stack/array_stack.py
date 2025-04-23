"""
An implementation of an array based stack in python
"""

stack_size = 5
stack = ["" for i in range(stack_size)]  # Create an array of empty items to represent the stack
end_pointer = -1  # Points to the highest in-use stack location, -1 represents an empty stack

# --- Pushing to the stack ---
data = "Are you sure?"  # Store the data we want to push
if end_pointer == stack_size:  # Check there is room to add the item to the stack, in order to prevent a stack overflow
    print("Stack overflow!")  # A stack overflow has occured and the data cannot be added due to a lack of space
else:
    end_pointer += 1  # Increase the pointer by one to account for the new data
    stack[end_pointer] = data  # Now we know there is room, we can add the data to the top of the stack


# --- Peeking at the stack ---
peek_result = stack[end_pointer]  # Peek at the top item, without changing it at all
print(peek_result)


# --- Popping an item from the stack ---
if end_pointer == -1:  # Check there is data within the stack already to prevent a stack underflow
    print("Stack underflow!")  # An underflow occurs, as there is no data to remove
else:
    stack[end_pointer] = ""  # Delete the data from the top of the stack
    end_pointer -= 1  # Decrement the pointer to account for the loss of data
