calculadora = {
    "soma": lambda a, b: a + b,
    "subtracao": lambda a, b: a - b,
    "multiplicacao": lambda a, b: a * b,
    "divisao": lambda a, b: a / b,
}

print(type(calculadora))

print()

soma = calculadora["soma"]
print("A soma é: {}".format(soma(10,8)))
print()
multiplicaco = calculadora["multiplicacao"]
print("A multiplicacao é: {}".format(multiplicaco(10,5)))