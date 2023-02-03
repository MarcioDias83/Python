# Escreva um programa para criar uma lista aninhada de palavras. O programa deve receber uma entrada do usuário e adicionar essa
# palavra à lista. O usuário pode adicionar quantas palavras desejar e o programa deve exibir a lista final.

def clear_screen():
    print("\033c", end="")

lista = []

palavras = input("Digite uma palavra ou pressione 1 para parar.\n")
lista.append(palavras)

while palavras:
    clear_screen()
    palavras = input("Digite uma palavra ou pressione 1 para parar.\n")
    if palavras != '1':
        lista.append(palavras)
    else:
        break
    
if '1' in lista:
    lista.remove('1')
    
print(lista)
    