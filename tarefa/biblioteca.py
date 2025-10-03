from bibliotecas import bibliotecas

livro_0 = bibliotecas("algoritimos")
livro_1 = bibliotecas("dom casmurro")
livro_2 = bibliotecas("superação")
livro_3 = bibliotecas("biblia sagrada")
livro_4 = bibliotecas("alice no pais da maravilha")



print("===================================================="
      '''
      ''')

print("Bem-vindo! Esse sao alguns livros que vc tem como escolher.")


nome = input("digite seu nome para começarmos: ")

print(f"{nome} temos 5 livros que combina com vc:"
'''
[0] algoritimos
[1] dom casmurro
[2] superação
[3] biblia sagrada
[4] alice no pais da maravilhas

''')


seleção = int(input("digite o numero do livro desejado: "))
livros = [livro_0, livro_1, livro_2, livro_3, livro_4]

opcao_selecionada = int(seleção)
for opcao in livros:
    if opcao_selecionada >= 5:
        print("esta opcao nao esta incluida em nossos livros disponiveis.")
        break

    if opcao_selecionada<= 4:
        print(f"{nome} o livro que vc escolheu {livros[opcao_selecionada].livro} foi resgatado.")
        break




# from bibliotecas import bibliotecas

# # Criando os livros
# livro_0 = bibliotecas("Algoritmos")
# livro_1 = bibliotecas("Dom Casmurro")
# livro_2 = bibliotecas("Superação")
# livro_3 = bibliotecas("Bíblia Sagrada")
# livro_4 = bibliotecas("Alice no País das Maravilhas")

# livros = [livro_0, livro_1, livro_2, livro_3, livro_4]

# print("====================================================\n")
# print("Bem-vindo! Esses são alguns livros que você pode escolher.")

# nome = input("Digite seu nome para começarmos: ")

# print(f"\n{nome}, temos 5 livros que combinam com você:\n"
#       "[0] Algoritmos\n"
#       "[1] Dom Casmurro\n"
#       "[2] Superação\n"
#       "[3] Bíblia Sagrada\n"
#       "[4] Alice no País das Maravilhas\n")

# seleção = int(input("Digite o número do livro desejado: "))

# if 0 <= seleção < len(livros):
#     print(f"\n{nome}, o livro que você escolheu, \"{livros[seleção].livro}\", foi resgatado.")
# else:
#     print("\nEssa opção não está incluída em nossos livros disponíveis.")
