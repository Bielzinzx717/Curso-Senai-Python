# from conexao_bd import conectar_bd
# def criar_enderecos():
#     conn = conectar_bd()
#     try:
#         with conn:
#             with conn.cursor() as cur:

#                 cur.execute("""
#                             INSERT INTO clientes (nome, email) VALUES ('marcelo', 'marcelo@gmail.com');
                            
#                             INSERT INTO pedidos (cliente_id, valor_total, status) VALUES (1, 89.00, 'pago'), (1, 110.00, 'pago');
#                             """)
#                 print("Pedidos inseridos com sucessso!")
#                 conn.commit()
#     except Exception as e:
#         print(f"Erro: {e}")
#         print("Alterações desfeitas!")
#     finally:
#         conn.close()
#         print("Conexão Fechada!")
# criar_enderecos()




from conexao_bd import conectar_bd

def criar_enderecos():
    conn = conectar_bd()
    try:
        with conn:
            with conn.cursor() as cur:

                # 1️⃣ Inserir cliente e capturar o ID gerado
                cur.execute("""
                    INSERT INTO clientes (nome, email)
                    VALUES ('marcelo', 'marcelo@gmail.com')
                    RETURNING id;
                """)
                cliente_id = cur.fetchone()[0]  # pega o ID do cliente

                # 2️⃣ Inserir pedidos usando o cliente_id retornado
                cur.execute("""
                    INSERT INTO pedidos (cliente_id, valor_total, status)
                    VALUES (%s, %s, %s),
                           (%s, %s, %s);
                """, (cliente_id, 89.00, 'pago', cliente_id, 110.00, 'pago'))

                conn.commit()
                print("Pedidos inseridos com sucesso!")

    except Exception as e:
        print(f"Erro: {e}")
        print("Alterações desfeitas!")
    finally:
        conn.close()
        print("Conexão Fechada!")

criar_enderecos()
