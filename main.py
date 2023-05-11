from Entidade.Produto import Produto
from Entidade.Categoria import Categoria

list_produtos = []
list_categoria = []

print('+-------- MENU  PRINCIPAL --------+')
print('| 1 - Cadastrar Categoria         |')
print('| 2 - Excluir Categoria           |')
print('| 3 - Cadastrar Produto           |')
print('| 4 - Excluir Produto             |')
print('| 5 - Exibir Produtos Cadastrados |')
print('| 6 - Adicionar Estoque a Produto |')
print('| 7 - Remover Estoque de Produto  |')
print('| 8 - SAIR                        |')
print('+---------------------------------+')
opcao = int(input('Informe o número que corresponde à opção desejada do menu: '))

while opcao != 8:
  if opcao == 1:
    Categoria.CadastrarCategoria(list_categoria)
    opcao = int(input('Informe o número que corresponde à opção desejada do menu: '))
  elif opcao == 2:
    Categoria.ExcluirCategoria(list_categoria)
    opcao = int(input('Informe o número que corresponde à opção desejada do menu: '))
  elif opcao == 3:
    Produto.CadastrarProduto(list_produtos,list_categoria)
    opcao = int(input('Informe o número que corresponde à opção desejada do menu: '))
  elif opcao == 4:
    Produto.ExcluirProduto(list_produtos)
    opcao = int(input('Informe o número que corresponde à opção desejada do menu: '))
  elif opcao == 5:
    Produto.ProdutosCadastrados(list_produtos)
    opcao = int(input('Informe o número que corresponde à opção desejada do menu: '))
  elif opcao == 6:
    Produto.AdicionarEstoque()
    opcao = int(input('Informe o número que corresponde à opção desejada do menu: '))
  elif opcao == 7:
    Produto.RemoverEstoque()
    opcao = int(input('Informe o número que corresponde à opção desejada do menu: '))
  else:
      print(('Opção não identificada.'))
      opcao = int(input('Informe novamente o número que corresponde à opção desejada do menu: '))
