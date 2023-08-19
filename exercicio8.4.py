entrada = open("entrada.txt", "r")

somaNotas = 0
contadorDeReprovacoes = 0
contadorDeAlunos = 0

linha = entrada.readline()
linha = entrada.readline()

while linha:
    somaNotas = somaNotas + float(linha.split()[1])
    if float(linha.split()[1]) < 7.0:
        contadorDeReprovacoes = contadorDeReprovacoes + 1
    contadorDeAlunos = contadorDeAlunos + 1
    linha = entrada.readline()

mediaDaTurma = somaNotas/contadorDeAlunos

print("Número de alunos: ", contadorDeAlunos)
print("Nùmero de reprovações: ", contadorDeReprovacoes)
print("Média da turma: ", mediaDaTurma)

paraGravar = "Número de alunos: " + str(contadorDeAlunos) + "\n" +"Número de reprovações: " + str(contadorDeReprovacoes) + "\n" + "Média da turma: " + str(mediaDaTurma) + "\n"
saida = open("saida.txt", "w")
saida.write(paraGravar)

saida.close()
entrada.close()

