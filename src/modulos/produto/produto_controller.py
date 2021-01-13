# ESTE ARQUIVO IRÁ RECEBER OS DADOS DA REQUISIÇÃO, VALIDÁ-LOS E ENCAMINHAR PARA O SERVIÇO
# Irá instanciar um ResultadoServico apenas quando falhar na validação dos dados da requisição

from flask import request

from src.http.resultado_servico import ResultadoServico
from . import produto_service, produto_model


def listar(app):
  return produto_service.listar()


def buscarPorId(app):
  if 'id' in request.args and request.args['id'].isnumeric():
    id = int(request.values['id'])
  else:
    return ResultadoServico('Parâmetros incorretos!', True)

  return produto_service.buscarPorId(id)


def novo(app):
  if 'descricao' in request.form and not request.form['descricao'].isnumeric() and 'preco' in request.form:
    descricao = str(request.values['descricao'])
    preco = float(request.values['preco'])
  else:
    return ResultadoServico('Parâmetros incorretos!', True)

  produto = produto_model.Produto(None, descricao, preco)

  return produto_service.novo(produto)


def editar(app):
  if 'id' in request.form and request.form['id'].isnumeric() and 'descricao' in request.form and not request.form['descricao'].isnumeric() and 'preco' in request.form:
    id = int(request.form['id'])
    descricao = str(request.form['descricao'])
    preco = float(request.form['preco'])
  else:
    return ResultadoServico('Parâmetros incorretos!', True)

  produto = produto_model.Produto(id, descricao, preco)

  return produto_service.editar(produto)


def excluir(app):
  if 'id' in request.form and request.form['id'].isnumeric():
    id = int(request.form['id'])
  else:
    return ResultadoServico('Parâmetros incorretos!', True)

  return produto_service.excluir(id)