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

class MgmtSoftwareModuleMetadata(object):
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
        'key': 'str',
        'value': 'str',
        'target_visible': 'bool'
    }

    attribute_map = {
        'key': 'key',
        'value': 'value',
        'target_visible': 'targetVisible'
    }

    def __init__(self, key=None, value=None, target_visible=None):  # noqa: E501
        """MgmtSoftwareModuleMetadata - a model defined in Swagger"""  # noqa: E501
        self._key = None
        self._value = None
        self._target_visible = None
        self.discriminator = None
        self.key = key
        if value is not None:
            self.value = value
        if target_visible is not None:
            self.target_visible = target_visible

    @property
    def key(self):
        """Gets the key of this MgmtSoftwareModuleMetadata.  # noqa: E501

        Metadata property key  # noqa: E501

        :return: The key of this MgmtSoftwareModuleMetadata.  # noqa: E501
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """Sets the key of this MgmtSoftwareModuleMetadata.

        Metadata property key  # noqa: E501

        :param key: The key of this MgmtSoftwareModuleMetadata.  # noqa: E501
        :type: str
        """
        if key is None:
            raise ValueError("Invalid value for `key`, must not be `None`")  # noqa: E501

        self._key = key

    @property
    def value(self):
        """Gets the value of this MgmtSoftwareModuleMetadata.  # noqa: E501

        Metadata property value  # noqa: E501

        :return: The value of this MgmtSoftwareModuleMetadata.  # noqa: E501
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this MgmtSoftwareModuleMetadata.

        Metadata property value  # noqa: E501

        :param value: The value of this MgmtSoftwareModuleMetadata.  # noqa: E501
        :type: str
        """

        self._value = value

    @property
    def target_visible(self):
        """Gets the target_visible of this MgmtSoftwareModuleMetadata.  # noqa: E501

        Metadata property is visible to targets as part of software update action  # noqa: E501

        :return: The target_visible of this MgmtSoftwareModuleMetadata.  # noqa: E501
        :rtype: bool
        """
        return self._target_visible

    @target_visible.setter
    def target_visible(self, target_visible):
        """Sets the target_visible of this MgmtSoftwareModuleMetadata.

        Metadata property is visible to targets as part of software update action  # noqa: E501

        :param target_visible: The target_visible of this MgmtSoftwareModuleMetadata.  # noqa: E501
        :type: bool
        """

        self._target_visible = target_visible

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
        if issubclass(MgmtSoftwareModuleMetadata, dict):
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
        if not isinstance(other, MgmtSoftwareModuleMetadata):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other