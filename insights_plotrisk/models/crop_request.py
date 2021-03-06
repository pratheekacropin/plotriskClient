# coding: utf-8

"""
    InsightsServices-Dev-QA

    SR Insight Service API Documentation  # noqa: E501

    OpenAPI spec version: 3.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from insights_plotrisk.configuration import Configuration


class CropRequest(object):
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
        'color_code': 'dict(str, str)',
        'common_names': 'list[str]',
        'id': 'str',
        'models_available': 'list[str]',
        'name': 'str',
        'properties': 'object',
        'scientific_name': 'str',
        'status': 'str',
        'variety': 'str'
    }

    attribute_map = {
        'color_code': 'colorCode',
        'common_names': 'commonNames',
        'id': 'id',
        'models_available': 'modelsAvailable',
        'name': 'name',
        'properties': 'properties',
        'scientific_name': 'scientificName',
        'status': 'status',
        'variety': 'variety'
    }

    def __init__(self, color_code=None, common_names=None, id=None, models_available=None, name=None, properties=None, scientific_name=None, status=None, variety=None, _configuration=None):  # noqa: E501
        """CropRequest - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._color_code = None
        self._common_names = None
        self._id = None
        self._models_available = None
        self._name = None
        self._properties = None
        self._scientific_name = None
        self._status = None
        self._variety = None
        self.discriminator = None

        if color_code is not None:
            self.color_code = color_code
        if common_names is not None:
            self.common_names = common_names
        if id is not None:
            self.id = id
        if models_available is not None:
            self.models_available = models_available
        if name is not None:
            self.name = name
        if properties is not None:
            self.properties = properties
        if scientific_name is not None:
            self.scientific_name = scientific_name
        if status is not None:
            self.status = status
        if variety is not None:
            self.variety = variety

    @property
    def color_code(self):
        """Gets the color_code of this CropRequest.  # noqa: E501


        :return: The color_code of this CropRequest.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._color_code

    @color_code.setter
    def color_code(self, color_code):
        """Sets the color_code of this CropRequest.


        :param color_code: The color_code of this CropRequest.  # noqa: E501
        :type: dict(str, str)
        """

        self._color_code = color_code

    @property
    def common_names(self):
        """Gets the common_names of this CropRequest.  # noqa: E501


        :return: The common_names of this CropRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._common_names

    @common_names.setter
    def common_names(self, common_names):
        """Sets the common_names of this CropRequest.


        :param common_names: The common_names of this CropRequest.  # noqa: E501
        :type: list[str]
        """

        self._common_names = common_names

    @property
    def id(self):
        """Gets the id of this CropRequest.  # noqa: E501


        :return: The id of this CropRequest.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this CropRequest.


        :param id: The id of this CropRequest.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def models_available(self):
        """Gets the models_available of this CropRequest.  # noqa: E501


        :return: The models_available of this CropRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._models_available

    @models_available.setter
    def models_available(self, models_available):
        """Sets the models_available of this CropRequest.


        :param models_available: The models_available of this CropRequest.  # noqa: E501
        :type: list[str]
        """

        self._models_available = models_available

    @property
    def name(self):
        """Gets the name of this CropRequest.  # noqa: E501


        :return: The name of this CropRequest.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CropRequest.


        :param name: The name of this CropRequest.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def properties(self):
        """Gets the properties of this CropRequest.  # noqa: E501


        :return: The properties of this CropRequest.  # noqa: E501
        :rtype: object
        """
        return self._properties

    @properties.setter
    def properties(self, properties):
        """Sets the properties of this CropRequest.


        :param properties: The properties of this CropRequest.  # noqa: E501
        :type: object
        """

        self._properties = properties

    @property
    def scientific_name(self):
        """Gets the scientific_name of this CropRequest.  # noqa: E501


        :return: The scientific_name of this CropRequest.  # noqa: E501
        :rtype: str
        """
        return self._scientific_name

    @scientific_name.setter
    def scientific_name(self, scientific_name):
        """Sets the scientific_name of this CropRequest.


        :param scientific_name: The scientific_name of this CropRequest.  # noqa: E501
        :type: str
        """

        self._scientific_name = scientific_name

    @property
    def status(self):
        """Gets the status of this CropRequest.  # noqa: E501


        :return: The status of this CropRequest.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this CropRequest.


        :param status: The status of this CropRequest.  # noqa: E501
        :type: str
        """

        self._status = status

    @property
    def variety(self):
        """Gets the variety of this CropRequest.  # noqa: E501


        :return: The variety of this CropRequest.  # noqa: E501
        :rtype: str
        """
        return self._variety

    @variety.setter
    def variety(self, variety):
        """Sets the variety of this CropRequest.


        :param variety: The variety of this CropRequest.  # noqa: E501
        :type: str
        """

        self._variety = variety

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
        if issubclass(CropRequest, dict):
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
        if not isinstance(other, CropRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CropRequest):
            return True

        return self.to_dict() != other.to_dict()
