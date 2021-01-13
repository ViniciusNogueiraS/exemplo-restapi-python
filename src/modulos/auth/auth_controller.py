# ESTE ARQUIVO IRÁ RECEBER OS DADOS DA REQUISIÇÃO, VALIDÁ-LOS E ENCAMINHAR PARA O SERVIÇO
# Irá instanciar um ResultadoServico apenas quando falhar na validação dos dados da requisição

from flask import request

from src.http.resultado_servico import ResultadoServico
from . import auth_service

def logar(app):
  if 'login' in request.form and 'senha' in request.form:
    login = str(request.form['login'])
    senha = str(request.form['senha'])
  else:
    return ResultadoServico('Erro!', True)

  return auth_service.logar(login, senha)
