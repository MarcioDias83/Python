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
usuario = int(input("1 - Rock\n2 - Paper\n3 - Scissors\n0 - Close the game.\n"))
while usuario != 0:
    random = randrange(1, 4) # change the range to include 3
    if usuario == 1:  # usuário escolheu pedra
        if random == 1:
            print("Empate!")
        elif random == 2:
            print("Você perdeu!")
        elif random == 3:
            print("Você ganhou!")
    elif usuario == 2:  # usuário escolheu papel
        if random == 1:
            print("Você ganhou!")
        elif random == 2:
            print("Empate!")
        elif random == 3:
            print("Você perdeu!")
    elif usuario == 3:  # usuário escolheu tesoura
        if random == 1:
            print("Você perdeu!")
        elif random == 2:
            print("Você ganhou!")
        elif random == 3:
            print("Empate!")
    elif usuario < 0 or usuario > 3:
        print("Opção inválida!")
    print("Select an option:")
    usuario = int(input("1 - Rock\n2 - Paper\n3 - Scissors\n0 - Close the game.\n"))

print("Saindo...")
exit()
