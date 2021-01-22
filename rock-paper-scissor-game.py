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

drawing = [rock,paper,scissors]

choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. "))

computer_choice = random.randint(0,2)

if choice == computer_choice:
  print("You chose:\n" + drawing[choice] + "\nComputer chose:" + drawing[computer_choice] + "\nIt's a draw, play again!")
elif choice == 0 and computer_choice == 1 or choice == 1 and computer_choice == 2 or choice == 2 and computer_choice == 0:
  print("You chose:\n" + drawing[choice] + "\nComputer chose:" + drawing[computer_choice] + "\nYou lost")
elif choice > 2:
  print("Invalid choice, play again!")
else: print("You chose:\n" + drawing[choice] + "\nComputer chose:" + drawing[computer_choice] + "\nYou won!")