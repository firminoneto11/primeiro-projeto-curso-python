
from random import choice
from resetar_tela import clear_console, clear_pycharm
from database_de_pontos import atribuir_ponto, reduzir_ponto


def easy_questions():
    """
    Esta função irá conter algumas questões matemáticas de dificuldade fácil, conforme escolhido pelo usuário
    :return: None
    """
    while True:
        clear_pycharm()
        clear_console()
        lista = ["3 + 23", "4 + 7", "80 + 20", "46 + 4", "50 + 23", "23 + 12", "42 + 8", "30 + 11"]

        # A função choice escolhe uma das perguntas da lista de perguntas
        pergunta_escolhida = choice(lista)
        print("\n" + pergunta_escolhida)

        # Realizar o cast de string para inteiro da pergunta escolhida
        pergunta_escolhida = pergunta_escolhida.split(" ")
        pergunta_escolhida.remove("+")
        resposta = int(pergunta_escolhida[0]) + int(pergunta_escolhida[1])

        # Solicitar uma resposta do usuário
        resposta_do_user = input("Resposta: ")

        # Verificando se a resposta informada é correta
        try:
            resposta_do_user = int(resposta_do_user)
        except ValueError:
            print(f"\nA resposta informada é inválida!")
        else:
            if resposta_do_user == resposta:
                print("\nCorreto! Você ganhou 1 ponto!")
                print(f"Você agora tem {atribuir_ponto()} ponto(s)!")
            else:
                print("\nErrado :( | Você perdeu 1 ponto!")
                print(f"Você agora tem {reduzir_ponto()} ponto(s)!")

        # Fazendo uma verificação se o usuário gostaria de continuar joganndo ou finalizar o programa
        next_option = input("Pressione 'ENTER' para continuar jogando ou (1) para voltar ao menu inicial: ")
        while next_option != '' and next_option != '1':
            print('\nEscolha inválida!')
            next_option = input("Pressione 'enter' para continuar jogando ou (1) para voltar ao menu inicial: ")

        if next_option == '1':
            break
        else:
            continue


if __name__ == '__main__':
    easy_questions()
