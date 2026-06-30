from rich import print
from rich import inspect

class Caneta:

    def __init__(self, cor, tampa=True):
        self.cor = cor.lower().strip()
        self.tampa = tampa
        self.cores = {
            '[blue]': 'azul',
            '[green]': 'verde',
            '[red]': 'vermelha',
            '[yellow]': 'amarela'
        }

    def quebrar_linha(self, linhas=0):
        cont = 1
        while cont < linhas:
            print()
            cont += 1

    def destampar(self):
        self.tampa = False
        return self.tampa

    def tampar(self):
        self.tampa = True
        return self.tampa

    def escrever(self, texto=''):
        if self.tampa:
            print(f':no_entry_sign: A [blue]caneta[/] está tampada!')
        else:
             for k, v in self.cores.items():
                 if self.cor == v:
                    print(f'{k}{texto}')

c1 = Caneta("azul")
c2 = Caneta("vermelha")
c3 = Caneta("verde")

c1.destampar()
c2.destampar()
c3.destampar()

c1.escrever("Olá, tudo bem? ")
c1.quebrar_linha(2)
c2.escrever("Olá, Gafanhoto! ")
c3.escrever("Vamos exercitar! ")
