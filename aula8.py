"""
módulos são aqrquivos .py (ex: aula8.py)
Podem interagir entre eles

"""

from aula7_3 import Televisao
from aula7_calculadora import Calculadora
from aula8_2 import contador_letras

if __name__=='__main__':
    televisao = Televisao()
    print(televisao.ligada)
    televisao.power()
    print(televisao.ligada)

    print()

    calculadora = Calculadora(5,10)
    print(calculadora.soma())

    print()

    lista = ["cachorro", "gato", "elefante"]
    total_letras = contador_letras(lista)
    print("Total de letras por lavra da listas: {}".format(total_letras))

