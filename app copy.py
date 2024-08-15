from flask import Flask, request, jsonify
from config import Config
from models import db
from models.user import User
from models.task import Task

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)

    with app.app_context():
        # Create all tables
        db.create_all()

        # User Management Endpoints
        @app.route('/users', methods=['GET'])
        def get_users():
            users = User.query.all()
            return jsonify([{'id': user.id, 'name': user.name, 'email': user.email} for user in users])

        @app.route('/users', methods=['POST'])
        def add_user():
            data = request.get_json()
            if not data or not data.get('name') or not data.get('email'):
                return jsonify({'error': 'Name and email are required'}), 400

            new_user = User(name=data['name'], email=data['email'])
            db.session.add(new_user)
            db.session.commit()
            return jsonify({'id': new_user.id, 'name': new_user.name, 'email': new_user.email}), 201

        @app.route('/users/<int:id>', methods=['GET'])
        def get_user(id):
            user = User.query.get_or_404(id)
            return jsonify({'id': user.id, 'name': user.name, 'email': user.email})

        @app.route('/users/<int:id>', methods=['PUT'])
        def update_user(id):
            user = User.query.get_or_404(id)
            data = request.get_json()
            user.name = data.get('name', user.name)
            user.email = data.get('email', user.email)
            db.session.commit()
            return jsonify({'id': user.id, 'name': user.name, 'email': user.email})

        @app.route('/users/<int:id>', methods=['DELETE'])
        def delete_user(id):
            user = User.query.get_or_404(id)
            db.session.delete(user)
            db.session.commit()
            return '', 204

        # Task Management Endpoints
        @app.route('/tasks', methods=['GET'])
        def get_tasks():
            tasks = Task.query.all()
            return jsonify([{'id': task.id, 'title': task.title, 'description': task.description, 'completed': task.completed} for task in tasks])

        @app.route('/tasks', methods=['POST'])
        def add_task():
            data = request.get_json()
            if not data or not data.get('title') or not data.get('user_id'):
                return jsonify({'error': 'Title and user_id are required'}), 400

            new_task = Task(title=data['title'], description=data.get('description'), completed=data.get('completed', False), user_id=data['user_id'])
            db.session.add(new_task)
            db.session.commit()
            return jsonify({'id': new_task.id, 'title': new_task.title, 'description': new_task.description, 'completed': new_task.completed}), 201

        @app.route('/tasks/<int:id>', methods=['GET'])
        def get_task(id):
            task = Task.query.get_or_404(id)
            return jsonify({'id': task.id, 'title': task.title, 'description': task.description, 'completed': task.completed})

        @app.route('/tasks/<int:id>', methods=['PUT'])
        def update_task(id):
            task = Task.query.get_or_404(id)
            data = request.get_json()
            task.title = data.get('title', task.title)
            task.description = data.get('description', task.description)
            task.completed = data.get('completed', task.completed)
            db.session.commit()
            return jsonify({'id': task.id, 'title': task.title, 'description': task.description, 'completed': task.completed})

        @app.route('/tasks/<int:id>', methods=['DELETE'])
        def delete_task(id):
            task = Task.query.get_or_404(id)
            db.session.delete(task)
            db.session.commit()
            return '', 204

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
