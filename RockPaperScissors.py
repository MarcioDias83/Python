# Esse é um jogo simples de pedra, papel e tesoura para ser jogado contra o computador em Python. O programa permite que o usuário escolha uma opção e exibe o resultado. O jogo continua até que o usuário decida sair.
# This is a simple Python code for playing rock, paper, and scissors against the computer. The program prompts the user to choose an option and displays the result. The game continues until the user decides to quit.

from random import randrange

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

print("Select an option:")
user = int(input("1 - Rock\n2 - Paper\n3 - Scissors\n0 - Close the game.\n"))
while user != 0:
    random = randrange(1, 4) # change the range to include 3
    if user == 1:  # user choose rock
        if random == 1:
            print("Tie!")
        elif random == 2:
            print("You lose!")
        elif random == 3:
            print("You win!")
    elif user == 2:  # user choose paper
        if random == 1:
            print("You win!")
        elif random == 2:
            print("Tie!")
        elif random == 3:
            print("You lose!")
    elif user == 3:  # user choose scissors
        if random == 1:
            print("You lose!")
        elif random == 2:
            print("You win!")
        elif random == 3:
            print("Tie!")
    elif user < 0 or user > 3:
        print("Invalid option!")
    print("Select an option:")
    user = int(input("1 - Rock\n2 - Paper\n3 - Scissors\n0 - Close the game.\n"))

print("Closing...")
exit()
