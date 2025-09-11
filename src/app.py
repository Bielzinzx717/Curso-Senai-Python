from flask import Flask
from dotenv import load_dotenv
import os


load_dotenv()


app = Flask (__name__)


@app.route("/")
def home():
    return"Olá, mundo!"


if __name__ == "__main__":
    app.run(debug=True)




  

# exec 1
input("Descubra os resultados das contas com a senha de 123:  ")
n1 = 15
n2 = 27
soma = n1 + n2

print("O resultado é:", soma)

# exec 2

n1 = 12
n2 = 8
multiplicacao = n1 * n2
print("O resultado é:", multiplicacao)

# exec 3
n1 = 25
n2 = 4
divisao = n1 // n2
print("O resultado é:", divisao)

# exec 4
n1 = 37
n2 = 5
resto = n1 % n2
print("O resultado é:", resto)

# exec 5
n1 = 3
n2 = 4
potencia = n1 ** n2
print("O resultado é:", potencia)


print(10 > 7) # Retorna True pois 10 é maior que 7

print(15 == 20) # Retorna False pois 15 não é igual a 20

print(100 <= 100) # Retorna True pois 100 é igual a 100

print(45 != 30) # Retorna o resultado True é diferente

##################################################################

print("Novo desafio abaixo: ")

print(5 > 2 and 8 > 3)

print(10 < 3 or 4 == 4)

print (not 7 > 2)

print("Novo desafio abaixo: ")

x = 10
x += 5
x *= 2
x -= 4
print(x)


a = [1,2,3]
b = a
c = [1,2,3]
print (a is b)
print (a is c)

 
print(""" podemos imprimir
      multiplas linhas
      na saida do print""")





########################################################
print(f""" 14 . verifique se (a is b): {a is b}
            14 . verifique se (a is c) : {a is c}""")


print("o valor é:", a)
print("o valor de A é:",a, "e o valor de B é:", b)
print(f"o valor de A é: {a} e o alor de B é: {b}")

##########################


a = [1,2,3]
b = a
c = [1,2,3]
print (a is b)
print (a is c)


print("o valor é:", )
print("o valor de A é:",a, "e o valor de B é:", b)
print(f"o valor de A é: {a} e o alor de B é: {b}")



numeros = [1,2,3,4,5]
print(6 in numeros)


numeros = [12,15,17,23,27]
print(17 in numeros)

########################################################################

nome = input("digite seu nome:  ")
idade = int(input("digite sua idade:  "))


Idade_daqui_100 = print (100 - idade)


if idade >= 18:  print("vc é maioridade")
else: print("vc é menor de idade")


if 13 <= idade <=19: print("vc é adolescente")

idade += 5 
print (f"sua idade daqui 5 anos sera de: {idade}")

 
print("vc tem a letra N no nome", 'n' in nome)
