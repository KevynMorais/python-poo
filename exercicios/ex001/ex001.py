# Declaração de Classes
class Gafanhoto:
    def __init__(self): # Método Construtor
        # Atributos de Instância
        self.nome = ""
        self.idade = 0
        self.matricula = True

    # Métodos de Instância
    def aniversario(self):
        self.idade += 1

    def mensagem(self):
        if self.matricula:
            return f"{self.nome} é Gafanhoto(a) e tem {self.idade} anos de idade, e é regularmente matriculado."
        else:
            return f"{self.nome} é Gafanhoto(a) e tem {self.idade} anos de idade, e não é regularmente matriculado."

# Declaração de Objetos
g1 = Gafanhoto()
g1.nome = 'Maria'
g1.idade = 17
g1.aniversario()
g1.matricula = False
print(g1.mensagem())

g2 = Gafanhoto()
g2.nome = 'Mauro'
g2.idade = 53
g2.aniversario()
g2.matricula = True
print(g2.mensagem())

g3 = Gafanhoto()
g3.nome = 'Kevyn'
g3.idade = 18
g3.aniversario()
print(g3.mensagem())

g4 = Gafanhoto()
g4.nome = 'Otávio Otário'
g4.idade = 989834898398823
print(g4.mensagem())