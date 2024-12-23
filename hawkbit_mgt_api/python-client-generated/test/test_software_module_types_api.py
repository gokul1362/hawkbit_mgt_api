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
from swagger_client.api.software_module_types_api import SoftwareModuleTypesApi  # noqa: E501
from swagger_client.rest import ApiException


class TestSoftwareModuleTypesApi(unittest.TestCase):
    """SoftwareModuleTypesApi unit test stubs"""

    def setUp(self):
        self.api = SoftwareModuleTypesApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_create_software_module_types(self):
        """Test case for create_software_module_types

        Creates new Software Module Types  # noqa: E501
        """
        pass

    def test_delete_software_module_type(self):
        """Test case for delete_software_module_type

        Delete Software Module Type by Id  # noqa: E501
        """
        pass

    def test_get_software_module_type(self):
        """Test case for get_software_module_type

        Return single Software Module Type  # noqa: E501
        """
        pass

    def test_get_types(self):
        """Test case for get_types

        Return all Software Module Types  # noqa: E501
        """
        pass

    def test_update_software_module_type(self):
        """Test case for update_software_module_type

        Update Software Module Type  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
