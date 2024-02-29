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

# Write your code below this line 👇
import random

player_choose = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors: "))
computer_choose = random.randint(0, 2)

icons = [rock, paper, scissors]

if player_choose == computer_choose:
    print("You choose:\n")
    print(icons[player_choose])
    print("Computer choose:\n")
    print(icons[computer_choose])
    print("It's draw!")
elif (player_choose == 0 and computer_choose == 2) or (player_choose == 1 and computer_choose == 0) or (player_choose == 2 and computer_choose == 1):
    print("You choose:\n")
    print(icons[player_choose])
    print("Computer choose:\n")
    print(icons[computer_choose])
    print("You win!")
elif (player_choose == 0 and computer_choose == 1) or (player_choose == 1 and computer_choose == 2) or (player_choose == 2 and computer_choose == 0):
    print("You choose:\n")
    print(icons[player_choose])
    print("Computer choose:\n")
    print(icons[computer_choose])
    print("Computer wins!")
else:
    print("Incorrect input. Try again!")



