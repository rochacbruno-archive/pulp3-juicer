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


class ManifestListTag(object):
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
        'href': 'str',
        'created': 'datetime',
        'type': 'str',
        'artifact': 'str',
        'relative_path': 'str',
        'name': 'str',
        'manifest_list': 'str'
    }

    attribute_map = {
        'href': '_href',
        'created': '_created',
        'type': '_type',
        'artifact': '_artifact',
        'relative_path': '_relative_path',
        'name': 'name',
        'manifest_list': 'manifest_list'
    }

    def __init__(self, href=None, created=None, type=None, artifact=None, relative_path=None, name=None, manifest_list=None):  # noqa: E501
        """ManifestListTag - a model defined in Swagger"""  # noqa: E501

        self._href = None
        self._created = None
        self._type = None
        self._artifact = None
        self._relative_path = None
        self._name = None
        self._manifest_list = None
        self.discriminator = None

        if href is not None:
            self.href = href
        if created is not None:
            self.created = created
        if type is not None:
            self.type = type
        self.artifact = artifact
        self.relative_path = relative_path
        self.name = name
        self.manifest_list = manifest_list

    @property
    def href(self):
        """Gets the href of this ManifestListTag.  # noqa: E501


        :return: The href of this ManifestListTag.  # noqa: E501
        :rtype: str
        """
        return self._href

    @href.setter
    def href(self, href):
        """Sets the href of this ManifestListTag.


        :param href: The href of this ManifestListTag.  # noqa: E501
        :type: str
        """

        self._href = href

    @property
    def created(self):
        """Gets the created of this ManifestListTag.  # noqa: E501

        Timestamp of creation.  # noqa: E501

        :return: The created of this ManifestListTag.  # noqa: E501
        :rtype: datetime
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this ManifestListTag.

        Timestamp of creation.  # noqa: E501

        :param created: The created of this ManifestListTag.  # noqa: E501
        :type: datetime
        """

        self._created = created

    @property
    def type(self):
        """Gets the type of this ManifestListTag.  # noqa: E501


        :return: The type of this ManifestListTag.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ManifestListTag.


        :param type: The type of this ManifestListTag.  # noqa: E501
        :type: str
        """
        if type is not None and len(type) < 1:
            raise ValueError("Invalid value for `type`, length must be greater than or equal to `1`")  # noqa: E501

        self._type = type

    @property
    def artifact(self):
        """Gets the artifact of this ManifestListTag.  # noqa: E501

        Artifact file representing the physical content  # noqa: E501

        :return: The artifact of this ManifestListTag.  # noqa: E501
        :rtype: str
        """
        return self._artifact

    @artifact.setter
    def artifact(self, artifact):
        """Sets the artifact of this ManifestListTag.

        Artifact file representing the physical content  # noqa: E501

        :param artifact: The artifact of this ManifestListTag.  # noqa: E501
        :type: str
        """
        if artifact is None:
            raise ValueError("Invalid value for `artifact`, must not be `None`")  # noqa: E501

        self._artifact = artifact

    @property
    def relative_path(self):
        """Gets the relative_path of this ManifestListTag.  # noqa: E501

        Path where the artifact is located relative to distributions base_path  # noqa: E501

        :return: The relative_path of this ManifestListTag.  # noqa: E501
        :rtype: str
        """
        return self._relative_path

    @relative_path.setter
    def relative_path(self, relative_path):
        """Sets the relative_path of this ManifestListTag.

        Path where the artifact is located relative to distributions base_path  # noqa: E501

        :param relative_path: The relative_path of this ManifestListTag.  # noqa: E501
        :type: str
        """
        if relative_path is None:
            raise ValueError("Invalid value for `relative_path`, must not be `None`")  # noqa: E501
        if relative_path is not None and len(relative_path) < 1:
            raise ValueError("Invalid value for `relative_path`, length must be greater than or equal to `1`")  # noqa: E501

        self._relative_path = relative_path

    @property
    def name(self):
        """Gets the name of this ManifestListTag.  # noqa: E501

        Tag name  # noqa: E501

        :return: The name of this ManifestListTag.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ManifestListTag.

        Tag name  # noqa: E501

        :param name: The name of this ManifestListTag.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501
        if name is not None and len(name) < 1:
            raise ValueError("Invalid value for `name`, length must be greater than or equal to `1`")  # noqa: E501

        self._name = name

    @property
    def manifest_list(self):
        """Gets the manifest_list of this ManifestListTag.  # noqa: E501

        Manifest List that is tagged  # noqa: E501

        :return: The manifest_list of this ManifestListTag.  # noqa: E501
        :rtype: str
        """
        return self._manifest_list

    @manifest_list.setter
    def manifest_list(self, manifest_list):
        """Sets the manifest_list of this ManifestListTag.

        Manifest List that is tagged  # noqa: E501

        :param manifest_list: The manifest_list of this ManifestListTag.  # noqa: E501
        :type: str
        """
        if manifest_list is None:
            raise ValueError("Invalid value for `manifest_list`, must not be `None`")  # noqa: E501

        self._manifest_list = manifest_list

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
        if not isinstance(other, ManifestListTag):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
