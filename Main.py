from Atleta import ArremessoPeso, ginasticaArtistica

def nomeAtletas(atleta1, atleta2):
    atleta1 = input("\nO primeiro atleta a competir é: ")
    atleta2 = input("O primeiro atleta a competir é: ")

def main():

    print("***Bem vindo às olimpíadas***\n")
    print("Escolha um dos esportes abaixo:")
    while True:
        opcao = int(input(" 1 - Arremesso de peso\n 2 - Ginástica Artística\n 3 - Ir embora\n Opção: "))
        if opcao == 1:
            print("\n***ARREMESSO DE PESO***\n")
            atleta1 = input("\nO primeiro atleta a competir é: ")
            atleta2 = input("O primeiro atleta a competir é: ")
            ArremessoPeso.fazerTresArremessos(atleta1, atleta2)
            break
        if opcao == 2:
            print("\n***GINÁSTICA ARTÍSTICA***\n")
            atleta1 = input("\nO primeiro atleta a competir é: ")
            atleta2 = input("O primeiro atleta a competir é: ")
            ginasticaArtistica.fazerApresentacao(atleta1, atleta2)
            break
        elif opcao == 3:
            print("\nObrigado por participar dos Jogos Olímpicos. Até a próxima!")
            break
        else:
            print("\nDesculpe-nos, mas só conseguimos atletas para dois esportes! Escolha outra opção\n ")
main()