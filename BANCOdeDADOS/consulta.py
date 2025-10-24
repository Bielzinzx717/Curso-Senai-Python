# from conexao_bd import conectar_bd

# def listar_pedidos():
#     conn = conectar_bd()
#     with conn:
#         with conn.cursor() as cur:
#             cur.execute("""
#                      SELECT c.nome, p.id, p.valor_total, p.status
#                     FROM clientes c
#                     JOIN pedidos p ON c.id = p.cliente_id;
#             """)
#             for linha in cur.fetchall():
#                 print(linha)
#     conn.close()
# listar_pedidos()



# from conexao_bd import conectar_bd

# def criar_tabelas():
#     conn = conectar_bd()
#     try:
#         with conn:
#             with conn.cursor() as cur:
#                 cur.execute("""
#                     CREATE TABLE IF NOT EXISTS fornecedores (
#                         id BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
#                         nome VARCHAR(100) NOT NULL,
#                         cnpj CHAR(14) UNIQUE
#                     );
                            
#                     CREATE TABLE IF NOT EXISTS produtos_fornecedores (
#                         id_produto BIGINT NOT NULL REFERENCES produtos(id) ON DELETE CASCADE,
#                         id_fornecedor BIGINT NOT NULL REFERENCES fornecedores(id) ON DELETE CASCADE,
#                         PRIMARY KEY (id_produto, id_fornecedor)
#                     );
#                 """)
#                 print("Tabela 'fornecedores' e tabela auxiliar 'produtos_fornecedores' criadas com êxito!")
#     finally:
#         conn.close()

# criar_tabelas()
















from conexao_bd import conectar_bd

def criar_tabelas():
    conn = conectar_bd()
    try:
        with conn:
            with conn.cursor() as cur:
                
                cur.execute("""
                    INSERT INTO produtos (nome, preco, estoque)
                    VALUES ('Notebook Dell', 5000.00, 10)
                    ON CONFLICT DO NOTHING;
                """)
                print("Produto adicionado com sucesso!")

                
                cur.execute("""
                    INSERT INTO fornecedores (nome, cnpj) VALUES
                        ('fornecedor A', '1234567'),
                        ('fornecedor B', '3472841283')
                    ON CONFLICT (cnpj) DO NOTHING;
                """)
                print("Fornecedores adicionados com sucesso!")

                
                cur.execute("""
                    INSERT INTO produtos_fornecedores (id_produto, id_fornecedor)
                    VALUES (7, 9), (7, 10);
                """)
                print("Produto ligado aos fornecedores com sucesso!")

                

    finally:
        conn.close()
        

criar_tabelas()











