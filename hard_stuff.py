
from random import choice
from medium_stuff import parsing_string
from resetar_tela import clear_console, clear_pycharm
from database_de_pontos import atribuir_ponto, reduzir_ponto


def hard_questions():
    """
    Esta função realiza as perguntas matemáticas de adição, subtração, multiplicação e divisão de dificuldade difícil e
    verifica se as mesmas estão certas ou erradas. Se certas, adiciona 3 pontos ao score do usuário, caso contrário,
    remove 3 pontos do score do usuário.
    :return: None
    """
    while True:
        clear_pycharm()
        clear_console()

        # Modo de dificuldade para as funções atribuir e reduzir pontos
        mode = 'hard'

        # Lista que contém perguntas envolvendo expressões matemáticas contendo as 4 operações. Diferentemente das ante
        # riores, somente há uma lista que engloba todas as operações, tornando esse modo escolhido, realmente 'dificil'
        # para o usuário
        hard = [
            "((20 ** 2) + (25 / 5)) / 5",
            "(((9 / 3) * 5) + (30 / 15)) / 17",
            "((5 ** 3) / 5) + ((5 ** 2) * 2) / 5",
            "((((9 / 3) * 5) + (30 / 15)) / 17) / (((2 ** 2) + 4) / 8)",
            "((10 ** 2) ** (1 / 2)) / ((1 ** 10) + ((50 - 30) - 19))",
            "((7 * 7) + 5) / ((18 - (15 / 3) + 5) * 2)",
            "(30 - (5 * 6)) / ((7 + (2 * 10)) * ((40 - 30) + 5))",
            "(18 + (3 * 2)) / ((8 + (5 * 2)) / 6)",
            "((2 ** 2) / 4) + ((3 ** 2) * (100 ** 0.5))",
            "((-3 ** 2) * (-9 + (-3 ** 3))) / (-3 ** 2)"
        ]

        # Escolhendo uma das expressões da lista de expressões matemáticas
        pergunta_escolhida = choice(hard)

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
                print("\nCorreto! Você ganhou 3 pontos!")
                print(f"Você agora tem {atribuir_ponto(mode)} ponto(s)!")
            else:
                print("\nErrado :( | Você perdeu 3 pontos!")
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
    hard_questions()
