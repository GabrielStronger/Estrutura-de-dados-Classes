class Carro:
    def __init__(self, consumo):
        self.consumo = consumo  # km por litro
        self.nivel_combustivel = 0  # nível inicial do tanque

    def andar(self, distancia):
        litros_necessarios = distancia / self.consumo
        if litros_necessarios > self.nivel_combustivel:
            print("Combustível insuficiente para completar a viagem.")
            return
        self.nivel_combustivel -= litros_necessarios
        print(f"O carro andou {distancia} km. Combustível restante: {self.nivel_combustivel:.2f} litros.")

    def adicionarGasolina(self, litros):
        self.nivel_combustivel += litros
        print(f"Adicionados {litros} litros de combustível. Nível atual: {self.nivel_combustivel:.2f} litros.")

    def obterGasolina(self):
        print(f"Nível atual de combustível: {self.nivel_combustivel:.2f} litros.")
        return self.nivel_combustivel

# Exemplo de uso:
meuFusca = Carro(15)  # 15 km por litro de combustível
meuFusca.adicionarGasolina(20)  # abastece com 20 litros de combustível
meuFusca.andar(100)  # anda 100 quilômetros
meuFusca.obterGasolina()  # imprime o combustível que resta no tanque
