import hashlib
from mysql.connector import connect
from _config import Config


class Database():

    def __init__(self):
        self.db_connection = connect(
            host=Config.DB_HOST,
            user=Config.DB_USER,
            password=Config.DB_PASSWORD,
            database=Config.DB_NAME
        )

        self.cursor = self.db_connection.cursor()

    def get_user_by_name(self, username):
        """
        Query configured database for user info.

        Args:
            param1 (`str`): the username to match in the query

        Returns:
            `tuple`: salt value, password and role of the user
        """
        self.cursor.execute(
            f"SELECT salt, password, role \
                FROM users WHERE username ='{username}';")

        return self.cursor.fetchall()

    def validate_user_password(self, username, password_from_request):
        """
        Validate user password

        Args:
            param1 (`str`): User to test password
            param2 (`str`): password to validate

        Returns:
            `bool`: True if password is valid, False otherwise
        """
        user_info = self.get_user_by_name(username)
        if user_info:
            salt = user_info[0][0]
            user_password_from_db = user_info[0][1]
            hashed_password = hashlib.sha512(
                (password_from_request+salt).encode()).hexdigest()

            return hashed_password == user_password_from_db
        return False

    def get_role_by_username(self, username):
        """
        Get role of an specific user

        Args:
            param1 (`str`): user to match the query

        Returns:
            `str`: Role name of the matched user

        """
        user_info = self.get_user_by_name(username)

        if user_info:
            return user_info[0][2]
        return False

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.cursor.close()
        self.db_connection.close()
