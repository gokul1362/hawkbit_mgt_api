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

class MgmtArtifact(object):
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
        'created_by': 'str',
        'created_at': 'int',
        'last_modified_by': 'str',
        'last_modified_at': 'int',
        'hashes': 'MgmtArtifactHash',
        'provided_filename': 'str',
        'size': 'int',
        'links': 'Links',
        'id': 'int'
    }

    attribute_map = {
        'created_by': 'createdBy',
        'created_at': 'createdAt',
        'last_modified_by': 'lastModifiedBy',
        'last_modified_at': 'lastModifiedAt',
        'hashes': 'hashes',
        'provided_filename': 'providedFilename',
        'size': 'size',
        'links': '_links',
        'id': 'id'
    }

    def __init__(self, created_by=None, created_at=None, last_modified_by=None, last_modified_at=None, hashes=None, provided_filename=None, size=None, links=None, id=None):  # noqa: E501
        """MgmtArtifact - a model defined in Swagger"""  # noqa: E501
        self._created_by = None
        self._created_at = None
        self._last_modified_by = None
        self._last_modified_at = None
        self._hashes = None
        self._provided_filename = None
        self._size = None
        self._links = None
        self._id = None
        self.discriminator = None
        if created_by is not None:
            self.created_by = created_by
        if created_at is not None:
            self.created_at = created_at
        if last_modified_by is not None:
            self.last_modified_by = last_modified_by
        if last_modified_at is not None:
            self.last_modified_at = last_modified_at
        if hashes is not None:
            self.hashes = hashes
        if provided_filename is not None:
            self.provided_filename = provided_filename
        if size is not None:
            self.size = size
        if links is not None:
            self.links = links
        if id is not None:
            self.id = id

    @property
    def created_by(self):
        """Gets the created_by of this MgmtArtifact.  # noqa: E501

        Entity was originally created by (User, AMQP-Controller, anonymous etc.)  # noqa: E501

        :return: The created_by of this MgmtArtifact.  # noqa: E501
        :rtype: str
        """
        return self._created_by

    @created_by.setter
    def created_by(self, created_by):
        """Sets the created_by of this MgmtArtifact.

        Entity was originally created by (User, AMQP-Controller, anonymous etc.)  # noqa: E501

        :param created_by: The created_by of this MgmtArtifact.  # noqa: E501
        :type: str
        """

        self._created_by = created_by

    @property
    def created_at(self):
        """Gets the created_at of this MgmtArtifact.  # noqa: E501

        Entity was originally created at (timestamp UTC in milliseconds)  # noqa: E501

        :return: The created_at of this MgmtArtifact.  # noqa: E501
        :rtype: int
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this MgmtArtifact.

        Entity was originally created at (timestamp UTC in milliseconds)  # noqa: E501

        :param created_at: The created_at of this MgmtArtifact.  # noqa: E501
        :type: int
        """

        self._created_at = created_at

    @property
    def last_modified_by(self):
        """Gets the last_modified_by of this MgmtArtifact.  # noqa: E501

        Entity was last modified by (User, AMQP-Controller, anonymous etc.)  # noqa: E501

        :return: The last_modified_by of this MgmtArtifact.  # noqa: E501
        :rtype: str
        """
        return self._last_modified_by

    @last_modified_by.setter
    def last_modified_by(self, last_modified_by):
        """Sets the last_modified_by of this MgmtArtifact.

        Entity was last modified by (User, AMQP-Controller, anonymous etc.)  # noqa: E501

        :param last_modified_by: The last_modified_by of this MgmtArtifact.  # noqa: E501
        :type: str
        """

        self._last_modified_by = last_modified_by

    @property
    def last_modified_at(self):
        """Gets the last_modified_at of this MgmtArtifact.  # noqa: E501

        Entity was last modified at (timestamp UTC in milliseconds)  # noqa: E501

        :return: The last_modified_at of this MgmtArtifact.  # noqa: E501
        :rtype: int
        """
        return self._last_modified_at

    @last_modified_at.setter
    def last_modified_at(self, last_modified_at):
        """Sets the last_modified_at of this MgmtArtifact.

        Entity was last modified at (timestamp UTC in milliseconds)  # noqa: E501

        :param last_modified_at: The last_modified_at of this MgmtArtifact.  # noqa: E501
        :type: int
        """

        self._last_modified_at = last_modified_at

    @property
    def hashes(self):
        """Gets the hashes of this MgmtArtifact.  # noqa: E501


        :return: The hashes of this MgmtArtifact.  # noqa: E501
        :rtype: MgmtArtifactHash
        """
        return self._hashes

    @hashes.setter
    def hashes(self, hashes):
        """Sets the hashes of this MgmtArtifact.


        :param hashes: The hashes of this MgmtArtifact.  # noqa: E501
        :type: MgmtArtifactHash
        """

        self._hashes = hashes

    @property
    def provided_filename(self):
        """Gets the provided_filename of this MgmtArtifact.  # noqa: E501


        :return: The provided_filename of this MgmtArtifact.  # noqa: E501
        :rtype: str
        """
        return self._provided_filename

    @provided_filename.setter
    def provided_filename(self, provided_filename):
        """Sets the provided_filename of this MgmtArtifact.


        :param provided_filename: The provided_filename of this MgmtArtifact.  # noqa: E501
        :type: str
        """

        self._provided_filename = provided_filename

    @property
    def size(self):
        """Gets the size of this MgmtArtifact.  # noqa: E501

        Size of the artifact  # noqa: E501

        :return: The size of this MgmtArtifact.  # noqa: E501
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        """Sets the size of this MgmtArtifact.

        Size of the artifact  # noqa: E501

        :param size: The size of this MgmtArtifact.  # noqa: E501
        :type: int
        """

        self._size = size

    @property
    def links(self):
        """Gets the links of this MgmtArtifact.  # noqa: E501


        :return: The links of this MgmtArtifact.  # noqa: E501
        :rtype: Links
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this MgmtArtifact.


        :param links: The links of this MgmtArtifact.  # noqa: E501
        :type: Links
        """

        self._links = links

    @property
    def id(self):
        """Gets the id of this MgmtArtifact.  # noqa: E501

        Artifact id  # noqa: E501

        :return: The id of this MgmtArtifact.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this MgmtArtifact.

        Artifact id  # noqa: E501

        :param id: The id of this MgmtArtifact.  # noqa: E501
        :type: int
        """

        self._id = id

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
        if issubclass(MgmtArtifact, dict):
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
        if not isinstance(other, MgmtArtifact):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
