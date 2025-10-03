from feira_livre import feira_livre

f1 = feira_livre("maça")
f2 = feira_livre("pera")
f3 = feira_livre("banana")
f4 = feira_livre("kiwi")


print("-------------------------------------")

print("Bem-vindo a feira")

comprador = input("digite seu nome: ")

print(f"{comprador} temos essas frutas:"
'''
      [0] maça
      [1] pera
      [2] banana
      [3] kiwi
'''
)

seleção = int(input("figite qual fruta vc quer:  "))
lista_frutas = [f1,f2,f3,f4]
opcao_seleciona = int(seleção)

for opcao in lista_frutas:
    if opcao_seleciona >=5:
        print("essa fruta nao esta disponivel")
    
    if opcao_seleciona <=4:
        print(f"{comprador} a fruta {lista_frutas[opcao_seleciona].estante} é sua!")
        print("vlt smp")
        break