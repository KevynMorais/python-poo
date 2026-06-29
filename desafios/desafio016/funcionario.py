from rich import print
from rich import inspect

class Funcionario:
    # Atributos de Classe
    empresa = "Curso em Vídeo"

    def __init__(self, nome = "Desconhecido", setor = "N/A", cargo = "N/A"):
        # Atributos de Instância
        self.nome = nome
        self.setor = setor
        self.cargo = cargo

    def apresentacao(self) -> str:
        return f":handshake: Olá, sou [blue]{self.nome}[/] e sou {self.cargo} do setor de {self.setor} da empresa {self.__class__.empresa}"


c1 = Funcionario("Maria", "Administração", "Diretora")
print(c1.apresentacao())

c2 = Funcionario("Pedro", "TI", "Programador")
print(c2.apresentacao())

