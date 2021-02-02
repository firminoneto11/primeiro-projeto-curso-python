
from os.path import exists


def atribuir_ponto():

    # Setando o nome do arquivo txt dos pontos
    documento_dos_pontos = ".\\pontos.txt"

    # Fazendo uma verificação se o mesmo existe, se não, ele será criado
    if exists(documento_dos_pontos) is False:
        with open(documento_dos_pontos, mode='w', encoding='utf-8', newline=None) as file:
            file.write("0")

    # Fazendo a lógica de escrita de pontos no arquivo
    pontos_anteriores = 0
    with open(documento_dos_pontos, mode='r', encoding='utf-8', newline=None) as file:
        pontos_anteriores = int(file.read())

    novo_total = pontos_anteriores + 1
    with open(documento_dos_pontos, mode='w', encoding='utf-8', newline=None) as file:
        file.write(str(novo_total))

    return novo_total


def reduzir_ponto():

    # Setando o nome do arquivo txt dos pontos
    documento_dos_pontos = ".\\pontos.txt"

    # Fazendo uma verificação se o mesmo existe, se não, ele será criado
    if exists(documento_dos_pontos) is False:
        with open(documento_dos_pontos, mode='w', encoding='utf-8', newline=None) as file:
            file.write("0")

    # Fazendo a lógica de escrita de pontos no arquivo
    pontos_anteriores = 0
    with open(documento_dos_pontos, mode='r', encoding='utf-8', newline=None) as file:
        pontos_anteriores = int(file.read())

    if pontos_anteriores == 0:
        return pontos_anteriores

    novo_total = pontos_anteriores - 1
    with open(documento_dos_pontos, mode='w', encoding='utf-8', newline=None) as file:
        file.write(str(novo_total))

    return novo_total
