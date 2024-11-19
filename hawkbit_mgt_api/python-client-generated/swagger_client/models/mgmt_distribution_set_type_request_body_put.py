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

class MgmtDistributionSetTypeRequestBodyPut(object):
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
        'description': 'str',
        'colour': 'str'
    }

    attribute_map = {
        'description': 'description',
        'colour': 'colour'
    }

    def __init__(self, description=None, colour=None):  # noqa: E501
        """MgmtDistributionSetTypeRequestBodyPut - a model defined in Swagger"""  # noqa: E501
        self._description = None
        self._colour = None
        self.discriminator = None
        if description is not None:
            self.description = description
        if colour is not None:
            self.colour = colour

    @property
    def description(self):
        """Gets the description of this MgmtDistributionSetTypeRequestBodyPut.  # noqa: E501

        The description of the entity  # noqa: E501

        :return: The description of this MgmtDistributionSetTypeRequestBodyPut.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this MgmtDistributionSetTypeRequestBodyPut.

        The description of the entity  # noqa: E501

        :param description: The description of this MgmtDistributionSetTypeRequestBodyPut.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def colour(self):
        """Gets the colour of this MgmtDistributionSetTypeRequestBodyPut.  # noqa: E501

        The colour of the entity  # noqa: E501

        :return: The colour of this MgmtDistributionSetTypeRequestBodyPut.  # noqa: E501
        :rtype: str
        """
        return self._colour

    @colour.setter
    def colour(self, colour):
        """Sets the colour of this MgmtDistributionSetTypeRequestBodyPut.

        The colour of the entity  # noqa: E501

        :param colour: The colour of this MgmtDistributionSetTypeRequestBodyPut.  # noqa: E501
        :type: str
        """

        self._colour = colour

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
        if issubclass(MgmtDistributionSetTypeRequestBodyPut, dict):
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
        if not isinstance(other, MgmtDistributionSetTypeRequestBodyPut):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
