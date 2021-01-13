# ESTE ARQUIVO IRÁ APENAS ENCAMINHAR A REQUISIÇÃO PARA A ROTA CORRETA

from flask import request, Response

from . import auth_controller

def aplicarRotas(app):

  @app.route('/login', methods=['POST'])
  def login(): return auth_controller.logar(app).toJSON()