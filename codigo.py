# numeros = [1, 2, 2, 3, 4, 4,5, 1]
# unicos = []

# for i in numeros:
#     if i not in unicos:
#         unicos.append(i)


# print(unicos)


# numeros = [1, 2, 2, 3, 4, 4,5, 1]
# unicos = list(set(numeros))
# print(unicos)

#######################################################################


# lista1 = ["mirella", "gabriel", "chico"]
# lista2 = ["mada", "clau", "chico"]

# repets = set(lista1)
# repets2 = set(lista2)

# interseçao = repets & repets2

# interseçao2 = list(interseçao)

# print(f"esse é o nome repetido: {interseçao2}")


###########################################################


# lista1 = ["mirella", "gabriel", "chico"]
# lista2 = ["mada", "clau", "chico"]

# conjunto1 = set(lista1)
# conjunto2 = set(lista2)



# diferença = conjunto1 - conjunto2
# print("diferença", diferença)




############################################################


frase = input("digite uma frase:")

palavras = frase.split()

unicas = []

for palavra in palavras:
    if palavra not in unicas:
        unicas.append(palavras)
print("palavras unicas:")

for palavra in unicas:
            print(palavra)


