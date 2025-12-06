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

import random
rps = [rock , paper , scissors]
userChoice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. "))
computer = random.randint(0, 1)

if userChoice < 0 and userChoice > 2:
    print("Invalid choice! Please pick 0, 1, or 2.")

print("You chose:")
print(rps[userChoice])
print("Computer chose:")
print(rps[computer])

if userChoice == computer:
    print("It's a draw!")
elif (userChoice == 0 and computer == 2) or \
    (userChoice == 1 and computer == 0) or \
    (userChoice == 2 and computer == 1):
    print("You win!")
else:
    print("You lose!")