def calculate():
    numbers = [] #creating an ampty list

    for i in range(10): #taking 10 inputs 
        n = int(input("Enter integer: "))
        numbers.append(n)

    total = 0 #assuming total 0

    for n in numbers:
        total = total + n #getting the total sum

    average = total / 10 #getting the average 

    print("Sum =", total) #printing the sum which is total
    print("Average =", average) #printing the average 


calculate()