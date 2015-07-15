from flask import Blueprint, Flask, request
from flask_restful import Resource, Api

# Attach the REST Resources to a Blueprint.
blueprint = Blueprint('api', __name__)

todos = {}

class TodoSimple(Resource):
    def get(self, todo_id):
        return {todo_id: todos[todo_id]}

    def put(self, todo_id):
        todos[todo_id] = request.form['data']
        return {todo_id: todos[todo_id]}

api_bp = Api(blueprint)
api_bp.add_resource(TodoSimple, '/todo/<string:todo_id>')

app = Flask(__name__)
app.register_blueprint(blueprint)

if __name__ == '__main__':
    app.run(debug=True, port=5008)
