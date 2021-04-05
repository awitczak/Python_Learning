a = [1, 12, 1, 222, 3, 15, 822, 13, 21, 34, 55, 89, 111991, 1092,1290,11]
b = [1, 12, 3, 3, 35, 6, 7, 8, 9, 10, 11, 12, 13]
c = []

for num in a:
    if num in b:
        if num not in c:
            c.append(num)
print(c)