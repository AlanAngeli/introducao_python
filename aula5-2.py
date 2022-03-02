lista = [1,3,5,7]
lista_animais = ["Cachorro", "Gato", "Elefante"]

if "Gato" in lista_animais:
    print("Existe um gato na lista")
else:
    print("Não existe um gato na lista")

print()

if "Lobo" in lista_animais:
    print("Existe um lobona lista")
else:
    print("Não existe um lobo na lista")
    lista_animais.append("Lobo") #adiciona o lobo na lista
    lista_animais.pop(1) #remove o gato da lista
    lista_animais.remove("Elefante") #outra maneira de remover

print()
print(lista_animais)