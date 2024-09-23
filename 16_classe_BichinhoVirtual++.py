class BichinhoVirtual:
    def __init__(self, nome):
        self.nome = nome
        self.fome = 50  # Nível de fome, de 0 a 100
        self.tedio = 50  # Nível de tédio, de 0 a 100
        self.saude = 100  # Nível de saúde, de 0 a 100
        self.idade = 0  # Idade do bichinho

    def humor(self):
        return (self.fome + self.tedio) // 2

    def alimentar(self, quantidade_comida):
        self.fome -= quantidade_comida
        if self.fome < 0:
            self.fome = 0
        print(f"Você alimentou {self.nome} com {quantidade_comida} unidades de comida.")
        print(f"Fome atual de {self.nome}: {self.fome}/100")

    def brincar(self, tempo_brincadeira):
        self.tedio -= tempo_brincadeira
        if self.tedio < 0:
            self.tedio = 0
        print(f"Você brincou com {self.nome} por {tempo_brincadeira} unidades de tempo.")
        print(f"Tédio atual de {self.nome}: {self.tedio}/100")

    def passar_tempo(self, tempo):
        self.fome += tempo
        self.tedio += tempo
        if self.fome > 100:
            self.fome = 100
        if self.tedio > 100:
            self.tedio = 100
        print(f"Passaram-se {tempo} unidades de tempo.")
        print(f"Fome atual de {self.nome}: {self.fome}/100")
        print(f"Tédio atual de {self.nome}: {self.tedio}/100")

    def estado(self):
        print(f"{self.nome} - Fome: {self.fome}/100, Tédio: {self.tedio}/100, Saúde: {self.saude}/100, Humor: {self.humor()}/100")

    # Método especial __str__ para revelar todos os atributos do bichinho
    def __str__(self):
        return f"Nome: {self.nome}\nFome: {self.fome}\nTédio: {self.tedio}\nSaúde: {self.saude}\nIdade: {self.idade}\nHumor: {self.humor()}"

# Função principal com menu
def menu_bichinho(bichinho):
    while True:
        print("\nEscolha uma opção:")
        print("1 - Alimentar")
        print("2 - Brincar")
        print("3 - Passar tempo")
        print("4 - Ver estado")
        print("0 - Sair")

        opcao = input("Opção: ")

        if opcao == "1":
            quantidade_comida = int(input("Quantidade de comida: "))
            bichinho.alimentar(quantidade_comida)
        elif opcao == "2":
            tempo_brincadeira = int(input("Tempo de brincadeira: "))
            bichinho.brincar(tempo_brincadeira)
        elif opcao == "3":
            tempo = int(input("Quanto tempo passou? "))
            bichinho.passar_tempo(tempo)
        elif opcao == "4":
            bichinho.estado()
        elif opcao == "0":
            print("Saindo...")
            break
        elif opcao == "42":  # Porta escondida - código secreto
            print("\n--- Valores Exatos dos Atributos ---")
            print(bichinho)
        else:
            print("Opção inválida. Tente novamente.")

# Exemplo de uso:
bichinho = BichinhoVirtual("Tamagotchi")
menu_bichinho(bichinho)
