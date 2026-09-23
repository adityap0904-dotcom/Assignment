def reverse_list():
    numbers = list(map(int, input("Enter integers separated by space: ").split())) #taking the inputs from the users

    reversed_list = [] #creating a empty list

    for i in range(len(numbers) - 1, -1, -1):
        reversed_list.append(numbers[i]) #reversing the list

    print("Original list:", numbers) #print the original list
    print("Reversed list:", reversed_list) #print the reversed list


reverse_list()