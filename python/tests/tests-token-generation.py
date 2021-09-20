import unittest
from modules.auth_methods import Token
from _config import Config

class TestStringMethods(unittest.TestCase):

    def setUp(self):
        self.convert = Token()
        self.test_token = Config.TOKEN

    def test_generate_token(self):
        self.assertEqual(self.test_token,
                         self.convert.generateToken('admin'))

    # def test_access_data(self):
    #     self.assertEquals('You are under protected data',
    #                       Restricted.requiere_token(self.test_token))


if __name__ == '__main__':
    unittest.main()
