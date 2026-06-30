from rich import print
from rich.panel import Panel

class Gamer:

    def __init__(self, nome = 'desconhecido', nick = 'vazio'):
        self.jogador_nome = nome
        self.jogador_nick = nick
        self.jogos_favoritos = list()

    def add_favoritos(self, jogo):
        self.jogos_favoritos.append(jogo)
        self.jogos_favoritos = sorted(self.jogos_favoritos, key=str.lower)

    def ficha(self):
        conteudo = f'Nome real: [black on blue] {self.jogador_nome} [/]'
        conteudo += '\nJogos favoritos: '
        for jogo in self.jogos_favoritos:
            conteudo += f"\n:video_game: [blue]{jogo}[/]"
        caixa = Panel(conteudo, title = f'Jogador <{self.jogador_nick}>', width = 40)
        print(caixa)


j1 = Gamer("Fabricio da Silva", "detonator2025")
j1.add_favoritos("Mario Bros")
j1.add_favoritos("Sonic")
j1.add_favoritos("God of War")
j1.add_favoritos("Fortnite")
j1.ficha()

j2 = Gamer("Olívia Souza", "peach_raivosa")
j2.add_favoritos('Mario Bros')
j2.add_favoritos('Call of Duty')
j2.ficha()
