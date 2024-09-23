class Funcionario:
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario

    def obter_nome(self):
        return self.nome

    def obter_salario(self):
        return self.salario


empregado = Funcionario("João", 3000)
print(f"Nome: {empregado.obter_nome()}, Salário: R$ {empregado.obter_salario():.2f}")
