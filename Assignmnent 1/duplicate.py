def remove_duplicates():
    numbers = list(map(int, input("Enter integers separated by space: ").split())) # Take integers from the user and convert them into a list

    unique = [] #create a empty list

    for n in numbers:  # Check every number in the original list
        if n not in unique:
            unique.append(n)

    print("List after removing duplicates:", unique) #printing the list after removing the duplicates


remove_duplicates()