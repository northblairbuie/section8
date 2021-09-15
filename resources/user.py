import sqlite3
from flask_restful import Resource, reqparse
from models.user import UserModel

class UserRegister(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('username',
        type=str,
        required=True,
        help="this field cannot be blank."
        )
    parser.add_argument('password',
        type=str,
        required=True,
        help="this field cannot be blank."
    )

    def post(self):
        data = UserRegister.parser.parse_args()

        if UserModel.find_by_username(data['username']):
            return {"message": "A user with that username already exists."}, 401

        user = UserModel(**data) # unpack the data tuple as using a parser it will always have dict username and  dict password
        user.save_to_db()

        return {"message": "User created sucessfully."}, 201
