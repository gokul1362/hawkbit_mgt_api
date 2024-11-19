# coding: utf-8

"""
    hawkBit REST APIs

    Eclipse hawkBit™ is a domain-independent back-end framework for rolling out software updates to constrained edge devices as well as more powerful controllers and gateways connected to IP based networking infrastructure.   # noqa: E501

    OpenAPI spec version: v1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class MgmtDistributionSetStatistics(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'total_auto_assignments': 'int',
        'actions': 'dict(str, int)',
        'rollouts': 'dict(str, int)'
    }

    attribute_map = {
        'total_auto_assignments': 'totalAutoAssignments',
        'actions': 'actions',
        'rollouts': 'rollouts'
    }

    def __init__(self, total_auto_assignments=None, actions=None, rollouts=None):  # noqa: E501
        """MgmtDistributionSetStatistics - a model defined in Swagger"""  # noqa: E501
        self._total_auto_assignments = None
        self._actions = None
        self._rollouts = None
        self.discriminator = None
        if total_auto_assignments is not None:
            self.total_auto_assignments = total_auto_assignments
        if actions is not None:
            self.actions = actions
        if rollouts is not None:
            self.rollouts = rollouts

    @property
    def total_auto_assignments(self):
        """Gets the total_auto_assignments of this MgmtDistributionSetStatistics.  # noqa: E501


        :return: The total_auto_assignments of this MgmtDistributionSetStatistics.  # noqa: E501
        :rtype: int
        """
        return self._total_auto_assignments

    @total_auto_assignments.setter
    def total_auto_assignments(self, total_auto_assignments):
        """Sets the total_auto_assignments of this MgmtDistributionSetStatistics.


        :param total_auto_assignments: The total_auto_assignments of this MgmtDistributionSetStatistics.  # noqa: E501
        :type: int
        """

        self._total_auto_assignments = total_auto_assignments

    @property
    def actions(self):
        """Gets the actions of this MgmtDistributionSetStatistics.  # noqa: E501


        :return: The actions of this MgmtDistributionSetStatistics.  # noqa: E501
        :rtype: dict(str, int)
        """
        return self._actions

    @actions.setter
    def actions(self, actions):
        """Sets the actions of this MgmtDistributionSetStatistics.


        :param actions: The actions of this MgmtDistributionSetStatistics.  # noqa: E501
        :type: dict(str, int)
        """

        self._actions = actions

    @property
    def rollouts(self):
        """Gets the rollouts of this MgmtDistributionSetStatistics.  # noqa: E501


        :return: The rollouts of this MgmtDistributionSetStatistics.  # noqa: E501
        :rtype: dict(str, int)
        """
        return self._rollouts

    @rollouts.setter
    def rollouts(self, rollouts):
        """Sets the rollouts of this MgmtDistributionSetStatistics.


        :param rollouts: The rollouts of this MgmtDistributionSetStatistics.  # noqa: E501
        :type: dict(str, int)
        """

        self._rollouts = rollouts

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(MgmtDistributionSetStatistics, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, MgmtDistributionSetStatistics):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other