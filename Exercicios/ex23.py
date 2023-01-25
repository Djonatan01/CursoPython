'''Exercício Python 23: Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.

A condição de % vai pegar o resto da divisão e como o numero esta sendo dividido por 1 vai pegar a casa da unidade
#A condição de % vai pegar o resto da divisão e como o numero esta sendo dividido por 10 vai pegar a casa da dezena
'''
num = int(input("informe um numero: "))

u = num // 1 % 10

d = num // 10 % 10

c = num // 100 % 10

m = num // 1000 % 10

print("Analisando o numero informado {}".format(num)) 

print("Unidade: {}".format(u))
print("Dezena: {}".format(d))
print("Centena: {}".format(c))
print("Milhar: {} ".format(m))