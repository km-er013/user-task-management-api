from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)

"""
#from models import user, task

# Import models
from models.user import User
from models.task import Task


# Create the database tables
with app.app_context():
    db.create_all()

"""




# Delay the import until after db is initialized
def create_app():
    with app.app_context():
        from models.user import User
        from models.task import Task
        db.create_all()

create_app()

if __name__ == "__main__":
    app.run(debug=True)
