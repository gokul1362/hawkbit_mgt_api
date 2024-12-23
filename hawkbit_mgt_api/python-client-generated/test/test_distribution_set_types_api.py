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
from swagger_client.api.distribution_set_types_api import DistributionSetTypesApi  # noqa: E501
from swagger_client.rest import ApiException


class TestDistributionSetTypesApi(unittest.TestCase):
    """DistributionSetTypesApi unit test stubs"""

    def setUp(self):
        self.api = DistributionSetTypesApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_add_mandatory_module(self):
        """Test case for add_mandatory_module

        Add mandatory Software Module Type to a Distribution Set Type  # noqa: E501
        """
        pass

    def test_add_optional_module(self):
        """Test case for add_optional_module

        Add optional Software Module Type to a Distribution Set Type  # noqa: E501
        """
        pass

    def test_create_distribution_set_types(self):
        """Test case for create_distribution_set_types

        Create new distribution set types  # noqa: E501
        """
        pass

    def test_delete_distribution_set_type(self):
        """Test case for delete_distribution_set_type

        Delete Distribution Set Type by Id  # noqa: E501
        """
        pass

    def test_get_distribution_set_type(self):
        """Test case for get_distribution_set_type

        Return single Distribution Set Type  # noqa: E501
        """
        pass

    def test_get_distribution_set_types(self):
        """Test case for get_distribution_set_types

        Return all Distribution Set Types  # noqa: E501
        """
        pass

    def test_get_mandatory_module(self):
        """Test case for get_mandatory_module

        Return single mandatory Software Module Type in a Distribution Set Type  # noqa: E501
        """
        pass

    def test_get_mandatory_modules(self):
        """Test case for get_mandatory_modules

        Return mandatory Software Module Types in a Distribution Set Type  # noqa: E501
        """
        pass

    def test_get_optional_module(self):
        """Test case for get_optional_module

        Return single optional Software Module Type in a Distribution Set Type  # noqa: E501
        """
        pass

    def test_get_optional_modules(self):
        """Test case for get_optional_modules

        Return optional Software Module Types in a Distribution Set Type  # noqa: E501
        """
        pass

    def test_remove_mandatory_module(self):
        """Test case for remove_mandatory_module

        Delete a mandatory module from a Distribution Set Type  # noqa: E501
        """
        pass

    def test_remove_optional_module(self):
        """Test case for remove_optional_module

        Delete an optional module from a Distribution Set Type  # noqa: E501
        """
        pass

    def test_update_distribution_set_type(self):
        """Test case for update_distribution_set_type

        Update Distribution Set Type  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
