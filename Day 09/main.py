import clear
#HINT: You can call clear() to clear the output in the console.
from art import logo

print(logo)

print("Welcome to the secret acution program.")

record_dict = {}

acution_running = True
while acution_running:
  user_name = str(input("What is your name?: "))
  user_bid = int(input("What's your bid?: $"))

  record_dict[user_name] = user_bid
  
  other_bidders = str(input("Are there any others bidders? Type 'yes' or 'no'. \n")).lower()
  if other_bidders == "yes":
    acution_running = True
    clear()
  else:
    acution_running = False
# Used max function to get the maximum value in the dictionary
max_bidder_name = max(record_dict, key=record_dict.get)

print(f"The winner is {max_bidder_name} with a bid of ${record_dict[max_bidder_name]} .")
