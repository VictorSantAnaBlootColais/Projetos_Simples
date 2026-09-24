import mysql.connector

conexao = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Drito_42_u",
    database="cadastro_clientes"
)

cursor = conexao.cursor()


def linhas():
    print('-'*30)

def Quer_continuar():
    linhas()
    print('Voltar ao menu - 1\nSair - 2')
    linhas()


while True:
    linhas()
    print('     MENU DE CADASTROS')
    linhas()
    print('1 - Cadastrar Clientes\n2 - Buscar Clientes\n3 - Listar Clientes\n4 - Remover Clientes\n5 - Editar Clientes\n6 - Sair')
    escolha = int(input('Digite a opção desejada: '))

    if escolha == 1:
        linhas()
        print('Para cadastrar um usuario insira as informações abaixo: ')
        nome = input('Digite o nome: ')
        email = input('Digite o email: ')
        telefone = input('Digite o telefone: ')
        cidade = input('Digite a cidade: ')
        cliente = {
            "nome" : nome,
            "email" : email,
            "telefone" : telefone,
            "cidade" : cidade
        }
        clientes.append(cliente)
        Quer_continuar()
        escolha = int(input('Escolha uma opção no menu para continuar: '))
        if escolha == 1:
            continue
        else:
            break
    elif escolha == 2:
        linhas()
        nome = input('Digite em o nome para pesquisar: ')
        linhas()
        for cliente in clientes:
            if nome == cliente["nome"]:
                print(f'nome : {cliente["nome"]}')
                print(f'email : {cliente["email"]}')
                print(f'telefone : {cliente["telefone"]}')
                print(f'cidade : {cliente["cidade"]}')
                linhas()
        Quer_continuar()
        escolha = int(input('Escolha uma opção no menu para continuar: '))
        if escolha == 1:
            continue
        else:
            break
    elif escolha == 3:
        linhas()

        cursor.execute("SELECT * FROM clientes")

        clientes = cursor.fetchall()

        for numero, cliente in enumerate(clientes, start=1):
            linhas()
            print(f'Cliente {numero}')
            print(f'ID: {cliente[0]}')
            print(f'Nome: {cliente[1]}')
            print(f'Email: {cliente[2]}')
            print(f'Telefone: {cliente[3]}')
            print(f'Cidade: {cliente[4]}')

        Quer_continuar()
        escolha = int(input('Escolha uma opção no menu para continuar: '))

        if escolha == 1:
            continue
        else:
            break

    elif escolha == 4:
        linhas()
        for numero, cliente in enumerate(clientes, start=1):
                print(f'{numero} - {cliente["nome"]}')
        remover = int(input('Digite o indice que deseja remover(ex: 1 - Victor)'))
        clientes.pop(remover - 1)
        print("Cliente removido com sucesso")

        Quer_continuar()
        escolha = int(input('Escolha uma opção no menu para continuar: '))
        if escolha == 1:
            continue
        else:
            break

    elif escolha == 5:
        linhas()
        for numero, cliente in enumerate(clientes, start=1):
                      print(f'{numero} - {cliente["nome"]}')
        atualizar = int(input("Digite o número do usuário que deseja atualizar: "))
        cliente = clientes[atualizar - 1]
        print(f"Nome: {cliente["nome"]}")
        print(f"Email: {cliente["email"]}")
        print(f"Telefone: {cliente["telefone"]}")
        print(f"Cidade: {cliente["cidade"]}")

        print("Campo de atualização liberado")
        nome = input('Digite o nome: ')
        cliente["nome"] = nome

        email = input('Digite o email: ')
        cliente["email"] = email

        telefone = input('Digite o telefone: ')
        cliente["telefone"] = telefone

        cidade = input('Digite a cidade: ')
        cliente["cidade"] = cidade

        print("Cliente Atualizado com sucesso")
        Quer_continuar()
        escolha = int(input('Escolha uma opção no menu para continuar: '))
        if escolha == 1:
            continue
        else:
            break

    if escolha == 6:
        break

    else:
        print('Opção Invalida, escolha outra opção')
        continue





