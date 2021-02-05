
from resetar_tela import clear_console, clear_pycharm
from easy_stuff import easy_questions
from medium_stuff import medium_questions
from hard_stuff import hard_questions
from database_de_pontos import score_atual

# Esta é a tela inicial da aplicação

while True:
    clear_pycharm()
    clear_console()

    print("\nBem vindo ao jogo das perguntas sobre matemática!")
    print("Selecione um nível de dificuldade - "
          "\n(1) - Fácil"
          "\n(2) - Médio"
          "\n(3) - Difícil"
          "\n(4) - Sair")
    escolha = input("Escolha o nível de dificuldade: ")

    while escolha != '1' and escolha != '2' and escolha != '3' and escolha != '4':
        print("\nA opção escolhida é inválida!")
        escolha = input("Escolha o nível de dificuldade: ")

    if escolha == '4':
        input("\nAté a próxima! Pressione enter para finalizar o programa: ")
        break

    elif escolha == '1':
        clear_pycharm()
        clear_console()
        print("\nVocê escolheu a dificuldade Fácil! Cada questão certa adiciona 1 ponto ao seu score e cada questão"
              " errada subtrai 1 ponto do seu score!")
        print(f"\nSeu score atual é de {score_atual()} ponto(s)!\n")
        input("Pressione enter para continuar: ")
        easy_questions()

    elif escolha == '2':
        clear_pycharm()
        clear_console()
        print("\nVocê escolheu a dificuldade Médio! Cada questão certa adiciona 2 pontos ao seu score e cada questão"
              " errada subtrai 2 pontos do seu score!")
        print(f"\nSeu score atual é de {score_atual()} ponto(s)!\n")
        input("Pressione enter para continuar: ")
        medium_questions()

    elif escolha == '3':
        clear_pycharm()
        clear_console()
        print("\nVocê escolheu a dificuldade Difícil! Cada questão certa adiciona 3 pontos ao seu score e cada questão"
              " errada subtrai 3 pontos do seu score!")
        print(f"\nSeu score atual é de {score_atual()} ponto(s)!\n")
        input("Pressione enter para continuar: ")
        hard_questions()
