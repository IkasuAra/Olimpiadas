from Atleta import ArremessoPeso, ginasticaArtistica

class menu():
    #Classe principal para implementar a funcionalidade final das Olimpíadas
    def main():
        print("***Bem vindo às olimpíadas***\n")
        #Loop do Menu de escolha de modalidades 
        while True:
            print("Escolha um dos esportes abaixo:")
            opcao = int(input(" 1 - Arremesso de peso\n 2 - Ginástica Artística\n 3 - Ir embora\n Opção: "))
            if opcao == 1:
                print("\n***ARREMESSO DE PESO***\n")
                #Entrada do usuário no nome dos atletas para a modalidade arremesso de peso
                atleta1 = input("\nO(a) primeiro(a) atleta a competir é: ")
                atleta2 = input("O(a) segundo(a) atleta a competir é: ")
                ArremessoPeso.fazerTresArremessos(atleta1, atleta2)
            elif opcao == 2:
                print("\n***GINÁSTICA ARTÍSTICA***\n")
                #Entrada do usuário no nome dos atletas para a modalidade ginástica artística
                atleta1 = input("\nO(a) primeiro(a) atleta a competir é: ")
                atleta2 = input("O(a) segundo(a) atleta a competir é: ")
                ginasticaArtistica.fazerApresentacao(atleta1, atleta2)
            elif opcao == 3:
                #Encerramento do programa
                print("\nObrigado por participar dos Jogos Olímpicos. Até a próxima!")
                break
            else:
                #Opção inválida
                print("\nDesculpe-nos, mas só conseguimos atletas para dois esportes! Escolha outra opção\n ")
    main()
