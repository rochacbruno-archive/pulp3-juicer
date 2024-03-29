# coding: utf-8

"""
    Pulp3 API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: v3
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class RepositoryVersionCreate(object):
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
        'add_content_units': 'list[str]',
        'remove_content_units': 'list[str]',
        'base_version': 'str'
    }

    attribute_map = {
        'add_content_units': 'add_content_units',
        'remove_content_units': 'remove_content_units',
        'base_version': 'base_version'
    }

    def __init__(self, add_content_units=None, remove_content_units=None, base_version=None):  # noqa: E501
        """RepositoryVersionCreate - a model defined in Swagger"""  # noqa: E501

        self._add_content_units = None
        self._remove_content_units = None
        self._base_version = None
        self.discriminator = None

        self.add_content_units = add_content_units
        self.remove_content_units = remove_content_units
        if base_version is not None:
            self.base_version = base_version

    @property
    def add_content_units(self):
        """Gets the add_content_units of this RepositoryVersionCreate.  # noqa: E501

        A list of content units to add to a new repository version  # noqa: E501

        :return: The add_content_units of this RepositoryVersionCreate.  # noqa: E501
        :rtype: list[str]
        """
        return self._add_content_units

    @add_content_units.setter
    def add_content_units(self, add_content_units):
        """Sets the add_content_units of this RepositoryVersionCreate.

        A list of content units to add to a new repository version  # noqa: E501

        :param add_content_units: The add_content_units of this RepositoryVersionCreate.  # noqa: E501
        :type: list[str]
        """
        if add_content_units is None:
            raise ValueError("Invalid value for `add_content_units`, must not be `None`")  # noqa: E501

        self._add_content_units = add_content_units

    @property
    def remove_content_units(self):
        """Gets the remove_content_units of this RepositoryVersionCreate.  # noqa: E501

        A list of content units to remove from the latest repository version  # noqa: E501

        :return: The remove_content_units of this RepositoryVersionCreate.  # noqa: E501
        :rtype: list[str]
        """
        return self._remove_content_units

    @remove_content_units.setter
    def remove_content_units(self, remove_content_units):
        """Sets the remove_content_units of this RepositoryVersionCreate.

        A list of content units to remove from the latest repository version  # noqa: E501

        :param remove_content_units: The remove_content_units of this RepositoryVersionCreate.  # noqa: E501
        :type: list[str]
        """
        if remove_content_units is None:
            raise ValueError("Invalid value for `remove_content_units`, must not be `None`")  # noqa: E501

        self._remove_content_units = remove_content_units

    @property
    def base_version(self):
        """Gets the base_version of this RepositoryVersionCreate.  # noqa: E501

        A repository version whose content will be used as the initial set of content for the new repository version  # noqa: E501

        :return: The base_version of this RepositoryVersionCreate.  # noqa: E501
        :rtype: str
        """
        return self._base_version

    @base_version.setter
    def base_version(self, base_version):
        """Sets the base_version of this RepositoryVersionCreate.

        A repository version whose content will be used as the initial set of content for the new repository version  # noqa: E501

        :param base_version: The base_version of this RepositoryVersionCreate.  # noqa: E501
        :type: str
        """

        self._base_version = base_version

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

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, RepositoryVersionCreate):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
