a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
kk = []

for element in a:
    if element < 5:
        kk.append(element)
    else:
        exit
print(kk)

userInput=input("Please enter a number: ")

for element in a:
    if element < int(userInput):
        print(element)
    else:
        exit


print([aa for aa in a if aa < 5])