import random

def localizar_posicao_palavras(texto, letra):
    posicoes = []
    for i in range(len(texto)):
        if texto[i] == letra:
            posicoes.append(i)
    return posicoes

def add_animal_txt(add_animal):
    arquivo = open('animais.txt', 'a', encoding="utf-8")
    arquivo.write(add_animal + "\n")
    print("Operação concluída!")
    arquivo.close()

    print("\nArquivo atualizado:")
    arquivo = open('animais.txt', 'r')
    for linha in arquivo:
        linha = linha.strip()
        print(linha)
    arquivo.close()

def remove_animal_txt(remove_animal):
    try:
        linhas = []
        arquivo = open('animais.txt', 'r')
        linhas = arquivo.readlines()

        arquivo = open('animais.txt', 'w')
        for pos, linha in enumerate(linhas, 1):
            if pos != remove_animal:
                arquivo.write(linha)
        print(f"Operação Concluída!")
        print("--------------------")
        print("\nArquivo atualizado:")
        arquivo = open('animais.txt', 'r', encoding='utf-8')
        for linha in arquivo:
            linha = linha.strip()
            print(linha)
        arquivo.close()

    except:
        print("Algo deu errado! Tente novamente!")

def menu():
    while True:
        print("----------MENU-----------")
        print("1 - Iniciar o jogo")
        print("2 - Cadastrar um novo animal")
        print("3 - Remover um animal")
        print("4 - Sair")
        opcao = input("Digite a opção desejada para continuar: ")

        if opcao == "1":
            jogar_forca()
        elif opcao == "2":
            print("------------------------------------------------------------------")
            add_animal = input("Digite um animal para acrescentar a lista da forca:\n")
            add_animal_txt(add_animal)
        elif opcao == "3":
            print("----------------------------------------------------------------------------------")

            arquivo = open('animais.txt', 'r', encoding='utf-8')
            animais = [linha.strip() for linha in arquivo]

            if not animais:
                print("--------------------------------------------------------------------------")
                print("A lista de animais está vazia. Cadastre um animal primeiro para continuar.")
                print("--------------------------------------------------------------------------")
                menu()

            arquivo = open('animais.txt', 'r', encoding='utf-8')
            animais = [linha.strip() for linha in arquivo]
            for i, linha in enumerate(animais, 1):
                print(f"{i} - {linha}")
            arquivo.close()

            print("---------------------------------------------------------------------------------------")
            remove_animal = int(input("Digite a posição do animal que deseja remover da lista da forca:\n"))
            remove_animal_txt(remove_animal)
        elif opcao == "4":
            break
        else:
            print("Opção inválida. Tente novamente.")

def jogar_forca():
    arquivo = open('animais.txt', 'r', encoding='utf-8')
    animais = [linha.strip() for linha in arquivo]

    if not animais:
        print("--------------------------------------------------------------------------")
        print("A lista de animais está vazia. Cadastre um animal primeiro para continuar.")
        print("--------------------------------------------------------------------------")
        menu()

    animal = random.choice(animais).upper()
    chances = 6

    print("----------------------------------------")
    print("JOGO DA FORCA:")
    print(f"Tema: Animal")
    print(f"Dica: A palavra tem {len(animal)} letras")
    print(f"Você tem {chances} chances")

    palavra_secreta = list('_' * len(animal))
    palavras_erradas = []

    while chances > 0 and palavra_secreta.count('_') != 0:
        print("----------------------------")
        letra = input("Digite uma letra: ").upper()

        while not letra.isalpha():
            print("------------------------")
            print("Digite uma letra válida.")
            letra = input("\nDigite uma letra: ").upper()

        if letra in animal:
            posicao = localizar_posicao_palavras(animal, letra)
            for i in posicao:
                palavra_secreta[i] = letra
            print(palavra_secreta)

            print("------------------")
            print("Palavras Erradas: ")
            print(palavras_erradas)

        else:
            chances -= 1
            print("--------")
            print("ERROU!!!")
            print(f"Você possui agora {chances} chances")
            print(palavra_secreta)

            print("------------------")
            print("Palavras Erradas: ")
            palavras_erradas.append(letra)
            print(palavras_erradas)

    if chances <= 0:
        print("----------------------")
        print("Suas chances acabaram!")
        print("Game Over!!!")
        print(f"A palavra era: {animal}")
        print("----------------------")

    else:
        print("----------------------")
        print("Você acertou! Parabéns!!!")
        print("----------------------")

    opcao = input("Deseja jogar novamente? (S/N)").lower()
    if opcao == "s":
        jogar_forca()

if __name__ == "__main__":
    menu()
