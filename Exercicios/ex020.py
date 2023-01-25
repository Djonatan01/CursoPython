import random

'''Exercício Python 20: O mesmo professor do desafio 19 quer sortear a ordem de apresentação de trabalhos dos alunos. Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.
'''

n1 = input("Primeiro aluno: ")
n2 = input("Segundo aluno: ")
n3 = input("Terceiro aluno: ")
n4 = input("Quarto aluno: ")

#'Criar uma lista para qua o sistema radom faça as escolhas aleatórias'
lista = [n1,n2,n3,n4]
#'shuffle serve para embaralhar a lista informada'
random.shuffle(lista)
print("O aluno escolhido foi {} ".format(lista))