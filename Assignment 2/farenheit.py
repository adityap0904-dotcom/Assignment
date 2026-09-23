# Function to convert Celsius to Fahrenheit
def celsius_to_fahrenheit(celsius):
    # Apply the temperature conversion formula
    fahrenheit = (celsius * 9 / 5) + 32

    # Return the Fahrenheit value
    return fahrenheit


# Taking temperature in Celsius from the user
celsius = float(input("Enter temperature in Celsius: "))

# Calling the function
fahrenheit = celsius_to_fahrenheit(celsius)

# Displaying the converted temperature
print("Temperature in Fahrenheit:", fahrenheit)