from unittest import TestCase
from pyassert import assert_that

from . import client


class TestPurchasesResource(TestCase):

    @staticmethod
    def assert_base(response):
        assert_that(response.status_code).is_equal_to(200)
        assert_that(response.json).is_not_empty()

    def test_get(self):
        endpoint = '/purchases'
        response = client().get(endpoint)
        self.assert_base(response)

    def test_get_user_id(self):
        endpoint = '/purchases?user_id=aafebd18b22f83103aa218bb'
        response = client().get(endpoint)
        self.assert_base(response)

    def test_get_unknown_user_id(self):
        endpoint = '/purchases?user_id=fekkm35'
        response = client().get(endpoint)
        assert_that(response.status_code).is_equal_to(204)

    def test_get_wrong_key(self):
        endpoint = '/purchases?user_i=aafebd18b22f83103aa218bb'
        response = client().get(endpoint)
        self.assert_base(response)
