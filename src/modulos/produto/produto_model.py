class Produto:

  id = None
  descricao = ''
  preco = 0.00

  def __init__(self, id, descricao, preco):
    self.id = id
    self.descricao = descricao
    self.preco = preco
    pass

  def setId(self, id):
    self.id = id