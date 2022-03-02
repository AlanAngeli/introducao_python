def contador_letras(lista_palavras):
    contador =[]
    for x in lista_palavras:
        quantidade = len(x)
        contador.append(quantidade) #adicionando a variável quantidade na lista
    return contador

if __name__=='__main__':
    lista = {"cachorro", "gato"}
    print(contador_letras(lista)) #quantas letras têm cada palavra da lista