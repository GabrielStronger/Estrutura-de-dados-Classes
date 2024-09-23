class BichinhoVirtual:
    def __init__(self, nome, fome=0, tedio=0):
        self.nome = nome
        self.fome = fome
        self.tedio = tedio

    def alterar_humor(self):
        return "Feliz" if self.fome < 5 and self.tedio < 5 else "Triste"

    def brincar(self, tempo):
        self.tedio = max(0, self.tedio - tempo)
        print(f"{self.nome} está brincando por {tempo} minutos.")

    def alimentar(self, quantidade):
        self.fome = max(0, self.fome - quantidade)
        print(f"{self.nome} está comendo {quantidade} de comida.")

    def passar_tempo(self):
        self.fome += 1
        self.tedio += 1

    def ouvir(self):
        humor = self.alterar_humor()
        print(f"{self.nome} está {humor}!")

    def __str__(self):
        return f"Nome: {self.nome}, Fome: {self.fome}, Tédio: {self.tedio}"

class FazendaDeBichinhos:
    def __init__(self):
        self.bichinhos = []

    def adicionar_bichinho(self, bichinho):
        self.bichinhos.append(bichinho)

    def alimentar_todos(self, quantidade):
        for bichinho in self.bichinhos:
            bichinho.alimentar(quantidade)

    def brincar_com_todos(self, tempo):
        for bichinho in self.bichinhos:
            bichinho.brincar(tempo)

    def ouvir_todos(self):
        for bichinho in self.bichinhos:
            bichinho.ouvir()

    def mostrar_status(self):
        for bichinho in self.bichinhos:
            print(bichinho)


fazenda = FazendaDeBichinhos()

# Criando bichinhos
bichinho1 = BichinhoVirtual("Tamagotchi")
bichinho2 = BichinhoVirtual("GigaPet")
bichinho3 = BichinhoVirtual("NanoPet")


fazenda.adicionar_bichinho(bichinho1)
fazenda.adicionar_bichinho(bichinho2)
fazenda.adicionar_bichinho(bichinho3)

# Ações na fazenda
fazenda.ouvir_todos()
fazenda.alimentar_todos(3)
fazenda.brincar_com_todos(4)

# Mostrando status de todos os bichinhos
fazenda.mostrar_status()
