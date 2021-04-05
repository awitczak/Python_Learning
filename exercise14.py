a = [1, 1, 2, 3, 4, 5, 1, 5, 23, 1]
b = []


def loop_list():
    for element in a:
        if element not in b:
            b.append(element)
    return print(b)


loop_list()


def sets():
    return print(set(a))


sets()
