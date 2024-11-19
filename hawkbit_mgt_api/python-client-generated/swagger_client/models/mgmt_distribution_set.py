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

class MgmtDistributionSet(object):
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
        'name': 'str',
        'description': 'str',
        'version': 'str',
        'type': 'str',
        'type_name': 'str',
        'complete': 'bool',
        'locked': 'bool',
        'deleted': 'bool',
        'valid': 'bool',
        'required_migration_step': 'bool',
        'modules': 'list[MgmtSoftwareModule]',
        'links': 'Links',
        'id': 'int'
    }

    attribute_map = {
        'created_by': 'createdBy',
        'created_at': 'createdAt',
        'last_modified_by': 'lastModifiedBy',
        'last_modified_at': 'lastModifiedAt',
        'name': 'name',
        'description': 'description',
        'version': 'version',
        'type': 'type',
        'type_name': 'typeName',
        'complete': 'complete',
        'locked': 'locked',
        'deleted': 'deleted',
        'valid': 'valid',
        'required_migration_step': 'requiredMigrationStep',
        'modules': 'modules',
        'links': '_links',
        'id': 'id'
    }

    def __init__(self, created_by=None, created_at=None, last_modified_by=None, last_modified_at=None, name=None, description=None, version=None, type=None, type_name=None, complete=None, locked=None, deleted=None, valid=None, required_migration_step=None, modules=None, links=None, id=None):  # noqa: E501
        """MgmtDistributionSet - a model defined in Swagger"""  # noqa: E501
        self._created_by = None
        self._created_at = None
        self._last_modified_by = None
        self._last_modified_at = None
        self._name = None
        self._description = None
        self._version = None
        self._type = None
        self._type_name = None
        self._complete = None
        self._locked = None
        self._deleted = None
        self._valid = None
        self._required_migration_step = None
        self._modules = None
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
        self.name = name
        if description is not None:
            self.description = description
        if version is not None:
            self.version = version
        if type is not None:
            self.type = type
        if type_name is not None:
            self.type_name = type_name
        if complete is not None:
            self.complete = complete
        if locked is not None:
            self.locked = locked
        if deleted is not None:
            self.deleted = deleted
        if valid is not None:
            self.valid = valid
        if required_migration_step is not None:
            self.required_migration_step = required_migration_step
        if modules is not None:
            self.modules = modules
        if links is not None:
            self.links = links
        self.id = id

    @property
    def created_by(self):
        """Gets the created_by of this MgmtDistributionSet.  # noqa: E501

        Entity was originally created by (User, AMQP-Controller, anonymous etc.)  # noqa: E501

        :return: The created_by of this MgmtDistributionSet.  # noqa: E501
        :rtype: str
        """
        return self._created_by

    @created_by.setter
    def created_by(self, created_by):
        """Sets the created_by of this MgmtDistributionSet.

        Entity was originally created by (User, AMQP-Controller, anonymous etc.)  # noqa: E501

        :param created_by: The created_by of this MgmtDistributionSet.  # noqa: E501
        :type: str
        """

        self._created_by = created_by

    @property
    def created_at(self):
        """Gets the created_at of this MgmtDistributionSet.  # noqa: E501

        Entity was originally created at (timestamp UTC in milliseconds)  # noqa: E501

        :return: The created_at of this MgmtDistributionSet.  # noqa: E501
        :rtype: int
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this MgmtDistributionSet.

        Entity was originally created at (timestamp UTC in milliseconds)  # noqa: E501

        :param created_at: The created_at of this MgmtDistributionSet.  # noqa: E501
        :type: int
        """

        self._created_at = created_at

    @property
    def last_modified_by(self):
        """Gets the last_modified_by of this MgmtDistributionSet.  # noqa: E501

        Entity was last modified by (User, AMQP-Controller, anonymous etc.)  # noqa: E501

        :return: The last_modified_by of this MgmtDistributionSet.  # noqa: E501
        :rtype: str
        """
        return self._last_modified_by

    @last_modified_by.setter
    def last_modified_by(self, last_modified_by):
        """Sets the last_modified_by of this MgmtDistributionSet.

        Entity was last modified by (User, AMQP-Controller, anonymous etc.)  # noqa: E501

        :param last_modified_by: The last_modified_by of this MgmtDistributionSet.  # noqa: E501
        :type: str
        """

        self._last_modified_by = last_modified_by

    @property
    def last_modified_at(self):
        """Gets the last_modified_at of this MgmtDistributionSet.  # noqa: E501

        Entity was last modified at (timestamp UTC in milliseconds)  # noqa: E501

        :return: The last_modified_at of this MgmtDistributionSet.  # noqa: E501
        :rtype: int
        """
        return self._last_modified_at

    @last_modified_at.setter
    def last_modified_at(self, last_modified_at):
        """Sets the last_modified_at of this MgmtDistributionSet.

        Entity was last modified at (timestamp UTC in milliseconds)  # noqa: E501

        :param last_modified_at: The last_modified_at of this MgmtDistributionSet.  # noqa: E501
        :type: int
        """

        self._last_modified_at = last_modified_at

    @property
    def name(self):
        """Gets the name of this MgmtDistributionSet.  # noqa: E501


        :return: The name of this MgmtDistributionSet.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this MgmtDistributionSet.


        :param name: The name of this MgmtDistributionSet.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def description(self):
        """Gets the description of this MgmtDistributionSet.  # noqa: E501


        :return: The description of this MgmtDistributionSet.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this MgmtDistributionSet.


        :param description: The description of this MgmtDistributionSet.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def version(self):
        """Gets the version of this MgmtDistributionSet.  # noqa: E501

        Package version  # noqa: E501

        :return: The version of this MgmtDistributionSet.  # noqa: E501
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this MgmtDistributionSet.

        Package version  # noqa: E501

        :param version: The version of this MgmtDistributionSet.  # noqa: E501
        :type: str
        """

        self._version = version

    @property
    def type(self):
        """Gets the type of this MgmtDistributionSet.  # noqa: E501

        The type of the distribution set  # noqa: E501

        :return: The type of this MgmtDistributionSet.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this MgmtDistributionSet.

        The type of the distribution set  # noqa: E501

        :param type: The type of this MgmtDistributionSet.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def type_name(self):
        """Gets the type_name of this MgmtDistributionSet.  # noqa: E501

        The type name of the distribution set  # noqa: E501

        :return: The type_name of this MgmtDistributionSet.  # noqa: E501
        :rtype: str
        """
        return self._type_name

    @type_name.setter
    def type_name(self, type_name):
        """Sets the type_name of this MgmtDistributionSet.

        The type name of the distribution set  # noqa: E501

        :param type_name: The type_name of this MgmtDistributionSet.  # noqa: E501
        :type: str
        """

        self._type_name = type_name

    @property
    def complete(self):
        """Gets the complete of this MgmtDistributionSet.  # noqa: E501

        True of the distribution set software module setup is complete as defined by the distribution set type  # noqa: E501

        :return: The complete of this MgmtDistributionSet.  # noqa: E501
        :rtype: bool
        """
        return self._complete

    @complete.setter
    def complete(self, complete):
        """Sets the complete of this MgmtDistributionSet.

        True of the distribution set software module setup is complete as defined by the distribution set type  # noqa: E501

        :param complete: The complete of this MgmtDistributionSet.  # noqa: E501
        :type: bool
        """

        self._complete = complete

    @property
    def locked(self):
        """Gets the locked of this MgmtDistributionSet.  # noqa: E501

        If the distribution set is locked  # noqa: E501

        :return: The locked of this MgmtDistributionSet.  # noqa: E501
        :rtype: bool
        """
        return self._locked

    @locked.setter
    def locked(self, locked):
        """Sets the locked of this MgmtDistributionSet.

        If the distribution set is locked  # noqa: E501

        :param locked: The locked of this MgmtDistributionSet.  # noqa: E501
        :type: bool
        """

        self._locked = locked

    @property
    def deleted(self):
        """Gets the deleted of this MgmtDistributionSet.  # noqa: E501

        Deleted flag, used for soft deleted entities  # noqa: E501

        :return: The deleted of this MgmtDistributionSet.  # noqa: E501
        :rtype: bool
        """
        return self._deleted

    @deleted.setter
    def deleted(self, deleted):
        """Sets the deleted of this MgmtDistributionSet.

        Deleted flag, used for soft deleted entities  # noqa: E501

        :param deleted: The deleted of this MgmtDistributionSet.  # noqa: E501
        :type: bool
        """

        self._deleted = deleted

    @property
    def valid(self):
        """Gets the valid of this MgmtDistributionSet.  # noqa: E501

        True by default and false after the distribution set is invalidated by the user  # noqa: E501

        :return: The valid of this MgmtDistributionSet.  # noqa: E501
        :rtype: bool
        """
        return self._valid

    @valid.setter
    def valid(self, valid):
        """Sets the valid of this MgmtDistributionSet.

        True by default and false after the distribution set is invalidated by the user  # noqa: E501

        :param valid: The valid of this MgmtDistributionSet.  # noqa: E501
        :type: bool
        """

        self._valid = valid

    @property
    def required_migration_step(self):
        """Gets the required_migration_step of this MgmtDistributionSet.  # noqa: E501

        True if DS is a required migration step for another DS. As a result the DS’s assignment will not be cancelled when another DS is assigned (note: updatable only if DS is not yet assigned to a target)  # noqa: E501

        :return: The required_migration_step of this MgmtDistributionSet.  # noqa: E501
        :rtype: bool
        """
        return self._required_migration_step

    @required_migration_step.setter
    def required_migration_step(self, required_migration_step):
        """Sets the required_migration_step of this MgmtDistributionSet.

        True if DS is a required migration step for another DS. As a result the DS’s assignment will not be cancelled when another DS is assigned (note: updatable only if DS is not yet assigned to a target)  # noqa: E501

        :param required_migration_step: The required_migration_step of this MgmtDistributionSet.  # noqa: E501
        :type: bool
        """

        self._required_migration_step = required_migration_step

    @property
    def modules(self):
        """Gets the modules of this MgmtDistributionSet.  # noqa: E501


        :return: The modules of this MgmtDistributionSet.  # noqa: E501
        :rtype: list[MgmtSoftwareModule]
        """
        return self._modules

    @modules.setter
    def modules(self, modules):
        """Sets the modules of this MgmtDistributionSet.


        :param modules: The modules of this MgmtDistributionSet.  # noqa: E501
        :type: list[MgmtSoftwareModule]
        """

        self._modules = modules

    @property
    def links(self):
        """Gets the links of this MgmtDistributionSet.  # noqa: E501


        :return: The links of this MgmtDistributionSet.  # noqa: E501
        :rtype: Links
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this MgmtDistributionSet.


        :param links: The links of this MgmtDistributionSet.  # noqa: E501
        :type: Links
        """

        self._links = links

    @property
    def id(self):
        """Gets the id of this MgmtDistributionSet.  # noqa: E501

        The technical identifier of the entity  # noqa: E501

        :return: The id of this MgmtDistributionSet.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this MgmtDistributionSet.

        The technical identifier of the entity  # noqa: E501

        :param id: The id of this MgmtDistributionSet.  # noqa: E501
        :type: int
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

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
        if issubclass(MgmtDistributionSet, dict):
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
        if not isinstance(other, MgmtDistributionSet):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
