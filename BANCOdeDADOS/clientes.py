from conexao_bd import conectar_db

def criar_enderecos():
    conn = conectar_db()
    try:
        with conn:
            with conn.cursor() as cur:
                cur.execute("""
                    CREATE TABLE IF NOT EXISTS enderecos (
                        id BIGINT GENERATED ALWAYS AS IDENTIFY PRIMARY KEY,
                        cliente_id BIGING UNIQUE NOT NULL REFERENCES clientes(id) ON DELETE CASCADE,
                        rua VARCHAR(120) NOT NULL,
                        numero VARCHAR(10),
                        cidade VARCHAR(60) NOT NULL,
                        estado CHAR(2) NOT NULL
                    );
                """)
                print("Tabela 'enderecos' criada com sucesso!")
                conn.commit()
    except Exception as e:
        print(f"Erro: {e}")
        print("Alterações desfeitas!")
    finally:
        conn.close()
        print("Conexão Fechada!")
        criar_enderecos()