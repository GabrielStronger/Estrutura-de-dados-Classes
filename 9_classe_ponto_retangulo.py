class Ponto:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})"

class Retangulo:
    def __init__(self, largura, altura, vertice_inferior_esquerdo):
        self.largura = largura
        self.altura = altura
        self.vertice_inferior_esquerdo = vertice_inferior_esquerdo

    def centro(self):
        centro_x = self.vertice_inferior_esquerdo.x + self.largura / 2
        centro_y = self.vertice_inferior_esquerdo.y + self.altura / 2
        return Ponto(centro_x, centro_y)


ponto_inicial = Ponto(0, 0)
retangulo = Retangulo(4, 6, ponto_inicial)


print(f"Retângulo de largura {retangulo.largura} e altura {retangulo.altura} com vértice inferior esquerdo em {retangulo.vertice_inferior_esquerdo}")


centro = retangulo.centro()
print(f"O centro do retângulo está em {centro}")
