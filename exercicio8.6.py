entrada = open("lista.txt", "r")
lista = []
novosDados = []

def insercaoDadosNaLista(listaEntrada):
    for linha in listaEntrada:
        lista.append(linha)
    
    return lista

def ordenacaoPorNome(listaEntrada):
    listaEntrada.sort()
    return listaEntrada

def ordenacaoPorIdade(listaEntrada):
    listaPorIdade =[]
    for linha in listaEntrada:
        idade = str(linha.split(";")[1])
        nome = linha.split(";")[0]
        dado = idade +";" + nome
        listaPorIdade.append(dado)
    listaPorIdade.sort()
    return listaPorIdade

def calculoDaIdadeMedia(listaEntrada):
    soma = 0
    cont = 0
    mediaDasIdades = 0

    for linha in listaEntrada:
        soma = soma + float(linha.split(";")[1])
        cont = cont + 1
    mediaDasIdades = soma/cont

    return mediaDasIdades

def pessoaMaisVelha(listaEntrada):
    maiorIdade = 0
    
    for linha in listaEntrada:
        if int(linha.split(";")[1]) > maiorIdade:
            maiorIdade = int(linha.split(";")[1])
            nomeMaisVelha = linha.split(";")[0]
    nomeEidade = "Nome: " + nomeMaisVelha + "\nIdade: " + str(maiorIdade)
    return nomeEidade

def novoDado(nome, idade):
    novoDado = nome + ";" + str(idade)
    return novoDado

def insercaoDeNovoDado(novaLista, novoDado):
    novaLista.append(novoDado)

def atualizarDadosNoArquivo(listaNova, arquivoAtual):
    arquivo = open(arquivoAtual, "w")
    for linha in listaNova:
        nome = linha.split(";")[0]
        idade = linha.split(";")[1]
        novoDado = nome + ";" + str(idade)+"\n"
        arquivo.write(novoDado)
    arquivo.close()

listaDados = insercaoDadosNaLista(entrada)

listaOrdenadaPorNome = ordenacaoPorNome(listaDados)
listaOrdenadaPorIdade = ordenacaoPorIdade(listaDados)
mediaDeIdades = calculoDaIdadeMedia(listaDados)
maisVelho = pessoaMaisVelha(listaDados)

print("Ordenação por nome: ", listaOrdenadaPorNome)
print("===================")
print("Ordenação por idade: ", listaOrdenadaPorIdade)
print("===================")
print("Média das idades: ", mediaDeIdades)
print("===================")
print(maisVelho)

resp = "S"
while resp == "S":
    nome = input("Informe o nome: ")
    idade = int(input("Informe a idade a ser inserida: "))
    dados = novoDado(nome, idade)
    insercaoDeNovoDado(novosDados, dados)
    resp = input("Escreva <S> para nova inserção: ").upper()

atualizarDadosNoArquivo(novosDados, "lista.txt")
entrada.close()
