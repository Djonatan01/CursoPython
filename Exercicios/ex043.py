
num  = int(input("Digite um numero para sua tabuada "))
print("-*" * num)
for tab in range(0,11):
    print("{} X {} = {}".format(num, tab, (num * tab)))
print("-*" * num)