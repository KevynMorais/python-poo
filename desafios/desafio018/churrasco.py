from rich import print
from rich.panel import Panel

class Churrasco:
    # Atributos de Classe
    consumo_padrao:float = 0.400 # Cada pessoa em média come 400g de carne
    preco_kg:float = 82.40 # Cada Kg de carne custa R$82.40

    def __init__(self, evento="vazio", quant=0):
        # Atributos de Instância
        self.titulo = evento
        self.quant = quant

    def calcular_qtd_carne(self) -> float:
        return self.quant * Churrasco.consumo_padrao

    def calcular_custo_total(self) -> float:
        return self.calcular_qtd_carne() * Churrasco.preco_kg

    def calcular_custo_individual(self) -> float:
        return self.calcular_custo_total() / self.quant

    def analisar(self):
        conteudo = f"Analisando [green]{self.titulo}[/] com [blue]{self.quant} convidados[/]"
        conteudo += f"\nCada participante comerá [purple]{Churrasco.consumo_padrao:.1f}[/] e cada Kg custa [purple]R${Churrasco.preco_kg:.2f}[/]"
        conteudo += f"\nRecomendo comprar [blue]{self.calcular_qtd_carne():.3f}Kg[/] de carne"
        conteudo += f"\nO custo total será de [green]R${self.calcular_custo_total():.2f}[/]"
        conteudo += f"\nCada pessoa pagará [yellow]R${self.calcular_custo_individual()}[/] para participar."
        caixa = Panel(conteudo, title=self.titulo, width=70, height=7)
        print(caixa)


c1 = Churrasco("Churras dos Amigos", 15)
c1.analisar()
