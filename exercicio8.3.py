arquivoDeSaida = open("saida.txt", "w")

contador = int(input("Informe quantas linhas serão gravadas no arquivo: "))
cont = 0

while contador >= cont:
    linhaAdicionada = "Linha " + str(cont) + "\n"
    arquivoDeSaida.write(linhaAdicionada)
    cont = cont + 1



