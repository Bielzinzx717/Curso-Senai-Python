nome = input("digite seu nome: ")
idade = input("digite sua idade: ")
with open("usuarios.txt", "a") as arq:
    arq.write(f"{nome};{idade}\n")
    