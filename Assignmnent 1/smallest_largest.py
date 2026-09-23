def find_smallest_largest():
    numbers = [] #creating an empty list

    for i in range(7): #taking 7 inputs 
        n = int(input("Enter integer: "))
        numbers.append(n)

    smallest = numbers[0] #asuming the smallest
    largest = numbers[0] #assuming the largest

    for n in numbers:
        if n < smallest:
            smallest = n #getting the smallest nymber

        if n > largest:
            largest = n #getting the largest number

    print("Smallest =", smallest) #printing the smallest number
    print("Largest =", largest) #printing the largest number


find_smallest_largest()