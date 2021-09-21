import json
import jwt
from flask import Response, request
from _config import Config


class Token:
    """ This class is for operatiions related to JWT tokens"""

    def generate_token(self, role):
        """
        Generates a JWT token.

        Args:
            param1 : user role to be added in the token body.

        Returns:
            JWT signed token
        """
        encoded_token = jwt.encode(
            {"role": role},
            Config.SIGNATURE, algorithm='HS256')

        return encoded_token

    def requiere_token(wrapped_function):
        """
        Decorator function for a flask route, to provide
        token vaidation before granting acccess to the route function.

        Args:
            param1: ´function´ to be protected

        returns:
            The execution of the input function, or acccess denied in
            case the token validation failed.
        """
        def wrapper():
            access_denied_response = Response(
                json.dumps({"error": "Authentication Failed"}),
                status=401, mimetype='application/json')
            try:
                authorization = request.headers.get('Authorization')
                request_token = authorization.split()[-1]
                decoded_token = jwt.decode(
                    request_token, Config.SIGNATURE, algorithms='HS256')

                if 'role' not in decoded_token:
                    return access_denied_response
                response = wrapped_function()

            except (AttributeError, jwt.DecodeError):
                # TODO: Save failed access attempt in log
                return access_denied_response

            return response
        wrapper.__name__ = wrapped_function.__name__
        return wrapper
