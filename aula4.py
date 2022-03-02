#for x in range(0, 101):
#    print(x)

a = int(input("Entre com um número: "))


div = 0
for x in range(1, a+1):
    resto = a % x
    print(a, resto)
    if resto == 0:
        div = div + 1

if div == 2:
    print("Número {} é primo.".format(a))
else:
    print("Número {} não é primo".format(a))