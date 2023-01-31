'''Exercício Python 36: Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar. A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.'''


valorCasa = float(input("Informe o valor da casa a ser financiada R$ "))

Salario = float(input("Informe o salário do comprador R$ "))

anos = int(input("Quantos anos de financiamento? "))

prestação = valorCasa / (anos * 12)

minimo = Salario * 30 /100

print("Para pagar uma casa de R${:.2f} em {} anos" .format(valorCasa, anos), end="")

print(" a prestação será de R${:.2f}" .format(prestação))

if prestação <= minimo:
    print("Emprestimo pode ser aprovado!!!")
else:
    print("Emprestimo negado!!!")
