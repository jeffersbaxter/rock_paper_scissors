import random

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

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
ROCK = 0
PAPER = 1
SCISSORS = 2
choices = [
  {
    "name": "ROCK",
    "choice": rock
  },
  {
    "name": "PAPER",
    "choice": paper
  },
  {
    "name": "SCISSORS",
    "choice": scissors
  }
]
choice_names = ["ROCK", "PAPER", "SCISSORS"]
# random choice Rock, Paper or Scissors
cpu_choice = random.choice(choices)

user_input = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))
if user_input > SCISSORS:
  user_input = int(input("Too High! Choose either Rock (0), Paper (1), Scissors (2) "))

user_choice = choices[user_input]

if user_choice["name"] == cpu_choice["name"]:
  print(f"Draw! You both chose {user_choice['choice']}. Game Over!")

if user_choice["name"] == choice_names[ROCK]:
  if cpu_choice["name"] == choice_names[PAPER]:
    print(f"CPU wins with Paper! {cpu_choice['choice']} beats {user_choice['choice']}")

  if cpu_choice["name"] == choice_names[SCISSORS]:
    print(f"You win! {user_choice['choice']} beats {cpu_choice['choice']}")

if user_choice["name"] == choice_names[PAPER]:
  if cpu_choice["name"] == choice_names[SCISSORS]:
    print(f"CPU wins! {cpu_choice['choice']} beats {user_choice['choice']}")

  if cpu_choice["name"] == choice_names[ROCK]:
    print(f"You win! {user_choice['choice']} beats {cpu_choice['choice']}")

if user_choice["name"] == choice_names[SCISSORS]:
  if cpu_choice["name"] == choice_names[ROCK]:
    print(f"CPU wins! {cpu_choice['choice']} beats {user_choice['choice']}")

  if cpu_choice["name"] == choice_names[PAPER]:
    print(f"You win! {user_choice['choice']} beats {cpu_choice['choice']}")
