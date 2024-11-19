# coding: utf-8

"""
    hawkBit REST APIs

    Eclipse hawkBit™ is a domain-independent back-end framework for rolling out software updates to constrained edge devices as well as more powerful controllers and gateways connected to IP based networking infrastructure.   # noqa: E501

    OpenAPI spec version: v1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import unittest

import swagger_client
from swagger_client.api.basic_authentication_api import BasicAuthenticationApi  # noqa: E501
from swagger_client.rest import ApiException


class TestBasicAuthenticationApi(unittest.TestCase):
    """BasicAuthenticationApi unit test stubs"""

    def setUp(self):
        self.api = BasicAuthenticationApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_validate_basic_auth(self):
        """Test case for validate_basic_auth

        """
        pass


if __name__ == '__main__':
    unittest.main()