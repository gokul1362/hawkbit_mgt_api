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

class MgmtDistributionSetTypeRequestBodyPost(object):
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
        'colour': 'str',
        'name': 'str',
        'key': 'str',
        'mandatorymodules': 'list[MgmtSoftwareModuleTypeAssigment]',
        'optionalmodules': 'list[MgmtSoftwareModuleTypeAssigment]'
    }

    attribute_map = {
        'description': 'description',
        'colour': 'colour',
        'name': 'name',
        'key': 'key',
        'mandatorymodules': 'mandatorymodules',
        'optionalmodules': 'optionalmodules'
    }

    def __init__(self, description=None, colour=None, name=None, key=None, mandatorymodules=None, optionalmodules=None):  # noqa: E501
        """MgmtDistributionSetTypeRequestBodyPost - a model defined in Swagger"""  # noqa: E501
        self._description = None
        self._colour = None
        self._name = None
        self._key = None
        self._mandatorymodules = None
        self._optionalmodules = None
        self.discriminator = None
        if description is not None:
            self.description = description
        if colour is not None:
            self.colour = colour
        self.name = name
        self.key = key
        if mandatorymodules is not None:
            self.mandatorymodules = mandatorymodules
        if optionalmodules is not None:
            self.optionalmodules = optionalmodules

    @property
    def description(self):
        """Gets the description of this MgmtDistributionSetTypeRequestBodyPost.  # noqa: E501

        The description of the entity  # noqa: E501

        :return: The description of this MgmtDistributionSetTypeRequestBodyPost.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this MgmtDistributionSetTypeRequestBodyPost.

        The description of the entity  # noqa: E501

        :param description: The description of this MgmtDistributionSetTypeRequestBodyPost.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def colour(self):
        """Gets the colour of this MgmtDistributionSetTypeRequestBodyPost.  # noqa: E501

        The colour of the entity  # noqa: E501

        :return: The colour of this MgmtDistributionSetTypeRequestBodyPost.  # noqa: E501
        :rtype: str
        """
        return self._colour

    @colour.setter
    def colour(self, colour):
        """Sets the colour of this MgmtDistributionSetTypeRequestBodyPost.

        The colour of the entity  # noqa: E501

        :param colour: The colour of this MgmtDistributionSetTypeRequestBodyPost.  # noqa: E501
        :type: str
        """

        self._colour = colour

    @property
    def name(self):
        """Gets the name of this MgmtDistributionSetTypeRequestBodyPost.  # noqa: E501

        The name of the entity  # noqa: E501

        :return: The name of this MgmtDistributionSetTypeRequestBodyPost.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this MgmtDistributionSetTypeRequestBodyPost.

        The name of the entity  # noqa: E501

        :param name: The name of this MgmtDistributionSetTypeRequestBodyPost.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def key(self):
        """Gets the key of this MgmtDistributionSetTypeRequestBodyPost.  # noqa: E501

        Functional key of the distribution set type  # noqa: E501

        :return: The key of this MgmtDistributionSetTypeRequestBodyPost.  # noqa: E501
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """Sets the key of this MgmtDistributionSetTypeRequestBodyPost.

        Functional key of the distribution set type  # noqa: E501

        :param key: The key of this MgmtDistributionSetTypeRequestBodyPost.  # noqa: E501
        :type: str
        """
        if key is None:
            raise ValueError("Invalid value for `key`, must not be `None`")  # noqa: E501

        self._key = key

    @property
    def mandatorymodules(self):
        """Gets the mandatorymodules of this MgmtDistributionSetTypeRequestBodyPost.  # noqa: E501

        Mandatory module type IDs  # noqa: E501

        :return: The mandatorymodules of this MgmtDistributionSetTypeRequestBodyPost.  # noqa: E501
        :rtype: list[MgmtSoftwareModuleTypeAssigment]
        """
        return self._mandatorymodules

    @mandatorymodules.setter
    def mandatorymodules(self, mandatorymodules):
        """Sets the mandatorymodules of this MgmtDistributionSetTypeRequestBodyPost.

        Mandatory module type IDs  # noqa: E501

        :param mandatorymodules: The mandatorymodules of this MgmtDistributionSetTypeRequestBodyPost.  # noqa: E501
        :type: list[MgmtSoftwareModuleTypeAssigment]
        """

        self._mandatorymodules = mandatorymodules

    @property
    def optionalmodules(self):
        """Gets the optionalmodules of this MgmtDistributionSetTypeRequestBodyPost.  # noqa: E501

        Optional module type IDs  # noqa: E501

        :return: The optionalmodules of this MgmtDistributionSetTypeRequestBodyPost.  # noqa: E501
        :rtype: list[MgmtSoftwareModuleTypeAssigment]
        """
        return self._optionalmodules

    @optionalmodules.setter
    def optionalmodules(self, optionalmodules):
        """Sets the optionalmodules of this MgmtDistributionSetTypeRequestBodyPost.

        Optional module type IDs  # noqa: E501

        :param optionalmodules: The optionalmodules of this MgmtDistributionSetTypeRequestBodyPost.  # noqa: E501
        :type: list[MgmtSoftwareModuleTypeAssigment]
        """

        self._optionalmodules = optionalmodules

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
        if issubclass(MgmtDistributionSetTypeRequestBodyPost, dict):
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
        if not isinstance(other, MgmtDistributionSetTypeRequestBodyPost):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
