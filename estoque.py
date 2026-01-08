import os
import json
from colorama import Fore, init
init(autoreset=True)

arquivo_estoque = 'estoque.json'

#Carregar estoque
def carregar_estoque():
    try:
        with open(arquivo_estoque, 'r') as e:
            return json.load(e)
    except FileNotFoundError:
        return []

estoque = carregar_estoque()

#Salvar estoque
def salvar_estoque():
    with open(arquivo_estoque, 'w') as e:
        json.dump(estoque, e, indent=2)

#Função limpar a tela
def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

#Função exibir menu
def exibir_menu():
      print('''==== MENU DE OPÇÕES ====
[ 1 ] Adicionar Produto
[ 2 ] Atualizar Produto
[ 3 ] Excluir Produto
[ 4 ] Visualizar Estoque
[ 0 ] Sair do Sistema
''')

#Função adicionar produtos
def adicionar_produto():
    print()
    nome = str(input('Digite o nome do produto: '))
    try:
        preco = float(input('Digite o preço do produto: R$'))
        quantidade = int(input('Quantidade no estoque: '))
    except ValueError:
         print('Erro: Digite apenas números válidos.')
         return
    estoque.append({
        'nome': nome,
        'preco': preco,
        'quantidade': quantidade
    })
    salvar_estoque()
    print(f'Produto {nome} adicionado!')

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
                novo_preco = float(input('Digite o novo preço do produto: R$'))
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
            print('Produto atualizado com sucesso!')
            return
     
def excluir_produto():
    print()
    if not estoque:
        print('Produto não encontrado. Tente novamente.')
        return
    buscar_produto = input('Digite o nome do produto que deseja excluir: ')
    for produto in estoque:
        if produto['nome'].lower() == buscar_produto.lower():
            print('''Deseja realmente excluir esse produto?
[ SIM ]
[ NÃO ]''')
            
            opcao = input('Escolha uma opção: ').upper().strip()

            if opcao == 'SIM':

            elif opcao == 'NAO':

            else:
                print('Opcão inválida, tente novamente.')
                return

#def visualizar_estoque():
    

while True:
    limpar_tela()
    exibir_menu()
    opcao = input('Digite a opção desejada: ')
    if opcao == '0':
         print('Saindo do sistema :)')
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
        print('Opção inválida, tente novamente.')
