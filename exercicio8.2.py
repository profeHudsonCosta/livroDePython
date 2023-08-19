fileObj = open("dados.txt")

linhas = fileObj.readlines()
soma = 0

for linha in linhas:
    soma = soma + float(linha.split()[1])

print(soma)