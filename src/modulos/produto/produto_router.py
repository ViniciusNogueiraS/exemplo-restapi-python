# ESTE ARQUIVO IRÁ APENAS ENCAMINHAR A REQUISIÇÃO PARA A ROTA CORRETA ANOTANDO AS ROTAS QUE NECESSITAM AUTORIZAÇÃO

from . import produto_controller
from src.http.autorizacao import autorizado

def aplicarRotas(app):

  @app.route('/produtos', methods=['GET'])
  def listarProdutos(): return produto_controller.listar(app).toJSON()


  @app.route('/produto', methods=['GET'])
  def buscarPorIdProduto(): return produto_controller.buscarPorId(app).toJSON()


  @app.route('/produto', methods=['POST'])
  @autorizado
  def novoProduto(): return produto_controller.novo(app).toJSON()


  @app.route('/produto', methods=['PUT'])
  @autorizado
  def editarProduto(): return produto_controller.editar(app).toJSON()


  @app.route('/produto', methods=['DELETE'])
  @autorizado
  def excluirProduto(): return produto_controller.excluir(app).toJSON()