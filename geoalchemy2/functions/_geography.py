# -*- coding: utf-8 -*-
# flake8: noqa
from geoalchemy2 import types

_FUNCTIONS = [
    ("ST_Area", None, """Returns the area of a polygonal geometry."""),
    (
        "ST_AsBinary",
        None,
        """[gometry] Return the Well-Known Binary (WKB) representation of the geometry/geography without SRID meta data.\nOR\n[raster] Return the Well-Known Binary (WKB) representation of the raster.""",
    ),
    (
        "ST_AsEWKT",
        None,
        """Return the Well-Known Text (WKT) representation of the geometry with SRID meta data.""",
    ),
    ("ST_AsGML", None, """Return the geometry as a GML version 2 or 3 element."""),
    (
        "ST_AsGeoJSON",
        None,
        '''Return a geometry as a GeoJSON "geometry", or a row as a GeoJSON "feature"''',
    ),
    (
        "ST_AsKML",
        None,
        """Return the geometry as a KML element. Several variants. Default version=2, default maxdecimaldigits=15""",
    ),
    ("ST_AsSVG", None, """Returns SVG path data for a geometry."""),
    (
        "ST_AsText",
        None,
        """Return the Well-Known Text (WKT) representation of the geometry/geography without SRID metadata.""",
    ),
    (
        "ST_Azimuth",
        None,
        """Returns the north-based azimuth as the angle in radians measured clockwise from the vertical on pointA to pointB.""",
    ),
    (
        "ST_Buffer",
        types.Geometry,
        """(T) Returns a geometry covering all points within a given distance from the input geometry.""",
    ),
    ("ST_Centroid", types.Geometry, """Returns the geometric center of a geometry."""),
    (
        "ST_CoveredBy",
        None,
        """[geometry] Returns 1 (TRUE) if no point in Geometry/Geography A is outside Geometry/Geography B\nOR\n[raster] Return true if no points of raster rastA lie outside raster rastB.""",
    ),
    (
        "ST_Covers",
        None,
        """[geometry] Returns 1 (TRUE) if no point in Geometry B is outside Geometry A\nOR\n[raster] Return true if no points of raster rastB lie outside raster rastA.""",
    ),
    (
        "ST_DWithin",
        None,
        """[geometry] Returns true if the geometries are within the specified distance of one another. For geometry units are in those of spatial reference and for geography units are in meters and measurement is defaulted to use_spheroid=true (measure around spheroid), for faster check, use_spheroid=false to measure along sphere.\nOR\n[raster] Return true if rasters rastA and rastB are within the specified distance of each other.""",
    ),
    (
        "ST_Distance",
        None,
        """Returns the distance between two geometry or geography values.""",
    ),
    (
        "ST_GeogFromText",
        types.Geography,
        """Return a specified geography value from Well-Known Text representation or extended (WKT).""",
    ),
    (
        "ST_GeogFromWKB",
        types.Geography,
        """Creates a geography instance from a Well-Known Binary geometry representation (WKB) or extended Well Known Binary (EWKB).""",
    ),
    (
        "ST_GeographyFromText",
        types.Geography,
        """Return a specified geography value from Well-Known Text representation or extended (WKT).""",
    ),
    (
        "ST_Intersection",
        types.Geography,
        """[geometry] (T) Returns a geometry that represents the shared portion of geomA and geomB.\nOR\n[raster] Returns a raster or a set of geometry-pixelvalue pairs representing the shared portion of two rasters or the geometrical intersection of a vectorization of the raster and a geometry.""",
    ),
    (
        "ST_Intersects",
        None,
        """[geometry] Returns TRUE if the Geometries/Geography \"spatially intersect in 2D\" - (share any portion of space) and FALSE if they don't (they are Disjoint). For geography tolerance is 0.00001 meters (so any points that close are considered to intersect)\nOR\n[raster] Return true if raster rastA spatially intersects raster rastB.""",
    ),
    ("ST_Length", None, """Returns the 2D length of a linear geometry."""),
    (
        "ST_Perimeter",
        None,
        """Returns the length of the boundary of a polygonal geometry or geography.""",
    ),
    (
        "ST_Project",
        types.Geography,
        """Returns a point projected from a start point by a distance and bearing (azimuth).""",
    ),
    (
        "ST_Segmentize",
        types.Geography,
        """Return a modified geometry/geography having no segment longer than the given distance.""",
    ),
    (
        "ST_Summary",
        None,
        """[geometry] Returns a text summary of the contents of a geometry.\nOR\n[raster] Returns a text summary of the contents of the raster.""",
    ),
]
