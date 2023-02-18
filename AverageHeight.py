# Este código pede ao usuário uma lista de alturas de alunos, converte cada altura para um número inteiro e, em seguida, calcula a média aritmética das alturas e imprime o resultado arredondado para o número inteiro mais próximo.
# This code prompts the user for a list of student heights, converts each height to an integer, and then calculates the arithmetic mean of the heights and prints the result rounded to the nearest integer.

# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆

#Write your code below this row 👇
from itertools import count

total_height = 0
num_students = 0
for height in student_heights:
  total_height += height
  num_students += 1
average_height = total_height / num_students
print(round(average_height))