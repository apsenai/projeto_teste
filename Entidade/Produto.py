from Entidade import Categoria

class Produto:
   def __init__(self,prod_nome, custo, estoque, categoria):
       '''
        O método construtor cria o objeto da classe Produto
       :param prod_nome: Recebe o nome do produto
       :param custo: Recebe o custodo produto na compra
       :param estoque: Recebe a quantidade de produtos em estoque
       :param categoria: Recebe a categoria que o produto pertence
       '''
       self.prod_nome = prod_nome.upper()
       self.custo = custo
       self.estoque = estoque
       self.categoria = categoria
       self.total = 0

   def __str__(self):
       '''
        Sobrecarga no método para retornar uma string
       :return:  Retorna o nome do produto, a categoria, qtd em estoque e preço de venda
       '''
       return f'Produto: {self.prod_nome} / Custo: R${self.custo} ' \
              f'\n Categoria: {self.categoria} / Estoque: {self.estoque}' \
              f'\n Preço de venda: R${self.total}'

   '''
           Método estático para cadastrar produtos

          :param lista_prod:
          :param lista_cat:
          :return:
          '''
   @staticmethod
   def CadastrarProduto(lista_prod, lista_cat):
       prod_nome = input('Digite o nome do produto: ').upper()
       preco = float(input('Digite o preço do produto: '))
       estoque = int(input('Digite a quantidade de produtos em estoque: '))
       if estoque < 0:
           print('O número de itens em estoque não pode ser negativo')
       else:
          categoria = input('Digite a categoria do produto: ').upper()
          if categoria in lista_cat:
              if categoria.cat_nome == categoria:
                porc = categoria.porc_lucro
                custo = preco* porc + preco
                prod = Produto(prod_nome,custo,estoque,categoria)
                lista_prod.append(prod)
                print(lista_prod)

   @staticmethod
   def ExcluirProduto(lista_prod):
       '''
       Método estático para excluir um produto da lista de produtos,  caso o item que se deseja excluir não
       esteja cadastrado, é exibida uma mensagem informando que o produto não foi encontrado

       :param lista_prod: Lista que tem seus itens alterados
       :return:
       '''
       try:
           for i, item in enumerate(lista_prod):
               print(i, '-', item)
           remover_item = int(input('Digite o índice do produto que deseja remover: '))
           removido = lista_prod.pop(remover_item)
           print(f'{removido} foi removido da lista de produtos')
       except:
           print('Produto não foi removido pois não foi encontrado')

   @staticmethod
   def ProdutosCadastrados(lista_prod):
       '''
       Método estático que exibe a lista com todos os produtos previamente cadastrados

       :param lista_prod: Parametro da função, a lista que tem seus itens exibidos
       :return:
       '''
       print('Produtos cadastrados: ')
       for item in (lista_prod):
           print(item)

   @staticmethod
   def AdicionarEstoque(Produto):
       '''
       Método estático para alterar o estoque do produto adicionando determinado valor

       :param Produto: Recebe o novo valor para o estoque
       :return:
       '''
       adicionar = int(input('Quantos itens deseja adicionar no estoque?'))
       if adicionar>=0:
           Produto.estoque += adicionar
       else:
            print('Não é possível adicionar quantidade de estoque menor que 0')

   @staticmethod
   def RemoverEstoque(Produto):
       '''
       Método estático para alterar o estoque do produto retirando determinado valor
       Método estático para alterar o estoque do produto retirando determinado valor

       :param Produto: Recebe o novo valor para o estoque
       :return:
       '''
       adicionar = int(input('Quantos itens deseja adicionar no estoque?'))
       if adicionar >= 0:
           Produto.estoque -= adicionar
       else:
            print('Não é possível remover quantidade de estoque menor que 0')


if __name__ == '__main__':
    lista_prod = []
    lista_cat = ['TEC',25]
    Produto.CadastrarProduto(lista_prod,lista_cat)
    Produto.ProdutosCadastrados(lista_prod)
