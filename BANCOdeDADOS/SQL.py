# # import psycopg2

# # conexao = psycopg2.connect(
# #     dbname = "postgres",
# #     user = "postgres",
# #     password = "senaisp",
# #     host = "localhost",
# #     port = "5432"
    
# # )


# # conexao.autocommit = True

# # cursor = conexao.cursor()
# # cursor.execute("CREATE DATABASE meubanco")
# # cursor.close()
# # conexao.close()

# # print("meu banco foi criado")



# import psycopg2
# from psycopg2 import OperationalError

# def conectar():
#     try:

#         conexao = psycopg2.connect(
#             dbname= "postgres",
#             user = "postgres",
#             password = "senaisp",
#             host = "localhost",
#             port = "5432"
            
#         )
        
#         print("Conexão com o banco de dados bem sucedida!")
#         conexao.close()

#     except OperationalError as e:
#         print("Erro ao conectar ao banco de dados:")
#         print(e)
# conectar()


# import psycopg2

# conexao = psycopg2.connect(
#     dbname = "postgres",
#     user = "postgres",
#     password = "senaisp",
#     host = "localhost",
#     port = "5432"
# )

# cursor = conexao.cursor()
# cursor.execute("""
#     CREATE TABLE IF NOT EXISTS clientes ( 
#         id SERIAL PRIMARY KEY,
#         nome VARCHAR(80) NOT NULL,
#         email VARCHAR(120) UNIQUE,
#         telefone VARCHAR(20),
#         data_cadastro DATE DEFAULT CURRENT_DATE
#     )
# """)


# conexao.commit()
# cursor.close()
# conexao.close()
# print("Tabela 'clientes' criada com sucesso!")



import psycopg2

conexao = psycopg2.connect(
    dbname = "postgres",
    user = "postgres",
    password = "senaisp",
    host = "localhost",
    port = "5432"
)


cursor = conexao.cursor()
cursor.execute("""
    
    CREATE TABLE IF NOT EXISTS loja ( 
        id SERIAL PRIMARY KEY,
        nome VARCHAR(80) NOT NULL,
        email VARCHAR(120) UNIQUE,
        telefone VARCHAR(20),
        data_cadastro DATE DEFAULT CURRENT_DATE
    )
""")

cursor.execute("""
    INSERT INTO loja (nome, email, telefone) VALUES
    ('marcelo', 'marcelo@gmail.com', '19-997020921'),
    ('junio', 'junio@gmail.com', '19-7777777'),
    ('ana julia', 'anajulia@gmail.com', '19-9999999')
    ON CONFLICT (email) DO NOTHING;
    """)




conexao.commit()
cursor.close()
conexao.close()
print("Tabela 'loja' criada com sucesso!")
