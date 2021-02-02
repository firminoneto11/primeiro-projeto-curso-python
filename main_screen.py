
from resetar_tela import clear_console, clear_pycharm
from easy_stuff import easy_questions

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
        print("Você escolheu a dificuldade Fácil!")
        input("Pressione enter para continuar: ")
        easy_questions()

    elif escolha == '2':
        pass
    elif escolha == '3':
        pass
