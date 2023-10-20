from art import logo, vs
import random
from game_data import data
import clear


print(logo)
profiles = data
score = 0

def compareA_name():
  """
  Create a random key for option A.
  """
  global compare_A
  compare_A = random.randrange(50)
  print(
    f"Compare A: {profiles[compare_A]['name']}, {profiles[compare_A]['description']}, form {profiles[compare_A]['country']}."
  )


def compareB_name():
  """
  Create a random key for option B.
  """
  global compare_B
  compare_B = random.randrange(50)
  print(
    f"Against B: {profiles[compare_B]['name']}, {profiles[compare_B]['description']}, from {profiles[compare_B]['country']}."
  )


def winner():
  """
  Function to find correct option. Whose follower is more.
  """
  user_ans = str(input("Who has more followers? Type 'A' or 'B': ")).lower()
  if user_ans == "a" and user_ans == "b":
    if user_ans == "a" and profiles[compare_A]['follower_count'] > profiles[compare_B]['follower_count']:
      print("Pass1a")
    elif user_ans == "b" and profiles[compare_B]['follower_count'] > profiles[compare_A]['follower_count']:
      print('Pass2b')
  else:
    return 'wrong'
  

running = True
while running:
  compareA_name()
  print(vs)
  compareB_name()
  if winner() == 'wrong':
    clear()
    print(logo)
    print(f"Sorry, that's wrong. Final score: {score}")
    running = False
  else:
    clear()
    score += 1
    print(logo)
    print(f"You are right! Current score: {score}.")

