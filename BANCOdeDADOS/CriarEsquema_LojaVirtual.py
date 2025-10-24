## CriarEsquema_LojaVirtual.py
from psycopg2.extras import execute_batch
from conexao_bd import conectar_bd

Tabelas = [
    """
    CREATE TABLE IF NOT EXISTS clientes (
        id                BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
        nome              VARCHAR(80)        NOT NULL,
        email             VARCHAR(120)       UNIQUE,
        telefone          VARCHAR(20),
        data_cadastro     DATE               NOT NULL DEFAULT CURRENT_DATE,
        ativo             BOOLEAN            NOT NULL DEFAULT TRUE,
        CHECK (length(nome) >= 2)
    )
    """,
    """
    CREATE TABLE IF NOT EXISTS produtos (
        id                BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
        nome              VARCHAR(100)       NOT NULL,
        preco             NUMERIC(10,2)      NOT NULL CHECK (preco >= 0),
        estoque           INT                NOT NULL DEFAULT 0 CHECK (estoque >= 0),
        criado_em         TIMESTAMPTZ        NOT NULL DEFAULT CURRENT_TIMESTAMP
    )
    """,
    """
    CREATE TABLE IF NOT EXISTS pedidos (
        id                BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
        cliente_id        BIGINT             NOT NULL REFERENCES clientes(id),
        criado_em         TIMESTAMPTZ        NOT NULL DEFAULT CURRENT_TIMESTAMP,
        valor_total       NUMERIC(10,2)      NOT NULL DEFAULT 0 CHECK (valor_total >= 0),
        status            VARCHAR(20)        NOT NULL DEFAULT 'aberto',
        CHECK (status IN ('aberto', 'pago', 'cancelado'))
    )
    """,
    """
    CREATE TABLE IF NOT EXISTS itens_pedido (
        id                BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
        pedido_id         BIGINT             NOT NULL REFERENCES pedidos(id) ON DELETE CASCADE,
        produto_id        BIGINT             NOT NULL REFERENCES produtos(id),
        quantidade        INT                NOT NULL CHECK (quantidade > 0),
        preco_unitario    NUMERIC(10,2)      NOT NULL CHECK (preco_unitario >= 0),
        UNIQUE (pedido_id, produto_id)
    )
    """,
    "CREATE INDEX IF NOT EXISTS idx_pedidos_cliente ON pedidos(cliente_id);",
    "CREATE INDEX IF NOT EXISTS idx_itens_pedido_pedido ON itens_pedido(pedido_id);",
    "CREATE INDEX IF NOT EXISTS idx_produtos_nome ON produtos(LOWER(nome));"
]

def criar_esquema():
    conn = conectar_bd()
    try:
        with conn:
            with conn.cursor() as cur:
                for stmt in Tabelas:
                    cur.execute(stmt)
                    conn.commit()
        print("Esquema criado com sucesso!")
    except Exception as e:
        print(f"Erro: {e}")
        print("Alterações desfeitas!")            
    finally:
        conn.close()
        print("Conexão Fechada!")

if __name__ == "__main__":
    criar_esquema()