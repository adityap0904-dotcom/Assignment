# Function to add a new key-value pair to the dictionary
def add_entry(d):
    key = input("Enter new key: ")
    value = input("Enter value: ")

    # Adding the new key-value pair
    d[key] = value


# Function to reassign the dictionary variable
def reassign_dict(d):
    # Creating a completely new dictionary
    d = {"new_key": "new_value"}

    # Displaying the new dictionary inside the function
    print("Inside reassign_dict():", d)


# Taking initial dictionary data from the user
d = {}

n = int(input("Enter number of entries: "))

# Taking key-value pairs from the user
for i in range(n):
    key = input("Enter key: ")
    value = input("Enter value: ")
    d[key] = value

# Displaying the original dictionary
print("\nOriginal dictionary:", d)

# Calling add_entry()
add_entry(d)

# Checking the dictionary after adding an entry
print("After add_entry():", d)

# Calling reassign_dict()
reassign_dict(d)

# Checking the original dictionary again
print("After reassign_dict():", d)