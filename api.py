from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restx import Api, Resource
from sqlalchemy import func 
from models import db
from models import Person, VisitOccurrence, ConditionOccurrence, DrugExposure, Concept, Death
from person import person
from visit import visit
from search_concept import search
from ask import ask
#database configuration
app = Flask(__name__) #application instance

#이곳에 접속정보 입력
h = {
    'Host': ,
    'User': ,
    'Password': ,
    'Database': ,
    'port': ,
}

uri = f'postgresql://{h["User"]}:{h["Password"]}@{h["Host"]}:{h["port"]}/{h["Database"]}'
app.config['SQLALCHEMY_DATABASE_URI'] = uri
db.init_app(app)
api = Api(app)

api.add_namespace(person, '/person')
api.add_namespace(visit, '/visit')
api.add_namespace(search, '/search')
api.add_namespace(ask, '/ask')
app.run()

# if __name__=='__main__':
#     app.run()