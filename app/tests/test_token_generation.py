import unittest
from modules.auth_methods import Token
from _config import Config


class TestTokenMethods(unittest.TestCase):

    def setUp(self):
        self.convert = Token()
        self.test_token = Config.TOKEN

    def test_generate_token(self):
        self.assertEqual(self.test_token,
                         self.convert.generate_token('admin'))


if __name__ == '__main__':
    unittest.main()
