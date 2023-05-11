class Categoria:
   def __init__(self, cat_nome, porc_lucro):
       '''
        O método construtor cria o objeto da classe Categoria

       :param cat_nome: Recebe o nome da categoria
       :param porc_lucro: Recebe a porcentagem de lucro da categoria
       '''
       self.cat_nome = cat_nome.upper()
       self.porc_lucro = float(porc_lucro)

   def __str__(self):
       '''
       Sobrecarga no método para retornar uma string

       :return: Retorna o nome da categoria
       '''
       return f'{self.cat_nome}'

   @staticmethod
   def CadastrarCategoria(lista_cat):
       '''
       Método estático para cadastrar categorias verificando se a quantidade limite de categorias já foi cadastrada
       e se não, adiciona a categoria na lista de categorias

       :param lista_cat: Recebe as categorias cadastradas
       :return:
       '''
       if len(lista_cat)<5:
           cat_nome = input('Digite a categoria: ').upper()
           porc_lucro = float(input('Digite a porcentagem de lucro: '))
           categoria = Categoria(cat_nome,porc_lucro)
           lista_cat.append(categoria)
       else:
           print('O limite de 5 categorias cadastradas já foi atingido')

   @staticmethod
   def ExcluirCategoria(lista_cat):
       '''
       Método estático para excluir uma categoria cadastrada da lista de cartegorias, caso o item que se
       deseja excluir não esteja cadastrado, é exibida uma mensagem informando que o item não foi encontrado caso o item que se
       deseja excluir não esteja cadastrado, é exibida uma mensagem informando que o item não foi encontrado

       :param lista_cat: Lista com categorias cadastradas que sofre as alterações
       :return:
       '''
       try:
           for i,item in enumerate(lista_cat):
               print(i,'-',item)
           remover_item = int(input('Digite o índice da categoria que deseja remover: '))
           removido = lista_cat.pop(remover_item)
           print(f'{removido} foi removido da lista categoria')
       except:
           print('Categoria não foi removida pois não foi encontrado')


   def ExibirCategoria(lista_cat):
       print('Categorias cadastradas')
       for i, item in enumerate(lista_cat):
           print(i, '-', item)

if __name__ == '__main__':
    lista_cat = []
    Categoria.CadastrarCategoria(lista_cat)
    Categoria.CadastrarCategoria(lista_cat)
    Categoria.CadastrarCategoria(lista_cat)
    for item in lista_cat:
        print(item)

    # Categoria.ExcluirCategoria(lista_cat)

    Categoria.ExibirCategoria(lista_cat)