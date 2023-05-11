import pytest
from Entidade.Categoria import Categoria

@pytest.fixture
def categoria():
    categoria = Categoria('Eletrônicos', 30.0)
    return categoria

@pytest.fixture
def lista_cat():
    lista_cat = [Categoria('Eletrônicos', 30.0), Categoria('Livros', 25.0), Categoria('Roupas', 50.0),
                 Categoria('Alimentos', 20.0), Categoria('Cosméticos', 40.0)]
    return lista_cat

def test_cadastrar_categoria(lista_cat):
    assert lista_cat[0].cat_nome == 'ELETRÔNICOS'
    assert lista_cat[0].porc_lucro == 30.0
    assert lista_cat[4].cat_nome == 'COSMÉTICOS'
    assert lista_cat[4].porc_lucro == 40.0

def test_cadastrar_categoria_limite(lista_cat):
    Categoria.CadastrarCategoria(lista_cat)
    assert len(lista_cat) == 5

def test_excluir_categoria():
    lista_cat = [Categoria('Eletrônicos', 30.0), Categoria('Livros', 25.0), Categoria('Roupas', 50.0)]
    Categoria.ExcluirCategoria(lista_cat)
    remover_item = 2
    assert len(lista_cat) == 2
    assert lista_cat[0].cat_nome == 'ELETRÔNICOS'
    assert lista_cat[1].cat_nome == 'ROUPAS'

def test_excluir_categoria_nao_encontrado():
    lista_cat = [Categoria('Eletrônicos', 30.0), Categoria('Livros', 25.0), Categoria('Roupas', 50.0)]
    Categoria.ExcluirCategoria(lista_cat, 3)
    assert len(lista_cat) == 3
