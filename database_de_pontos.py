
from os.path import exists


def atribuir_ponto(dificuldade):
    """
    Esta função cria um arquivo de texto contendo o score do usuário e também realiza a operação de adição de pontos do
    score do mesmo. Caso o arquivo contendo o score do usuário não exista, ele cria um novo, porém este é inicializado
    em 0.
    :param dificuldade: Modo de dificuldade passado pela função que contem as perguntas matemáticas.
    :return: Retorna a quantidade atual de pontos.
    """

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

    if dificuldade == 'easy':
        novo_total = pontos_anteriores + 1
    elif dificuldade == 'medium':
        novo_total = pontos_anteriores + 2
    else:
        novo_total = pontos_anteriores + 3
    with open(documento_dos_pontos, mode='w', encoding='utf-8', newline=None) as file:
        file.write(str(novo_total))

    return novo_total


def reduzir_ponto(dificuldade):
    """
    Esta função cria um arquivo de texto contendo o score do usuário e também realiza a operação de remoção de pontos do
    score do mesmo. Caso o arquivo contendo o score do usuário não exista, ele cria um novo, porém este é inicializado
    em 0.
    :param dificuldade: Modo de dificuldade passado pela função que contem as perguntas matemáticas.
    :return: Retorna a quantidade atual de pontos.
    """

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

    if dificuldade == 'easy':
        novo_total = pontos_anteriores - 1
    elif dificuldade == 'medium':
        novo_total = pontos_anteriores - 2
    else:
        novo_total = pontos_anteriores - 3
    with open(documento_dos_pontos, mode='w', encoding='utf-8', newline=None) as file:
        file.write(str(novo_total))

    return novo_total
