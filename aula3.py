a = int(input("Primeiro valor: "))
b = int(input("Segundo valor: "))
c = int(input("Terceiro valor: "))

if a > b:
    print("O maior número é {}".format(a))
elif b > a:
    print("O maior número é {}".format(b))
else:
    print("O maior número é {}".format(c))
print("Fim do programa")