from rich import print
from rich.panel import Panel

class Produto:

    def __init__(self, nome = "Vazio", preco = 0):
        self.modelo = nome
        self.preco = preco

    def etiqueta(self):
        precof = f"R${self.preco:,.2f}"
        caixa = Panel(f'{self.modelo:^31}{"-"*30}\n{precof:.^30}', title="Produto", height=5, width=35)
        print(caixa)


p1 = Produto("iPhone 17 Pro Max", 25_000.85)
p2 = Produto("Notebook Gamer", 8_000)
p3 = 

p1.etiqueta()
p2.etiqueta()
