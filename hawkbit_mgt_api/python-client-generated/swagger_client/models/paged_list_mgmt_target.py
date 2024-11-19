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

class PagedListMgmtTarget(object):
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
        'content': 'list[MgmtTarget]',
        'total': 'int',
        'size': 'int',
        'links': 'Links'
    }

    attribute_map = {
        'content': 'content',
        'total': 'total',
        'size': 'size',
        'links': '_links'
    }

    def __init__(self, content=None, total=None, size=None, links=None):  # noqa: E501
        """PagedListMgmtTarget - a model defined in Swagger"""  # noqa: E501
        self._content = None
        self._total = None
        self._size = None
        self._links = None
        self.discriminator = None
        self.content = content
        if total is not None:
            self.total = total
        if size is not None:
            self.size = size
        if links is not None:
            self.links = links

    @property
    def content(self):
        """Gets the content of this PagedListMgmtTarget.  # noqa: E501


        :return: The content of this PagedListMgmtTarget.  # noqa: E501
        :rtype: list[MgmtTarget]
        """
        return self._content

    @content.setter
    def content(self, content):
        """Sets the content of this PagedListMgmtTarget.


        :param content: The content of this PagedListMgmtTarget.  # noqa: E501
        :type: list[MgmtTarget]
        """
        if content is None:
            raise ValueError("Invalid value for `content`, must not be `None`")  # noqa: E501

        self._content = content

    @property
    def total(self):
        """Gets the total of this PagedListMgmtTarget.  # noqa: E501


        :return: The total of this PagedListMgmtTarget.  # noqa: E501
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        """Sets the total of this PagedListMgmtTarget.


        :param total: The total of this PagedListMgmtTarget.  # noqa: E501
        :type: int
        """

        self._total = total

    @property
    def size(self):
        """Gets the size of this PagedListMgmtTarget.  # noqa: E501


        :return: The size of this PagedListMgmtTarget.  # noqa: E501
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        """Sets the size of this PagedListMgmtTarget.


        :param size: The size of this PagedListMgmtTarget.  # noqa: E501
        :type: int
        """

        self._size = size

    @property
    def links(self):
        """Gets the links of this PagedListMgmtTarget.  # noqa: E501


        :return: The links of this PagedListMgmtTarget.  # noqa: E501
        :rtype: Links
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this PagedListMgmtTarget.


        :param links: The links of this PagedListMgmtTarget.  # noqa: E501
        :type: Links
        """

        self._links = links

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
        if issubclass(PagedListMgmtTarget, dict):
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
        if not isinstance(other, PagedListMgmtTarget):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
