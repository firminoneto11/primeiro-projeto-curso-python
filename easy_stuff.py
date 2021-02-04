
from random import choice
from resetar_tela import clear_console, clear_pycharm
from database_de_pontos import atribuir_ponto, reduzir_ponto


def easy_questions():
    """
    Esta função realiza as perguntas matemáticas de adição, subtração e multiplicação de dificuldade fácil e verifica
    se as mesmas estão certas ou erradas. Se certas, adiciona 1 ponto ao score do usuário, caso contrário, remove 1
    ponto do score do usuário.
    :return: None
    """
    while True:
        clear_pycharm()
        clear_console()

        # Modo de dificuldade para as funções atribuir e reduzir pontos
        mode = 'easy'

        # Listas que contem as perguntas matemáticas de somar, subtrair e multiplicar
        l_add = ["3 + 23", "4 + 7", "80 + 20", "46 + 4", "50 + 23", "23 + 12", "42 + 8", "30 + 11", "13 + 2", "21 + 13"]
        l_sub = ["3 - 23", "4 - 7", "80 - 20", "46 - 4", "50 - 23", "23 - 12", "42 - 8", "30 - 11", "13 - 2", "21 - 13"]
        l_mul = ["3 * 3", "4 * 7", "80 * 2", "4 * 4", "5 * 2", "3 * 2", "8 * 4", "30 * 10", "13 * 2", "21 * 3"]

        # Escolhendo um tipo de pergunta matemática de forma aleatória
        modo_escolhido = choice(['l_add', 'l_sub', 'l_mul'])

        # Lógica que é realizada se o código escolher questões de adição
        if modo_escolhido == 'l_add':
            pergunta_escolhida = choice(l_add)
            print("\n" + pergunta_escolhida)
            pergunta_escolhida = pergunta_escolhida.split(" ")
            pergunta_escolhida.remove("+")
            resposta = int(pergunta_escolhida[0]) + int(pergunta_escolhida[1])
            resposta_do_user = input("Resposta: ")

            try:
                resposta_do_user = int(resposta_do_user)
            except ValueError:
                print(f"\nA resposta informada é inválida!")
            else:
                if resposta_do_user == resposta:
                    print("\nCorreto! Você ganhou 1 ponto!")
                    print(f"Você agora tem {atribuir_ponto(mode)} ponto(s)!")
                else:
                    print("\nErrado :( | Você perdeu 1 ponto!")
                    print(f"A resposta certa era: {resposta}")
                    print(f"Você agora tem {reduzir_ponto(mode)} ponto(s)!")
        # Lógica que é realizada se o código escolher questões de subtração
        elif modo_escolhido == 'l_sub':
            pergunta_escolhida = choice(l_sub)
            print("\n" + pergunta_escolhida)
            pergunta_escolhida = pergunta_escolhida.split(" ")
            pergunta_escolhida.remove("-")
            resposta = int(pergunta_escolhida[0]) - int(pergunta_escolhida[1])
            resposta_do_user = input("Resposta: ")

            try:
                resposta_do_user = int(resposta_do_user)
            except ValueError:
                print(f"\nA resposta informada é inválida!")
            else:
                if resposta_do_user == resposta:
                    print("\nCorreto! Você ganhou 1 ponto!")
                    print(f"Você agora tem {atribuir_ponto(mode)} ponto(s)!")
                else:
                    print("\nErrado :( | Você perdeu 1 ponto!")
                    print(f"A resposta certa era: {resposta}")
                    print(f"Você agora tem {reduzir_ponto(mode)} ponto(s)!")
        # Lógica que é realizada se o código escolher questões de multiplicação
        else:
            pergunta_escolhida = choice(l_mul)
            print("\n" + pergunta_escolhida)
            pergunta_escolhida = pergunta_escolhida.split(" ")
            pergunta_escolhida.remove("*")
            resposta = int(pergunta_escolhida[0]) * int(pergunta_escolhida[1])
            resposta_do_user = input("Resposta: ")

            try:
                resposta_do_user = int(resposta_do_user)
            except ValueError:
                print(f"\nA resposta informada é inválida!")
            else:
                if resposta_do_user == resposta:
                    print("\nCorreto! Você ganhou 1 ponto!")
                    print(f"Você agora tem {atribuir_ponto(mode)} ponto(s)!")
                else:
                    print("\nErrado :( | Você perdeu 1 ponto!")
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
    easy_questions()
