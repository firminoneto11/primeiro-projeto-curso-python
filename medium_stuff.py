
from random import choice
from resetar_tela import clear_console, clear_pycharm


def medium_questions():
    """
    Esta função realiza as perguntas matemáticas de adição, subtração e multiplicação de dificuldade média e verifica
    se as mesmas estão certas ou erradas. Se certas, adiciona 1 ponto ao score do usuário, caso contrário, remove 1
    ponto do score do usuário.
    :return: None
    """
    while True:
        clear_pycharm()
        clear_console()

        # Modo de dificuldade para as funções atribuir e reduzir pontos
        mode = 'medium'

        # Como escolher perguntas medias
        l_add = ["( 2 * 5 ) + 5", "( 2 * 2 ) + 20"]
        question = choice(l_add)
        print(f"A pergunta escolhida é: {question}")
        list_of_n = []

        # Transformar em uma função essa lógica
        for le in question:
            if le == ')':
                break
            else:
                try:
                    list_of_n.append(int(le))
                except Exception:
                    continue

        question = question.split(' ')
        question.remove('+')
        question.remove('(')
        question.remove(')')
        question.remove('*')

        multi = 1
        for n in list_of_n:
            multi = multi * n

        return f"A resposta é: {int(question[2]) + multi}"


if __name__ == '__main__':
    print(medium_questions())
