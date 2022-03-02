a = int(input("Primeiro bimestre: "))
while a > 10:
    a = int(input("Você digitou errado. Primeiro bimestre: "))
b = int(input("Segundo bimestre: "))
while b > 10:
    b = int(input("Você digitou errado. Segundo bimestre: "))
c = int(input("Terceiro bimestre: "))
while c > 10:
    c = int(input("Você digitou errado. Terceiro bimestre: "))
d = int(input("Quarto bimestre: "))
while d > 10:
    d = int(input("Você digitou errado. Quarto bimestre: "))
media = (a + b + c + d) / 4

if a < 10 and b < 10 and c < 10 and d < 10:
    print("Média: {}".format(media))
else:
    print("Foi informada alguma nota errada")
