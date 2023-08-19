objFile = open("arquivo.txt", "r")

linha = objFile.readline()
linha = objFile.readline()

soma = 0

while linha:
    soma = soma + float(linha.split()[1])
    linha = objFile.readline()

print(soma)