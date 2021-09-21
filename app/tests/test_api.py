import unittest
from api import app
from _config import Config
import json
from schema import Schema, And, Use


class TestFlaskAPI(unittest.TestCase):

    def setUp(self):
        app.testing = True
        self.app = app.test_client()
        self.headers = {'Authorization':
                        f'Bearer JWT  {Config.TOKEN}'}

        self.success_schema = Schema(And(Use(json.loads), {
            "function": str,
            "input": str,
            "output": str
        }))

        self.error_schema = Schema(And(Use(json.loads), {
            "error": str,
        }))

        self.test_values = [
            ('8', '255.0.0.0'),
            ('16', '255.255.0.0'),
            ('20', '255.255.240.0'),
            ('32', '255.255.255.255')
        ]

    def test_health_check_urls(self):
        self.assertEqual(
            self.app.get('/_health').status_code, 200)
        self.assertEqual(
            self.app.get('/').status_code, 200)

    def is_valid_schema(self, test_string):
        if 'function' in test_string:
            return self.success_schema.validate(test_string)
        elif 'error' in test_string:
            return self.error_schema.validate(test_string)
        return False

    def make_assertions(self, url, input_value, expected_response):
        """
        Use the input value to make the request to a url, and validates
        against the expected result.

        Args:
            param1(`str`): url to make the request
            param2(`str`): input value to send,
            param3(`str`): expected output from the request

        Returns:
            None
        """
        json_response = self.app.get(f'{url}?value={input_value}',
                                     headers=self.headers)
        decoded_response = json_response.data.decode()
        parsed_response = json.loads(decoded_response)

        self.assertTrue(self.is_valid_schema(decoded_response))
        self.assertEqual(
            parsed_response['output'], expected_response
        )

    def test_cidr_to_mask(self):

        for (cidr, mask) in self.test_values:
            self.make_assertions('/cidr-to-mask', cidr, mask)

    def test_mask_to_cidr(self):

        for (cidr, mask) in self.test_values:
            self.make_assertions('/mask-to-cidr', mask, cidr)

    def test_failed_access_request(self):

        for url in '/cidr-to-mask', '/mask-to-cidr':
            json_response = self.app.get(url)
            self.assertEqual(
                json_response.status_code, 401
            )
            self.assertTrue(
                self.is_valid_schema(json_response.data.decode()
                                     ))
