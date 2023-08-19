objFile = open("arquivo.txt", "r")

for linha in objFile:
    print(linha, end="")

objFile.close()