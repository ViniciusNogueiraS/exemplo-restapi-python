# exemplo-restapi-python

Um exemplo simples de como funciona uma aplicação REST em Python.
Responde requisições GET, POST, PUT e DELETE.
Possui rotas protegidas para uso autorizado por token de acesso.
Inseri um arquivo HTML apenas para caráter de informação.

Requisitos:
 - Python 3.9.1

Para preparar o ambiente no Windows é só clonar o repositório e executar estes comandos no console:
 - `py -3 -m venv .venv`
 - `.venv\scripts\activate`
 - `pip install flask`
 - `pip install jwt`
	
 Então é só iniciar a aplicação com `python main.py`!
