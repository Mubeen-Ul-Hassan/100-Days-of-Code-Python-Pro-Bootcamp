from art import logo
import random

#Number Guessing Game Objectives:

# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer.
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player.
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

# Include an ASCII art logo.


def guess():
    list = []
    for element in range(1, 101):
        list.append(element)
    computer_guess = int(random.choice(list))
    return computer_guess


def level():
    if difficulty_level == "easy":
        return easy
    else:
        return hard


def checking():
  global attempts
  if user_guess == guess_number:
      print(f"You guess it right {guess_number}")
      attempts = 0
  else:
      if user_guess > guess_number:
          print("Too high.")
      else:
          print("Too low.")

      print("Guess again.")
      attempts -= 1
      print(f"You have {attempts} remaining to guess the number.")


print(logo)

easy = 10
hard = 5

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 to 100.")
difficulty_level = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()

guess_number = guess()
attempts = level()

print(f"You have {level()} attempts remaining guess the number.")

running = True
while running:
    user_guess = int(input("Make a guess: "))
    checking()
    if attempts == 0:
        running = False
