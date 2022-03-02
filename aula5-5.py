lista = [12,10,7,5]
lista_animais = ["Cachorro", "Gato", "Elefante", "Lobo", "Arara"]

tupla = (1,10,12,14) #tupla é imutável
print(len(tupla)) #quantos elementos têm na tupla
print(len(lista_animais))#quantos elementos têm na lista

tupla_animal = tuple(lista_animais)
print(type(tupla_animal))

lista_numerica  = list(tupla)
print(type(lista_numerica))
lista_numerica[0] = 100
print(lista_numerica)

