# Function to merge two lists into a sorted one
def merge(list1: list, list2: list) -> list:                            # Take 2 params of type list and returns a sorted list
    new_list = []                                                       # Make an empty list that will house the sorted items
    l1_p = 0                                                            # Create a pointer to use on list1
    l2_p = 0                                                            # Create a pointer to use on list2

    # Compare lists
    while l1_p < len(list1) and l2_p < len(list2):                      # While the pointers are within the sizes of the lists
        if list1[l1_p] > list2[l2_p]:                                   # If the currently checked item of list1 is larger than that of list2
            new_list.append(list2[l2_p])                                # Add the item from list2 to the final sorted list
            l2_p += 1                                                   # Increment the pointer for list2 to essentially disregard the now sorted item
        elif list1[l1_p] < list2[l2_p]:                                 # If the next item of list2 is larger than that of list1
            new_list.append(list1[l1_p])                                # Add the larger item from list1 to the final sorted list
            l1_p += 1                                                   # Increment the pointer for list1
        else:                                                           # If the 2 items being compared are equal
            new_list.append(list1[l1_p])                                # Add both items to the sorted list
            new_list.append(list2[l2_p])
            l1_p += 1                                                   # Increment both pointers
            l2_p += 1

    # Add remaining items, these are what are left over in one list after all items from the other have been sorted
    if l1_p < len(list1):                                               # If there are still items in list 1
        for i in range(l1_p, len(list1)):                               # Iterate through the remaining items and add them to the sorted list
            new_list.append(list1[i])
    elif l2_p < len(list2):                                             # If there are still items in list 2
        for ii in range(l2_p, len(list2)):                              # Iterate through and add to sorted list
            new_list.append(list2[ii])

    # Return the final list, which has been sorted
    return new_list


# --------- Main algorithm ---------
# Create unsorted dataset
data = ["Syntax Error", "Logic Error", "FileNotFound Error", "Type Error", "Memory Error", "Trait Bounds Error"]

all_lists = []                                                          # Create a list to store all sublists in
for item in data:                                                       # Append each item from the data to all_lists, as its own list of one item
    all_lists.append([item])
index = 0                                                               # Set an index pointer variable to 0
while index < len(all_lists) - 1:                                       # While the index pointer is less than the number of items in the list - 1 (the -1 accounts for the fact we are checking the next item too)
    merged_list = merge(all_lists[index], all_lists[index + 1])         # Run the above merge functon on 2 lists to get a sorted list
    all_lists[index] = merged_list                                      # Replace the current item with the newly sorted list
    del all_lists[index + 1]                                            # Remove the second of the lists that were merged, as it has been incorporated into the merged list before

# Print the sorted list
sorted_list = all_lists[0]                                              # There should only be one item in all_lists, the final sorted list
print(sorted_list)
