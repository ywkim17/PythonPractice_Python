print("Hello world!")
correctNumber = 8
guessedNumber = 0

while guessedNumber != 8:
    guessedNumber = int(input("Guess a number from 1 to 10: "))

    if guessedNumber == 8:
        print("You are correct!")
    elif guessedNumber > correctNumber:
        print("You are too high")
    elif guessedNumber < correctNumber:
        print("You are too low")
        