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


class Point(object):
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
        'bbox': 'list[float]',
        'coordinates': 'list[float]',
        'type': 'str'
    }

    attribute_map = {
        'bbox': 'bbox',
        'coordinates': 'coordinates',
        'type': 'type'
    }

    def __init__(self, bbox=None, coordinates=None, type=None, _configuration=None):  # noqa: E501
        """Point - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._bbox = None
        self._coordinates = None
        self._type = None
        self.discriminator = None

        if bbox is not None:
            self.bbox = bbox
        if coordinates is not None:
            self.coordinates = coordinates
        if type is not None:
            self.type = type

    @property
    def bbox(self):
        """Gets the bbox of this Point.  # noqa: E501


        :return: The bbox of this Point.  # noqa: E501
        :rtype: list[float]
        """
        return self._bbox

    @bbox.setter
    def bbox(self, bbox):
        """Sets the bbox of this Point.


        :param bbox: The bbox of this Point.  # noqa: E501
        :type: list[float]
        """

        self._bbox = bbox

    @property
    def coordinates(self):
        """Gets the coordinates of this Point.  # noqa: E501


        :return: The coordinates of this Point.  # noqa: E501
        :rtype: list[float]
        """
        return self._coordinates

    @coordinates.setter
    def coordinates(self, coordinates):
        """Sets the coordinates of this Point.


        :param coordinates: The coordinates of this Point.  # noqa: E501
        :type: list[float]
        """

        self._coordinates = coordinates

    @property
    def type(self):
        """Gets the type of this Point.  # noqa: E501


        :return: The type of this Point.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this Point.


        :param type: The type of this Point.  # noqa: E501
        :type: str
        """

        self._type = type

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
        if issubclass(Point, dict):
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
        if not isinstance(other, Point):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Point):
            return True

        return self.to_dict() != other.to_dict()
