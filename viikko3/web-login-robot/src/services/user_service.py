from entities.user import User
from repositories.user_repository import (
    user_repository as default_user_repository
)
import re


class UserInputError(Exception):
    pass


class AuthenticationError(Exception):
    pass


class UserService:
    def __init__(self, user_repository=default_user_repository):
        self._user_repository = user_repository

    def check_credentials(self, username, password):
        if not username or not password:
            raise UserInputError("Username and password are required")

        user = self._user_repository.find_by_username(username)

        if not user or user.password != password:
            raise AuthenticationError("Invalid username or password")

        return user

    def create_user(self, username, password, password_confirmation):
        self.validate(username, password, password_confirmation)

        user = self._user_repository.create(
            User(username, password)
        )

        return user

    def validate(self, username, password, password_confirmation):
        if not username or not password or not password_confirmation:
            raise UserInputError("Username and password are required")

        if len(username) < 3 or not re.match("^[a-z]+$", username):
            raise AuthenticationError("Invalid username")

        if len(password) < 8:
            raise AuthenticationError("Password too short")

        if not re.match(".*[^a-zA-Z]+.*$", password):
            raise AuthenticationError("Password doesn't contain a non-letter character")

        if not re.match(password, password_confirmation):
            raise AuthenticationError("Password and password confirmation don't match")


user_service = UserService()
