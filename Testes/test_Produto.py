import builtins

import pytest
from _pytest import monkeypatch

from Entidade.Produto import Produto

def test_CadastrarProduto(monkeypatch):
    lista_prod = []
    lista_cat = ['TEC', 25]

    def mock_input(prompt):
        if prompt == 'Digite o nome do produto: ':
            return 'Produto de Teste'
        elif prompt == 'Digite o preço do produto: ':
            return '10.0'
        elif prompt == 'Digite a quantidade de produtos em estoque: ':
            return '15'
        elif prompt == 'Digite a categoria do produto: ':
            return 'tec'
        else:
            pytest.fail(f'Entrada inesperada: {prompt}')

    monkeypatch.setattr('builtins.input', mock_input)
    Produto.CadastrarProduto(lista_prod, lista_cat)
    assert len(lista_prod) == 1


def test_ExcluirProduto(monkeypatch):
    lista_prod = []
    lista_cat = ['TEC', 25]

    def mock_input(prompt):
        if prompt == 'Digite o índice do produto que deseja remover: ':
            return '1'
        else:
            pytest.fail(f'Entrada inesperada: {prompt}')

    monkeypatch.setattr('builtins.input', mock_input)
    Produto.CadastrarProduto(lista_prod, lista_cat)
    Produto.ExcluirProduto(lista_prod)
    assert len(lista_prod) == 0

def test_AdicionarEstoque():
    p = Produto("ESTE", 10, 10, "TEC")
    Produto.AdicionarEstoque(p)
    assert p.estoque == 15

def test_RemoverEstoque():
    p = Produto("TESTE", 10, 10, "TEC")
    Produto.RemoverEstoque(p)
    assert p.estoque == 5

def test_CadastrarProduto_custo():
    lista_prod = []
    lista_cat = ['TEC', 25]
    Produto.CadastrarProduto(lista_prod, lista_cat)
    assert lista_prod[0].custo == pytest.approx(31.25, 0.01)