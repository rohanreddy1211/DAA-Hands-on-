def insertion_sort(elements):
    # Loop from the second element to the last element
    for index in range(1, len(elements)):
        key = elements[index]  # The element to be positioned
        position = index - 1   # Position of the previous element
        
        # Shift elements of the sorted portion of the array to the right
        while position >= 0 and key < elements[position]:
            elements[position + 1] = elements[position]
            position -= 1
        
        # Insert the key at the correct position
        elements[position + 1] = key
    
    return elements

# Test Case 1: Random list of integers
test_case_1 = [29, 1, 16, 8, 44]
print("Sorted Test Case 1:", insertion_sort(test_case_1))

# Test Case 2: List with all elements already in ascending order
test_case_2 = [2, 4, 6, 8, 10]
print("Sorted Test Case 2:", insertion_sort(test_case_2))

# Test Case 3: List with elements in descending order
test_case_3 = [30, 25, 20, 15, 10]
print("Sorted Test Case 3:", insertion_sort(test_case_3))

# Test Case 4: List with repeated values
test_case_4 = [7, 7, 7, 7]
print("Sorted Test Case 4:", insertion_sort(test_case_4))

# Test Case 5: List with a mix of positive and negative numbers
test_case_5 = [-5, 3, -1, 8, 0]
print("Sorted Test Case 5:", insertion_sort(test_case_5))
