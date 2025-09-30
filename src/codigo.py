# class ContaBancaria:
#     def __init__(self, titular):
#         self.titular = titular
#         self.saldo = 0

#     def depositar(self, valor):
#         self.saldo += valor
#         print(f"Depósito de R${valor:.2f} realizado com sucesso.")

#     def sacar(self, valor):
#         if valor <= self.saldo:
#             self.saldo -= valor
#             print(f"saque de R${valor:.2f} ralizado com sucesso.")
#         else:
#             print("Saldo insuficiente para saque.")

#     def mostrar_saldo(self):
#         print(f"saldo atual de {self.titular}: R${self.saldo:.2f}")


# Conta = ContaBancaria("gabriel")

# Conta.depositar (float(input("quanto deseja depositar? R$")))
# Conta.sacar (float(input("quanto deseja sacar? R$")))
# Conta.sacar (float(input("quanto deseja sacar? R$")))
# Conta.mostrar_saldo()



# class Vendedor:
#     def __init__(self, nome, vendas, meta):
#         self.nome = nome
#         self.vendas = vendas
#         self.meta = meta

#     def bateu_meta(self):
    
#         if self.vendas >= self.meta:
#             print("vc bateu a meta")
            
#         else:
#             print("vc nao bateu a meta")
            
# v = Vendedor("gabriel", 1000, 1000)
# v.bateu_meta()


















# class Vendedor:
#     def __init__(self, nome, vendas, meta):
#         self.nome = nome
#         self.vendas = vendas
#         self.meta = meta

#     def bateu_meta(self):
    
    
#         if self.vendas >= self.meta:
            
#             return("vc bateu a meta")
            
#         else:
            
#             return("vc nao bateu a meta")
            
# v = Vendedor("gabriel", 1000, 1000)
# resultado = v.bateu_meta()
# print(resultado)









# class Usuario:
#     def __init__(self, nome, email, senha):
#         self.nome = nome
#         self.email = email
#         self.senha = senha


#     def mostrar_dados(self):
#         print(f"nome: {self.nome}, email: {self.email}")


#     def alterar_senha(self, nova_senha):
#         self.senha = nova_senha

    
#     def entrar(self, email, senha):
#         return self.email == email and self.senha == senha
    

# U1 = Usuario('gabriel', 'gabriel@gmail.com', '1506')
# U2 = Usuario('mirella', 'mirella@gmail.com', '1312')


# U1.mostrar_dados()
# U2.mostrar_dados()


# U1.alterar_senha('2309')
# U2.alterar_senha('2705')


# print(U1.entrar('gabriel@gmail.com' , '2309'))
# print(U2.entrar('mirella@gmail.com' , '2705')) 






class Usuario:
    def __init__(self, nome, email, senha):
        self.nome = nome
        self.email = email
        self.senha = senha

    def __str__(self):
        return f"seu nome: {self.nome}. seu email: {self.email}"


    def mostrar_dados(self):
        print(self)


    def alterar_senha(self, nova_senha):
        self.senha = nova_senha

    
    def entrar(self, email, senha):
        return self.email == email and self.senha == senha
    

U1 = Usuario('gabriel', 'gabriel@gmail.com', '1506')
U2 = Usuario('mirella', 'mirella@gmail.com', '1312')


U1.mostrar_dados()
U2.mostrar_dados()


U1.alterar_senha('2309')
U2.alterar_senha('2705')


print(U1.entrar('gabriel@gmail.com' , '2309'))
print(U2.entrar('mirella@gmail.com' , '2705')) 