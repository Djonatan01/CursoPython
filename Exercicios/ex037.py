'''Exercício Python 37: Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal.'''

numero = int(input("Digite um numero inteiro? "))

print('''Escolha uma das bases para converção:
[ 1 ] para binário
[ 2 ] para octal
[ 3 ] para hexadecimal

''')
opcao = int(input("Sua opção desejada? "))

if opcao == 1:
    print("{} convertido para binario é igual a {}".format(numero, bin(numero) [2:]))
elif opcao == 2:
     print("{} convertido para octal é igual a {}".format(numero, oct(numero) [2:]))
elif opcao == 3:
    print("{} convertido para hexadecimal é igual a {}".format(numero, hex(numero) [2:]))
else:
    print("{} valor incorreto")
    