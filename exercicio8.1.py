arquivo = open("arquivo.txt", "r")

conteudo = arquivo.readlines()

cont = 0

while cont <= 2:
    print(conteudo[cont])
    cont = cont +1