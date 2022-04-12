from flask_restful import Resource, reqparse
from user_repository import UserRepository


class UserRegister(Resource):
    user_repository = UserRepository()
    parser = reqparse.RequestParser()
    parser.add_argument('username',
                        type=str,
                        required=True,
                        help="This field cannot be left blank!"
                        )
    parser.add_argument('password',
                        type=str,
                        required=True,
                        help="This field cannot be left blank!"
                        )

    def post(self):
        data = UserRegister.parser.parse_args()
        if self.user_repository.find_by_username(data['username']):
            return {"message": "User with that username already exists."}, 400
        self.user_repository.insert(data['username'], data['password'])
        return {"message": "User created successfully."}, 201
    