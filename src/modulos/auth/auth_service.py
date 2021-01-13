# ESTE ARQUIVO IRÁ REALIZAR AS OPERAÇÕES (PERSISTIR NO BANCO, PROJETAR DO BANCO, CRIAR NOVO ESQUEMA NO BANCO...)
from flask import jsonify
import jwt
import datetime

from src.http import resultado_servico as rs
from enviroment import SECRET_KEY

usuarios = [ # SIMULANDO A BASE DE DADOS
    {'id': 0,
     'login': 'Admin',
     'senha': '123'
    }
]

def logar(login, senha):
  try:

    user = [x for x in usuarios if x['login'] == login and x['senha'] == senha][0]

    if user != None:
      token = jwt.encode({'user': user, 'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=1)}, SECRET_KEY)

      return rs.ResultadoServico(token.decode("utf-8"), False)

    else:
      return rs.ResultadoServico('Login ou senha inválidos!', True)

  except Exception as err:
    return rs.ResultadoServico(f'Erro! / {err}', True)