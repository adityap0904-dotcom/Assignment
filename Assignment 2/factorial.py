# Function to calculate the factorial of a number
def factorial(n):
    fact = 1

    # Calculate factorial using a loop
    for i in range(1, n + 1):
        fact = fact * i

    # Return the factorial value
    return fact


# Taking an integer from the user
num = int(input("Enter a number: "))

# Calling the function
result = factorial(num)

# Displaying the factorial
print("Factorial of", num, "is:", result)