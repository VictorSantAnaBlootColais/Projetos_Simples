import mysql.connector

conexao = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Drito_42_u",
    database="cadastro_clientes"
)

cursor = conexao.cursor()

cursor.execute("SELECT * FROM clientes")

clientes = cursor.fetchall()

for cliente in clientes:
    print(f"ID: {cliente[0]}")
    print(f"Nome: {cliente[1]}")
    print(f"Email: {cliente[2]}")
    print(f"Telefone: {cliente[3]}")
    print(f"Cidade: {cliente[4]}")

cursor.close()
conexao.close()