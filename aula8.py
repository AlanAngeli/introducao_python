"""
módulos são aqrquivos .py (ex: aula8.py)
Podem interagir entre eles

"""

from aula7_3 import Televisao
from aula7_calculadora import Calculadora

if__name__=='__main__':
    televisao = Televisao
    print(televisao.ligada)
    televisao.power()
    print(televisao.ligada)

    print()

    calculadora = Calculadora(5,10)
    print(calculadora.soma())

