# from dataclasses import dataclass

# @dataclass
# class Produto:
#     nome: str
#     preço: float
#     estoque: int = 0

# p1 = Produto ("Caneta", 2.50, 10)
# p2 = Produto ("Caneta", 2.50, 10)

# print (p1)
# print(p1 == p2)


# import sqlite3

# conexao = sqlite3.connect('meubanco.db')

# cursor = conexao.cursor()

# cursor.execute('''
# CREATE TABLE IF NOT EXISTS usuarios (
#     id INTEGER PRIMARY KEY AUTOINCREMENT, 
#     nome TEXT NOT NULL,
#     email TEXT UNIQUE NOT NULL
# )
#  ''')


# cursor.execute('INSERT INTO usuarios (nome, email) VALUES (?, ?)', ("Gabriel", 'gabriel@email.com'))

# conexao.commit()
# conexao.close()

# print("Banco criado e usuari inserido com sucesso!")


# import sqlite3
# conexao = sqlite3.connect('loja.db')
# cursor = conexao.cursor()
# cursor.execute('''
# CREATE TABLE IF NOT EXISTS produtos (
#     id INTERGER PRIMARY KEY AUTOINCREMENT,
#     nome TEXT NOT NULL,
#     preco INTEGER NOT NULL,
#     estuque  INTEGER NOT NULL
# )
# ''')

# cursor.execute('INSERT INTO produtos (nome, preco, estoque) VALUES (?, ?)', ("agua", 2, 10)) #("miojo", 10, 20), ("cafe", 5, 10))

# conexao.commit()
# conexao.close()
# print("PRODUTOS")




import sqlite3


conexao = sqlite3.connect('loja.db')
cursor = conexao.cursor()


cursor.execute('''
CREATE TABLE IF NOT EXISTS produtos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    preco INTEGER NOT NULL,
    estoque INTEGER NOT NULL
)
''')


# cursor.execute('INSERT INTO produtos (nome, preco, estoque) VALUES (?, ?, ?)', ("agua", 2, 10))

produtos = [
    ("agua", 2, 10),
    ("miojo", 10, 20),
    ("cafe", 5, 10)
]

cursor.executemany('INSERT INTO produtos (nome, preco, estoque) VALUES (?, ?, ?)', produtos)



conexao.commit()
conexao.close()

print("PRODUTO INSERIDO COM SUCESSO!")
print(produtos)
 