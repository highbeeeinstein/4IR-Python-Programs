# secretNumber = 15
# guessNumber = int(input('Guess a number '))

# if secretNumber == guessNumber:
#     print('Congratulations! You are correct')
# elif guessNumber == secretNumber - 2 or guessNumber == secretNumber + 2:
#     print('Oh! You are almost there!')
# else:
#     print('You are wrong!')

secretNumber = 30
count = 0
while True:
    guess= int(input("Guess a number "))
    count += 1
    if guess == secretNumber:
        print("Congratulations! You got it right")
        print("You have guessed up to", count, "times")
        break
    elif guess > secretNumber:
        print("Try a lesser number")
    elif guess < secretNumber:
        print("Try a larger number")
    if count == 5:
        print("End of Game")
        break
    