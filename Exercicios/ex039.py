'''
Exercício Python 43: Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu Índice de Massa Corporal (IMC) e mostre seu status, de acordo com a tabela abaixo:

– IMC abaixo de 18,5: Abaixo do Peso

– Entre 18,5 e 25: Peso Ideal

– 25 até 30: Sobrepeso

– 30 até 40: Obesidade

– Acima de 40: Obesidade Mórbida
'''

peso = float(input("Informe seu peso? (KG) ")) 
altura = float(input("Qual a sua altura (m) "))

imc = peso / (altura ** 2)

print("O IMC dessa pessoa é de {:.1f} ".format(imc))

if imc > 40 :
    print("Você esta com obsidade morbida")
elif 30 <= imc < 40:
    print("Você esta com obesidade")
elif 25 <= imc < 30 :
    print("Você está com sobrepeso")
elif 18.5 <= imc < 25 :
    print("Parbens, você esta na faixa de peso normal")
else:
    print("Você está abaixo do peso")