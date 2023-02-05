# Crie um programa que cria uma lista aninhada com números inteiros. O programa deve permitir que o usuário insira números e
# adicione à lista. O programa deve exibir a lista final e a soma de todos os números na lista.

lista = [] # Cria uma lista vazia
soma = 0
numeros = input("Digite um número inteiro ou pressione A para encerrar!\n")
lista.append(numeros)

while numeros:
    numeros = input("Digite um número inteiro ou pressione A para encerrar!\n")
    if numeros != 'A':
        lista.append(numeros)
    else:
        break
if 'A' in lista:
    lista.remove('A')
    lista = numeros.sort(key=int)
print(lista)

# Soma os números da lista e imprime na tela
for numeros in lista:
    soma += int(numeros)
print(soma)
        