from flask import request, Response
import jwt
from functools import wraps

from . import resultado_servico as rs
from enviroment import SECRET_KEY

def autorizado(f):
  @wraps(f)
  def decorated(*args, **kwargs):

    if 'token' in request.headers:
      token = str(request.headers['token'])
    else:
      return rs.ResultadoServico('Token inexistente ou inválido!', True).toJSON(), 403

    try:
      data = jwt.decode(token, SECRET_KEY)
    except Exception as err:
      return rs.ResultadoServico(f'Autorização negada! / {err}', True).toJSON(), 403

    return f(*args, **kwargs)

  return decorated