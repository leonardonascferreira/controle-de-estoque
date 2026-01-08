import os
import json
from colorama import Fore, init
init(autoreset=True)

arquivo_estoque = 'estoque.json'



#Função limpar a tela
def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

#Função exibir menu
def exibir_menu():
      print('''==== MENU DE OPÇÕES ====
[ 0 ] Adicionar Produto
[ 1 ] Atualizar Produto
[ 2 ] Excluir Produto
[ 3 ] Visualizar Estoque
[ 4 ] Sair do Sistema
''')

#Função adicionar produtos
def adicionar_produto():
    nome_produto = str(input('Digite o nome do produto: '))
    preco_produto = float(input('Digite o preço do produto: R$'))
    qtde_estoque = float(input('Quantidade no estoque: '))

def atualizar_produto():
     
def excluir_produto():
     
def visualizar_estoque():
     

exibir_menu()