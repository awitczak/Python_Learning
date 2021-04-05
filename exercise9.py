import random
answer = "yes"

while answer == "yes":
    randomNum = random.randint(1,10)
    guess = "wrong"
    userChoice = int(input("Guess the number that I am thinking of! Enter a number (1-9): "))
    noOfGuesses = 0

    while guess == "wrong" :
        noOfGuesses = noOfGuesses + 1
        if userChoice == randomNum :
            print("Congratulations, You guessed it! It took you " + str(noOfGuesses) + " attempts.\n\n")
            answer = input("Again?")
            break
        elif userChoice < randomNum :
            userChoice = int(input("Too low. Guess again: "))
        elif userChoice > randomNum :
            userChoice = int(input("Too high. Guess again: "))