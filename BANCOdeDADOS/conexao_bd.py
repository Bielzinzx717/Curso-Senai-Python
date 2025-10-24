## conexao_bd.py
import psycopg2
## Funcão para conectar ao Bando de Dados
def conectar_bd():
    conecta_bd = psycopg2.connect(
        database='loja_virtual',
        user='postgres',
        password='senaisp',
        host='localhost',
        port='5432'
    )
    return conecta_bd  # Retornar a conexão

