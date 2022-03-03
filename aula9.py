#arquivo = open("teste.txt", "w")
arquivo = open("teste.txt", "a") #"w" cria arquivi novo, "a" atualiza
arquivo.write("\nSegunda linha")
arquivo.close()