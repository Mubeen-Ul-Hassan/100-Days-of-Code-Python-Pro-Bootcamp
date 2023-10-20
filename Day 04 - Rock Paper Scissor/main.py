rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissor = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
import random

game_map = [rock, paper, scissor]

user_input = int(
    input(
        "What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissor. "))
control_user = game_map[user_input]
print(f"User move: {control_user}")

computer_move = random.randrange(0, 3, 1)
control_computer = game_map[computer_move]
print(f"Computer move: {control_computer}")

if control_user == control_computer :
  print("Status: Tie")
elif control_user != control_computer:
  if control_user > control_computer:
    if control_user == "scissor" and control_computer == "rock" or control_computer == "":
      print("Status: You lose1.")
    else:
      print("Status: You win.")
  elif control_user < control_computer:
    if control_user == "rock" and control_computer == "scissor" or control_computer == "paper":
      print("Status: You win.")
    else:
      print("Status: You lose2.")
  else:
    print("Indevelopment Stages.")
else:
  print("O.!.O")