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
from swagger_client.api.rollouts_api import RolloutsApi  # noqa: E501
from swagger_client.rest import ApiException


class TestRolloutsApi(unittest.TestCase):
    """RolloutsApi unit test stubs"""

    def setUp(self):
        self.api = RolloutsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_approve(self):
        """Test case for approve

        Approve a Rollout  # noqa: E501
        """
        pass

    def test_create(self):
        """Test case for create

        Create a new Rollout  # noqa: E501
        """
        pass

    def test_delete(self):
        """Test case for delete

        Delete a Rollout  # noqa: E501
        """
        pass

    def test_deny(self):
        """Test case for deny

        Deny a Rollout  # noqa: E501
        """
        pass

    def test_get_rollout(self):
        """Test case for get_rollout

        Return single Rollout  # noqa: E501
        """
        pass

    def test_get_rollout_group(self):
        """Test case for get_rollout_group

        Return single rollout group  # noqa: E501
        """
        pass

    def test_get_rollout_group_targets(self):
        """Test case for get_rollout_group_targets

        Return all targets related to a specific rollout group  # noqa: E501
        """
        pass

    def test_get_rollout_groups(self):
        """Test case for get_rollout_groups

        Return all rollout groups referred to a Rollout  # noqa: E501
        """
        pass

    def test_get_rollouts(self):
        """Test case for get_rollouts

        Return all Rollouts  # noqa: E501
        """
        pass

    def test_pause(self):
        """Test case for pause

        Pause a Rollout  # noqa: E501
        """
        pass

    def test_resume(self):
        """Test case for resume

        Resume a Rollout  # noqa: E501
        """
        pass

    def test_retry_rollout(self):
        """Test case for retry_rollout

        Retry a rollout  # noqa: E501
        """
        pass

    def test_start(self):
        """Test case for start

        Start a Rollout  # noqa: E501
        """
        pass

    def test_trigger_next_group(self):
        """Test case for trigger_next_group

        Force trigger processing next group of a Rollout  # noqa: E501
        """
        pass

    def test_update(self):
        """Test case for update

        Update Rollout  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
