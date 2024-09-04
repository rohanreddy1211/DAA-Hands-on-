def bubble_sort(sequence):
    length = len(sequence)
    # Loop through each element in the sequence
    for pass_num in range(length):
        swapped = False  # Flag to track if any swaps occur during this pass
        # Elements after pass_num are already sorted
        for index in range(length - pass_num - 1):
            # Swap if the element found is greater than the next element
            if sequence[index] > sequence[index + 1]:
                sequence[index], sequence[index + 1] = sequence[index + 1], sequence[index]
                swapped = True
        # If no elements were swapped, the list is sorted
        if not swapped:
            break
    return sequence

# Test Case 1: Unordered list of integers
test_case_1 = [45, 3, 12, 7, 29]
print("Sorted Test Case 1:", bubble_sort(test_case_1))

# Test Case 2: List with duplicate integers
test_case_2 = [5, 5, 5, 5]
print("Sorted Test Case 2:", bubble_sort(test_case_2))

# Test Case 3: List with negative integers
test_case_3 = [-1, -3, 2, 0, -7]
print("Sorted Test Case 3:", bubble_sort(test_case_3))

# Test Case 4: List of strings (sorting lexicographically)
test_case_4 = ["apple", "orange", "banana", "pear"]
print("Sorted Test Case 4:", bubble_sort(test_case_4))

# Test Case 5: Empty list
test_case_5 = []
print("Sorted Test Case 5:", bubble_sort(test_case_5))
