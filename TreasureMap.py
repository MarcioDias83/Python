# Você foi designado para escrever um código em que um mapa do tesouro é representado por uma matriz de quadrados brancos ("⬜️"). O mapa é armazenado como uma lista de três listas, cada uma representando uma linha. O usuário é solicitado a inserir a posição onde eles desejam colocar o tesouro e o código colocará um "X" nessa posição no mapa. Finalmente, o mapa atualizado é impresso.
# You have been tasked to write a code in which a treasure map is represented by a matrix of white squares ("⬜️"). The map is stored as a list of three lists, each representing a row. The user is asked to input the position where they want to put the treasure and the code will place an "X" in that position on the map. Finally, the updated map is printed.

row1 = ["⬜️","️⬜️","️⬜️"]
row2 = ["⬜️","⬜️","️⬜️"]
row3 = ["⬜️️","⬜️️","⬜️️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")

column = int(position[0]) - 1
row = int(position[1]) - 1
map[row][column] = 'X'

print(f"{row1}\n{row2}\n{row3}")