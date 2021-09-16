import os
import re

from db import db
from flask import Flask
from flask_restful import  Api
from flask_jwt import JWT

from security import authenticate, identity
from resources.user import UserRegister
from resources.item import Item, ItemList
from resources.store import Store, StoreList


uri = os.getenv("DATABASE_URL")  # or other relevant config var
if uri.startswith("postgres://"):
    uri = uri.replace("postgres://", "postgresql://", 1)
    print(uri)
app = Flask(__name__)
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_DATABASE_URI'] = (uri, 'sqlite:///data.db')
app.config['SQLALCHEMY_DATABASE_URI'] = uri
#app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get(['DATABASE_URL'])#, 'sqlite:///data.db')
#app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'sqlite:///data.db')

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False # turns off flask sqlalchemy mod tracking
app.secret_key = 'jose'
api = Api(app)


jwt = JWT(app, authenticate, identity) # /auth - new end point

api.add_resource(Store, '/store/<string:name>')  # http://127.0.0.1:5000/student/Rolf
api.add_resource(Item, '/item/<string:name>')  # http://127.0.0.1:5000/student/Rolf
api.add_resource(ItemList, '/items')
api.add_resource(StoreList, '/stores')
api.add_resource(UserRegister, '/register')

if __name__ == '__main__':
    db.init_app(app)
    app.run(port=5000, debug=True)
