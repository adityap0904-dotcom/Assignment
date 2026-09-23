# Function to remove the last element from the list
def remove_last(lst):
    lst.pop()  # Removes the last element of the list


# Taking list elements from the user
numbers = list(map(int, input("Enter list elements separated by space: ").split()))

# Displaying the original list
print("Before function call:", numbers)

# Calling the function
remove_last(numbers)

# Checking the list after the function call
print("After function call:", numbers)

# Conclusion: The original list is changed because lists are mutable1 2 