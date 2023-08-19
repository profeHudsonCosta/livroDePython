objFile = open("arquivo.txt", "r")

todoConteudo = objFile.readlines()

print("---------------------------")
for linha in todoConteudo:
    print(linha, end="")
print("---------------------------")
objFile.close()