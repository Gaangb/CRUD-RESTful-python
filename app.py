from flask import Flask, request
from flask_restful import Resource, Api
import json

app = Flask(__name__)
api = Api(app)

alunos = [{
    'id': 0,
    'nome': 'aluno teste',
    'rg': 1122334455,
    'serie': 6,
    'turma': 'A'
}]


class Aluno(Resource):
    def get(self, id):
        try:
            response = alunos[id]
        except IndexError:
            response = {'status': 'erro', 'mensagem': 'Aluno de id {} não foi encontaro'.format(id)}
        return response

    def put(self, id):
        dados = json.loads(request.data)
        alunos[id] = dados
        return dados

    def delete(self, id):
        alunos.pop(id)
        return {'status': 'sucesso', 'menssagem': 'aluno de id {} excluido com sucesso'.format(id)}


class ListaAlunos(Resource):
    def get(self):
        return {'alunos': alunos}

    def post(self):
        dados = json.loads(request.data)
        posicao = len(alunos)
        dados['id'] = posicao
        alunos.append(dados)
        return alunos[posicao]


api.add_resource(Aluno, '/aluno/<int:id>')
api.add_resource(ListaAlunos, '/aluno')

if __name__ == '__main__':
    app.run(debug=True)
