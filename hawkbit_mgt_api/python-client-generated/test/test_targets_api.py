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
from swagger_client.api.targets_api import TargetsApi  # noqa: E501
from swagger_client.rest import ApiException


class TestTargetsApi(unittest.TestCase):
    """TargetsApi unit test stubs"""

    def setUp(self):
        self.api = TargetsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_activate_auto_confirm(self):
        """Test case for activate_auto_confirm

        Activate auto-confirm on a specific target  # noqa: E501
        """
        pass

    def test_assign_target_type(self):
        """Test case for assign_target_type

        Assign target type to a target  # noqa: E501
        """
        pass

    def test_cancel_action(self):
        """Test case for cancel_action

        Cancel action for a specific target  # noqa: E501
        """
        pass

    def test_create_metadata(self):
        """Test case for create_metadata

        Create a list of meta data for a specific target  # noqa: E501
        """
        pass

    def test_create_targets(self):
        """Test case for create_targets

        Create target(s)  # noqa: E501
        """
        pass

    def test_deactivate_auto_confirm(self):
        """Test case for deactivate_auto_confirm

        Deactivate auto-confirm on a specific target  # noqa: E501
        """
        pass

    def test_delete_metadata(self):
        """Test case for delete_metadata

        Deletes a single meta data entry from a target  # noqa: E501
        """
        pass

    def test_delete_target(self):
        """Test case for delete_target

        Delete target by id  # noqa: E501
        """
        pass

    def test_get_action(self):
        """Test case for get_action

        Return action by id of a specific target  # noqa: E501
        """
        pass

    def test_get_action_history(self):
        """Test case for get_action_history

        Return actions for a specific target  # noqa: E501
        """
        pass

    def test_get_action_status_list(self):
        """Test case for get_action_status_list

        Return status of a specific action on a specific target  # noqa: E501
        """
        pass

    def test_get_assigned_distribution_set(self):
        """Test case for get_assigned_distribution_set

        Return the assigned distribution set of a specific target  # noqa: E501
        """
        pass

    def test_get_attributes(self):
        """Test case for get_attributes

        Return attributes of a specific target  # noqa: E501
        """
        pass

    def test_get_auto_confirm_status(self):
        """Test case for get_auto_confirm_status

        Return the current auto-confitm state for a specific target  # noqa: E501
        """
        pass

    def test_get_installed_distribution_set(self):
        """Test case for get_installed_distribution_set

        Return installed distribution set of a specific target  # noqa: E501
        """
        pass

    def test_get_metadata(self):
        """Test case for get_metadata

        Return metadata for specific target  # noqa: E501
        """
        pass

    def test_get_metadata_value(self):
        """Test case for get_metadata_value

        Return single metadata value for a specific key of a target  # noqa: E501
        """
        pass

    def test_get_tags(self):
        """Test case for get_tags

        Return tags for specific target  # noqa: E501
        """
        pass

    def test_get_target(self):
        """Test case for get_target

        Return target by id  # noqa: E501
        """
        pass

    def test_get_targets(self):
        """Test case for get_targets

        Return all targets  # noqa: E501
        """
        pass

    def test_post_assigned_distribution_set(self):
        """Test case for post_assigned_distribution_set

        Assigns a distribution set to a specific target  # noqa: E501
        """
        pass

    def test_unassign_target_type(self):
        """Test case for unassign_target_type

        Unassign target type from target.  # noqa: E501
        """
        pass

    def test_update_action(self):
        """Test case for update_action

        Switch an action from soft to forced  # noqa: E501
        """
        pass

    def test_update_metadata(self):
        """Test case for update_metadata

        Updates a single meta data value of a target  # noqa: E501
        """
        pass

    def test_update_target(self):
        """Test case for update_target

        Update target by id  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
