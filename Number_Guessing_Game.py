import random
random.seed()   #Prepare random number generator


# Andie Meddaugh
# CTI 110 Section 5
# Test Case 1 (Quit):
# Target Number = 42
# User inputs: 10, 20, -999
# Expected Output: "You quit the game."
# 
# Test Case 2 (Win):
# Target Number = 37
# User inputs: 50, 25, 37
# Expected Output: "Congratulations, you guessed the number!"
# Random starts at 0. To start at 1, we need to add 1.
targetNumber = int(random.random() * 100) + 1
print("Please guess a whole number between 1-100 (or enter -99 to quit):")
userGuess = int(input())
while userGuess != targetNumber and userGuess != -999:
    print("Tough luck, not quite! Try again! (Or type -999 to quit): ")
    userGuess = int(input())
if userGuess == targetNumber:
    print("Congratulations, you guessed the number!")
else:
    print("No worries, have a good day!")
