user_String = input("Enter a string, to learn whether it is a palindrome or not: ").lower()
#reversed_String = ''


#print(user_String)

#for letter in user_String:
    #reversed_String = letter + reversed_String


#print(reversed_String)


#if reversed_String == user_String:
    #print("Your word is a palindrome!")
#else:
    #print("I am sorry, better luck next time!")

if user_String[::] == user_String[::-1]:
    print("That is a palindrome!")



