import jwt

class TokenCreator:
    def __init__(self, secret_key):
        self.secret_key = secret_key

    def create_token(self, payload):
        return jwt.encode(payload, self.secret_key, algorithm='HS256')
    