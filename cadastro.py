# with open("alunos.txt", "w") as nomes:
#     nomes.write("gabriel\n")
#     nomes.write("mirella\n")
#     nomes.write("chico\n")




    
with open("alunos.txt", "r") as nomes:
    for nome in nomes:
        print(nome.strip())