'''Exercício Python 47: Crie um programa que mostre na tela todos os números pares que estão no intervalo entre 1 e 50.'''

soma = 0

for a in range(2, 51, 2):
    print(a , end=" ")
    soma = a + soma
print("O total de numeros pares de 0 até 50 {} " .format(soma))