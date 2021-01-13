from flask import Flask, render_template

app = Flask(__name__, template_folder='public')
app.config['DEBUG'] = True

@app.route('/', methods=['GET'])
def home():
  return render_template('index.html')

# Rotas
from src.modulos.produto import produto_router
from src.modulos.auth import auth_router

produto_router.aplicarRotas(app)
auth_router.aplicarRotas(app)

app.run()