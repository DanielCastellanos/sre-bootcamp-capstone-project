from flask import Blueprint, request, Response
from modules.auth_methods import Token
from modules.database import Database
import json


login = Blueprint('auth', __name__)
token = Token()

@login.route("/login", methods=['POST'])
def url_login():
    """
    Main login function.

    Args:
        param1 (`request`): Username and password.

    Returns: 
        JWT token if credentials are valid or failed authentication
        message otherwise.
    """

    access_denied_response = Response(
        json.dumps({"error": "invalid credentials"}),
        status=401, mimetype='application/json'
        )

    try:
        username = request.form['username']
        password = request.form['password']
    except KeyError:
        return access_denied_response

    with Database() as database:
        valid_creadentials = database.validate_user_password(username, password)
        if not valid_creadentials:
            return access_denied_response
        role = database.get_role_by_username(username)

    generated_token = token.generate_token(role)
    if generated_token is not False:
        return json.dumps(
            {"data": generated_token}
        )
