# with open("alunos.txt", "w") as nomes:
#     nomes.write("gabriel\n")
#     nomes.write("mirella\n")
#     nomes.write("chico\n")


#############################################################

    
# with open("alunos.txt", "r") as nomes:
#     for nome in nomes:
#         print(nome.strip())



# with open("amigos.txt", "w") as nomes:
#     nomes.write("gabriel\n")
#     nomes.write("mirella\n")
#     nomes.write("claudia\n")
#     nomes.write("rodrigo\n")
#     nomes.write("chico\n")
#     nomes.write("mayara\n")

# with open("amigos.txt", "a") as nomes:
#     nomes.write("esse texto foi modificado com append")


# linhas = ["gabriel\n", "mirella\n"]
# with open("participantes.txt", "w") as arq:
#     arq.writelines(linhas)


with open("nome.txt", "a") as arq:
    arq.write("gabriel\n")
    arq.write("giovani\n")

with open("nome.txt", "r") as arq:
    # for nome in arq:
    #     print(nome.strip())

    linhas = arq.readlines()
    print(linhas)




