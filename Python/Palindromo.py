# Verificar se uma palavra é um palíndromo:
# Pedir ao usuário para digitar uma palavra
# Armazenar a palavra em uma variável
# Verificar se a palavra é um palíndromo (a palavra é igual quando lida da esquerda para a direita e da direita para a esquerda)
# Imprimir a resposta se a palavra é um palíndromo ou não.

# Palavras para teste: afã, aia, aibofobia, ala, ama, anã, anilina, ata, arara, asa, ele, esse, mamam
# matam, metem, mirim, oco, omissíssimo, osso, ovo, radar, raiar, ralar, rapar, rasar, reger, reler
# reter, rever, reviver, rir, sacas, saias, salas, socos, sopapos, sós

palavra = input("Digite uma palavra!\n")
palavra = palavra.lower()
palavraInvertida = palavra[::-1]
if palavraInvertida == palavra:
    print("É palindromo")
else:
    print("Não é palindromo")
