# Menu de Cadastros

Este projeto é um menu simples em Python para gerenciar clientes em memória. O script principal, `menu.py`, permite cadastrar, buscar, listar, remover e editar clientes sem salvar os dados em banco ou arquivo.

## Funcionalidades

- Cadastrar clientes com nome, e-mail, telefone e cidade
- Buscar clientes por nome
- Listar todos os clientes cadastrados
- Remover clientes pelo índice da lista
- Editar os dados de um cliente existente
- Encerrar o programa pelo menu

## Menu principal

1. Cadastrar Clientes
2. Buscar Clientes
3. Listar Clientes
4. Remover Clientes
5. Editar Clientes
6. Sair

Ao finalizar uma ação, o programa exibe a opção:

- Voltar ao menu - 1
- Sair - 2

## Como usar

1. Abra o terminal na pasta do projeto.
2. Execute o script:

```bash
python menu.py
```

3. Escolha uma opção no menu.
4. Siga as instruções exibidas para cadastrar, buscar, listar, remover ou editar clientes.

## Requisitos

- Python 3

## Observações

- Os dados ficam armazenados em memória enquanto o programa estiver em execução.
- O projeto começa com um cliente pré-cadastrado de exemplo: Victor.
- Não há persistência em disco; ao fechar o programa, os dados são perdidos.

## Estrutura do arquivo

- `menu.py`: script principal do projeto.
- `README.md`: documentação do projeto.
