from flask import Flask
from model.session import engine
from model.diet_stats import DietStats
from sqlmodel import SQLModel
from flask_cors import CORS
from routes.diets import diet
from seed import seed_dietrec
# import seed

app = Flask(__name__)

CORS(app)

def create_tables():
    print("creating tables")
    SQLModel.metadata.create_all(engine)
    seed_dietrec()

def drop_tables():
    print("dropping tables")
    SQLModel.metadata.drop_all(engine)
    
@app.route('/')
def hello():
    return "hello" 

def register_blueprints():
    app.register_blueprint(diet)

if __name__ == "__main__":
    register_blueprints()
    create_tables()
    app.run(debug=False)
    drop_tables()