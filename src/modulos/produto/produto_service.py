# ESTE ARQUIVO IRÁ REALIZAR AS OPERAÇÕES (PERSISTIR NO BANCO, PROJETAR DO BANCO, CRIAR NOVO ESQUEMA NO BANCO...)

from src.http import resultado_servico as rs
from . import produto_model

# SIMULANDO A BASE DE DADOS
produtos = []
produtos.append(produto_model.Produto(1, 'TV LED Samsumg', 1600.00))
produtos.append(produto_model.Produto(2, 'Geladeira Eletrolux', 1390.99))
produtos.append(produto_model.Produto(3, 'Fogão Brastemp', 999.99))

def listar():
  try:
    return rs.ResultadoServico(produtos, False)

  except Exception as err:
    return rs.ResultadoServico(f'Erro! / {err}', True)


def buscarPorId(id):
  try:

    result = [x for x in produtos if x.id == id][0]

    return rs.ResultadoServico(result, False)

  except Exception as err:
    return rs.ResultadoServico(f'Erro! / {err}', True)


def novo(produto):
  try:

    produto.setId(produtos[-1].id + 1)
    produtos.append(produto)

    return rs.ResultadoServico('Novo produto cadastrado com sucesso!', False)

  except Exception as err:
    return rs.ResultadoServico(f'Erro! / {err}', True)


def editar(produto):
  try:

    index = produtos.index()
    produtos[index].descricao = produto.descricao
    produtos[index].preco = produto.preco

    return rs.ResultadoServico('Produto editado com sucesso!', False)

  except Exception as err:
    return rs.ResultadoServico(f'Erro! / {err}', True)


def excluir(id):
  try:

    produtos.remove([x for x in produtos if x.id == x.id][0])

    return rs.ResultadoServico('Produto excluído com sucesso!', False)

  except Exception as err:
    return rs.ResultadoServico(f'Erro! / {err}', True)