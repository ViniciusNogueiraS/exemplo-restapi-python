import json

class ResultadoServico:

  conteudo = None
  erro = False

  def __init__(self, conteudo, erro):
    self.conteudo = conteudo
    self.erro = erro
    pass

  def toJSON(self):
    return json.loads(json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=2))