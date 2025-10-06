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


# #########################################################################


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


# ##################################################################


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


# ########################################################################


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


# ##############################################################################


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



# ##########################################################################



# class Funcionario:
#     def trabalhar(self):
#         print("O funcionario está trabalhando normalmente")


# class Estagiario(Funcionario):
#     def trabalhar(self):
#         print("O estagiario está aprendendo e ajudando nas tarefas")



# f1 = Funcionario()
# e1 = Estagiario()

# f1.trabalhar()
# e1.trabalhar()



# ###################################################


# class ContaCorrente:
#     def __init__ (self, saldo):
#         self.__saldo = saldo


#     def depositar(self, valor):
#         if valor > 0:
#             self.__saldo += valor
#             print(f"Deposito de R${valor} realizado com sucesso")
#         else:
#             print("Valor invalido.")

    
#     def sacar(self, valor):
#         if valor <= 0:
#             print("valor invalido")
#         elif valor <= self.__saldo:
#             self.__saldo -= valor
#             print(f"seu saque foi concluido no valor deR$ {valor}")

#         else:
#             print("seu saque nao foi concluido por falta de money")


#     def consultar_saldo(self):
#         print(f"saldo atual R$ {self.__saldo}")


# v1 = ContaCorrente(100)
# v1.depositar(50)
# v1.sacar(50)
# v1.consultar_saldo()




# ##############################




# class Aluno:
#     def __init__(self, nome, nota):
#         self.__nome = nome
#         self.__nota = nota

#     def get_nota(self):
#         return self.__nota
    
#     def set_nota(self):
#         if self.__nota > 0:
#             print("sua nota foi aceita")
#         else:
#             print("sua nota nao foi aceita")


#     def nota_max(self):
#         if self.__nota == 10:
#             print("parabens vc tirou nota maxima")



# n1 = Aluno("gabriel", 10)
# n1.get_nota()
# n1.set_nota()
# n1.nota_max()
        
    

# #####################################################


# class Pessoa:
#     def __init__(self, nome, idade):
#         self.nome = nome
#         self.idade = idade

    
# class Prof(Pessoa):
#     def __init__(self, nome, idade, materia):
#         super().__init__(nome, idade)
#         self.materia = materia

# p1 = Pessoa()
# f1 = Prof()





# ########################################



# class Veiculo:
#     def __init__(self, nome):
#         self.nome = nome
    
#     def mover(self):
#         print("carro parado")


# class Carro(Veiculo):
#     def mover(self):
#         print("carro esta andando")


# class Bicicleta(Veiculo):
#     def mover(self):
#         print("A bike esta andando")



# Carro = Carro("civic")
# Bicicleta = Bicicleta("moto")
# Carro.mover()
# Bicicleta.mover()





# ############################################


# class Usuario:
#     def __init__(self, nome, senha):
#         self.nome = nome
#         self.__senha = senha

#     def alterar_senha(self, antiga, nova):
#         if antiga == self.__senha:
#             self.__senha = nova
#             print("senha alterada com sucesso")

#         else:
#             print("senha antiga incorreta. Tente novamente")

#     def login(self, senha):
#         if senha == self.__senha:
#             print(f"aecsso permitido. Bem-vindo {self.nome}")

#         else:
#             print("senha incorreta.")

# usuario1 = Usuario("gabriel" , "1234")

# usuario1.login("1234")

# usuario1.alterar_senha("1234" , "123")

# usuario1.login("123")

# usuario1.login("123")



# ##############################################################



# class Animal:
#     def mover(self):
#         print("movendo")

# class Mamifero(Animal):
#     def amamentar(self):
#         print("amamentou")

# class Cachorro(Mamifero):
#     def latir(self):
#         print("latiu")


# dog = Cachorro()

# dog.mover()
# dog.amamentar()
# dog.latir()



##########################################################



# from abc import ABC, abstractclassmethod

# class Instrumento(ABC):
#     @abstractclassmethod
#     def tocar(self):
#         pass

# class Violão(Instrumento):
#     def tocar(self):
#         print("O violão está ticando um som suave de cordas.")


# class Bateria(Instrumento):
#     def tocar(self):
#         print("a bateria está marcadoo ritimo com batidas fortes")

# violao = Violão()
# bater = Bateria()

# violao.tocar()
# bater.tocar()




##########################################


# from abc import ABC, abstractclassmethod


# class Funcionario(ABC):
#     @abstractclassmethod
#     def calcular_pagamento(self):
#         pass


# class Assalariado(Funcionario):
#     def __init__(self, salario):
#         self.salario = salario


#     def calcular_pagamento(self):
#         return self.salario
    


# class Horista(Funcionario):
#     def __init__ (self, valor_hora, horas_trabalhadas):
#         self.valor_hora = valor_hora
#         self.horas_trabalhadas = horas_trabalhadas

#         def calcular_pagamento(self):
#             return self.valor_hora * self.horas_trabalhadas
        


# f1 = Assalariado(3000)
# f2 = Horista(50)  #nao completei 






from tarefa.viagem_class import viagem_class

viagem_0 = viagem_class("florida")
viagem_1 = viagem_class("Havai")
viagem_2 = viagem_class("toquio")
viagem_3 = viagem_class("egito")
viagem_4 = viagem_class("londres")


print("===================================================="
      '''
      ''')
print("Bem-vindo! Senai viagens tem algumas ofertas para você")


viajante = input("Digite seu nome para começarmos: ")

print(f"{viajante} temos 5 destinos que combina com você:"
'''
[0] florida
[1] havai
[2] toquio
[3] egito
[4] londres

''')

selecao = int(input("selecione o numero da viagem desejada: "))
lista_viagem = [viagem_0, viagem_1, viagem_2, viagem_3,viagem_4]

opcao_selecionada = int(selecao)
for opcao in lista_viagem:
    if opcao_selecionada >= 5:
        print("esta opcao nao esta incluida em nossos destinos.")
        break

    if opcao_selecionada<= 4:
        print(f"{viajante} sua viagem para {lista_viagem[opcao_selecionada].destino} esta marcada.")
        break
