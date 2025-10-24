# ## Exercicio prático de Criação e Alteração de Tabelas
# from conexao_bd import conectar_bd
# def run():
#     conn = conectar_bd()
#     try:
#         with conn:
#             with conn.cursor() as cur:
#                 cur.execute("""
#                     CREATE TABLE IF NOT EXISTS categorias (
#                         id   BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
#                         nome VARCHAR(60) NOT NULL UNIQUE);
                            
#                     ALTER TABLE produtos ADD COLUMN IF NOT EXISTS categoria_id BIGINT;
                            
#                     ALTER TABLE produtos
#                         ADD CONSTRAINT fk_produtos_categoria 
#                         FOREIGN KEY (categoria_id) REFERENCES categorias(id) IF NOT EXISTS;
                            
#                     INSERT INTO categorias (nome)
#                             ('Informática'), ('Papelaria'), ('Livros')
#                             ON CONFLICT (nome) DO NOTHING;
#                 """)
#                 conn.commit()
#                 print("Categorias criadas e produtos atualizados (se existirem).")
#     except Exception as e:
#         print(f"Erro: {e}")
#         print("Alterações desfeitas!")            
#     finally:
#         conn.close()
#         print("Conexão Fechada!")
# if __name__ == "__main__":
#     run()




# from conexao_bd import conectar_bd

# def run():
#     conn = conectar_bd()
#     try:
#         with conn:
#             with conn.cursor() as cur:
#                 cur.execute("""
#                     CREATE TABLE IF NOT EXISTS categorias (
#                         id   BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
#                         nome VARCHAR(60) NOT NULL UNIQUE
#                     );

#                     ALTER TABLE produtos ADD COLUMN IF NOT EXISTS categoria_id BIGINT;

#                     DO $$
#                     BEGIN
#                         IF NOT EXISTS (
#                             SELECT 1 FROM information_schema.table_constraints
#                             WHERE constraint_name = 'fk_produtos_categoria'
#                               AND table_name = 'produtos'
#                         ) THEN
#                             ALTER TABLE produtos
#                                 ADD CONSTRAINT fk_produtos_categoria
#                                 FOREIGN KEY (categoria_id) REFERENCES categorias(id);
#                         END IF;
#                     END $$;

#                     INSERT INTO categorias (nome)
#                         VALUES ('Informática'), ('Papelaria'), ('Livros')
#                         ON CONFLICT (nome) DO NOTHING;
#                 """)
#                 conn.commit()
#                 print("Categorias criadas e produtos atualizados (se existirem).")
#     except Exception as e:
#         print(f"Erro: {e}")
#         print("Alterações desfeitas!")            
#     finally:
#         conn.close()
#         print("Conexão Fechada!")

# if __name__ == "__main__":
#     run()
