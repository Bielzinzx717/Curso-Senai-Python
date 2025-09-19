class conta_bancaria:
    def __init__(self, titular):
        self.titular = titular
        self.saldo = 0
    
    def depositar(self, valor):
        self.saldo += valor
        print("deposito de R$ {valor:.2f} realizado. saldo atual: R${self.saldo:.2f}")
    
    def sacar(self, valor):
        if valor <= self.saldo:
            self.saldo -+ valor
            print (f"saque de R${valor:.2f} realizado! saldo atual: R$ {self.saldo:.2f}")
        else:
            print("saldo insuficiente")

    def mostrar_saldo(self):
        print(f"saldo final de {self.titular}: R${self.saldo:.2f}")



conta = conta_bancaria("gabriel")
conta.depositar(500)
conta.sacar(200)
conta.sacar(400)
conta.mostrar_saldo()