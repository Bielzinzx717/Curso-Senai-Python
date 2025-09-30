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


##########################################################################


# class ContaBancaria:
#     def __init__(self, titular,saldo):
#         self.__titular = titular
#         self.__saldo = saldo


#     def get_saldo(self):
#             return self.__saldo
    
#     def depostitar(self, valor):
#             self.__saldo += valor


    
# conta = ContaBancaria("gabriel", 1000)
# print(conta.get_saldo())
# conta.depostitar(int(input("digite o quanto deseja depositar: R$")))
# print(conta.get_saldo())


###################################################################


# class animal:
#     def __init__(self, nome):
#         self.nome = nome

#     def emitir_som(self):
#         print("som generico...")


# class cachorro(animal):
#     def emitir_som(self):
#         print("Au au")

# class gato(animal):
#     def emitir_som(self):
#         print("Miau")

# dog = cachorro("rex")
# cat = gato("mimi")


# dog.emitir_som() 
# cat.emitir_som()
# print(f"{dog}")
# print(f"{cat}")


#########################################################################


# class Funcionario:
#     def __init__ (self, nome, salario):
#         self.__nome = nome
#         self.__salario = salario

    
#     def get_salario(self):
#             return self.__salario 
    
#     def setar_salario(self, salario):
#             self.__salario = salario


# class Gerente(Funcionario):
#     def __init__ (self, nome, salario, departamento):
#          self.departamento = departamento

#     def mostrar_departamento():
#           return
            


# salario = Funcionario("gabriel", 5000)
# print(f"seu salario é de {salario.get_salario()}")
# salario.setar_salario(10000)
# print(f"seu novo salario é de {salario.get_salario()}")


###############################################################################


# class Produto:
#     def __init__ (self, nome, preço):
#         self.nome = nome
#         self.__preço = preço

#     def get_preço(self):
#         return self.__preço
    
#     def aplicar_desconto(self):
#         self.__preço *= 0.9

#     def exibir_produto(self):
#         print(f"produto: {self.nome} | preço: {self.__preço}")




# p1 = Produto("Camisa", 100)
# p2 = Produto("tenis", 300)

# print("antes do desconto")
# p1.exibir_produto()
# p2.exibir_produto()

# p1.aplicar_desconto()
# p2.aplicar_desconto()

# print("\nDepois do desconto de 10%: ")
# p1.exibir_produto()
# p2.exibir_produto()



# class Veículo:
#     def __init__(self, marca, ano):
#         self.marca = marca
#         self.ano = ano


# class carro(Veículo):
#     def mostrar_caracteristica(self):
#         print("Marca: BYD | Ano: 2025")

# class moto(Veículo):
#     def mostrar_caracteriscas(self):
#         print("Marca: BMW R1200 | Ano: 2020")


# car = carro("BYD", 2025)
# bike = moto("BMW", 2025)

# car.mostrar_caracteristica()
# bike.mostrar_caracteriscas()



###########################################################################



