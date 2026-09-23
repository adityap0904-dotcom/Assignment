# Function to try to change the first character of the string
def change_string(s):
    # Strings are immutable, so we cannot directly change s[0]
    s = "X" + s[1:]
    
    # Display the changed string inside the function
    print("Inside function:", s)


# Taking a string from the user
text = input("Enter a string: ")

# Displaying the original string
print("Before function call:", text)

# Calling the function
change_string(text)

# Checking the original string after the function call
print("After function call:", text)

# Conclusion: The original string does not change because strings are immutable