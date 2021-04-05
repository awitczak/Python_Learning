userIn = input("Number: ")
nums = range(1,int(userIn)+1)
listOfDivisors = []
for i in nums:
    if int(userIn)%i==0:
        listOfDivisors.append(i)
       # print(listOfDivisors)
       # print(str(i) + " is the divisor of that number.")
    else:
        pass

print(listOfDivisors)