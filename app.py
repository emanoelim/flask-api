from flask import Flask
from flask_restful import Api
from flask_jwt import JWT
from flasgger import Swagger
from db import db

from security import authenticate, identity
from resources.user import UserRegister
from resources.item import Item, ItemList
from resources.store import Store, StoreList


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
# utilizar o flask flask sqlalchemy
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['PROPAGATE_EXCEPTIONS'] = True

app.secret_key = 'asdf'
api = Api(app)

swagger = Swagger(app)

@app.before_first_request
def create_tables():
    db.create_all()

jwt = JWT(app, authenticate, identity)

api.add_resource(UserRegister, '/register')
api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/item')
api.add_resource(Store, '/store/<string:name>')
api.add_resource(StoreList, '/store')

if __name__ == '__main__':
    db.init_app(app)
    app.run(debug=True)
