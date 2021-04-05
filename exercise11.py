userIn = input("Number: ")
nums = range(1,int(userIn)+1)
listOfDivisors = []
for i in nums:
    if int(userIn)%i==0:
        listOfDivisors.append(i)
    else:
        pass

print(listOfDivisors)

listLength = len(listOfDivisors)

if listLength == 2:
    print("This is a prime number!")