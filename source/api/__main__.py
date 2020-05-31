from flask import Flask, request
from flask_restplus import Api, Resource

app = Flask(__name__)
api = Api(app)

todos = {}


@api.route('/hello')
class HelloWorld(Resource):
    def get(self):
        return 'Hello world!'


@api.route('/todos')
class Todos(Resource):
    def get(self):
        return todos


@api.route('/todos/<string:todo_id>')
class TodoSimple(Resource):
    def get(self, todo_id):
        return {todo_id: todos[todo_id]}


    def put(self, todo_id):
        todos[todo_id] = request.form['data']
        return {todo_id: todos[todo_id]}


app.run(debug=True)
