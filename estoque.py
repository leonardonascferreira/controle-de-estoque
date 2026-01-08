import os
import json

arquivo_estoque = 'estoque.json'

#Carregar estoque
def carregar_estoque():
    try:
        with open(arquivo_estoque, 'r') as e:
            return json.load(e)
    except FileNotFoundError:
        return[]

estoque = carregar_estoque()

#Salvar estoque
def salvar_estoque():
    with open(arquivo_estoque, 'w') as e:
        json.dump(estoque, e, indent=2)

#Função limpar a tela
def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

#Função de continuar
def continuar():
    print()
    (input('\033[32mAperte ENTER para continuar!\033[m'))

#Função exibir menu
def exibir_menu():
      print('''\033[34m==== MENU DE OPÇÕES ====
[ 1 ] Adicionar Produto
[ 2 ] Atualizar Produto
[ 3 ] Excluir Produto
[ 4 ] Visualizar Estoque
[ 0 ] Sair do Sistema
\033[m''')

#Função adicionar produtos
def adicionar_produto():
    print()
    nome = str(input('Digite o nome do produto: '))
    try:
        preco = float(input('Digite o preço do produto: R$'))
        quantidade = int(input('Quantidade no estoque: '))
    except ValueError:
         print('\033[31mErro: Digite apenas números válidos.\033[m')
         return
    estoque.append({
        'nome': nome,
        'preco': preco,
        'quantidade': quantidade
    })
    salvar_estoque()
    print()
    print(f'\033[32mProduto {nome} adicionado!\033[m')

#Função atualizar os produtos
def atualizar_produto():
    print()
    if not estoque:
        print('Produto não encontrado. Tente novamente.')
        return
    buscar_produto = input('Digite o nome do produto que deseja atualizar: ')
    for produto in estoque:
        if produto['nome'].lower() == buscar_produto.lower():
            print(f'Produto encontrado! {produto['nome']} | Preço: {produto['preco']:.2f} | Quantidade: {produto['quantidade']}')
            print()
            print('''Opções disponíveis para a atualização:
[ 1 ] Preço
[ 2 ] Quantidade
[ 0 ] Cancelar''')
        
            opcao = input('Escolha uma opção: ')

            if opcao == '1':
                novo_preco = float(input('Digite o novo preço: R$'))
                produto['preco'] = novo_preco
                salvar_estoque()
            elif opcao == '2':
                nova_qtde = int(input('Digite a nova quantidade: '))
                produto['quantidade'] = nova_qtde
                salvar_estoque()
            elif opcao == '0':
                print('Cancelado!')
                return
            else:
                print('Opção inválida, tente novamente.')
                return
            print('\033[32mProduto atualizado com sucesso!\033[m')
            return

#Função para excluir produtos     
def excluir_produto():
    print()
    if not estoque:
        print('Produto não encontrado. Tente novamente.')
        return
    excluir_produto = input('Digite o nome do produto que deseja excluir: ')
    for i, produto in enumerate(estoque):
        if produto['nome'].lower() == excluir_produto.lower():
            print(f'''\033[33mDeseja realmente excluir esse produto? {produto['nome']}
[ SIM ]
[ NÃO ]''')
            
            opcao = input('Escolha uma opção: ').upper().strip()

            if opcao == 'SIM':
                estoque.pop(i)
                print('\033[32mProduto excluído com sucesso!')
            elif opcao == 'NAO':
                print('Exclusão cancelada.')
            else:
                print('Opcão inválida, tente novamente.')
                return
    print('Produto não encontrado!')
    salvar_estoque()

#Função para visualizar o estoque
def visualizar_estoque():
    print()
    if not estoque:
        print()
        print('Estoque vazio!')
    else:
        print(' ==== ESTOQUE ====')
        for i, produto in enumerate(estoque, 1):
            print(f'{i}. {produto['nome']} | Preço R${produto['preco']} | Quantidade: {produto['quantidade']}')

#Loop
while True:
    limpar_tela()
    exibir_menu()
    opcao = input('\033[33mDigite a opção desejada: \033[m')
    if opcao == '0':
         print()
         print('Saindo do sistema...')
         break
    elif opcao == '1':
        adicionar_produto()
    elif opcao == '2':
        atualizar_produto()
    elif opcao == '3':
        excluir_produto()
    elif opcao == '4':
        visualizar_estoque()
    else:
        print('\033[31mOpção inválida, tente novamente.\033[m')
    continuar()