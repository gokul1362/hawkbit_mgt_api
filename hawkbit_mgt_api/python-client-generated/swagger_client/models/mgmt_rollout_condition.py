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

class MgmtRolloutCondition(object):
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
        'condition': 'str',
        'expression': 'str'
    }

    attribute_map = {
        'condition': 'condition',
        'expression': 'expression'
    }

    def __init__(self, condition=None, expression=None):  # noqa: E501
        """MgmtRolloutCondition - a model defined in Swagger"""  # noqa: E501
        self._condition = None
        self._expression = None
        self.discriminator = None
        if condition is not None:
            self.condition = condition
        if expression is not None:
            self.expression = expression

    @property
    def condition(self):
        """Gets the condition of this MgmtRolloutCondition.  # noqa: E501

        The type of the condition  # noqa: E501

        :return: The condition of this MgmtRolloutCondition.  # noqa: E501
        :rtype: str
        """
        return self._condition

    @condition.setter
    def condition(self, condition):
        """Sets the condition of this MgmtRolloutCondition.

        The type of the condition  # noqa: E501

        :param condition: The condition of this MgmtRolloutCondition.  # noqa: E501
        :type: str
        """
        allowed_values = ["THRESHOLD"]  # noqa: E501
        if condition not in allowed_values:
            raise ValueError(
                "Invalid value for `condition` ({0}), must be one of {1}"  # noqa: E501
                .format(condition, allowed_values)
            )

        self._condition = condition

    @property
    def expression(self):
        """Gets the expression of this MgmtRolloutCondition.  # noqa: E501

        The expression according to the condition, e.g. the value of threshold in percentage  # noqa: E501

        :return: The expression of this MgmtRolloutCondition.  # noqa: E501
        :rtype: str
        """
        return self._expression

    @expression.setter
    def expression(self, expression):
        """Sets the expression of this MgmtRolloutCondition.

        The expression according to the condition, e.g. the value of threshold in percentage  # noqa: E501

        :param expression: The expression of this MgmtRolloutCondition.  # noqa: E501
        :type: str
        """

        self._expression = expression

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
        if issubclass(MgmtRolloutCondition, dict):
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
        if not isinstance(other, MgmtRolloutCondition):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other