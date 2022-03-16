lista = [1,10]
try:
    divisao = 10/0
    numero = lista[1]
    x = a

except ZeroDivisionError:
    print("Não é possível realizar uma divisão por zero")
except ArithmeticError:
    print("Houve um erro ao realizar uma operação aritmética")
except IndexError:
    print("Erro ao acessar um índice inválido da lista")
except Exception as ex:
    print('Erro desconhecido. Erro: {}'.format(ex))
else:
    print('Execita quando não ocorre excessão')