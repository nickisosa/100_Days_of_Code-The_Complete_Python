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

""" 
Rock beats Scissors
Paper beats Rock
Scissors beats Paper
"""
choices = [rock, paper, scissors]
user_input_choice = int(input("What do you want to choose? Type 0 for Rock, 1 for Paper or 2 for Scissors: "))
#computer_choice = random.choice(choices)

random_index = random.randint(0, 2)
computer_choice = choices[random_index]

#Rock Logic
if user_input_choice == 0 and computer_choice == 0: # A Draw
    print("User Input:" + rock)
    print(f'Computer Choice: ' + {computer_choice})
    print("Its a draw!")
    if user_input_choice == 0 and computer_choice == 2: # Computer Loses
        print("User Wins")
        print("Users Choice: " + rock)
        print("Computer Choice: " + scissors)
else:
    print("User: " + rock)
    print("Computer: " + computer_choice)
    print("You Lose!")

"""
#Paper Logic
elif user_input_choice == 1 and computer_choice == 1:
    print("Its a draw!")
    if user_input_choice == 1 and computer_choice == 0:
        print("Users Choice: " + paper)
        print("Computer Choice: " + computer_choice)
        print("You Win!")
    else:
        print("User Input: " + paper)
        print("Computer Choice: " + computer_choice)
        print("YOU LOSEEEEE!")
else:
    print("Invalid Entry, You lose!")

#Scissors Logic

elif user_input_choice == 2 and computer_choice == 2:
    print("Its a draw!")
    if user_input_choice == 2 and computer_choice == 1:
        print("Users Choice: " + paper)
        print("Computer Choice: " + choices[computer_choice])
        print("Winner")
    else:
        print("User Input: " + user_input_choice)
        print("Computer Choice: " + computer_choice)
        print("YOU LOSEEEEEE!")
"""


