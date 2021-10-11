class Atleta():
    def __init__(self, indiceResultado):
        self.indiceResultado = 0

    def getNome(self):
        return self.__nome

    def setNome(self, nome):
        self.__nome = nome

    def getResultado(self):
        return self.__resultado

    def setResultado(self, resultado):
        self.__resultado = resultado

    def getIndiceResultado(self):
        return self.__indiceResultado

    def setIndiceResultado(self, indiceResultado):
        self.__indiceResultado = indiceResultado

class ArremessoPeso(Atleta):
    def __init__(self, atleta1, atleta2):
        self.atleta1 = atleta1
        self.atleta2 = atleta2

    def definirVencedor(tentativas_jogador1, tentativas_jogador2, atleta1, atleta2):
        if max(tentativas_jogador1) > max(tentativas_jogador2):
            return ("O vencedor foi o atleta " + atleta1 + ", com um arremesso de " + str(max(tentativas_jogador1)) + " metros\n")
        elif max(tentativas_jogador1) < max(tentativas_jogador2):
            return ("O vencedor foi o atleta " + atleta2 + ", com um arremesso de " + str(max(tentativas_jogador2)) + " metros\n")
        else:
            if tentativas_jogador1[1] > tentativas_jogador2[1]:
                return ("Após empate, foi julgado o segundo maior arremesso. Sendo assim, o atleta " + atleta1 + " vence com o arremesso de " + str(tentativas_jogador1[1]) + " metros\n")
            elif tentativas_jogador1[1] < tentativas_jogador2[1]:
                return ("Após empate, foi julgado o segundo maior arremesso. Sendo assim, o atleta " + atleta2 + " vence com o arremesso de " + str(tentativas_jogador2[1]) + " metros\n")

    def fazerTresArremessos(atleta1, atleta2):
        tentativas_jogador1 = list()
        tentativas_jogador2 = list()
        print("\nO atleta " + atleta1 + " irá jogar...")
        for i in range(1, 4):
            arremesso = float(input(str(i) + "° arremesso: "))
            tentativas_jogador1.append(arremesso)
            print("O atleta " + atleta1 + " faz seu " + str(i) + "° arremesso, " + str(arremesso) + " metros\n")
        print("\nO atleta " + atleta2 + " irá jogar...")
        for i in range(1, 4):
            arremesso = float(input(str(i) + "° arremesso: "))
            tentativas_jogador2.append(arremesso)
            print("O atleta " + atleta2 + " faz seu " + str(i) + "° arremesso, " + str(arremesso) + " metros\n")
        tentativas_jogador1.sort()
        tentativas_jogador2.sort()
        print(ArremessoPeso.definirVencedor(tentativas_jogador1, tentativas_jogador2, atleta1, atleta2))

class ginasticaArtistica(Atleta):
    def __init__(self, atleta1, atleta2):
        self.atleta1 = atleta1
        self.atleta2 = atleta2

    def definirVencedor(atleta1, atleta2, notas_jogador1, notas_jogador2):
        nota_final_jogador1 = 0
        nota_final_jogador2 = 0
        for j in range(0, len(notas_jogador1)):
            nota_final_jogador1 += notas_jogador1[j]
            nota_final_jogador2 += notas_jogador2[j]
        if nota_final_jogador1 > nota_final_jogador2:
            print("\nA menor nota da atleta " + atleta2 + " foi " + str(min(notas_jogador2)) + ", sua avaliação final foi de: " + str(nota_final_jogador2))
            return ("\nA vencedora foi a atleta " + atleta1 + ", com uma nota final de " + str(nota_final_jogador1))
        print("\nA menor nota da atleta " + atleta1 + " foi " + str(min(notas_jogador1)) + ", sua avaliação final foi de: " + str(nota_final_jogador1))
        return ("\nA vencedora foi a atleta " + atleta2 + ", com uma nota final de " + str(nota_final_jogador2))
    
    def fazerApresentacao(atleta1, atleta2):
        notas_jogador1 = list()
        notas_jogador2 = list()
        print("\nA atleta " + atleta1 + " está se apresentando...")
        for i in range(1, 6):
            nota = float(input(str(i) + "° nota: "))
            notas_jogador1.append(nota)
            print("A " + str(i) + "ª nota da atleta " + atleta1 + " é: " + str(nota))
        print("\nA atleta " + atleta2 + " está se apresentando...")
        for i in range(1, 6):
            nota = float(input(str(i) + "° nota: "))
            notas_jogador2.append(nota)
            print("A " + str(i) + "ª nota da atleta " + atleta2 + " é: " + str(nota))
        print(ginasticaArtistica.definirVencedor(atleta1, atleta2, notas_jogador1, notas_jogador2))
