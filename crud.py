# with open("nome.txt", "r") as arq:
#     nomes = arq.readlines()


# nomes_formatados=[]
# for n in nomes:
#     n = n.strip().upper()+"\n"
#     nomes_formatados.append(n)

# with open("nome.txt", "w") as arq:
#     arq.writelines(nomes_formatados)

# with open("nome.txt", "r") as arq:
#     for arq in nomes:
#         print(arq)






# with open("usuarios.txt", "r") as arq:
#     linhas = arq.readlines()

# linhas_formatadas = []
# for linha in linhas:
#     nome, idade = linha.strip().split(";")
#     linhas_formatadas.append(f"{nome.upper()};{idade}\n")

# with open("usuarios.txt", "w") as arq:
#     arq.writelines(linhas_formatadas)



try:
    with open("log.txt", "x") as arq:
        arq.write("arquivo criado com sucesso!\n")
except FileExistsError:
    print("O arquivo log.txt ja existe.")