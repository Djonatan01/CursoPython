import random

n1 = input("Primeiro aluno: ")
n2 = input("Segundo aluno: ")
n3 = input("Terceiro aluno: ")
n4 = input("Quarto aluno: ")

'Criar uma lista para qua o sistema radom faça as escolhas aleatórias'
lista = [n1,n2,n3,n4]
escolhido = random.choice(lista)
print("O aluno escolhido foi {}".format(escolhido))