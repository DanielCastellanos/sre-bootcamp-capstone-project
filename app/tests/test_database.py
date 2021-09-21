import unittest
from modules.database import Database


class TestDatabaseMethods(unittest.TestCase):

    def setUp(self):
        self.database = Database()

    def test_get_user_by_name(self):

        username = "admin"
        db_response = self.database.get_user_by_name(username)

        self.assertTrue(db_response)

    def test_validate_user_password(self):

        valid_username = 'admin'
        valid_password = 'secret'
        is_valid = self.database.validate_user_password(
            valid_username, valid_password
        )

        self.assertTrue(is_valid)

    def test_get_role_by_username(self):

        valid_username = 'admin'
        role = self.database.get_role_by_username(valid_username)

        self.assertTrue(role in ['admin', 'viewer', 'editor'])


if __name__ == '__main__':
    unittest.main()
