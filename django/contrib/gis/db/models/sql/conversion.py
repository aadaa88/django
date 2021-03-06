"""
This module holds simple classes to convert geospatial values from the
database.
"""

from django.contrib.gis.geometry.backend import Geometry
from django.contrib.gis.measure import Area, Distance


class BaseField(object):
    empty_strings_allowed = True


class AreaField(BaseField):
    "Wrapper for Area values."
    def __init__(self, area_att):
        self.area_att = area_att

    def from_db_value(self, value, connection):
        if value is not None:
            value = Area(**{self.area_att: value})
        return value

    def get_internal_type(self):
        return 'AreaField'


class DistanceField(BaseField):
    "Wrapper for Distance values."
    def __init__(self, distance_att):
        self.distance_att = distance_att

    def from_db_value(self, value, connection):
        if value is not None:
            value = Distance(**{self.distance_att: value})
        return value

    def get_internal_type(self):
        return 'DistanceField'


class GeomField(BaseField):
    """
    Wrapper for Geometry values.  It is a lightweight alternative to
    using GeometryField (which requires an SQL query upon instantiation).
    """
    def from_db_value(self, value, connection):
        if value is not None:
            value = Geometry(value)
        return value

    def get_internal_type(self):
        return 'GeometryField'
