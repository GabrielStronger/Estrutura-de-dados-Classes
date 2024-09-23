class BombaCombustivel:
    def __init__(self, tipo_combustivel, valor_litro, quantidade_combustivel):
        self.tipo_combustivel = tipo_combustivel
        self.valor_litro = valor_litro
        self.quantidade_combustivel = quantidade_combustivel

    def abastecerPorValor(self, valor):
        litros = valor / self.valor_litro
        if litros > self.quantidade_combustivel:
            print("Não há combustível suficiente na bomba.")
            return 0
        self.quantidade_combustivel -= litros
        print(f"Abastecido {litros:.2f} litros.")
        return litros

    def abastecerPorLitro(self, litros):
        valor = litros * self.valor_litro
        if litros > self.quantidade_combustivel:
            print("Não há combustível suficiente na bomba.")
            return 0
        self.quantidade_combustivel -= litros
        print(f"Você deve pagar R$ {valor:.2f}")
        return valor

    def alterarValor(self, novo_valor):
        self.valor_litro = novo_valor
        print(f"Valor por litro alterado para R$ {self.valor_litro:.2f}")

    def alterarCombustivel(self, novo_tipo):
        self.tipo_combustivel = novo_tipo
        print(f"Tipo de combustível alterado para {self.tipo_combustivel}")

    def alterarQuantidadeCombustivel(self, nova_quantidade):
        self.quantidade_combustivel = nova_quantidade
        print(f"Quantidade de combustível alterada para {self.quantidade_combustivel:.2f} litros")


bomba = BombaCombustivel("Gasolina", 5.50, 1000)
bomba.abastecerPorValor(50)
bomba.abastecerPorLitro(10)
bomba.alterarValor(6.00)
bomba.alterarQuantidadeCombustivel(1200)
bomba.alterarCombustivel("Diesel")
