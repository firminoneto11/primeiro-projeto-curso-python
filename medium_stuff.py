
from random import choice
from resetar_tela import clear_console, clear_pycharm
from database_de_pontos import atribuir_ponto, reduzir_ponto


def parsing_string(expr):
    """
    Esta função recebe uma expressão matemática no formato de string e retorna essa string executada em código Python.
    :param expr: Expressão matemática em string.
    :return: Resultado da expressão matemática.
    """
    return eval(expr)


def medium_questions():
    """
    Esta função realiza as perguntas matemáticas de adição, subtração e multiplicação de dificuldade média e verifica
    se as mesmas estão certas ou erradas. Se certas, adiciona 2 pontos ao score do usuário, caso contrário, remove 2
    pontos do score do usuário.
    :return: None
    """
    while True:
        clear_pycharm()
        clear_console()

        # Modo de dificuldade para as funções atribuir e reduzir pontos
        mode = 'medium'

        # Listas que contem as perguntas matemáticas de somar, subtrair e multiplicar
        l_add = [
            "( 2 * 5 ) + 5", "(2 * 2) + 10 + 2", "(4 + 3) ** 2", "2 + 4 + (2 * 3)", "( 2 * 2 ) + 20"
        ]
        l_sub = [
            "(2 * 5) - 5", "(2 * 2) + 10 - 2", "(4 - 3) ** 2", "2 - 4 + (2 * 3)", "(2 * 2) - 20"
        ]
        l_mul = [
            "(2 * 5) * 5", "(2 * 2) + (10 * 2)", "(4 * 3) ** 2", "(2 * 4) * (2 * 3)", "(2 * 2) * 20"
        ]

        # Escolhendo um tipo de pergunta matemática de forma aleatória
        modo_escolhido = choice(["l_add", "l_sub", "l_mul"])

        # Lógica que é realizada se o código escolher questões de adição
        if modo_escolhido == 'l_add':
            pergunta_escolhida = choice(l_add)
        # Lógica que é realizada se o código escolher questões de subtração
        elif modo_escolhido == 'l_sub':
            pergunta_escolhida = choice(l_sub)
        # Lógica que é realizada se o código escolher questões de multiplicação
        else:
            pergunta_escolhida = choice(l_mul)

        # Apresentação da pergunta e solicitação da resposta
        print("\n" + pergunta_escolhida)
        resposta = parsing_string(pergunta_escolhida)
        resposta_do_user = input("Resposta: ")

        try:
            resposta_do_user = int(resposta_do_user)
        except ValueError:
            print(f"\nA resposta informada é inválida!")
        else:
            if resposta_do_user == resposta:
                print("\nCorreto! Você ganhou 2 pontos!")
                print(f"Você agora tem {atribuir_ponto(mode)} ponto(s)!")
            else:
                print("\nErrado :( | Você perdeu 2 pontos!")
                print(f"A resposta certa era: {resposta}")
                print(f"Você agora tem {reduzir_ponto(mode)} ponto(s)!")

        # Fazendo uma verificação se o usuário gostaria de continuar jogando ou finalizar o programa
        next_option = input("\nPressione 'ENTER' para continuar jogando ou (1) para voltar ao menu inicial: ")
        while next_option != '' and next_option != '1':
            print('\nEscolha inválida!')
            next_option = input("Pressione 'enter' para continuar jogando ou (1) para voltar ao menu inicial: ")

        if next_option == '1':
            break
        else:
            continue


if __name__ == '__main__':
    medium_questions()
