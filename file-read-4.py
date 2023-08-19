objFile = open("arquivo.txt", "r")

linha = objFile.readline()

while linha:
    print(linha, end="")
    linha = objFile.readline()

objFile.close()