from typing import TYPE_CHECKING

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///local.db"


db = SQLAlchemy(app)
# if TYPE_CHECKING:
#     from flask_sqlalchemy.model import Model
#     BaseModel = db.make_declarative_base(Model)
# else:
#     BaseModel = db.Model

BaseModel = db.Model
BaseModel.query = db.session.query_property()

class Student(BaseModel):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))

    def __init__(self, name):
        self.name = name

    

with app.app_context():
    BaseModel.metadata.create_all(db.engine)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/test")
def test():
    db.session.add(Student("John"))
    db.session.commit()

    # list all students
    students = Student.query.all()
    print(students)

    return '<p>Test</p>'
