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


class WeatherDataRequest(object):
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
        'boundary_id': 'str',
        '_date': 'datetime',
        'gdd': 'Gdd',
        'properties': 'object',
        'status': 'str',
        'weather': 'Weather'
    }

    attribute_map = {
        'boundary_id': 'boundaryId',
        '_date': 'date',
        'gdd': 'gdd',
        'properties': 'properties',
        'status': 'status',
        'weather': 'weather'
    }

    def __init__(self, boundary_id=None, _date=None, gdd=None, properties=None, status=None, weather=None, _configuration=None):  # noqa: E501
        """WeatherDataRequest - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._boundary_id = None
        self.__date = None
        self._gdd = None
        self._properties = None
        self._status = None
        self._weather = None
        self.discriminator = None

        if boundary_id is not None:
            self.boundary_id = boundary_id
        if _date is not None:
            self._date = _date
        if gdd is not None:
            self.gdd = gdd
        if properties is not None:
            self.properties = properties
        if status is not None:
            self.status = status
        if weather is not None:
            self.weather = weather

    @property
    def boundary_id(self):
        """Gets the boundary_id of this WeatherDataRequest.  # noqa: E501


        :return: The boundary_id of this WeatherDataRequest.  # noqa: E501
        :rtype: str
        """
        return self._boundary_id

    @boundary_id.setter
    def boundary_id(self, boundary_id):
        """Sets the boundary_id of this WeatherDataRequest.


        :param boundary_id: The boundary_id of this WeatherDataRequest.  # noqa: E501
        :type: str
        """

        self._boundary_id = boundary_id

    @property
    def _date(self):
        """Gets the _date of this WeatherDataRequest.  # noqa: E501


        :return: The _date of this WeatherDataRequest.  # noqa: E501
        :rtype: datetime
        """
        return self.__date

    @_date.setter
    def _date(self, _date):
        """Sets the _date of this WeatherDataRequest.


        :param _date: The _date of this WeatherDataRequest.  # noqa: E501
        :type: datetime
        """

        self.__date = _date

    @property
    def gdd(self):
        """Gets the gdd of this WeatherDataRequest.  # noqa: E501


        :return: The gdd of this WeatherDataRequest.  # noqa: E501
        :rtype: Gdd
        """
        return self._gdd

    @gdd.setter
    def gdd(self, gdd):
        """Sets the gdd of this WeatherDataRequest.


        :param gdd: The gdd of this WeatherDataRequest.  # noqa: E501
        :type: Gdd
        """

        self._gdd = gdd

    @property
    def properties(self):
        """Gets the properties of this WeatherDataRequest.  # noqa: E501


        :return: The properties of this WeatherDataRequest.  # noqa: E501
        :rtype: object
        """
        return self._properties

    @properties.setter
    def properties(self, properties):
        """Sets the properties of this WeatherDataRequest.


        :param properties: The properties of this WeatherDataRequest.  # noqa: E501
        :type: object
        """

        self._properties = properties

    @property
    def status(self):
        """Gets the status of this WeatherDataRequest.  # noqa: E501


        :return: The status of this WeatherDataRequest.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this WeatherDataRequest.


        :param status: The status of this WeatherDataRequest.  # noqa: E501
        :type: str
        """

        self._status = status

    @property
    def weather(self):
        """Gets the weather of this WeatherDataRequest.  # noqa: E501


        :return: The weather of this WeatherDataRequest.  # noqa: E501
        :rtype: Weather
        """
        return self._weather

    @weather.setter
    def weather(self, weather):
        """Sets the weather of this WeatherDataRequest.


        :param weather: The weather of this WeatherDataRequest.  # noqa: E501
        :type: Weather
        """

        self._weather = weather

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
        if issubclass(WeatherDataRequest, dict):
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
        if not isinstance(other, WeatherDataRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, WeatherDataRequest):
            return True

        return self.to_dict() != other.to_dict()
