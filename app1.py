from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    
    db.init_app(app)

    with app.app_context():
        # Import models here to avoid circular import
        from models import user, task
        db.create_all()

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
