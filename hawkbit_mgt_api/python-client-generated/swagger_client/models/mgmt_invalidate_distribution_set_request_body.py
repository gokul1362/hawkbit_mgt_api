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

class MgmtInvalidateDistributionSetRequestBody(object):
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
        'action_cancelation_type': 'str',
        'cancel_rollouts': 'bool'
    }

    attribute_map = {
        'action_cancelation_type': 'actionCancelationType',
        'cancel_rollouts': 'cancelRollouts'
    }

    def __init__(self, action_cancelation_type=None, cancel_rollouts=None):  # noqa: E501
        """MgmtInvalidateDistributionSetRequestBody - a model defined in Swagger"""  # noqa: E501
        self._action_cancelation_type = None
        self._cancel_rollouts = None
        self.discriminator = None
        self.action_cancelation_type = action_cancelation_type
        if cancel_rollouts is not None:
            self.cancel_rollouts = cancel_rollouts

    @property
    def action_cancelation_type(self):
        """Gets the action_cancelation_type of this MgmtInvalidateDistributionSetRequestBody.  # noqa: E501

        Type of cancelation for actions referring to the given distribution set  # noqa: E501

        :return: The action_cancelation_type of this MgmtInvalidateDistributionSetRequestBody.  # noqa: E501
        :rtype: str
        """
        return self._action_cancelation_type

    @action_cancelation_type.setter
    def action_cancelation_type(self, action_cancelation_type):
        """Sets the action_cancelation_type of this MgmtInvalidateDistributionSetRequestBody.

        Type of cancelation for actions referring to the given distribution set  # noqa: E501

        :param action_cancelation_type: The action_cancelation_type of this MgmtInvalidateDistributionSetRequestBody.  # noqa: E501
        :type: str
        """
        if action_cancelation_type is None:
            raise ValueError("Invalid value for `action_cancelation_type`, must not be `None`")  # noqa: E501
        allowed_values = ["soft", "force", "none"]  # noqa: E501
        if action_cancelation_type not in allowed_values:
            raise ValueError(
                "Invalid value for `action_cancelation_type` ({0}), must be one of {1}"  # noqa: E501
                .format(action_cancelation_type, allowed_values)
            )

        self._action_cancelation_type = action_cancelation_type

    @property
    def cancel_rollouts(self):
        """Gets the cancel_rollouts of this MgmtInvalidateDistributionSetRequestBody.  # noqa: E501

        Defines if rollouts referring to this distribution set should be canceled  # noqa: E501

        :return: The cancel_rollouts of this MgmtInvalidateDistributionSetRequestBody.  # noqa: E501
        :rtype: bool
        """
        return self._cancel_rollouts

    @cancel_rollouts.setter
    def cancel_rollouts(self, cancel_rollouts):
        """Sets the cancel_rollouts of this MgmtInvalidateDistributionSetRequestBody.

        Defines if rollouts referring to this distribution set should be canceled  # noqa: E501

        :param cancel_rollouts: The cancel_rollouts of this MgmtInvalidateDistributionSetRequestBody.  # noqa: E501
        :type: bool
        """

        self._cancel_rollouts = cancel_rollouts

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
        if issubclass(MgmtInvalidateDistributionSetRequestBody, dict):
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
        if not isinstance(other, MgmtInvalidateDistributionSetRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
