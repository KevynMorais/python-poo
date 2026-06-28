from rich import print
from rich import inspect


class ContaBancaria:
    """
Cria uma conta bancária e permite fazer saques e depósitos
    """
    def __init__(self, id, nome, saldo = 0):
        self.id = id
        self.titular = nome
        self.saldo = saldo
        print(f'Conta {self.id} criada com sucesso. Saldo atual de R${self.saldo:,.2f}')

    def __str__(self):
        return f"A conta {self.id} de {self.titular} tem R${self.saldo:,.2f} de saldo."

    def depositar(self, valor):
        self.saldo += valor
        print(f"\033[32mDepósito de R${valor:,.2f} autorizado na conta {self.id}\033[m")

    def sacar(self, valor):
        if valor > self.saldo:
            print(f"\033[31mSaque NEGADO de R${valor:,.2f} na conta {self.id}: SALDO INSUFICIENTE\033[m")
        else:
            self.saldo -= valor
            print(f"\033[32mSaque de R${valor:,.2f} autorizado na conta {self.id}\033[m")


c1 = ContaBancaria(111, "José", 500)
print(c1)