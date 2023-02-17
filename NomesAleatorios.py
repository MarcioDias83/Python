# Este exercício visa escolher um nome aleatoriamente de uma lista fornecida pelo usuário. O usuário fornece uma string de nomes separados por vírgulas que é convertida em uma lista. Um nome é então escolhido aleatoriamente e a mensagem "Nome selecionado + vai pagar o jantar hoje" é impressa.
# This exercise aims to randomly select a name from a list provided by the user. The user provides a string of names separated by commas which is converted into a list. A name is then randomly selected and the message "Selected Name + will pay for dinner tonight" is printed.

import random

names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")

print(names [random.randrange(len(names))] + " is going to buy the meal today")