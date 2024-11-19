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

class ExceptionInfo(object):
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
        'exception_class': 'str',
        'error_code': 'str',
        'message': 'str',
        'parameters': 'list[str]'
    }

    attribute_map = {
        'exception_class': 'exceptionClass',
        'error_code': 'errorCode',
        'message': 'message',
        'parameters': 'parameters'
    }

    def __init__(self, exception_class=None, error_code=None, message=None, parameters=None):  # noqa: E501
        """ExceptionInfo - a model defined in Swagger"""  # noqa: E501
        self._exception_class = None
        self._error_code = None
        self._message = None
        self._parameters = None
        self.discriminator = None
        if exception_class is not None:
            self.exception_class = exception_class
        if error_code is not None:
            self.error_code = error_code
        if message is not None:
            self.message = message
        if parameters is not None:
            self.parameters = parameters

    @property
    def exception_class(self):
        """Gets the exception_class of this ExceptionInfo.  # noqa: E501


        :return: The exception_class of this ExceptionInfo.  # noqa: E501
        :rtype: str
        """
        return self._exception_class

    @exception_class.setter
    def exception_class(self, exception_class):
        """Sets the exception_class of this ExceptionInfo.


        :param exception_class: The exception_class of this ExceptionInfo.  # noqa: E501
        :type: str
        """

        self._exception_class = exception_class

    @property
    def error_code(self):
        """Gets the error_code of this ExceptionInfo.  # noqa: E501


        :return: The error_code of this ExceptionInfo.  # noqa: E501
        :rtype: str
        """
        return self._error_code

    @error_code.setter
    def error_code(self, error_code):
        """Sets the error_code of this ExceptionInfo.


        :param error_code: The error_code of this ExceptionInfo.  # noqa: E501
        :type: str
        """

        self._error_code = error_code

    @property
    def message(self):
        """Gets the message of this ExceptionInfo.  # noqa: E501


        :return: The message of this ExceptionInfo.  # noqa: E501
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this ExceptionInfo.


        :param message: The message of this ExceptionInfo.  # noqa: E501
        :type: str
        """

        self._message = message

    @property
    def parameters(self):
        """Gets the parameters of this ExceptionInfo.  # noqa: E501


        :return: The parameters of this ExceptionInfo.  # noqa: E501
        :rtype: list[str]
        """
        return self._parameters

    @parameters.setter
    def parameters(self, parameters):
        """Sets the parameters of this ExceptionInfo.


        :param parameters: The parameters of this ExceptionInfo.  # noqa: E501
        :type: list[str]
        """

        self._parameters = parameters

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
        if issubclass(ExceptionInfo, dict):
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
        if not isinstance(other, ExceptionInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
