import mysql.connector

conexao = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Drito_42_u",
    database="cadastro_clientes"
)

cursor = conexao.cursor()

sql = """
INSERT INTO clientes (nome, email, telefone, cidade)
VALUES (%s, %s, %s, %s)
"""

dados = (
    "Victor",
    "victor@gmail.com",
    "41984825864",
    "Curitiba"
)

cursor.execute(sql, dados)

conexao.commit()

print("Cliente cadastrado com sucesso!")

cursor.close()
conexao.close()