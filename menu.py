def linhas():
    print('-'*30)

def Quer_continuar():
    linhas()
    print('Voltar ao menu - 1\nSair - 2')
    linhas()

nomes = ['Sofia', 'Samara', 'Manuela']
idades = [18, 20, 40]
cpfs = [143, 222, 000]

while True:
    linhas()
    print('     MENU DE CADASTROS')
    linhas()
    print('Cadastrar Usuarios - 1\nBuscar Usuarios - 2\nListar Usuarios - 3\nRemover Usuarios - 4\nSair - 5')
    escolha = int(input('Digite a opção desejada: '))
    
    if escolha == 1:
        linhas()
        print('Para cadastrar um usuario insira as informações abaixo: ')
        nome = input('Digite o nome: ')
        idade = int(input('Digite a idade: '))
        cpf = int(input('Digite o cpf: '))
        nomes.append(nome)
        idades.append(idade)
        cpfs.append(cpf)
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
        for i in range(len(nomes)):
            if nome == nomes[i]:
                print(f'nome na posição {i}: {nomes[i]}')
                print(f'Idades na posição {i}: {idades[i]}')
                print(f'Cpf na posição {i}: {cpfs[i]}')
                linhas()
        Quer_continuar()
        escolha = int(input('Escolha uma opção no menu para continuar: '))
        if escolha == 1:
            continue
        else:
            break
    elif escolha == 3:
        linhas()
        for e in range(len(nomes)): 
            print(f'nome: {nomes[e]} |idade: {idades[e]}| cpf: {cpfs[e]}')
        Quer_continuar()
        escolha = int(input('Escolha uma opção no menu para continuar: '))
        if escolha == 1:
            continue
        else:
            break
    elif escolha == 4:
        linhas()
        for e in range(len(nomes)):
                print(f'{e + 1} - {nomes[e]}')
        remover = int(input('Digite o indice que deseja remover(ex: 1 - Victor)'))
        nomes.pop(remover - 1)
        idades.pop(remover - 1)
        cpfs.pop(remover - 1)

        Quer_continuar()
        escolha = int(input('Escolha uma opção no menu para continuar: '))
        if escolha == 1:
            continue
        else:
            break
    elif escolha == 5:
        break

    else:
        print('Opção Invalida, escolha outra opção')
        continue



    