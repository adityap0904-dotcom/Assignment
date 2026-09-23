# Function to find the maximum of two numbers
def find_max(a, b):
    # Check which number is greater
    if a > b:
        return a
    else:
        return b


# Taking two numbers from the user
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

# Calling the function
maximum = find_max(num1, num2)

# Displaying the greater number
print("The greater number is:", maximum)