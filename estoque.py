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
        preco_produto = float(input('Digite o preço do produto: R$'))
        qtde_estoque = int(input('Quantidade no estoque: '))
    except ValueError:
         print('Erro: Digite apenas números válidos.')
         return

def atualizar_produto():
    buscar_produto = input('Digite o nome do produto que deseja atualizar: ')
    for produto in estoque:
        if produto['nome'].lower() == buscar_produto.lower():
            print('sexo')
     
#def excluir_produto():
     
#def visualizar_estoque():
     

while True:
    limpar_tela()
    exibir_menu()
    opcao = input('Digite a opção desejada: ')
    if opcao == '0':
         print('Saiundo do sistema :)')
         break
    if opcao == '1':
        adicionar_produto()
    elif opcao == '2':
        atualizar_produto()