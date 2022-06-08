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


class Gdd(object):
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
        'crop_stage_name': 'str',
        'day_progression': 'float',
        'dd': 'float',
        'gdd': 'float',
        'season_progression': 'float'
    }

    attribute_map = {
        'crop_stage_name': 'cropStageName',
        'day_progression': 'dayProgression',
        'dd': 'dd',
        'gdd': 'gdd',
        'season_progression': 'seasonProgression'
    }

    def __init__(self, crop_stage_name=None, day_progression=None, dd=None, gdd=None, season_progression=None, _configuration=None):  # noqa: E501
        """Gdd - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._crop_stage_name = None
        self._day_progression = None
        self._dd = None
        self._gdd = None
        self._season_progression = None
        self.discriminator = None

        if crop_stage_name is not None:
            self.crop_stage_name = crop_stage_name
        if day_progression is not None:
            self.day_progression = day_progression
        if dd is not None:
            self.dd = dd
        if gdd is not None:
            self.gdd = gdd
        if season_progression is not None:
            self.season_progression = season_progression

    @property
    def crop_stage_name(self):
        """Gets the crop_stage_name of this Gdd.  # noqa: E501


        :return: The crop_stage_name of this Gdd.  # noqa: E501
        :rtype: str
        """
        return self._crop_stage_name

    @crop_stage_name.setter
    def crop_stage_name(self, crop_stage_name):
        """Sets the crop_stage_name of this Gdd.


        :param crop_stage_name: The crop_stage_name of this Gdd.  # noqa: E501
        :type: str
        """

        self._crop_stage_name = crop_stage_name

    @property
    def day_progression(self):
        """Gets the day_progression of this Gdd.  # noqa: E501


        :return: The day_progression of this Gdd.  # noqa: E501
        :rtype: float
        """
        return self._day_progression

    @day_progression.setter
    def day_progression(self, day_progression):
        """Sets the day_progression of this Gdd.


        :param day_progression: The day_progression of this Gdd.  # noqa: E501
        :type: float
        """

        self._day_progression = day_progression

    @property
    def dd(self):
        """Gets the dd of this Gdd.  # noqa: E501


        :return: The dd of this Gdd.  # noqa: E501
        :rtype: float
        """
        return self._dd

    @dd.setter
    def dd(self, dd):
        """Sets the dd of this Gdd.


        :param dd: The dd of this Gdd.  # noqa: E501
        :type: float
        """

        self._dd = dd

    @property
    def gdd(self):
        """Gets the gdd of this Gdd.  # noqa: E501


        :return: The gdd of this Gdd.  # noqa: E501
        :rtype: float
        """
        return self._gdd

    @gdd.setter
    def gdd(self, gdd):
        """Sets the gdd of this Gdd.


        :param gdd: The gdd of this Gdd.  # noqa: E501
        :type: float
        """

        self._gdd = gdd

    @property
    def season_progression(self):
        """Gets the season_progression of this Gdd.  # noqa: E501


        :return: The season_progression of this Gdd.  # noqa: E501
        :rtype: float
        """
        return self._season_progression

    @season_progression.setter
    def season_progression(self, season_progression):
        """Sets the season_progression of this Gdd.


        :param season_progression: The season_progression of this Gdd.  # noqa: E501
        :type: float
        """

        self._season_progression = season_progression

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
        if issubclass(Gdd, dict):
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
        if not isinstance(other, Gdd):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Gdd):
            return True

        return self.to_dict() != other.to_dict()
