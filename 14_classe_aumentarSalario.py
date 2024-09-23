class Funcionario:
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario

    def obter_nome(self):
        return self.nome

    def obter_salario(self):
        return self.salario

    def aumentarSalario(self, percentual_de_aumento):
        aumento = self.salario * (percentual_de_aumento / 100)
        self.salario += aumento
        print(f"Salário aumentado em {percentual_de_aumento}%. Novo salário: R$ {self.salario:.2f}")

harry = Funcionario("Harry", 25000)
harry.aumentarSalario(10)  # Aumenta o salário em 10%
