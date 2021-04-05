import string
import random

def pswd_generation():

    password_list = []
    length = random.randint(10,16)
    i = 0


    while length > i:
        char_randomizer = random.randint(1, 3)
        if char_randomizer == 1:
            random_char = random.randint(1, 9)
            password_list.append(random_char)
            i += 1
        elif char_randomizer == 2:
            random_char = random.choice(string.ascii_letters)
            password_list.append(random_char)
            i += 1
    password = "".join(map(str,password_list))
    return print(password)

pswd_generation()

def pswd_generation_simpler():
    password_list = []
    length = random.randint(10,16)
    i = 0
    char_string = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','r','s','t','u','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','R','S','T','U','W','X','Y','Z','!','@','$','%','^','&','',]

    while length > i:
        random_char = random.choice(char_string)
        password_list.append(random_char)
        i += 1
    password = "".join(map(str,password_list))
    return print(password)
pswd_generation_simpler()