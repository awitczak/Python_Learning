value = int(input("How many FN to generate? Enter: "))

i = 1
if value == 1:
    fib = [1]
elif value == 2:
    fib = [1,1]
elif value > 2:
    fib = [1,1]
    while i < (value - 1):
        fib.append(fib[i]+fib[i-1])
        i+=1


print(fib)