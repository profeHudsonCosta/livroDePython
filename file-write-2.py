objFile = open("saida.txt", "w")
novoTexto = ["ABC\n", "DEF\n", "FIM\n"]
objFile.writelines(novoTexto)
objFile.close()