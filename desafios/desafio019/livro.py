from rich import print
from time import sleep

class Livro:
    pag_atual = 1 # Sempre que o livro for adquirido, deve-se ler a primeira página
    soma_pag = 0

    def __init__(self, titulo="Vazio", paginas=0):
        self.titulo = titulo
        self.paginas = paginas

        print(f":book: [blue]Você acabou de abrir o livro '[red]{self.titulo}[/]' "
              f"que tem [green]{self.paginas} páginas [/]no total.", end=' ')
        print(f"[blue]Você está agora na [yellow]página {Livro.pag_atual}[/]")


    def avancar_paginas(self, paginas=0):
        Livro.soma_pag += paginas
        cont = 0
        while Livro.pag_atual < Livro.soma_pag+1:
            if Livro.pag_atual < self.paginas:
                Livro.pag_atual += 1
                print(f"Pág{Livro.pag_atual} :right_arrow:", end = ' ')
                sleep(0.2)
                cont += 1
            else:
                print(f'[blue]Você avançou [bold blue]{cont}[/] páginas e agora está na [yellow]página {Livro.pag_atual}[/]')
                print(f":notebook: [red]Você chegou ao final do livro '{self.titulo}")
                break
        print(f'[blue]Você avançou [bold blue]{paginas}[/] páginas e agora está na [yellow]página {Livro.pag_atual}[/]')


l1 = Livro("10 coisas que aprendi", 40)
l1.avancar_paginas(5)
l1.avancar_paginas(10)
l1.avancar_paginas(50)
