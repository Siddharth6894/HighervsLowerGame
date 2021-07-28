from art import logo, vs
from game_data import data
import random
from os import system, name
#display art
print(logo)
score = 0

def clear():
    if name == "nt":
        _ = system("cls")
def format_data(account):
  """format the account data into printable format"""
  account_name = account["name"]
  account_descr = account["description"]
  account_country = account["country"]
  return f"{account_name}, a {account_descr}, from {account_country}"

def check_answer(guess, a_follower_count, b_follower_count):
  """Take the user guess and follower counts and return if they got it right"""
  if a_follower_count > b_follower_count:
    return guess == "a"
  elif b_follower_count > a_follower_count:
    return guess == "b"  


game_should_continue = True
account_b = random.choice(data)

#make the game repetable
while game_should_continue:
  #generate random account from the data
  #making account at position b to become account a
  account_a = account_b
  account_b = random.choice(data)
  while account_a == account_b:
    account_b = random.choice(data)

  print(f"Compare A: {format_data(account_a)}")
  print(vs)
  print(f"Against B: {format_data(account_b)}")

  #Ask user for a guess
  guess = input("Who has more followers? 'A' or 'B': ").lower()

  #Check if the user got it right
  a_follower_count = account_a["follower_count"]
  b_follower_count = account_b["follower_count"]

  is_correct = check_answer(guess, a_follower_count, b_follower_count)
  
  clear()
  print(logo)
  if is_correct:
    score += 1 
    print(f"You're right! Current score: {score}")
  else:
    print(f"Sorry, that's wrong. Final score: {score}")
    game_should_continue = False
