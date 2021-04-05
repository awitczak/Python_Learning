name = input("Hello! Please enter Your name: ")
age = input("Also, how old are you? Please, let me know: ")

print("So you say, you are " + name + " and you are " + age + " years old? Cool!")

leftToHundred = 100-int(age)

input("\n\nWould you like to know, how many years do You have left till the age of hundred? ")

print("\nOkay then, You've got " + str(leftToHundred) + " years left. ")

answer = input("How many times would You like to see this answer pop-up? Enter: ")

print(int(answer) * ( "\n\nYou've got " + str(leftToHundred) + " years left." ) )
