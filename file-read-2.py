objFile = open("arquivo.txt", "r")

todoConteudo = objFile.read()
print("----------")
print(todoConteudo)
print("----------")

objFile.close()