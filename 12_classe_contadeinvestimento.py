class ContaInvestimento:
    def __init__(self, saldo_inicial, taxa_juros):
        self.saldo = saldo_inicial
        self.taxa_juros = taxa_juros / 100  # Converter porcentagem para decimal

    def adicioneJuros(self):
        self.saldo += self.saldo * self.taxa_juros
        print(f"Juros adicionados. Saldo atual: R$ {self.saldo:.2f}")

poupanca = ContaInvestimento(1000, 10)  # Saldo inicial de R$ 1000 e taxa de juros de 10%
for _ in range(5):  # Aplica o método adicioneJuros 5 vezes
    poupanca.adicioneJuros()
