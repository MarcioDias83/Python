# Este código simula uma jogada de moeda, gera um número inteiro aleatório usando randint() e armazena em uma variável "random". Usa uma estrutura de controle de fluxo "if" para determinar se é 0 (cauda) ou 1 (cabeça) e atribui a string correspondente a "random". Por fim, imprime a string.
# This code simulates a coin flip, generates a random integer using randint() and stores it in a "random" variable. It uses an "if" flow control structure to determine if it's 0 (tails) or 1 (heads) and assigns the corresponding string to "random". Finally, it prints the string.

import random

random = random.randint(0, 1)
if random == 0:
    random = "Tails"
else:
    random = "Heads"
print(random)