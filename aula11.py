lista = [1,10]
try:
    divisao = 10/1
    numero = lista[1]
    x = a
except ZeroDivisionError:
    print("Não é possível realizar uma divisão por zero")
except IndexError:
    print("Erro ao acessar um índice inválido da lista")
except BaseException as ex:
    print('Erro desconhecido. Erro: {}'.format(ex))
