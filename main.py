from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/cadastrar', methods=['POST'])
def cadastrar():
  data = request.get_json()

  if data:
    nome = data.get('nome')
    senha = data.get('senha')
    email = data.get('e-mail')
    cidade = data.get('cidade')
    estado = data.get('estado')

    if email and nome and senha and cidade and estado:
      with open('usuarios.txt', 'a') as file:
        file.write(f'{email},{nome},{senha},{cidade},{estado}\n')
          
      return jsonify({'status': 'success', 'message': 'Usuário cadastrado com sucesso!'})

  return jsonify({'status': 'error', 'message': 'Dados inválidos'})

@app.route('/login', methods=['POST'])
def login():
  data = request.get_json()

  if data:
    email = data.get('e-mail')
    senha = data.get('senha')

    if email and senha:
      with open('usuarios.txt', 'r') as file:
        for linha in file:
          linha = linha.split(',')
          if linha[0] == email and linha[2] == senha:
            return jsonify({'status': 'success', 'message': 'Login efetuado com sucesso!'})

  return jsonify({'status': 'error', 'message': 'Dados inválidos'})
 
if __name__ == '__main__':
  app.run(host='0.0.0.0')