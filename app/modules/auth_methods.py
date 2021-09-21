import jwt
from flask import Response, request
import json
from _config import Config


class Token:

    def generateToken(self, role):

        encoded_token = jwt.encode(
            {"role": role},
            Config.SIGNATURE, algorithm='HS256')

        return encoded_token

class Restricted:
    def requiere_token(wrapped_function):
        def wrapper():
            try:
                authorization = request.headers.get('Authorization')
                auth_string = authorization.split()[-1]
                decoded_token = jwt.decode(
                    auth_string,
                    Config.SIGNATURE, algorithms='HS256')

                if 'role' in decoded_token:
                    response = wrapped_function()

            except (AttributeError, jwt.DecodeError):
                # TODO: Save failed access attempt in log
                return Response(
                    json.dumps({"error": "Authentication Failed"}),
                    status=401, mimetype='application/json')

            return response
        wrapper.__name__ = wrapped_function.__name__
        return wrapper
