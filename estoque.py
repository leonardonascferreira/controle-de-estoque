import os

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def exibir_menu():
      print('''MENU DE OPÇÕES
      [ 0 ] Adicionar Produto
      [ 1 ] Atualizar Produto
      [ 2 ] Excluir Produto
      [ 3 ] Visualizar Estoque
      [ 4 ] Sair do Sistema
            ''')