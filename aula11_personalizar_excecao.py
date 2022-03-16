while True:
    try:
        x = int(input('Entre com uma nota de 0 a 10: '))
        print(x)
        break
    except ValueError:
        print('Valor inválido. Deve-se digitar apenas números.')
    