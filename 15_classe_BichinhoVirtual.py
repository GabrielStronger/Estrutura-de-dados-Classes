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

# Exemplo de uso:
bichinho = BichinhoVirtual("Tamagotchi")
bichinho.estado()
bichinho.alimentar(20)  # Alimenta o bichinho com 20 unidades de comida
bichinho.brincar(30)  # Brinca com o bichinho por 30 unidades de tempo
bichinho.passar_tempo(10) 
bichinho.estado()
