class ContaBancaria:
    def __init__(self, titular):
        self.titular = titular
        self.saldo = 0

    def depositar(self, valor):
        self.saldo += valor
        print(f"Depósito de R${valor:.2f} realizado com sucesso.")

    def sacar(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor
            print(f"saque de R${valor:.2f} ralizado com sucesso.")
        else:
            print("Saldo insuficiente para saque.")

    def mostrar_saldo(self):
        print(f"saldo atual de {self.titular}: R${self.saldo:.2f}")


Conta = ContaBancaria("gabriel")

Conta.depositar (float(input("quanto deseja depositar? R$")))
Conta.sacar (float(input("quanto deseja sacar? R$")))
Conta.sacar (float(input("quanto deseja sacar? R$")))
Conta.mostrar_saldo()