from typing import Any
from typing import List

from geoalchemy2.types import Geography
from geoalchemy2.types import Geometry
from geoalchemy2.types import GeomVal
from geoalchemy2.types import Raster
from geoalchemy2.types import SummaryStats

_FUNCTIONS = {
    "ST_3DClosestPoint": {
        (Geometry, Geometry): {
            "inst": Geometry,
            "type_hint": Geometry,
            "description": "args: g1, g2 - Returns the 3D point on g1 that is closest to g2. This is the first point of the 3D shortest line.",
            "doc_url": "https://postgis.net/docs/ST_3DClosestPoint.html",
        }
    },
    "ST_3DDFullyWithin": {
        (Geometry, Geometry, float): {
            "inst": bool,
            "type_hint": bool,
            "description": "None",
            "doc_url": "https://postgis.net/docs/ST_3DDFullyWithin.html",
        }
    },
    "ST_3DDWithin": {
        (Geometry, Geometry, float): {
            "inst": bool,
            "type_hint": bool,
            "description": "None",
            "doc_url": "https://postgis.net/docs/ST_3DDWithin.html",
        }
    },
    "ST_3DDistance": {
        (Geometry, Geometry): {
            "inst": float,
            "type_hint": float,
            "description": "args: g1, g2 - Returns the 3D cartesian minimum distance (based on spatial ref) between two geometries in projected units.",
            "doc_url": "https://postgis.net/docs/ST_3DDistance.html",
        }
    },
    "ST_3DExtent": {
        (Geometry,): {
            "inst": Geometry,
            "type_hint": Geometry,
            "description": "args: geomfield - Aggregate function that returns the 3D bounding box of geometries.",
            "doc_url": "https://postgis.net/docs/ST_3DExtent.html",
        }
    },
    "ST_3DIntersects": {
        (Geometry, Geometry): {
            "inst": bool,
            "type_hint": bool,
            "description": "None",
            "doc_url": "https://postgis.net/docs/ST_3DIntersects.html",
        }
    },
    "ST_3DLength": {
        (Geometry,): {
            "inst": float,
            "type_hint": float,
            "description": "args: a_3dlinestring - Returns the 3D length of a linear geometry.",
            "doc_url": "https://postgis.net/docs/ST_3DLength.html",
        }
    },
    "ST_3DLineInterpolatePoint": {
        (Geometry, float): {
            "inst": Geometry,
            "type_hint": Geometry,
            "description": "args: a_linestring, a_fraction - Returns a point interpolated along a 3D line at a fractional location.",
            "doc_url": "https://postgis.net/docs/ST_3DLineInterpolatePoint.html",
        }
    },
    "ST_3DLongestLine": {
        (Geometry, Geometry): {
            "inst": Geometry,
            "type_hint": Geometry,
            "description": "args: g1, g2 - Returns the 3D longest line between two geometries",
            "doc_url": "https://postgis.net/docs/ST_3DLongestLine.html",
        }
    },
    "ST_3DMakeBox": {
        (Geometry, Geometry): {
            "inst": Geometry,
            "type_hint": Geometry,
            "description": "args: point3DLowLeftBottom, point3DUpRightTop - Creates a BOX3D defined by two 3D point geometries.",
            "doc_url": "https://postgis.net/docs/ST_3DMakeBox.html",
        }
    },
    "ST_3DMaxDistance": {
        (Geometry, Geometry): {
            "inst": float,
            "type_hint": float,
            "description": "args: g1, g2 - Returns the 3D cartesian maximum distance (based on spatial ref) between two geometries in projected units.",
            "doc_url": "https://postgis.net/docs/ST_3DMaxDistance.html",
        }
    },
    "ST_3DPerimeter": {
        (Geometry,): {
            "inst": float,
            "type_hint": float,
            "description": "args: geomA - Returns the 3D perimeter of a polygonal geometry.",
            "doc_url": "https://postgis.net/docs/ST_3DPerimeter.html",
        }
    },
    "ST_3DShortestLine": {
        (Geometry, Geometry): {
            "inst": Geometry,
            "type_hint": Geometry,
            "description": "args: g1, g2 - Returns the 3D shortest line between two geometries",
            "doc_url": "https://postgis.net/docs/ST_3DShortestLine.html",
        }
    },
    "ST_AddBand": {
        (Raster, List[Any]): {
            "inst": Raster,
            "type_hint": Raster,
            "description": "args: rast, addbandargset - Returns a raster with the new band(s) of given type added with given initial value in the given index location. If no index is specified, the band is added to the end.",
            "doc_url": "https://postgis.net/docs/ST_AddBand.html",
        },
        (Raster, int, str, float, float): {
            "inst": Raster,
            "type_hint": Raster,
            "description": "args: rast, index, pixeltype, initialvalue=0, nodataval=NULL - Returns a raster with the new band(s) of given type added with given initial value in the given index location. If no index is specified, the band is added to the end.",
            "doc_url": "https://postgis.net/docs/ST_AddBand.html",
        },
        (Raster, str, float, float): {
            "inst": Raster,
            "type_hint": Raster,
            "description": "args: rast, pixeltype, initialvalue=0, nodataval=NULL - Returns a raster with the new band(s) of given type added with given initial value in the given index location. If no index is specified, the band is added to the end.",
            "doc_url": "https://postgis.net/docs/ST_AddBand.html",
        },
        (Raster, Raster, int, int): {
            "inst": Raster,
            "type_hint": Raster,
            "description": "args: torast, fromrast, fromband=1, torastindex=at_end - Returns a raster with the new band(s) of given type added with given initial value in the given index location. If no index is specified, the band is added to the end.",
            "doc_url": "https://postgis.net/docs/ST_AddBand.html",
        },
        (Raster, List[Raster], int, int): {
            "inst": Raster,
            "type_hint": Raster,
            "description": "args: torast, fromrasts, fromband=1, torastindex=at_end - Returns a raster with the new band(s) of given type added with given initial value in the given index location. If no index is specified, the band is added to the end.",
            "doc_url": "https://postgis.net/docs/ST_AddBand.html",
        },
        (Raster, int, str, List[int], float): {
            "inst": Raster,
            "type_hint": Raster,
            "description": "args: rast, index, outdbfile, outdbindex, nodataval=NULL - Returns a raster with the new band(s) of given type added with given initial value in the given index location. If no index is specified, the band is added to the end.",
            "doc_url": "https://postgis.net/docs/ST_AddBand.html",
        },
        (Raster, str, List[int], int, float): {
            "inst": Raster,
            "type_hint": Raster,
            "description": "args: rast, outdbfile, outdbindex, index=at_end, nodataval=NULL - Returns a raster with the new band(s) of given type added with given initial value in the given index location. If no index is specified, the band is added to the end.",
            "doc_url": "https://postgis.net/docs/ST_AddBand.html",
        },
    },
    "ST_AddMeasure": {
        (Geometry, float, float): {
            "inst": Geometry,
            "type_hint": Geometry,
            "description": "args: geom_mline, measure_start, measure_end - Interpolates measures along a linear geometry.",
            "doc_url": "https://postgis.net/docs/ST_AddMeasure.html",
        }
    },
    "ST_AddPoint": {
        (Geometry, Geometry): {
            "inst": Geometry,
            "type_hint": Geometry,
            "description": "args: linestring, point - Add a point to a LineString.",
            "doc_url": "https://postgis.net/docs/ST_AddPoint.html",
        },
        (Geometry, Geometry, int): {
            "inst": Geometry,
            "type_hint": Geometry,
            "description": "args: linestring, point, position = -1 - Add a point to a LineString.",
            "doc_url": "https://postgis.net/docs/ST_AddPoint.html",
        },
    },
    "ST_Affine": {
        (
            Geometry,
            float,
            float,
            float,
            float,
            float,
            float,
            float,
            float,
            float,
            float,
            float,
            float,
        ): {
            "inst": Geometry,
            "type_hint": Geometry,
            "description": "args: geomA, a, b, c, d, e, f, g, h, i, xoff, yoff, zoff - Apply a 3D affine transformation to a geometry.",
            "doc_url": "https://postgis.net/docs/ST_Affine.html",
        },
        (Geometry, float, float, float, float, float, float): {
            "inst": Geometry,
            "type_hint": Geometry,
            "description": "args: geomA, a, b, d, e, xoff, yoff - Apply a 3D affine transformation to a geometry.",
            "doc_url": "https://postgis.net/docs/ST_Affine.html",
        },
    },
    "ST_Angle": {
        (Geometry, Geometry, Geometry, Geometry): {
            "inst": float,
            "type_hint": float,
            "description": "args: point1, point2, point3, point4 - Returns the angle between two vectors defined by 3 or 4 points, or 2 lines.",
            "doc_url": "https://postgis.net/docs/ST_Angle.html",
        },
        (Geometry, Geometry): {
            "inst": float,
            "type_hint": float,
            "description": "args: line1, line2 - Returns the angle between two vectors defined by 3 or 4 points, or 2 lines.",
            "doc_url": "https://postgis.net/docs/ST_Angle.html",
        },
    },
    "ST_ApproxCount": {
        (Raster, int, bool, float): {
            "inst": int,
            "type_hint": int,
            "description": "None",
            "doc_url": "https://postgis.net/docs/ST_ApproxCount.html",
        },
        (Raster, int, float): {
            "inst": int,
            "type_hint": int,
            "description": "None",
            "doc_url": "https://postgis.net/docs/ST_ApproxCount.html",
        },
        (Raster, bool, float): {
            "inst": int,
            "type_hint": int,
            "description": "None",
            "doc_url": "https://postgis.net/docs/ST_ApproxCount.html",
        },
        (Raster, float): {
            "inst": int,
            "type_hint": int,
            "description": "None",
            "doc_url": "https://postgis.net/docs/ST_ApproxCount.html",
        },
    },
    "ST_ApproxHistogram": {
        (Raster, int, bool, float, int, List[float], bool, float, float, int, float): {
            "inst": object,
            "type_hint": List[Any],
            "description": "None",
            "doc_url": "https://postgis.net/docs/ST_ApproxHistogram.html",
        },
        (Raster, int, bool, float, int, bool, float, float, int, float): {
            "inst": object,
            "type_hint": List[Any],
            "description": "None",
            "doc_url": "https://postgis.net/docs/ST_ApproxHistogram.html",
        },
        (Raster, int, float, float, float, int, float): {
            "inst": object,
            "type_hint": List[Any],
            "description": "None",
            "doc_url": "https://postgis.net/docs/ST_ApproxHistogram.html",
        },
        (Raster, float, float, float, int, float): {
            "inst": object,
            "type_hint": List[Any],
            "description": "None",
            "doc_url": "https://postgis.net/docs/ST_ApproxHistogram.html",
        },
        (Raster, int, float, int, List[float], bool, float, float, int, float): {
            "inst": object,
            "type_hint": List[Any],
            "description": "None",
            "doc_url": "https://postgis.net/docs/ST_ApproxHistogram.html",
        },
        (Raster, int, float, int, bool, float, float, int, float): {
            "inst": object,
            "type_hint": List[Any],
            "description": "None",
            "doc_url": "https://postgis.net/docs/ST_ApproxHistogram.html",
        },
    },
    "ST_ApproxQuantile": {
        (Raster, int, bool, float, List[float], float, float): {
            "inst": object,
            "type_hint": List[Any],
            "description": "None",
            "doc_url": "https://postgis.net/docs/ST_ApproxQuantile.html",
        },
        (Raster, int, float, List[float], float, float): {
            "inst": object,
            "type_hint": List[Any],
            "description": "None",
            "doc_url": "https://postgis.net/docs/ST_ApproxQuantile.html",
        },
        (Raster, float, List[float], float, float): {
            "inst": object,
            "type_hint": List[Any],
            "description": "None",
            "doc_url": "https://postgis.net/docs/ST_ApproxQuantile.html",
        },
        (Raster, List[float], float, float): {
            "inst": object,
            "type_hint": List[Any],
            "description": "None",
            "doc_url": "https://postgis.net/docs/ST_ApproxQuantile.html",
        },
        (Raster, int, bool, float, float): {
            "inst": float,
            "type_hint": float,
            "description": "None",
            "doc_url": "https://postgis.net/docs/ST_ApproxQuantile.html",
        },
        (Raster, int, float, float): {
            "inst": float,
            "type_hint": float,
            "description": "None",
            "doc_url": "https://postgis.net/docs/ST_ApproxQuantile.html",
        },
        (Raster, float, float): {
            "inst": float,
            "type_hint": float,
            "description": "None",
            "doc_url": "https://postgis.net/docs/ST_ApproxQuantile.html",
        },
        (Raster, bool, float): {
            "inst": float,
            "type_hint": float,
            "description": "None",
            "doc_url": "https://postgis.net/docs/ST_ApproxQuantile.html",
        },
        (Raster, float): {
            "inst": float,
            "type_hint": float,
            "description": "None",
            "doc_url": "https://postgis.net/docs/ST_ApproxQuantile.html",
        },
    },
    "ST_ApproxSummarystats": {
        (Raster, float): {
            "inst": SummaryStats,
            "type_hint": SummaryStats,
            "description": "None",
            "doc_url": "https://postgis.net/docs/ST_ApproxSummarystats.html",
        },
        (Raster, int, bool, float): {
            "inst": SummaryStats,
            "type_hint": SummaryStats,
            "description": "None",
            "doc_url": "https://postgis.net/docs/ST_ApproxSummarystats.html",
        },
        (Raster, int, float): {
            "inst": SummaryStats,
            "type_hint": SummaryStats,
            "description": "None",
            "doc_url": "https://postgis.net/docs/ST_ApproxSummarystats.html",
        },
        (Raster, bool, float): {
            "inst": SummaryStats,
            "type_hint": SummaryStats,
            "description": "None",
            "doc_url": "https://postgis.net/docs/ST_ApproxSummarystats.html",
        },
    },
    "ST_Area": {
        (Geometry,): {
            "inst": float,
            "type_hint": float,
            "description": "args: g1 - Returns the area of a polygonal geometry.",
            "doc_url": "https://postgis.net/docs/ST_Area.html",
        },
        (Geography, bool): {
            "inst": float,
            "type_hint": float,
            "description": "args: geog, use_spheroid = true - Returns the area of a polygonal geometry.",
            "doc_url": "https://postgis.net/docs/ST_Area.html",
        },
        (str,): {
            "inst": float,
            "type_hint": float,
            "description": "None",
            "doc_url": "https://postgis.net/docs/ST_Area.html",
        },
    },
    "ST_AsBinary": {
        (Geometry, str): {
            "inst": bytes,
            "type_hint": bytes,
            "description": "None",
            "doc_url": "https://postgis.net/docs/ST_AsBinary.html",
        },
        (Geometry,): {
            "inst": bytes,
            "type_hint": bytes,
            "description": "None",
            "doc_url": "https://postgis.net/docs/ST_AsBinary.html",
        },
        (Geography,): {
            "inst": bytes,
            "type_hint": bytes,
            "description": "None",
            "doc_url": "https://postgis.net/docs/ST_AsBinary.html",
        },
        (Geography, str): {
            "inst": bytes,
            "type_hint": bytes,
            "description": "None",
            "doc_url": "https://postgis.net/docs/ST_AsBinary.html",
        },
        (Raster, bool): {
            "inst": bytes,
            "type_hint": bytes,
            "description": "args: rast, outasin=FALSE - Return the Well-Known Binary (WKB) representation of the raster.",
            "doc_url": "https://postgis.net/docs/ST_AsBinary.html",
        },
    },
    "ST_AsEWKB": {
        (Geometry,): {
            "inst": bytes,
            "type_hint": bytes,
            "description": "None",
            "doc_url": "https://postgis.net/docs/ST_AsEWKB.html",
        },
        (Geometry, str): {
            "inst": bytes,
            "type_hint": bytes,
            "description": "None",
            "doc_url": "https://postgis.net/docs/ST_AsEWKB.html",
        },
    },
    "ST_AsEWKT": {
        (Geometry,): {
            "inst": str,
            "type_hint": str,
            "description": "None",
            "doc_url": "https://postgis.net/docs/ST_AsEWKT.html",
        },
        (Geometry, int): {
            "inst": str,
            "type_hint": str,
            "description": "None",
            "doc_url": "https://postgis.net/docs/ST_AsEWKT.html",
        },
        (Geography,): {
            "inst": str,
            "type_hint": str,
            "description": "None",
            "doc_url": "https://postgis.net/docs/ST_AsEWKT.html",
        },
        (Geography, int): {
            "inst": str,
            "type_hint": str,
            "description": "None",
            "doc_url": "https://postgis.net/docs/ST_AsEWKT.html",
        },
        (str,): {
            "inst": str,
            "type_hint": str,
            "description": "None",
            "doc_url": "https://postgis.net/docs/ST_AsEWKT.html",
        },
    },
    "ST_AsEncodedPolyline": {
        (Geometry, int): {
            "inst": str,
            "type_hint": str,
            "description": "None",
            "doc_url": "https://postgis.net/docs/ST_AsEncodedPolyline.html",
        }
    },
    "ST_AsFlatGeobuf": {
        (Any,): {
            "inst": bytes,
            "type_hint": bytes,
            "description": "None",
            "doc_url": "https://postgis.net/docs/ST_AsFlatGeobuf.html",
        },
        (Any, bool): {
            "inst": bytes,
            "type_hint": bytes,
            "description": "None",
            "doc_url": "https://postgis.net/docs/ST_AsFlatGeobuf.html",
        },
        (Any, bool, str): {
            "inst": bytes,
            "type_hint": bytes,
            "description": "None",
            "doc_url": "https://postgis.net/docs/ST_AsFlatGeobuf.html",
        },
    },
    "ST_AsGDALRaster": {
        (Raster, str, List[str], int): {
            "inst": bytes,
            "type_hint": bytes,
            "description": "args: rast, format, options=NULL, srid=sameassource - Return the raster tile in the designated GDAL Raster format. Raster formats are one of those supported by your compiled library. Use ST_GDALDrivers() to get a list of formats supported by your library.",
            "doc_url": "https://postgis.net/docs/ST_AsGDALRaster.html",
        }
    },
    "ST_AsGML": {
        (Geometry, int, int): {
            "inst": str,
            "type_hint": str,
            "description": "None",
            "doc_url": "https://postgis.net/docs/ST_AsGML.html",
        },
        (int, Geometry, int, int, str, str): {
            "inst": str,
            "type_hint": str,
            "description": "None",
            "doc_url": "https://postgis.net/docs/ST_AsGML.html",
        },
        (int, Geography, int, int, str, str): {
            "inst": str,
            "type_hint": str,
            "description": "None",
            "doc_url": "https://postgis.net/docs/ST_AsGML.html",
        },
        (Geography, int, int, str, str): {
            "inst": str,
            "type_hint": str,
            "description": "None",
            "doc_url": "https://postgis.net/docs/ST_AsGML.html",
        },
        (str,): {
            "inst": str,
            "type_hint": str,
            "description": "None",
            "doc_url": "https://postgis.net/docs/ST_AsGML.html",
        },
    },
    "ST_AsGeoJSON": {
        (Geometry, int, int): {
            "inst": str,
            "type_hint": str,
            "description": "None",
            "doc_url": "https://postgis.net/docs/ST_AsGeoJSON.html",
        },
        (Any, str, int, bool): {
            "inst": str,
            "type_hint": str,
            "description": "None",
            "doc_url": "https://postgis.net/docs/ST_AsGeoJSON.html",
        },
        (Geography, int, int): {
            "inst": str,
            "type_hint": str,
            "description": "None",
            "doc_url": "https://postgis.net/docs/ST_AsGeoJSON.html",
        },
        (str,): {
            "inst": str,
            "type_hint": str,
            "description": "None",
            "doc_url": "https://postgis.net/docs/ST_AsGeoJSON.html",
        },
    },
    "ST_AsGeobuf": {
        (Any,): {
            "inst": bytes,
            "type_hint": bytes,
            "description": "None",
            "doc_url": "https://postgis.net/docs/ST_AsGeobuf.html",
        },
        (Any, str): {
            "inst": bytes,
            "type_hint": bytes,
            "description": "None",
            "doc_url": "https://postgis.net/docs/ST_AsGeobuf.html",
        },
    },
    "ST_AsHEXEWKB": {
        (Geometry,): {
            "inst": str,
            "type_hint": str,
            "description": "None",
            "doc_url": "https://postgis.net/docs/ST_AsHEXEWKB.html",
        },
        (Geometry, str): {
            "inst": str,
            "type_hint": str,
            "description": "None",
            "doc_url": "https://postgis.net/docs/ST_AsHEXEWKB.html",
        },
    },
    "ST_AsHexWKB": {
        (Raster, bool): {
            "inst": str,
            "type_hint": str,
            "description": "args: rast, outasin=FALSE - Return the Well-Known Binary (WKB) in Hex representation of the raster.",
            "doc_url": "https://postgis.net/docs/ST_AsHexWKB.html",
        }
    },
    "ST_AsJPEG": {
        (Raster, int, int): {
            "inst": bytes,
            "type_hint": bytes,
            "description": "args: rast, nband, quality - Return the raster tile selected bands as a single Joint Photographic Exports Group (JPEG) image (byte array). If no band is specified and 1 or more than 3 bands, then only the first band is used. If only 3 bands then all 3 bands are used and mapped to RGB.",
            "doc_url": "https://postgis.net/docs/ST_AsJPEG.html",
        },
        (Raster, List[str]): {
            "inst": bytes,
            "type_hint": bytes,
            "description": "args: rast, options=NULL - Return the raster tile selected bands as a single Joint Photographic Exports Group (JPEG) image (byte array). If no band is specified and 1 or more than 3 bands, then only the first band is used. If only 3 bands then all 3 bands are used and mapped to RGB.",
            "doc_url": "https://postgis.net/docs/ST_AsJPEG.html",
        },
        (Raster, List[int], List[str]): {
            "inst": bytes,
            "type_hint": bytes,
            "description": "args: rast, nbands, options=NULL - Return the raster tile selected bands as a single Joint Photographic Exports Group (JPEG) image (byte array). If no band is specified and 1 or more than 3 bands, then only the first band is used. If only 3 bands then all 3 bands are used and mapped to RGB.",
            "doc_url": "https://postgis.net/docs/ST_AsJPEG.html",
        },
        (Raster, List[int], int): {
            "inst": bytes,
            "type_hint": bytes,
            "description": "args: rast, nbands, quality - Return the raster tile selected bands as a single Joint Photographic Exports Group (JPEG) image (byte array). If no band is specified and 1 or more than 3 bands, then only the first band is used. If only 3 bands then all 3 bands are used and mapped to RGB.",
            "doc_url": "https://postgis.net/docs/ST_AsJPEG.html",
        },
        (Raster, int, List[str]): {
            "inst": bytes,
            "type_hint": bytes,
            "description": "args: rast, nband, options=NULL - Return the raster tile selected bands as a single Joint Photographic Exports Group (JPEG) image (byte array). If no band is specified and 1 or more than 3 bands, then only the first band is used. If only 3 bands then all 3 bands are used and mapped to RGB.",
            "doc_url": "https://postgis.net/docs/ST_AsJPEG.html",
        },
    },
    "ST_AsKML": {
        (Geometry, int, str): {
            "inst": str,
            "type_hint": str,
            "description": "None",
            "doc_url": "https://postgis.net/docs/ST_AsKML.html",
        },
        (Geography, int, str): {
            "inst": str,
            "type_hint": str,
            "description": "None",
            "doc_url": "https://postgis.net/docs/ST_AsKML.html",
        },
        (str,): {
            "inst": str,
            "type_hint": str,
            "description": "None",
            "doc_url": "https://postgis.net/docs/ST_AsKML.html",
        },
    },
    "ST_AsLatLonText": {
        (Geometry, str): {
            "inst": str,
            "type_hint": str,
            "description": "None",
            "doc_url": "https://postgis.net/docs/ST_AsLatLonText.html",
        }
    },
    "ST_AsMARC21": {
        (Geometry, str): {
            "inst": str,
            "type_hint": str,
            "description": "None",
            "doc_url": "https://postgis.net/docs/ST_AsMARC21.html",
        }
    },
    "ST_AsMVT": {
        (Any,): {
            "inst": bytes,
            "type_hint": bytes,
            "description": "None",
            "doc_url": "https://postgis.net/docs/ST_AsMVT.html",
        },
        (Any, str): {
            "inst": bytes,
            "type_hint": bytes,
            "description": "None",
            "doc_url": "https://postgis.net/docs/ST_AsMVT.html",
        },
        (Any, str, int): {
            "inst": bytes,
            "type_hint": bytes,
            "description": "None",
            "doc_url": "https://postgis.net/docs/ST_AsMVT.html",
        },
        (Any, str, int, str): {
            "inst": bytes,
            "type_hint": bytes,
            "description": "None",
            "doc_url": "https://postgis.net/docs/ST_AsMVT.html",
        },
        (Any, str, int, str, str): {
            "inst": bytes,
            "type_hint": bytes,
            "description": "None",
            "doc_url": "https://postgis.net/docs/ST_AsMVT.html",
        },
    },
    "ST_AsMVTGeom": {
        (Geometry, Geometry, int, int, bool): {
            "inst": Geometry,
            "type_hint": Geometry,
            "description": "None",
            "doc_url": "https://postgis.net/docs/ST_AsMVTGeom.html",
        }
    },
    "ST_AsPNG": {
        (Raster, List[str]): {
            "inst": bytes,
            "type_hint": bytes,
            "description": "args: rast, options=NULL - Return the raster tile selected bands as a single portable network graphics (PNG) image (byte array). If 1, 3, or 4 bands in raster and no bands are specified, then all bands are used. If more 2 or more than 4 bands and no bands specified, then only band 1 is used. Bands are mapped to RGB or RGBA space.",
            "doc_url": "https://postgis.net/docs/ST_AsPNG.html",
        },
        (Raster, List[int], List[str]): {
            "inst": bytes,
            "type_hint": bytes,
            "description": "args: rast, nbands, options=NULL - Return the raster tile selected bands as a single portable network graphics (PNG) image (byte array). If 1, 3, or 4 bands in raster and no bands are specified, then all bands are used. If more 2 or more than 4 bands and no bands specified, then only band 1 is used. Bands are mapped to RGB or RGBA space.",
            "doc_url": "https://postgis.net/docs/ST_AsPNG.html",
        },
        (Raster, List[int], int): {
            "inst": bytes,
            "type_hint": bytes,
            "description": "args: rast, nbands, compression - Return the raster tile selected bands as a single portable network graphics (PNG) image (byte array). If 1, 3, or 4 bands in raster and no bands are specified, then all bands are used. If more 2 or more than 4 bands and no bands specified, then only band 1 is used. Bands are mapped to RGB or RGBA space.",
            "doc_url": "https://postgis.net/docs/ST_AsPNG.html",
        },
        (Raster, int, List[str]): {
            "inst": bytes,
            "type_hint": bytes,
            "description": "args: rast, nband, options=NULL - Return the raster tile selected bands as a single portable network graphics (PNG) image (byte array). If 1, 3, or 4 bands in raster and no bands are specified, then all bands are used. If more 2 or more than 4 bands and no bands specified, then only band 1 is used. Bands are mapped to RGB or RGBA space.",
            "doc_url": "https://postgis.net/docs/ST_AsPNG.html",
        },
        (Raster, int, int): {
            "inst": bytes,
            "type_hint": bytes,
            "description": "args: rast, nband, compression - Return the raster tile selected bands as a single portable network graphics (PNG) image (byte array). If 1, 3, or 4 bands in raster and no bands are specified, then all bands are used. If more 2 or more than 4 bands and no bands specified, then only band 1 is used. Bands are mapped to RGB or RGBA space.",
            "doc_url": "https://postgis.net/docs/ST_AsPNG.html",
        },
    },
    "ST_AsRaster": {
        (
            Geometry,
            float,
            float,
            float,
            float,
            List[str],
            List[float],
            List[float],
            float,
            float,
            bool,
        ): {
            "inst": Raster,
            "type_hint": Raster,
            "description": "args: geom, scalex, scaley, gridx=NULL, gridy=NULL, pixeltype=ARRAY['8BUI'], value=ARRAY[1], nodataval=ARRAY[0], skewx=0, skewy=0, touched=false - Converts a PostGIS geometry to a PostGIS raster.",
            "doc_url": "https://postgis.net/docs/ST_AsRaster.html",
        },
        (
            Geometry,
            float,
            float,
            List[str],
            List[float],
            List[float],
            float,
            float,
            float,
            float,
            bool,
        ): {
            "inst": Raster,
            "type_hint": Raster,
            "description": "args: geom, scalex, scaley, pixeltype, value=ARRAY[1], nodataval=ARRAY[0], upperleftx=NULL, upperlefty=NULL, skewx=0, skewy=0, touched=false - Converts a PostGIS geometry to a PostGIS raster.",
            "doc_url": "https://postgis.net/docs/ST_AsRaster.html",
        },
        (
            Geometry,
            int,
            int,
            float,
            float,
            List[str],
            List[float],
            List[float],
            float,
            float,
            bool,
        ): {
            "inst": Raster,
            "type_hint": Raster,
            "description": "args: geom, width, height, gridx=NULL, gridy=NULL, pixeltype=ARRAY['8BUI'], value=ARRAY[1], nodataval=ARRAY[0], skewx=0, skewy=0, touched=false - Converts a PostGIS geometry to a PostGIS raster.",
            "doc_url": "https://postgis.net/docs/ST_AsRaster.html",
        },
        (
            Geometry,
            int,
            int,
            List[str],
            List[float],
            List[float],
            float,
            float,
            float,
            float,
            bool,
        ): {
            "inst": Raster,
            "type_hint": Raster,
            "description": "args: geom, width, height, pixeltype, value=ARRAY[1], nodataval=ARRAY[0], upperleftx=NULL, upperlefty=NULL, skewx=0, skewy=0, touched=false - Converts a PostGIS geometry to a PostGIS raster.",
            "doc_url": "https://postgis.net/docs/ST_AsRaster.html",
        },
        (Geometry, float, float, float, float, str, float, float, float, float, bool): {
            "inst": Raster,
            "type_hint": Raster,
            "description": "args: geom, scalex, scaley, gridx, gridy, pixeltype, value=1, nodataval=0, skewx=0, skewy=0, touched=false - Converts a PostGIS geometry to a PostGIS raster.",
            "doc_url": "https://postgis.net/docs/ST_AsRaster.html",
        },
        (Geometry, float, float, str, float, float, float, float, float, float, bool): {
            "inst": Raster,
            "type_hint": Raster,
            "description": "args: geom, scalex, scaley, pixeltype, value=1, nodataval=0, upperleftx=NULL, upperlefty=NULL, skewx=0, skewy=0, touched=false - Converts a PostGIS geometry to a PostGIS raster.",
            "doc_url": "https://postgis.net/docs/ST_AsRaster.html",
        },
        (Geometry, int, int, float, float, str, float, float, float, float, bool): {
            "inst": Raster,
            "type_hint": Raster,
            "description": "args: geom, width, height, gridx, gridy, pixeltype, value=1, nodataval=0, skewx=0, skewy=0, touched=false - Converts a PostGIS geometry to a PostGIS raster.",
            "doc_url": "https://postgis.net/docs/ST_AsRaster.html",
        },
        (Geometry, int, int, str, float, float, float, float, float, float, bool): {
            "inst": Raster,
            "type_hint": Raster,
            "description": "args: geom, width, height, pixeltype, value=1, nodataval=0, upperleftx=NULL, upperlefty=NULL, skewx=0, skewy=0, touched=false - Converts a PostGIS geometry to a PostGIS raster.",
            "doc_url": "https://postgis.net/docs/ST_AsRaster.html",
        },
        (Geometry, Raster, List[str], List[float], List[float], bool): {
            "inst": Raster,
            "type_hint": Raster,
            "description": "args: geom, ref, pixeltype=ARRAY['8BUI'], value=ARRAY[1], nodataval=ARRAY[0], touched=false - Converts a PostGIS geometry to a PostGIS raster.",
            "doc_url": "https://postgis.net/docs/ST_AsRaster.html",
        },
        (Geometry, Raster, str, float, float, bool): {
            "inst": Raster,
            "type_hint": Raster,
            "description": "args: geom, ref, pixeltype, value=1, nodataval=0, touched=false - Converts a PostGIS geometry to a PostGIS raster.",
            "doc_url": "https://postgis.net/docs/ST_AsRaster.html",
        },
    },
    "ST_AsSVG": {
        (Geometry, int, int): {
            "inst": str,
            "type_hint": str,
            "description": "None",
            "doc_url": "https://postgis.net/docs/ST_AsSVG.html",
        },
        (Geography, int, int): {
            "inst": str,
            "type_hint": str,
            "description": "None",
            "doc_url": "https://postgis.net/docs/ST_AsSVG.html",
        },
        (str,): {
            "inst": str,
            "type_hint": str,
            "description": "None",
            "doc_url": "https://postgis.net/docs/ST_AsSVG.html",
        },
    },
    "ST_AsTIFF": {
        (Raster, List[str], int): {
            "inst": bytes,
            "type_hint": bytes,
            "description": "args: rast, options=', srid=sameassource - Return the raster selected bands as a single TIFF image (byte array). If no band is specified or any of specified bands does not exist in the raster, then will try to use all bands.",
            "doc_url": "https://postgis.net/docs/ST_AsTIFF.html",
        },
        (Raster, List[int], List[str], int): {
            "inst": bytes,
            "type_hint": bytes,
            "description": "args: rast, nbands, options, srid=sameassource - Return the raster selected bands as a single TIFF image (byte array). If no band is specified or any of specified bands does not exist in the raster, then will try to use all bands.",
            "doc_url": "https://postgis.net/docs/ST_AsTIFF.html",
        },
        (Raster, str, int): {
            "inst": bytes,
            "type_hint": bytes,
            "description": "args: rast, compression=', srid=sameassource - Return the raster selected bands as a single TIFF image (byte array). If no band is specified or any of specified bands does not exist in the raster, then will try to use all bands.",
            "doc_url": "https://postgis.net/docs/ST_AsTIFF.html",
        },
        (Raster, List[int], str, int): {
            "inst": bytes,
            "type_hint": bytes,
            "description": "args: rast, nbands, compression=', srid=sameassource - Return the raster selected bands as a single TIFF image (byte array). If no band is specified or any of specified bands does not exist in the raster, then will try to use all bands.",
            "doc_url": "https://postgis.net/docs/ST_AsTIFF.html",
        },
    },
    "ST_AsTWKB": {
        (Geometry, int, int, int, bool, bool): {
            "inst": bytes,
            "type_hint": bytes,
            "description": "None",
            "doc_url": "https://postgis.net/docs/ST_AsTWKB.html",
        },
        (List[Geometry], List[int], int, int, int, bool, bool): {
            "inst": bytes,
            "type_hint": bytes,
            "description": "None",
            "doc_url": "https://postgis.net/docs/ST_AsTWKB.html",
        },
    },
    "ST_AsText": {
        (Geometry,): {
            "inst": str,
            "type_hint": str,
            "description": "None",
            "doc_url": "https://postgis.net/docs/ST_AsText.html",
        },
        (Geometry, int): {
            "inst": str,
            "type_hint": str,
            "description": "None",
            "doc_url": "https://postgis.net/docs/ST_AsText.html",
        },
        (Geography,): {
            "inst": str,
            "type_hint": str,
            "description": "None",
            "doc_url": "https://postgis.net/docs/ST_AsText.html",
        },
        (Geography, int): {
            "inst": str,
            "type_hint": str,
            "description": "None",
            "doc_url": "https://postgis.net/docs/ST_AsText.html",
        },
        (str,): {
            "inst": str,
            "type_hint": str,
            "description": "None",
            "doc_url": "https://postgis.net/docs/ST_AsText.html",
        },
    },
    "ST_AsWKB": {
        (Raster, bool): {
            "inst": bytes,
            "type_hint": bytes,
            "description": "args: rast, outasin=FALSE - Return the Well-Known Binary (WKB) representation of the raster.",
            "doc_url": "https://postgis.net/docs/ST_AsWKB.html",
        }
    },
    "ST_AsX3D": {
        (Geometry, int, int): {
            "inst": str,
            "type_hint": str,
            "description": "None",
            "doc_url": "https://postgis.net/docs/ST_AsX3D.html",
        }
    },
    "ST_Aspect": {
        (Raster, int, Raster, str, str, bool): {
            "inst": Raster,
            "type_hint": Raster,
            "description": "args: rast, band, customextent, pixeltype=32BF, units=DEGREES, interpolate_nodata=FALSE - Returns the aspect (in degrees by default) of an elevation raster band. Useful for analyzing terrain.",
            "doc_url": "https://postgis.net/docs/ST_Aspect.html",
        },
        (Raster, int, str, str, bool): {
            "inst": Raster,
            "type_hint": Raster,
            "description": "args: rast, band=1, pixeltype=32BF, units=DEGREES, interpolate_nodata=FALSE - Returns the aspect (in degrees by default) of an elevation raster band. Useful for analyzing terrain.",
            "doc_url": "https://postgis.net/docs/ST_Aspect.html",
        },
    },
    "ST_Azimuth": {
        (Geometry, Geometry): {
            "inst": float,
            "type_hint": float,
            "description": "args: origin, target - Returns the north-based azimuth of a line between two points.",
            "doc_url": "https://postgis.net/docs/ST_Azimuth.html",
        },
        (Geography, Geography): {
            "inst": float,
            "type_hint": float,
            "description": "args: origin, target - Returns the north-based azimuth of a line between two points.",
            "doc_url": "https://postgis.net/docs/ST_Azimuth.html",
        },
    },
    "ST_Band": {
        (Raster, List[int]): {
            "inst": Raster,
            "type_hint": Raster,
            "description": "args: rast, nbands = ARRAY[1] - Returns one or more bands of an existing raster as a new raster. Useful for building new rasters from existing rasters.",
            "doc_url": "https://postgis.net/docs/ST_Band.html",
        },
        (Raster, int): {
            "inst": Raster,
            "type_hint": Raster,
            "description": "args: rast, nband - Returns one or more bands of an existing raster as a new raster. Useful for building new rasters from existing rasters.",
            "doc_url": "https://postgis.net/docs/ST_Band.html",
        },
        (Raster, str, Any): {
            "inst": Raster,
            "type_hint": Raster,
            "description": "args: rast, nbands, delimiter=, - Returns one or more bands of an existing raster as a new raster. Useful for building new rasters from existing rasters.",
            "doc_url": "https://postgis.net/docs/ST_Band.html",
        },
    },
    "ST_BandFileSize": {
        (Raster, int): {
            "inst": int,
            "type_hint": int,
            "description": "args: rast, bandnum=1 - Returns the file size of a band stored in file system. If no bandnum specified, 1 is assumed.",
            "doc_url": "https://postgis.net/docs/ST_BandFileSize.html",
        }
    },
    "ST_BandFileTimestamp": {
        (Raster, int): {
            "inst": int,
            "type_hint": int,
            "description": "args: rast, bandnum=1 - Returns the file timestamp of a band stored in file system. If no bandnum specified, 1 is assumed.",
            "doc_url": "https://postgis.net/docs/ST_BandFileTimestamp.html",
        }
    },
    "ST_BandIsNoData": {
        (Raster, int, bool): {
            "inst": bool,
            "type_hint": bool,
            "description": "args: rast, band, forceChecking=true - Returns true if the band is filled with only nodata values.",
            "doc_url": "https://postgis.net/docs/ST_BandIsNoData.html",
        },
        (Raster, bool): {
            "inst": bool,
            "type_hint": bool,
            "description": "args: rast, forceChecking=true - Returns true if the band is filled with only nodata values.",
            "doc_url": "https://postgis.net/docs/ST_BandIsNoData.html",
        },
    },
    "ST_BandMetaData": {
        (Raster, List[int]): {
            "inst": object,
            "type_hint": Any,
            "description": "args: rast, band - Returns basic meta data for a specific raster band. band num 1 is assumed if none-specified.",
            "doc_url": "https://postgis.net/docs/ST_BandMetaData.html",
        },
        (Raster, int): {
            "inst": object,
            "type_hint": Any,
            "description": "args: rast, band=1 - Returns basic meta data for a specific raster band. band num 1 is assumed if none-specified.",
            "doc_url": "https://postgis.net/docs/ST_BandMetaData.html",
        },
    },
    "ST_BandNoDataValue": {
        (Raster, int): {
            "inst": float,
            "type_hint": float,
            "description": "args: rast, bandnum=1 - Returns the value in a given band that represents no data. If no band num 1 is assumed.",
            "doc_url": "https://postgis.net/docs/ST_BandNoDataValue.html",
        }
    },
    "ST_BandPath": {
        (Raster, int): {
            "inst": str,
            "type_hint": str,
            "description": "args: rast, bandnum=1 - Returns system file path to a band stored in file system. If no bandnum specified, 1 is assumed.",
            "doc_url": "https://postgis.net/docs/ST_BandPath.html",
        }
    },
    "ST_BandPixelType": {
        (Raster, int): {
            "inst": str,
            "type_hint": str,
            "description": "args: rast, bandnum=1 - Returns the type of pixel for given band. If no bandnum specified, 1 is assumed.",
            "doc_url": "https://postgis.net/docs/ST_BandPixelType.html",
        }
    },
    "ST_BdMPolyFromText": {
        (str, int): {
            "inst": Geometry,
            "type_hint": Geometry,
            "description": "None",
            "doc_url": "https://postgis.net/docs/ST_BdMPolyFromText.html",
        }
    },
    "ST_BdPolyFromText": {
        (str, int): {
            "inst": Geometry,
            "type_hint": Geometry,
            "description": "None",
            "doc_url": "https://postgis.net/docs/ST_BdPolyFromText.html",
        }
    },
    "ST_Boundary": {
        (Geometry,): {
            "inst": Geometry,
            "type_hint": Geometry,
            "description": "args: geomA - Returns the boundary of a geometry.",
            "doc_url": "https://postgis.net/docs/ST_Boundary.html",
        }
    },
    "ST_BoundingDiagonal": {
        (Geometry, bool): {
            "inst": Geometry,
            "type_hint": Geometry,
            "description": "args: geom, fits=false - Returns the diagonal of a geometry's bounding box.",
            "doc_url": "https://postgis.net/docs/ST_BoundingDiagonal.html",
        }
    },
    "ST_Box2dFromGeoHash": {
        (str, int): {
            "inst": Geometry,
            "type_hint": Geometry,
            "description": "None",
            "doc_url": "https://postgis.net/docs/ST_Box2dFromGeoHash.html",
        }
    },
    "ST_Buffer": {
        (Geometry, float, str): {
            "inst": Geometry,
            "type_hint": Geometry,
            "description": "args: g1, radius_of_buffer, buffer_style_parameters = ' - Computes a geometry covering all points within a given distance from a geometry.",
            "doc_url": "https://postgis.net/docs/ST_Buffer.html",
        },
        (Geometry, float, int): {
            "inst": Geometry,
            "type_hint": Geometry,
            "description": "args: g1, radius_of_buffer, num_seg_quarter_circle - Computes a geometry covering all points within a given distance from a geometry.",
            "doc_url": "https://postgis.net/docs/ST_Buffer.html",
        },
        (str, float, int): {
            "inst": Geometry,
            "type_hint": Geometry,
            "description": "None",
            "doc_url": "https://postgis.net/docs/ST_Buffer.html",
        },
        (Geography, float): {
            "inst": Geography,
            "type_hint": Geography,
            "description": "None",
            "doc_url": "https://postgis.net/docs/ST_Buffer.html",
        },
        (Geography, float, int): {
            "inst": Geography,
            "type_hint": Geography,
            "description": "args: g1, radius_of_buffer, num_seg_quarter_circle - Computes a geometry covering all points within a given distance from a geometry.",
            "doc_url": "https://postgis.net/docs/ST_Buffer.html",
        },
        (Geography, float, str): {
            "inst": Geography,
            "type_hint": Geography,
            "description": "args: g1, radius_of_buffer, buffer_style_parameters - Computes a geometry covering all points within a given distance from a geometry.",
            "doc_url": "https://postgis.net/docs/ST_Buffer.html",
        },
        (str, float): {
            "inst": Geometry,
            "type_hint": Geometry,
            "description": "None",
            "doc_url": "https://postgis.net/docs/ST_Buffer.html",
        },
        (str, float, str): {
            "inst": Geometry,
            "type_hint": Geometry,
            "description": "None",
            "doc_url": "https://postgis.net/docs/ST_Buffer.html",
        },
    },
    "ST_BuildArea": {
        (Geometry,): {
            "inst": Geometry,
            "type_hint": Geometry,
            "description": "args: geom - Creates a polygonal geometry formed by the linework of a geometry.",
            "doc_url": "https://postgis.net/docs/ST_BuildArea.html",
        }
    },
    "ST_CPAWithin": {
        (Geometry, Geometry, float): {
            "inst": bool,
            "type_hint": bool,
            "description": "args: track1, track2, dist - Tests if the closest point of approach of two trajectoriesis within the specified distance.",
            "doc_url": "https://postgis.net/docs/ST_CPAWithin.html",
        }
    },
    "ST_Centroid": {
        (Geometry,): {
            "inst": Geometry,
            "type_hint": Geometry,
            "description": "args: g1 - Returns the geometric center of a geometry.",
            "doc_url": "https://postgis.net/docs/ST_Centroid.html",
        },
        (Geography, bool): {
            "inst": Geography,
            "type_hint": Geography,
            "description": "args: g1, use_spheroid = true - Returns the geometric center of a geometry.",
            "doc_url": "https://postgis.net/docs/ST_Centroid.html",
        },
        (str,): {
            "inst": Geometry,
            "type_hint": Geometry,
            "description": "None",
            "doc_url": "https://postgis.net/docs/ST_Centroid.html",
        },
    },
    "ST_ChaikinSmoothing": {
        (Geometry, int, bool): {
            "inst": Geometry,
            "type_hint": Geometry,
            "description": "args: geom, nIterations = 1, preserveEndPoints = false - Returns a smoothed version of a geometry, using the Chaikin algorithm",
            "doc_url": "https://postgis.net/docs/ST_ChaikinSmoothing.html",
        }
    },
    "ST_Clip": {
        (Raster, List[int], Geometry, List[float], bool): {
            "inst": Raster,
            "type_hint": Raster,
            "description": "args: rast, nband, geom, nodataval=NULL, crop=TRUE - Returns the raster clipped by the input geometry. If band number not is specified, all bands are processed. If crop is not specified or TRUE, the output raster is cropped.",
            "doc_url": "https://postgis.net/docs/ST_Clip.html",
        },
        (Raster, int, Geometry, float, bool): {
            "inst": Raster,
            "type_hint": Raster,
            "description": "args: rast, nband, geom, nodataval, crop=TRUE - Returns the raster clipped by the input geometry. If band number not is specified, all bands are processed. If crop is not specified or TRUE, the output raster is cropped.",
            "doc_url": "https://postgis.net/docs/ST_Clip.html",
        },
        (Raster, int, Geometry, bool): {
            "inst": Raster,
            "type_hint": Raster,
            "description": "args: rast, nband, geom, crop - Returns the raster clipped by the input geometry. If band number not is specified, all bands are processed. If crop is not specified or TRUE, the output raster is cropped.",
            "doc_url": "https://postgis.net/docs/ST_Clip.html",
        },
        (Raster, Geometry, List[float], bool): {
            "inst": Raster,
            "type_hint": Raster,
            "description": "args: rast, geom, nodataval=NULL, crop=TRUE - Returns the raster clipped by the input geometry. If band number not is specified, all bands are processed. If crop is not specified or TRUE, the output raster is cropped.",
            "doc_url": "https://postgis.net/docs/ST_Clip.html",
        },
        (Raster, Geometry, float, bool): {
            "inst": Raster,
            "type_hint": Raster,
            "description": "args: rast, geom, nodataval, crop=TRUE - Returns the raster clipped by the input geometry. If band number not is specified, all bands are processed. If crop is not specified or TRUE, the output raster is cropped.",
            "doc_url": "https://postgis.net/docs/ST_Clip.html",
        },
        (Raster, Geometry, bool): {
            "inst": Raster,
            "type_hint": Raster,
            "description": "args: rast, geom, crop - Returns the raster clipped by the input geometry. If band number not is specified, all bands are processed. If crop is not specified or TRUE, the output raster is cropped.",
            "doc_url": "https://postgis.net/docs/ST_Clip.html",
        },
    },
    "ST_ClipByBox2D": {
        (Geometry, Geometry): {
            "inst": Geometry,
            "type_hint": Geometry,
            "description": "args: geom, box - Computes the portion of a geometry falling within a rectangle.",
            "doc_url": "https://postgis.net/docs/ST_ClipByBox2D.html",
        }
    },
    "ST_ClosestPoint": {
        (Geometry, Geometry): {
            "inst": Geometry,
            "type_hint": Geometry,
            "description": "args: geom1, geom2 - Returns the 2D point on g1 that is closest to g2. This is the first point of the shortest line from one geometry to the other.",
            "doc_url": "https://postgis.net/docs/ST_ClosestPoint.html",
        },
        (Geography, Geography, bool): {
            "inst": Geography,
            "type_hint": Geography,
            "description": "args: geom1, geom2, use_spheroid = true - Returns the 2D point on g1 that is closest to g2. This is the first point of the shortest line from one geometry to the other.",
            "doc_url": "https://postgis.net/docs/ST_ClosestPoint.html",
        },
        (str, str): {
            "inst": Geometry,
            "type_hint": Geometry,
            "description": "None",
            "doc_url": "https://postgis.net/docs/ST_ClosestPoint.html",
        },
    },
    "ST_ClosestPointOfApproach": {
        (Geometry, Geometry): {
            "inst": float,
            "type_hint": float,
            "description": "args: track1, track2 - Returns a measure at the closest point of approach of two trajectories.",
            "doc_url": "https://postgis.net/docs/ST_ClosestPointOfApproach.html",
        }
    },
    "ST_ClusterDBSCAN": {
        (Geometry, float, int): {
            "inst": int,
            "type_hint": int,
            "description": "args: geom, eps, minpoints - Window function that returns a cluster id for each input geometry using the DBSCAN algorithm.",
            "doc_url": "https://postgis.net/docs/ST_ClusterDBSCAN.html",
        }
    },
    "ST_ClusterIntersecting": {
        (Geometry,): {
            "inst": Geometry,
            "type_hint": List[Geometry],
            "description": "args: g - Aggregate function that clusters input geometries into connected sets.",
            "doc_url": "https://postgis.net/docs/ST_ClusterIntersecting.html",
        },
        (List[Geometry],): {
            "inst": Geometry,
            "type_hint": List[Geometry],
            "description": "None",
            "doc_url": "https://postgis.net/docs/ST_ClusterIntersecting.html",
        },
    },
    "ST_ClusterIntersectingWin": {
        (Geometry,): {
            "inst": int,
            "type_hint": int,
            "description": "args: geom - Window function that returns a cluster id for each input geometry, clustering input geometries into connected sets.",
            "doc_url": "https://postgis.net/docs/ST_ClusterIntersectingWin.html",
        }
    },
    "ST_ClusterKMeans": {
        (Geometry, int, float): {
            "inst": int,
            "type_hint": int,
            "description": "args: geom, number_of_clusters, max_radius - Window function that returns a cluster id for each input geometry using the K-means algorithm.",
            "doc_url": "https://postgis.net/docs/ST_ClusterKMeans.html",
        }
    },
    "ST_ClusterWithin": {
        (Geometry, float): {
            "inst": Geometry,
            "type_hint": List[Geometry],
            "description": "args: g, distance - Aggregate function that clusters geometries by separation distance.",
            "doc_url": "https://postgis.net/docs/ST_ClusterWithin.html",
        },
        (List[Geometry], float): {
            "inst": Geometry,
            "type_hint": List[Geometry],
            "description": "None",
            "doc_url": "https://postgis.net/docs/ST_ClusterWithin.html",
        },
    },
    "ST_ClusterWithinWin": {
        (Geometry, float): {
            "inst": int,
            "type_hint": int,
            "description": "args: geom, distance - Window function that returns a cluster id for each input geometry, clustering using separation distance.",
            "doc_url": "https://postgis.net/docs/ST_ClusterWithinWin.html",
        }
    },
    "ST_Collect": {
        (Geometry,): {
            "inst": Geometry,
            "type_hint": Geometry,
            "description": "args: g1field - Creates a GeometryCollection or Multi* geometry from a set of geometries.",
            "doc_url": "https://postgis.net/docs/ST_Collect.html",
        },
        (Geometry, Geometry): {
            "inst": Geometry,
            "type_hint": Geometry,
            "description": "args: g1, g2 - Creates a GeometryCollection or Multi* geometry from a set of geometries.",
            "doc_url": "https://postgis.net/docs/ST_Collect.html",
        },
        (List[Geometry],): {
            "inst": Geometry,
            "type_hint": Geometry,
            "description": "args: g1_array - Creates a GeometryCollection or Multi* geometry from a set of geometries.",
            "doc_url": "https://postgis.net/docs/ST_Collect.html",
        },
    },
    "ST_CollectionExtract": {
        (Geometry, int): {
            "inst": Geometry,
            "type_hint": Geometry,
            "description": "args: collection, type - Given a geometry collection, returns a multi-geometry containing only elements of a specified type.",
            "doc_url": "https://postgis.net/docs/ST_CollectionExtract.html",
        },
        (Geometry,): {
            "inst": Geometry,
            "type_hint": Geometry,
            "description": "args: collection - Given a geometry collection, returns a multi-geometry containing only elements of a specified type.",
            "doc_url": "https://postgis.net/docs/ST_CollectionExtract.html",
        },
    },
    "ST_CollectionHomogenize": {
        (Geometry,): {
            "inst": Geometry,
            "type_hint": Geometry,
            "description": "args: collection - Returns the simplest representation of a geometry collection.",
            "doc_url": "https://postgis.net/docs/ST_CollectionHomogenize.html",
        }
    },
    "ST_ColorMap": {
        (Raster, int, str, str): {
            "inst": Raster,
            "type_hint": Raster,
            "description": "args: rast, nband=1, colormap=grayscale, method=INTERPOLATE - Creates a new raster of up to four 8BUI bands (grayscale, RGB, RGBA) from the source raster and a specified band. Band 1 is assumed if not specified.",
            "doc_url": "https://postgis.net/docs/ST_ColorMap.html",
        },
        (Raster, str, str): {
            "inst": Raster,
            "type_hint": Raster,
            "description": "args: rast, colormap, method=INTERPOLATE - Creates a new raster of up to four 8BUI bands (grayscale, RGB, RGBA) from the source raster and a specified band. Band 1 is assumed if not specified.",
            "doc_url": "https://postgis.net/docs/ST_ColorMap.html",
        },
    },
    "ST_CombineBbox": {
        (Geometry, Geometry): {
            "inst": Geometry,
            "type_hint": Geometry,
            "description": "None",
            "doc_url": "https://postgis.net/docs/ST_CombineBbox.html",
        }
    },
    "ST_ConcaveHull": {
        (Geometry, float, bool): {
            "inst": Geometry,
            "type_hint": Geometry,
            "description": "args: param_geom, param_pctconvex, param_allow_holes = false - Computes a possibly concave geometry that contains all input geometry vertices",
            "doc_url": "https://postgis.net/docs/ST_ConcaveHull.html",
        }
    },
    "ST_Contains": {
        (Geometry, Geometry): {
            "inst": bool,
            "type_hint": bool,
            "description": "None",
            "doc_url": "https://postgis.net/docs/ST_Contains.html",
        },
        (Raster, int, Raster, int): {
            "inst": bool,
            "type_hint": bool,
            "description": "args: rastA, nbandA, rastB, nbandB - Return true if no points of raster rastB lie in the exterior of raster rastA and at least one point of the interior of rastB lies in the interior of rastA.",
            "doc_url": "https://postgis.net/docs/ST_Contains.html",
        },
        (Raster, Raster): {
            "inst": bool,
            "type_hint": bool,
            "description": "args: rastA, rastB - Return true if no points of raster rastB lie in the exterior of raster rastA and at least one point of the interior of rastB lies in the interior of rastA.",
            "doc_url": "https://postgis.net/docs/ST_Contains.html",
        },
    },
    "ST_ContainsProperly": {
        (Geometry, Geometry): {
            "inst": bool,
            "type_hint": bool,
            "description": "None",
            "doc_url": "https://postgis.net/docs/ST_ContainsProperly.html",
        },
        (Raster, int, Raster, int): {
            "inst": bool,
            "type_hint": bool,
            "description": "args: rastA, nbandA, rastB, nbandB - Return true if rastB intersects the interior of rastA but not the boundary or exterior of rastA.",
            "doc_url": "https://postgis.net/docs/ST_ContainsProperly.html",
        },
        (Raster, Raster): {
            "inst": bool,
            "type_hint": bool,
            "description": "args: rastA, rastB - Return true if rastB intersects the interior of rastA but not the boundary or exterior of rastA.",
            "doc_url": "https://postgis.net/docs/ST_ContainsProperly.html",
        },
    },
    "ST_Contour": {
        (Raster, int, float, float, List[float], bool): {
            "inst": object,
            "type_hint": Any,
            "description": "args: rast, bandnumber=1, level_interval=100.0, level_base=0.0, fixed_levels=ARRAY[], polygonize=false - Generates a set of vector contours from the provided raster band, using the GDAL contouring algorithm.",
            "doc_url": "https://postgis.net/docs/ST_Contour.html",
        }
    },
    "ST_ConvexHull": {
        (Geometry,): {
            "inst": Geometry,
            "type_hint": Geometry,
            "description": "args: geomA - Computes the convex hull of a geometry.",
            "doc_url": "https://postgis.net/docs/ST_ConvexHull.html",
        },
        (Raster,): {
            "inst": Geometry,
            "type_hint": Geometry,
            "description": "args: rast - Return the convex hull geometry of the raster including pixel values equal to BandNoDataValue. For regular shaped and non-skewed rasters, this gives the same result as ST_Envelope so only useful for irregularly shaped or skewed rasters.",
            "doc_url": "https://postgis.net/docs/ST_ConvexHull.html",
        },
    },
    "ST_CoordDim": {
        (Geometry,): {
            "inst": int,
            "type_hint": int,
            "description": "args: geomA - Return the coordinate dimension of a geometry.",
            "doc_url": "https://postgis.net/docs/ST_CoordDim.html",
        }
    },
    "ST_Count": {
        (Raster, int, bool): {
            "inst": int,
            "type_hint": int,
            "description": "args: rast, nband=1, exclude_nodata_value=true - Returns the number of pixels in a given band of a raster or raster coverage. If no band is specified defaults to band 1. If exclude_nodata_value is set to true, will only count pixels that are not equal to the nodata value.",
            "doc_url": "https://postgis.net/docs/ST_Count.html",
        },
        (Raster, bool): {
            "inst": int,
            "type_hint": int,
            "description": "args: rast, exclude_nodata_value - Returns the number of pixels in a given band of a raster or raster coverage. If no band is specified defaults to band 1. If exclude_nodata_value is set to true, will only count pixels that are not equal to the nodata value.",
            "doc_url": "https://postgis.net/docs/ST_Count.html",
        },
    },
    "ST_CountAgg": {
        (Raster, int, bool, float): {
            "inst": int,
            "type_hint": int,
            "description": "args: rast, nband, exclude_nodata_value, sample_percent - Aggregate. Returns the number of pixels in a given band of a set of rasters. If no band is specified defaults to band 1. If exclude_nodata_value is set to true, will only count pixels that are not equal to the NODATA value.",
            "doc_url": "https://postgis.net/docs/ST_CountAgg.html",
        },
        (Raster, int, bool): {
            "inst": int,
            "type_hint": int,
            "description": "args: rast, nband, exclude_nodata_value - Aggregate. Returns the number of pixels in a given band of a set of rasters. If no band is specified defaults to band 1. If exclude_nodata_value is set to true, will only count pixels that are not equal to the NODATA value.",
            "doc_url": "https://postgis.net/docs/ST_CountAgg.html",
        },
        (Raster, bool): {
            "inst": int,
            "type_hint": int,
            "description": "args: rast, exclude_nodata_value - Aggregate. Returns the number of pixels in a given band of a set of rasters. If no band is specified defaults to band 1. If exclude_nodata_value is set to true, will only count pixels that are not equal to the NODATA value.",
            "doc_url": "https://postgis.net/docs/ST_CountAgg.html",
        },
    },
    "ST_CoverageSimplify": {
        (Geometry, float, bool): {
            "inst": Geometry,
            "type_hint": Geometry,
            "description": "args: geom, tolerance, simplifyBoundary = true - Window function that simplifies the edges of a polygonal coverage.",
            "doc_url": "https://postgis.net/docs/ST_CoverageSimplify.html",
        }
    },
    "ST_CoverageUnion": {
        (List[Geometry],): {
            "inst": Geometry,
            "type_hint": Geometry,
            "description": "None",
            "doc_url": "https://postgis.net/docs/ST_CoverageUnion.html",
        },
        (Geometry,): {
            "inst": Geometry,
            "type_hint": Geometry,
            "description": "args: geom - Computes the union of a set of polygons forming a coverage by removing shared edges.",
            "doc_url": "https://postgis.net/docs/ST_CoverageUnion.html",
        },
    },
    "ST_CoveredBy": {
        (Geometry, Geometry): {
            "inst": bool,
            "type_hint": bool,
            "description": "None",
            "doc_url": "https://postgis.net/docs/ST_CoveredBy.html",
        },
        (Geography, Geography): {
            "inst": bool,
            "type_hint": bool,
            "description": "None",
            "doc_url": "https://postgis.net/docs/ST_CoveredBy.html",
        },
        (str, str): {
            "inst": bool,
            "type_hint": bool,
            "description": "None",
            "doc_url": "https://postgis.net/docs/ST_CoveredBy.html",
        },
        (Raster, int, Raster, int): {
            "inst": bool,
            "type_hint": bool,
            "description": "args: rastA, nbandA, rastB, nbandB - Return true if no points of raster rastA lie outside raster rastB.",
            "doc_url": "https://postgis.net/docs/ST_CoveredBy.html",
        },
        (Raster, Raster): {
            "inst": bool,
            "type_hint": bool,
            "description": "args: rastA, rastB - Return true if no points of raster rastA lie outside raster rastB.",
            "doc_url": "https://postgis.net/docs/ST_CoveredBy.html",
        },
    },
    "ST_Covers": {
        (Geometry, Geometry): {
            "inst": bool,
            "type_hint": bool,
            "description": "None",
            "doc_url": "https://postgis.net/docs/ST_Covers.html",
        },
        (Geography, Geography): {
            "inst": bool,
            "type_hint": bool,
            "description": "None",
            "doc_url": "https://postgis.net/docs/ST_Covers.html",
        },
        (str, str): {
            "inst": bool,
            "type_hint": bool,
            "description": "None",
            "doc_url": "https://postgis.net/docs/ST_Covers.html",
        },
        (Raster, int, Raster, int): {
            "inst": bool,
            "type_hint": bool,
            "description": "args: rastA, nbandA, rastB, nbandB - Return true if no points of raster rastB lie outside raster rastA.",
            "doc_url": "https://postgis.net/docs/ST_Covers.html",
        },
        (Raster, Raster): {
            "inst": bool,
            "type_hint": bool,
            "description": "args: rastA, rastB - Return true if no points of raster rastB lie outside raster rastA.",
            "doc_url": "https://postgis.net/docs/ST_Covers.html",
        },
    },
    "ST_CreateOverview": {
        (Any, Any, int, str): {
            "inst": object,
            "type_hint": Any,
            "description": "args: tab, col, factor, algo='NearestNeighbor' - Create an reduced resolution version of a given raster coverage.",
            "doc_url": "https://postgis.net/docs/ST_CreateOverview.html",
        }
    },
    "ST_Crosses": {
        (Geometry, Geometry): {
            "inst": bool,
            "type_hint": bool,
            "description": "None",
            "doc_url": "https://postgis.net/docs/ST_Crosses.html",
        }
    },
    "ST_CurveToLine": {
        (Geometry, float, int, int): {
            "inst": Geometry,
            "type_hint": Geometry,
            "description": "args: curveGeom, tolerance, tolerance_type, flags - Converts a geometry containing curves to a linear geometry.",
            "doc_url": "https://postgis.net/docs/ST_CurveToLine.html",
        }
    },
    "ST_DFullyWithin": {
        (Geometry, Geometry, float): {
            "inst": bool,
            "type_hint": bool,
            "description": "None",
            "doc_url": "https://postgis.net/docs/ST_DFullyWithin.html",
        },
        (Raster, int, Raster, int, float): {
            "inst": bool,
            "type_hint": bool,
            "description": "args: rastA, nbandA, rastB, nbandB, distance_of_srid - Return true if rasters rastA and rastB are fully within the specified distance of each other.",
            "doc_url": "https://postgis.net/docs/ST_DFullyWithin.html",
        },
        (Raster, Raster, float): {
            "inst": bool,
            "type_hint": bool,
            "description": "args: rastA, rastB, distance_of_srid - Return true if rasters rastA and rastB are fully within the specified distance of each other.",
            "doc_url": "https://postgis.net/docs/ST_DFullyWithin.html",
        },
    },
    "ST_DWithin": {
        (Geometry, Geometry, float): {
            "inst": bool,
            "type_hint": bool,
            "description": "None",
            "doc_url": "https://postgis.net/docs/ST_DWithin.html",
        },
        (Geography, Geography, float, bool): {
            "inst": bool,
            "type_hint": bool,
            "description": "None",
            "doc_url": "https://postgis.net/docs/ST_DWithin.html",
        },
        (str, str, float): {
            "inst": bool,
            "type_hint": bool,
            "description": "None",
            "doc_url": "https://postgis.net/docs/ST_DWithin.html",
        },
        (Raster, int, Raster, int, float): {
            "inst": bool,
            "type_hint": bool,
            "description": "args: rastA, nbandA, rastB, nbandB, distance_of_srid - Return true if rasters rastA and rastB are within the specified distance of each other.",
            "doc_url": "https://postgis.net/docs/ST_DWithin.html",
        },
        (Raster, Raster, float): {
            "inst": bool,
            "type_hint": bool,
            "description": "args: rastA, rastB, distance_of_srid - Return true if rasters rastA and rastB are within the specified distance of each other.",
            "doc_url": "https://postgis.net/docs/ST_DWithin.html",
        },
    },
    "ST_DelaunayTriangles": {
        (Geometry, float, int): {
            "inst": Geometry,
            "type_hint": Geometry,
            "description": "args: g1, tolerance = 0.0, flags = 0 - Returns the Delaunay triangulation of the vertices of a geometry.",
            "doc_url": "https://postgis.net/docs/ST_DelaunayTriangles.html",
        }
    },
    "ST_Difference": {
        (Geometry, Geometry, float): {
            "inst": Geometry,
            "type_hint": Geometry,
            "description": "args: geomA, geomB, gridSize = -1 - Computes a geometry representing the part of geometry A that does not intersect geometry B.",
            "doc_url": "https://postgis.net/docs/ST_Difference.html",
        }
    },
    "ST_Dimension": {
        (Geometry,): {
            "inst": int,
            "type_hint": int,
            "description": "args: g - Returns the topological dimension of a geometry.",
            "doc_url": "https://postgis.net/docs/ST_Dimension.html",
        }
    },
    "ST_Disjoint": {
        (Geometry, Geometry): {
            "inst": bool,
            "type_hint": bool,
            "description": "None",
            "doc_url": "https://postgis.net/docs/ST_Disjoint.html",
        },
        (Raster, int, Raster, int): {
            "inst": bool,
            "type_hint": bool,
            "description": "args: rastA, nbandA, rastB, nbandB - Return true if raster rastA does not spatially intersect rastB.",
            "doc_url": "https://postgis.net/docs/ST_Disjoint.html",
        },
        (Raster, Raster): {
            "inst": bool,
            "type_hint": bool,
            "description": "args: rastA, rastB - Return true if raster rastA does not spatially intersect rastB.",
            "doc_url": "https://postgis.net/docs/ST_Disjoint.html",
        },
    },
    "ST_Distance": {
        (Geometry, Geometry): {
            "inst": float,
            "type_hint": float,
            "description": "args: g1, g2 - Returns the distance between two geometry or geography values.",
            "doc_url": "https://postgis.net/docs/ST_Distance.html",
        },
        (Geography, Geography, bool): {
            "inst": float,
            "type_hint": float,
            "description": "args: geog1, geog2, use_spheroid = true - Returns the distance between two geometry or geography values.",
            "doc_url": "https://postgis.net/docs/ST_Distance.html",
        },
        (str, str): {
            "inst": float,
            "type_hint": float,
            "description": "None",
            "doc_url": "https://postgis.net/docs/ST_Distance.html",
        },
    },
    "ST_DistanceCPA": {
        (Geometry, Geometry): {
            "inst": float,
            "type_hint": float,
            "description": "args: track1, track2 - Returns the distance between the closest point of approach of two trajectories.",
            "doc_url": "https://postgis.net/docs/ST_DistanceCPA.html",
        }
    },
    "ST_DistanceSphere": {
        (Geometry, Geometry): {
            "inst": float,
            "type_hint": float,
            "description": "None",
            "doc_url": "https://postgis.net/docs/ST_DistanceSphere.html",
        },
        (Geometry, Geometry, float): {
            "inst": float,
            "type_hint": float,
            "description": "args: geomlonlatA, geomlonlatB, radius=6371008 - Returns minimum distance in meters between two lon/lat geometries using a spherical earth model.",
            "doc_url": "https://postgis.net/docs/ST_DistanceSphere.html",
        },
    },
    "ST_DistanceSpheroid": {
        (Geometry, Geometry, str): {
            "inst": float,
            "type_hint": float,
            "description": "args: geomlonlatA, geomlonlatB, measurement_spheroid=WGS84 - Returns the minimum distance between two lon/lat geometries using a spheroidal earth model.",
            "doc_url": "https://postgis.net/docs/ST_DistanceSpheroid.html",
        },
        (Geometry, Geometry): {
            "inst": float,
            "type_hint": float,
            "description": "None",
            "doc_url": "https://postgis.net/docs/ST_DistanceSpheroid.html",
        },
    },
    "ST_Distinct4ma": {
        (List[float], str, List[Any]): {
            "inst": float,
            "type_hint": float,
            "description": "args: matrix, nodatamode, VARIADIC args - Raster processing function that calculates the number of unique pixel values in a neighborhood.",
            "doc_url": "https://postgis.net/docs/ST_Distinct4ma.html",
        },
        (List[float], List[int], List[Any]): {
            "inst": float,
            "type_hint": float,
            "description": "args: value, pos, VARIADIC userargs - Raster processing function that calculates the number of unique pixel values in a neighborhood.",
            "doc_url": "https://postgis.net/docs/ST_Distinct4ma.html",
        },
    },
    "ST_Dump": {
        (Geometry,): {
            "inst": object,
            "type_hint": List[Any],
            "description": "args: g1 - Returns a set of geometry_dump rows for the components of a geometry.",
            "doc_url": "https://postgis.net/docs/ST_Dump.html",
        }
    },
    "ST_DumpAsPolygons": {
        (Raster, int, bool): {
            "inst": GeomVal,
            "type_hint": List[GeomVal],
            "description": "args: rast, band_num=1, exclude_nodata_value=TRUE - Returns a set of geomval (geom,val) rows, from a given raster band. If no band number is specified, band num defaults to 1.",
            "doc_url": "https://postgis.net/docs/ST_DumpAsPolygons.html",
        }
    },
    "ST_DumpPoints": {
        (Geometry,): {
            "inst": object,
            "type_hint": List[Any],
            "description": "args: geom - Returns a set of geometry_dump rows for the coordinates in a geometry.",
            "doc_url": "https://postgis.net/docs/ST_DumpPoints.html",
        }
    },
    "ST_DumpRings": {
        (Geometry,): {
            "inst": object,
            "type_hint": List[Any],
            "description": "args: a_polygon - Returns a set of geometry_dump rows for the exterior and interior rings of a Polygon.",
            "doc_url": "https://postgis.net/docs/ST_DumpRings.html",
        }
    },
    "ST_DumpSegments": {
        (Geometry,): {
            "inst": object,
            "type_hint": List[Any],
            "description": "args: geom - Returns a set of geometry_dump rows for the segments in a geometry.",
            "doc_url": "https://postgis.net/docs/ST_DumpSegments.html",
        }
    },
    "ST_DumpValues": {
        (Raster, List[int], bool): {
            "inst": object,
            "type_hint": Any,
            "description": "args: rast, nband=NULL, exclude_nodata_value=true - Get the values of the specified band as a 2-dimension array.",
            "doc_url": "https://postgis.net/docs/ST_DumpValues.html",
        },
        (Raster, int, bool): {
            "inst": float,
            "type_hint": List[float],
            "description": "args: rast, nband, exclude_nodata_value=true - Get the values of the specified band as a 2-dimension array.",
            "doc_url": "https://postgis.net/docs/ST_DumpValues.html",
        },
    },
    "ST_EndPoint": {
        (Geometry,): {
            "inst": Geometry,
            "type_hint": Geometry,
            "description": "args: g - Returns the last point of a LineString or CircularLineString.",
            "doc_url": "https://postgis.net/docs/ST_EndPoint.html",
        }
    },
    "ST_Envelope": {
        (Geometry,): {
            "inst": Geometry,
            "type_hint": Geometry,
            "description": "args: g1 - Returns a geometry representing the bounding box of a geometry.",
            "doc_url": "https://postgis.net/docs/ST_Envelope.html",
        },
        (Raster,): {
            "inst": Geometry,
            "type_hint": Geometry,
            "description": "args: rast - Returns the polygon representation of the extent of the raster.",
            "doc_url": "https://postgis.net/docs/ST_Envelope.html",
        },
    },
    "ST_Equals": {
        (Geometry, Geometry): {
            "inst": bool,
            "type_hint": bool,
            "description": "None",
            "doc_url": "https://postgis.net/docs/ST_Equals.html",
        }
    },
    "ST_EstimatedExtent": {
        (str, str, str, bool): {
            "inst": Geometry,
            "type_hint": Geometry,
            "description": "args: schema_name, table_name, geocolumn_name, parent_only - Returns the estimated extent of a spatial table.",
            "doc_url": "https://postgis.net/docs/ST_EstimatedExtent.html",
        },
        (str, str, str): {
            "inst": Geometry,
            "type_hint": Geometry,
            "description": "args: schema_name, table_name, geocolumn_name - Returns the estimated extent of a spatial table.",
            "doc_url": "https://postgis.net/docs/ST_EstimatedExtent.html",
        },
        (str, str): {
            "inst": Geometry,
            "type_hint": Geometry,
            "description": "args: table_name, geocolumn_name - Returns the estimated extent of a spatial table.",
            "doc_url": "https://postgis.net/docs/ST_EstimatedExtent.html",
        },
    },
    "ST_Expand": {
        (Geometry, float): {
            "inst": Geometry,
            "type_hint": Geometry,
            "description": "args: geom, units_to_expand - Returns a bounding box expanded from another bounding box or a geometry.",
            "doc_url": "https://postgis.net/docs/ST_Expand.html",
        },
        (Geometry, float, float): {
            "inst": Geometry,
            "type_hint": Geometry,
            "description": "args: box, dx, dy - Returns a bounding box expanded from another bounding box or a geometry.",
            "doc_url": "https://postgis.net/docs/ST_Expand.html",
        },
        (Geometry, float, float, float): {
            "inst": Geometry,
            "type_hint": Geometry,
            "description": "args: box, dx, dy, dz=0 - Returns a bounding box expanded from another bounding box or a geometry.",
            "doc_url": "https://postgis.net/docs/ST_Expand.html",
        },
        (Geometry, float, float, float, float): {
            "inst": Geometry,
            "type_hint": Geometry,
            "description": "args: geom, dx, dy, dz=0, dm=0 - Returns a bounding box expanded from another bounding box or a geometry.",
            "doc_url": "https://postgis.net/docs/ST_Expand.html",
        },
    },
    "ST_Extent": {
        (Geometry,): {
            "inst": Geometry,
            "type_hint": Geometry,
            "description": "args: geomfield - Aggregate function that returns the bounding box of geometries.",
            "doc_url": "https://postgis.net/docs/ST_Extent.html",
        }
    },
    "ST_ExteriorRing": {
        (Geometry,): {
            "inst": Geometry,
            "type_hint": Geometry,
            "description": "args: a_polygon - Returns a LineString representing the exterior ring of a Polygon.",
            "doc_url": "https://postgis.net/docs/ST_ExteriorRing.html",
        }
    },
    "ST_FilterByM": {
        (Geometry, float, float, bool): {
            "inst": Geometry,
            "type_hint": Geometry,
            "description": "args: geom, min, max = null, returnM = false - Removes vertices based on their M value",
            "doc_url": "https://postgis.net/docs/ST_FilterByM.html",
        }
    },
    "ST_FlipCoordinates": {
        (Geometry,): {
            "inst": Geometry,
            "type_hint": Geometry,
            "description": "args: geom - Returns a version of a geometry with X and Y axis flipped.",
            "doc_url": "https://postgis.net/docs/ST_FlipCoordinates.html",
        }
    },
    "ST_Force2D": {
        (Geometry,): {
            "inst": Geometry,
            "type_hint": Geometry,
            "description": "args: geomA - Force the geometries into a '2-dimensional mode'.",
            "doc_url": "https://postgis.net/docs/ST_Force2D.html",
        }
    },
    "ST_Force3D": {
        (Geometry, float): {
            "inst": Geometry,
            "type_hint": Geometry,
            "description": "args: geomA, Zvalue = 0.0 - Force the geometries into XYZ mode. This is an alias for ST_Force3DZ.",
            "doc_url": "https://postgis.net/docs/ST_Force3D.html",
        }
    },
    "ST_Force3DM": {
        (Geometry, float): {
            "inst": Geometry,
            "type_hint": Geometry,
            "description": "args: geomA, Mvalue = 0.0 - Force the geometries into XYM mode.",
            "doc_url": "https://postgis.net/docs/ST_Force3DM.html",
        }
    },
    "ST_Force3DZ": {
        (Geometry, float): {
            "inst": Geometry,
            "type_hint": Geometry,
            "description": "args: geomA, Zvalue = 0.0 - Force the geometries into XYZ mode.",
            "doc_url": "https://postgis.net/docs/ST_Force3DZ.html",
        }
    },
    "ST_Force4D": {
        (Geometry, float, float): {
            "inst": Geometry,
            "type_hint": Geometry,
            "description": "args: geomA, Zvalue = 0.0, Mvalue = 0.0 - Force the geometries into XYZM mode.",
            "doc_url": "https://postgis.net/docs/ST_Force4D.html",
        }
    },
    "ST_ForceCollection": {
        (Geometry,): {
            "inst": Geometry,
            "type_hint": Geometry,
            "description": "args: geomA - Convert the geometry into a GEOMETRYCOLLECTION.",
            "doc_url": "https://postgis.net/docs/ST_ForceCollection.html",
        }
    },
    "ST_ForceCurve": {
        (Geometry,): {
            "inst": Geometry,
            "type_hint": Geometry,
            "description": "args: g - Upcast a geometry into its curved type, if applicable.",
            "doc_url": "https://postgis.net/docs/ST_ForceCurve.html",
        }
    },
    "ST_ForcePolygonCCW": {
        (Geometry,): {
            "inst": Geometry,
            "type_hint": Geometry,
            "description": "args: geom - Orients all exterior rings counter-clockwise and all interior rings clockwise.",
            "doc_url": "https://postgis.net/docs/ST_ForcePolygonCCW.html",
        }
    },
    "ST_ForcePolygonCW": {
        (Geometry,): {
            "inst": Geometry,
            "type_hint": Geometry,
            "description": "args: geom - Orients all exterior rings clockwise and all interior rings counter-clockwise.",
            "doc_url": "https://postgis.net/docs/ST_ForcePolygonCW.html",
        }
    },
    "ST_ForceRHR": {
        (Geometry,): {
            "inst": Geometry,
            "type_hint": Geometry,
            "description": "args: g - Force the orientation of the vertices in a polygon to follow the Right-Hand-Rule.",
            "doc_url": "https://postgis.net/docs/ST_ForceRHR.html",
        }
    },
    "ST_ForceSFS": {
        (Geometry,): {
            "inst": Geometry,
            "type_hint": Geometry,
            "description": "args: geomA - Force the geometries to use SFS 1.1 geometry types only.",
            "doc_url": "https://postgis.net/docs/ST_ForceSFS.html",
        },
        (Geometry, str): {
            "inst": Geometry,
            "type_hint": Geometry,
            "description": "args: geomA, version - Force the geometries to use SFS 1.1 geometry types only.",
            "doc_url": "https://postgis.net/docs/ST_ForceSFS.html",
        },
    },
    "ST_FrechetDistance": {
        (Geometry, Geometry, float): {
            "inst": float,
            "type_hint": float,
            "description": "args: g1, g2, densifyFrac = -1 - Returns the Fréchet distance between two geometries.",
            "doc_url": "https://postgis.net/docs/ST_FrechetDistance.html",
        }
    },
    "ST_FromFlatGeobuf": {
        (Any, bytes): {
            "inst": object,
            "type_hint": List[Any],
            "description": "None",
            "doc_url": "https://postgis.net/docs/ST_FromFlatGeobuf.html",
        }
    },
    "ST_FromFlatGeobufToTable": {
        (str, str, bytes): {
            "inst": None,
            "type_hint": None,
            "description": "None",
            "doc_url": "https://postgis.net/docs/ST_FromFlatGeobufToTable.html",
        }
    },
    "ST_FromGDALRaster": {
        (bytes, int): {
            "inst": Raster,
            "type_hint": Raster,
            "description": "args: gdaldata, srid=NULL - Returns a raster from a supported GDAL raster file.",
            "doc_url": "https://postgis.net/docs/ST_FromGDALRaster.html",
        }
    },
    "ST_GDALDrivers": {
        (int, str, str, bool, bool, str): {
            "inst": object,
            "type_hint": List[Any],
            "description": "args: OUT idx, OUT short_name, OUT long_name, OUT can_read, OUT can_write, OUT create_options - Returns a list of raster formats supported by PostGIS through GDAL. Only those formats with can_write=True can be used by ST_AsGDALRaster",
            "doc_url": "https://postgis.net/docs/ST_GDALDrivers.html",
        }
    },
    "ST_GMLToSQL": {
        (str,): {
            "inst": Geometry,
            "type_hint": Geometry,
            "description": "None",
            "doc_url": "https://postgis.net/docs/ST_GMLToSQL.html",
        },
        (str, int): {
            "inst": Geometry,
            "type_hint": Geometry,
            "description": "None",
            "doc_url": "https://postgis.net/docs/ST_GMLToSQL.html",
        },
    },
    "ST_GeneratePoints": {
        (Geometry, int): {
            "inst": Geometry,
            "type_hint": Geometry,
            "description": "args: g, npoints - Generates random points contained in a Polygon or MultiPolygon.",
            "doc_url": "https://postgis.net/docs/ST_GeneratePoints.html",
        },
        (Geometry, int, int): {
            "inst": Geometry,
            "type_hint": Geometry,
            "description": "args: g, npoints, seed = 0 - Generates random points contained in a Polygon or MultiPolygon.",
            "doc_url": "https://postgis.net/docs/ST_GeneratePoints.html",
        },
    },
    "ST_GeoHash": {
        (Geometry, int): {
            "inst": str,
            "type_hint": str,
            "description": "None",
            "doc_url": "https://postgis.net/docs/ST_GeoHash.html",
        },
        (Geography, int): {
            "inst": str,
            "type_hint": str,
            "description": "None",
            "doc_url": "https://postgis.net/docs/ST_GeoHash.html",
        },
    },
    "ST_GeoReference": {
        (Raster, str): {
            "inst": str,
            "type_hint": str,
            "description": "args: rast, format=GDAL - Returns the georeference meta data in GDAL or ESRI format as commonly seen in a world file. Default is GDAL.",
            "doc_url": "https://postgis.net/docs/ST_GeoReference.html",
        }
    },
    "ST_GeogFromText": {
        (str,): {
            "inst": Geography,
            "type_hint": Geography,
            "description": "None",
            "doc_url": "https://postgis.net/docs/ST_GeogFromText.html",
        }
    },
    "ST_GeogFromWKB": {
        (bytes,): {
            "inst": Geography,
            "type_hint": Geography,
            "description": "None",
            "doc_url": "https://postgis.net/docs/ST_GeogFromWKB.html",
        }
    },
    "ST_GeographyFromText": {
        (str,): {
            "inst": Geography,
            "type_hint": Geography,
            "description": "None",
            "doc_url": "https://postgis.net/docs/ST_GeographyFromText.html",
        }
    },
    "ST_GeomCollFromText": {
        (str, int): {
            "inst": Geometry,
            "type_hint": Geometry,
            "description": "None",
            "doc_url": "https://postgis.net/docs/ST_GeomCollFromText.html",
        },
        (str,): {
            "inst": Geometry,
            "type_hint": Geometry,
            "description": "None",
            "doc_url": "https://postgis.net/docs/ST_GeomCollFromText.html",
        },
    },
    "ST_GeomFromEWKB": {
        (bytes,): {
            "inst": Geometry,
            "type_hint": Geometry,
            "description": "None",
            "doc_url": "https://postgis.net/docs/ST_GeomFromEWKB.html",
        }
    },
    "ST_GeomFromEWKT": {
        (str,): {
            "inst": Geometry,
            "type_hint": Geometry,
            "description": "None",
            "doc_url": "https://postgis.net/docs/ST_GeomFromEWKT.html",
        }
    },
    "ST_GeomFromGML": {
        (str, int): {
            "inst": Geometry,
            "type_hint": Geometry,
            "description": "None",
            "doc_url": "https://postgis.net/docs/ST_GeomFromGML.html",
        },
        (str,): {
            "inst": Geometry,
            "type_hint": Geometry,
            "description": "None",
            "doc_url": "https://postgis.net/docs/ST_GeomFromGML.html",
        },
    },
    "ST_GeomFromGeoHash": {
        (str, int): {
            "inst": Geometry,
            "type_hint": Geometry,
            "description": "None",
            "doc_url": "https://postgis.net/docs/ST_GeomFromGeoHash.html",
        }
    },
    "ST_GeomFromGeoJSON": {
        (str,): {
            "inst": Geometry,
            "type_hint": Geometry,
            "description": "None",
            "doc_url": "https://postgis.net/docs/ST_GeomFromGeoJSON.html",
        },
        (bytes,): {
            "inst": Geometry,
            "type_hint": Geometry,
            "description": "None",
            "doc_url": "https://postgis.net/docs/ST_GeomFromGeoJSON.html",
        },
    },
    "ST_GeomFromKML": {
        (str,): {
            "inst": Geometry,
            "type_hint": Geometry,
            "description": "None",
            "doc_url": "https://postgis.net/docs/ST_GeomFromKML.html",
        }
    },
    "ST_GeomFromMARC21": {
        (str,): {
            "inst": Geometry,
            "type_hint": Geometry,
            "description": "None",
            "doc_url": "https://postgis.net/docs/ST_GeomFromMARC21.html",
        }
    },
    "ST_GeomFromTWKB": {
        (bytes,): {
            "inst": Geometry,
            "type_hint": Geometry,
            "description": "None",
            "doc_url": "https://postgis.net/docs/ST_GeomFromTWKB.html",
        }
    },
    "ST_GeomFromText": {
        (str,): {
            "inst": Geometry,
            "type_hint": Geometry,
            "description": "None",
            "doc_url": "https://postgis.net/docs/ST_GeomFromText.html",
        },
        (str, int): {
            "inst": Geometry,
            "type_hint": Geometry,
            "description": "None",
            "doc_url": "https://postgis.net/docs/ST_GeomFromText.html",
        },
    },
    "ST_GeomFromWKB": {
        (bytes,): {
            "inst": Geometry,
            "type_hint": Geometry,
            "description": "None",
            "doc_url": "https://postgis.net/docs/ST_GeomFromWKB.html",
        },
        (bytes, int): {
            "inst": Geometry,
            "type_hint": Geometry,
            "description": "None",
            "doc_url": "https://postgis.net/docs/ST_GeomFromWKB.html",
        },
    },
    "ST_GeometricMedian": {
        (Geometry, float, int, bool): {
            "inst": Geometry,
            "type_hint": Geometry,
            "description": "args: geom, tolerance = NULL, max_iter = 10000, fail_if_not_converged = false - Returns the geometric median of a MultiPoint.",
            "doc_url": "https://postgis.net/docs/ST_GeometricMedian.html",
        }
    },
    "ST_GeometryFromText": {
        (str,): {
            "inst": Geometry,
            "type_hint": Geometry,
            "description": "None",
            "doc_url": "https://postgis.net/docs/ST_GeometryFromText.html",
        },
        (str, int): {
            "inst": Geometry,
            "type_hint": Geometry,
            "description": "None",
            "doc_url": "https://postgis.net/docs/ST_GeometryFromText.html",
        },
    },
    "ST_GeometryN": {
        (Geometry, int): {
            "inst": Geometry,
            "type_hint": Geometry,
            "description": "args: geomA, n - Return an element of a geometry collection.",
            "doc_url": "https://postgis.net/docs/ST_GeometryN.html",
        }
    },
    "ST_GeometryType": {
        (Geometry,): {
            "inst": str,
            "type_hint": str,
            "description": "args: g1 - Returns the SQL-MM type of a geometry as text.",
            "doc_url": "https://postgis.net/docs/ST_GeometryType.html",
        }
    },
    "ST_Grayscale": {
        (List[Any], str): {
            "inst": Raster,
            "type_hint": Raster,
            "description": "args: rastbandargset, extenttype=INTERSECTION - Creates a new one-8BUI band raster from the source raster and specified bands representing Red, Green and Blue",
            "doc_url": "https://postgis.net/docs/ST_Grayscale.html",
        },
        (Raster, int, int, int, str): {
            "inst": Raster,
            "type_hint": Raster,
            "description": "args: rast, redband=1, greenband=2, blueband=3, extenttype=INTERSECTION - Creates a new one-8BUI band raster from the source raster and specified bands representing Red, Green and Blue",
            "doc_url": "https://postgis.net/docs/ST_Grayscale.html",
        },
    },
    "ST_HasArc": {
        (Geometry,): {
            "inst": bool,
            "type_hint": bool,
            "description": "args: geomA - Tests if a geometry contains a circular arc",
            "doc_url": "https://postgis.net/docs/ST_HasArc.html",
        }
    },
    "ST_HasNoBand": {
        (Raster, int): {
            "inst": bool,
            "type_hint": bool,
            "description": "args: rast, bandnum=1 - Returns true if there is no band with given band number. If no band number is specified, then band number 1 is assumed.",
            "doc_url": "https://postgis.net/docs/ST_HasNoBand.html",
        }
    },
    "ST_HausdorffDistance": {
        (Geometry, Geometry): {
            "inst": float,
            "type_hint": float,
            "description": "args: g1, g2 - Returns the Hausdorff distance between two geometries.",
            "doc_url": "https://postgis.net/docs/ST_HausdorffDistance.html",
        },
        (Geometry, Geometry, float): {
            "inst": float,
            "type_hint": float,
            "description": "args: g1, g2, densifyFrac - Returns the Hausdorff distance between two geometries.",
            "doc_url": "https://postgis.net/docs/ST_HausdorffDistance.html",
        },
    },
    "ST_Height": {
        (Raster,): {
            "inst": int,
            "type_hint": int,
            "description": "args: rast - Returns the height of the raster in pixels.",
            "doc_url": "https://postgis.net/docs/ST_Height.html",
        }
    },
    "ST_Hexagon": {
        (float, int, int, Geometry): {
            "inst": Geometry,
            "type_hint": Geometry,
            "description": "args: size, cell_i, cell_j, origin - Returns a single hexagon, using the provided edge size and cell coordinate within the hexagon grid space.",
            "doc_url": "https://postgis.net/docs/ST_Hexagon.html",
        }
    },
    "ST_HexagonGrid": {
        (float, Geometry, Geometry, int, int): {
            "inst": object,
            "type_hint": List[Any],
            "description": "args: size, bounds - Returns a set of hexagons and cell indices that completely cover the bounds of the geometry argument.",
            "doc_url": "https://postgis.net/docs/ST_HexagonGrid.html",
        }
    },
    "ST_HillShade": {
        (Raster, int, Raster, str, float, float, float, float, bool): {
            "inst": Raster,
            "type_hint": Raster,
            "description": "args: rast, band, customextent, pixeltype=32BF, azimuth=315, altitude=45, max_bright=255, scale=1.0, interpolate_nodata=FALSE - Returns the hypothetical illumination of an elevation raster band using provided azimuth, altitude, brightness and scale inputs.",
            "doc_url": "https://postgis.net/docs/ST_HillShade.html",
        },
        (Raster, int, str, float, float, float, float, bool): {
            "inst": Raster,
            "type_hint": Raster,
            "description": "args: rast, band=1, pixeltype=32BF, azimuth=315, altitude=45, max_bright=255, scale=1.0, interpolate_nodata=FALSE - Returns the hypothetical illumination of an elevation raster band using provided azimuth, altitude, brightness and scale inputs.",
            "doc_url": "https://postgis.net/docs/ST_HillShade.html",
        },
    },
    "ST_Histogram": {
        (Raster, int, bool, int, List[float], bool, float, float, int, float): {
            "inst": object,
            "type_hint": List[Any],
            "description": "args: rast, nband=1, exclude_nodata_value=true, bins=autocomputed, width=NULL, right=false - Returns a set of record summarizing a raster or raster coverage data distribution separate bin ranges. Number of bins are autocomputed if not specified.",
            "doc_url": "https://postgis.net/docs/ST_Histogram.html",
        },
        (Raster, int, bool, int, bool, float, float, int, float): {
            "inst": object,
            "type_hint": List[Any],
            "description": "args: rast, nband, exclude_nodata_value, bins, right - Returns a set of record summarizing a raster or raster coverage data distribution separate bin ranges. Number of bins are autocomputed if not specified.",
            "doc_url": "https://postgis.net/docs/ST_Histogram.html",
        },
        (Raster, int, int, List[float], bool, float, float, int, float): {
            "inst": object,
            "type_hint": List[Any],
            "description": "args: rast, nband, bins, width=NULL, right=false - Returns a set of record summarizing a raster or raster coverage data distribution separate bin ranges. Number of bins are autocomputed if not specified.",
            "doc_url": "https://postgis.net/docs/ST_Histogram.html",
        },
        (Raster, int, int, bool, float, float, int, float): {
            "inst": object,
            "type_hint": List[Any],
            "description": "args: rast, nband, bins, right - Returns a set of record summarizing a raster or raster coverage data distribution separate bin ranges. Number of bins are autocomputed if not specified.",
            "doc_url": "https://postgis.net/docs/ST_Histogram.html",
        },
    },
    "ST_InteriorRingN": {
        (Geometry, int): {
            "inst": Geometry,
            "type_hint": Geometry,
            "description": "args: a_polygon, n - Returns the Nth interior ring (hole) of a Polygon.",
            "doc_url": "https://postgis.net/docs/ST_InteriorRingN.html",
        }
    },
    "ST_InterpolatePoint": {
        (Geometry, Geometry): {
            "inst": float,
            "type_hint": float,
            "description": "args: linear_geom_with_measure, point - Returns the interpolated measure of a geometry closest to a point.",
            "doc_url": "https://postgis.net/docs/ST_InterpolatePoint.html",
        }
    },
    "ST_InterpolateRaster": {
        (Geometry, str, Raster, int): {
            "inst": Raster,
            "type_hint": Raster,
            "description": "args: input_points, algorithm_options, template, template_band_num=1 - Interpolates a gridded surface based on an input set of 3-d points, using the X- and Y-values to position the points on the grid and the Z-value of the points as the surface elevation.",
            "doc_url": "https://postgis.net/docs/ST_InterpolateRaster.html",
        }
    },
    "ST_Intersection": {
        (Geometry, Geometry, float): {
            "inst": Geometry,
            "type_hint": Geometry,
            "description": "args: geomA, geomB, gridSize = -1 - Computes a geometry representing the shared portion of geometries A and B.",
            "doc_url": "https://postgis.net/docs/ST_Intersection.html",
        },
        (Geography, Geography): {
            "inst": Geography,
            "type_hint": Geography,
            "description": "args: geogA, geogB - Computes a geometry representing the shared portion of geometries A and B.",
            "doc_url": "https://postgis.net/docs/ST_Intersection.html",
        },
        (str, str): {
            "inst": Geometry,
            "type_hint": Geometry,
            "description": "None",
            "doc_url": "https://postgis.net/docs/ST_Intersection.html",
        },
        (Geometry, Raster, int): {
            "inst": GeomVal,
            "type_hint": List[GeomVal],
            "description": "args: geom, rast, band_num=1 - Returns a raster or a set of geometry-pixelvalue pairs representing the shared portion of two rasters or the geometrical intersection of a vectorization of the raster and a geometry.",
            "doc_url": "https://postgis.net/docs/ST_Intersection.html",
        },
        (Raster, int, Geometry): {
            "inst": GeomVal,
            "type_hint": List[GeomVal],
            "description": "args: rast, band, geomin - Returns a raster or a set of geometry-pixelvalue pairs representing the shared portion of two rasters or the geometrical intersection of a vectorization of the raster and a geometry.",
            "doc_url": "https://postgis.net/docs/ST_Intersection.html",
        },
        (Raster, Geometry): {
            "inst": GeomVal,
            "type_hint": List[GeomVal],
            "description": "args: rast, geom - Returns a raster or a set of geometry-pixelvalue pairs representing the shared portion of two rasters or the geometrical intersection of a vectorization of the raster and a geometry.",
            "doc_url": "https://postgis.net/docs/ST_Intersection.html",
        },
        (Raster, int, Raster, int, str, List[float]): {
            "inst": Raster,
            "type_hint": Raster,
            "description": "args: rast1, band1, rast2, band2, returnband, nodataval - Returns a raster or a set of geometry-pixelvalue pairs representing the shared portion of two rasters or the geometrical intersection of a vectorization of the raster and a geometry.",
            "doc_url": "https://postgis.net/docs/ST_Intersection.html",
        },
        (Raster, int, Raster, int, str, float): {
            "inst": Raster,
            "type_hint": Raster,
            "description": "None",
            "doc_url": "https://postgis.net/docs/ST_Intersection.html",
        },
        (Raster, int, Raster, int, List[float]): {
            "inst": Raster,
            "type_hint": Raster,
            "description": "args: rast1, band1, rast2, band2, nodataval - Returns a raster or a set of geometry-pixelvalue pairs representing the shared portion of two rasters or the geometrical intersection of a vectorization of the raster and a geometry.",
            "doc_url": "https://postgis.net/docs/ST_Intersection.html",
        },
        (Raster, int, Raster, int, float): {
            "inst": Raster,
            "type_hint": Raster,
            "description": "None",
            "doc_url": "https://postgis.net/docs/ST_Intersection.html",
        },
        (Raster, Raster, str, List[float]): {
            "inst": Raster,
            "type_hint": Raster,
            "description": "args: rast1, rast2, returnband, nodataval - Returns a raster or a set of geometry-pixelvalue pairs representing the shared portion of two rasters or the geometrical intersection of a vectorization of the raster and a geometry.",
            "doc_url": "https://postgis.net/docs/ST_Intersection.html",
        },
        (Raster, Raster, str, float): {
            "inst": Raster,
            "type_hint": Raster,
            "description": "None",
            "doc_url": "https://postgis.net/docs/ST_Intersection.html",
        },
        (Raster, Raster, List[float]): {
            "inst": Raster,
            "type_hint": Raster,
            "description": "args: rast1, rast2, nodataval - Returns a raster or a set of geometry-pixelvalue pairs representing the shared portion of two rasters or the geometrical intersection of a vectorization of the raster and a geometry.",
            "doc_url": "https://postgis.net/docs/ST_Intersection.html",
        },
        (Raster, Raster, float): {
            "inst": Raster,
            "type_hint": Raster,
            "description": "None",
            "doc_url": "https://postgis.net/docs/ST_Intersection.html",
        },
    },
    "ST_Intersects": {
        (Geometry, Geometry): {
            "inst": bool,
            "type_hint": bool,
            "description": "None",
            "doc_url": "https://postgis.net/docs/ST_Intersects.html",
        },
        (Geography, Geography): {
            "inst": bool,
            "type_hint": bool,
            "description": "None",
            "doc_url": "https://postgis.net/docs/ST_Intersects.html",
        },
        (str, str): {
            "inst": bool,
            "type_hint": bool,
            "description": "None",
            "doc_url": "https://postgis.net/docs/ST_Intersects.html",
        },
        (Raster, int, Raster, int): {
            "inst": bool,
            "type_hint": bool,
            "description": "args: rastA, nbandA, rastB, nbandB - Return true if raster rastA spatially intersects raster rastB.",
            "doc_url": "https://postgis.net/docs/ST_Intersects.html",
        },
        (Raster, Raster): {
            "inst": bool,
            "type_hint": bool,
            "description": "args: rastA, rastB - Return true if raster rastA spatially intersects raster rastB.",
            "doc_url": "https://postgis.net/docs/ST_Intersects.html",
        },
        (Geometry, Raster, int): {
            "inst": bool,
            "type_hint": bool,
            "description": "args: geommin, rast, nband=NULL - Return true if raster rastA spatially intersects raster rastB.",
            "doc_url": "https://postgis.net/docs/ST_Intersects.html",
        },
        (Raster, Geometry, int): {
            "inst": bool,
            "type_hint": bool,
            "description": "args: rast, geommin, nband=NULL - Return true if raster rastA spatially intersects raster rastB.",
            "doc_url": "https://postgis.net/docs/ST_Intersects.html",
        },
        (Raster, int, Geometry): {
            "inst": bool,
            "type_hint": bool,
            "description": "args: rast, nband, geommin - Return true if raster rastA spatially intersects raster rastB.",
            "doc_url": "https://postgis.net/docs/ST_Intersects.html",
        },
    },
    "ST_InvDistWeight4ma": {
        (List[float], List[int], List[Any]): {
            "inst": float,
            "type_hint": float,
            "description": "args: value, pos, VARIADIC userargs - Raster processing function that interpolates a pixels value from the pixels neighborhood.",
            "doc_url": "https://postgis.net/docs/ST_InvDistWeight4ma.html",
        }
    },
    "ST_InverseTransformPipeline": {
        (Geometry, str, int): {
            "inst": Geometry,
            "type_hint": Geometry,
            "description": "args: geom, pipeline, to_srid - Return a new geometry with coordinates transformed to a different spatial reference system using the inverse of a defined coordinate transformation pipeline.",
            "doc_url": "https://postgis.net/docs/ST_InverseTransformPipeline.html",
        }
    },
    "ST_IsClosed": {
        (Geometry,): {
            "inst": bool,
            "type_hint": bool,
            "description": "args: g - Tests if a LineStringss start and end points are coincident. For a PolyhedralSurface tests if it is closed (volumetric).",
            "doc_url": "https://postgis.net/docs/ST_IsClosed.html",
        }
    },
    "ST_IsCollection": {
        (Geometry,): {
            "inst": bool,
            "type_hint": bool,
            "description": "args: g - Tests if a geometry is a geometry collection type.",
            "doc_url": "https://postgis.net/docs/ST_IsCollection.html",
        }
    },
    "ST_IsEmpty": {
        (Geometry,): {
            "inst": bool,
            "type_hint": bool,
            "description": "args: geomA - Tests if a geometry is empty.",
            "doc_url": "https://postgis.net/docs/ST_IsEmpty.html",
        },
        (Raster,): {
            "inst": bool,
            "type_hint": bool,
            "description": "args: rast - Returns true if the raster is empty (width = 0 and height = 0). Otherwise, returns false.",
            "doc_url": "https://postgis.net/docs/ST_IsEmpty.html",
        },
    },
    "ST_IsPolygonCCW": {
        (Geometry,): {
            "inst": bool,
            "type_hint": bool,
            "description": "args: geom - Tests if Polygons have exterior rings oriented counter-clockwise and interior rings oriented clockwise.",
            "doc_url": "https://postgis.net/docs/ST_IsPolygonCCW.html",
        }
    },
    "ST_IsPolygonCW": {
        (Geometry,): {
            "inst": bool,
            "type_hint": bool,
            "description": "args: geom - Tests if Polygons have exterior rings oriented clockwise and interior rings oriented counter-clockwise.",
            "doc_url": "https://postgis.net/docs/ST_IsPolygonCW.html",
        }
    },
    "ST_IsRing": {
        (Geometry,): {
            "inst": bool,
            "type_hint": bool,
            "description": "args: g - Tests if a LineString is closed and simple.",
            "doc_url": "https://postgis.net/docs/ST_IsRing.html",
        }
    },
    "ST_IsSimple": {
        (Geometry,): {
            "inst": bool,
            "type_hint": bool,
            "description": "args: geomA - Tests if a geometry has no points of self-intersection or self-tangency.",
            "doc_url": "https://postgis.net/docs/ST_IsSimple.html",
        }
    },
    "ST_IsValid": {
        (Geometry, int): {
            "inst": bool,
            "type_hint": bool,
            "description": "args: g, flags - Tests if a geometry is well-formed in 2D.",
            "doc_url": "https://postgis.net/docs/ST_IsValid.html",
        },
        (Geometry,): {
            "inst": bool,
            "type_hint": bool,
            "description": "args: g - Tests if a geometry is well-formed in 2D.",
            "doc_url": "https://postgis.net/docs/ST_IsValid.html",
        },
    },
    "ST_IsValidDetail": {
        (Geometry, int): {
            "inst": object,
            "type_hint": Any,
            "description": "args: geom, flags - Returns a valid_detail row stating if a geometry is valid or if not a reason and a location.",
            "doc_url": "https://postgis.net/docs/ST_IsValidDetail.html",
        }
    },
    "ST_IsValidReason": {
        (Geometry,): {
            "inst": str,
            "type_hint": str,
            "description": "args: geomA - Returns text stating if a geometry is valid, or a reason for invalidity.",
            "doc_url": "https://postgis.net/docs/ST_IsValidReason.html",
        },
        (Geometry, int): {
            "inst": str,
            "type_hint": str,
            "description": "args: geomA, flags - Returns text stating if a geometry is valid, or a reason for invalidity.",
            "doc_url": "https://postgis.net/docs/ST_IsValidReason.html",
        },
    },
    "ST_IsValidTrajectory": {
        (Geometry,): {
            "inst": bool,
            "type_hint": bool,
            "description": "args: line - Tests if the geometry is a valid trajectory.",
            "doc_url": "https://postgis.net/docs/ST_IsValidTrajectory.html",
        }
    },
    "ST_LargestEmptyCircle": {
        (Geometry, float, Geometry, Geometry, Geometry, float): {
            "inst": object,
            "type_hint": Any,
            "description": "args: geom, tolerance=0.0, boundary=POINT EMPTY - Computes the largest circle not overlapping a geometry.",
            "doc_url": "https://postgis.net/docs/ST_LargestEmptyCircle.html",
        }
    },
    "ST_Length": {
        (Geometry,): {
            "inst": float,
            "type_hint": float,
            "description": "args: a_2dlinestring - Returns the 2D length of a linear geometry.",
            "doc_url": "https://postgis.net/docs/ST_Length.html",
        },
        (Geography, bool): {
            "inst": float,
            "type_hint": float,
            "description": "args: geog, use_spheroid = true - Returns the 2D length of a linear geometry.",
            "doc_url": "https://postgis.net/docs/ST_Length.html",
        },
        (str,): {
            "inst": float,
            "type_hint": float,
            "description": "None",
            "doc_url": "https://postgis.net/docs/ST_Length.html",
        },
    },
    "ST_Length2D": {
        (Geometry,): {
            "inst": float,
            "type_hint": float,
            "description": "args: a_2dlinestring - Returns the 2D length of a linear geometry. Alias for ST_Length",
            "doc_url": "https://postgis.net/docs/ST_Length2D.html",
        }
    },
    "ST_LengthSpheroid": {
        (Geometry, str): {
            "inst": float,
            "type_hint": float,
            "description": "args: a_geometry, a_spheroid - Returns the 2D or 3D length/perimeter of a lon/lat geometry on a spheroid.",
            "doc_url": "https://postgis.net/docs/ST_LengthSpheroid.html",
        }
    },
    "ST_Letters": {
        (str, str): {
            "inst": Geometry,
            "type_hint": Geometry,
            "description": "args:  letters,  font - Returns the input letters rendered as geometry with a default start position at the origin and default text height of 100.",
            "doc_url": "https://postgis.net/docs/ST_Letters.html",
        }
    },
    "ST_LineCrossingDirection": {
        (Geometry, Geometry): {
            "inst": int,
            "type_hint": int,
            "description": "None",
            "doc_url": "https://postgis.net/docs/ST_LineCrossingDirection.html",
        }
    },
    "ST_LineFromEncodedPolyline": {
        (str, int): {
            "inst": Geometry,
            "type_hint": Geometry,
            "description": "None",
            "doc_url": "https://postgis.net/docs/ST_LineFromEncodedPolyline.html",
        }
    },
    "ST_LineFromMultiPoint": {
        (Geometry,): {
            "inst": Geometry,
            "type_hint": Geometry,
            "description": "args: aMultiPoint - Creates a LineString from a MultiPoint geometry.",
            "doc_url": "https://postgis.net/docs/ST_LineFromMultiPoint.html",
        }
    },
    "ST_LineFromText": {
        (str,): {
            "inst": Geometry,
            "type_hint": Geometry,
            "description": "None",
            "doc_url": "https://postgis.net/docs/ST_LineFromText.html",
        },
        (str, int): {
            "inst": Geometry,
            "type_hint": Geometry,
            "description": "None",
            "doc_url": "https://postgis.net/docs/ST_LineFromText.html",
        },
    },
    "ST_LineFromWKB": {
        (bytes, int): {
            "inst": Geometry,
            "type_hint": Geometry,
            "description": "None",
            "doc_url": "https://postgis.net/docs/ST_LineFromWKB.html",
        },
        (bytes,): {
            "inst": Geometry,
            "type_hint": Geometry,
            "description": "None",
            "doc_url": "https://postgis.net/docs/ST_LineFromWKB.html",
        },
    },
    "ST_LineInterpolatePoint": {
        (Geometry, float): {
            "inst": Geometry,
            "type_hint": Geometry,
            "description": "args: a_linestring, a_fraction - Returns a point interpolated along a line at a fractional location.",
            "doc_url": "https://postgis.net/docs/ST_LineInterpolatePoint.html",
        },
        (Geography, float, bool): {
            "inst": Geography,
            "type_hint": Geography,
            "description": "args: a_linestring, a_fraction, use_spheroid = true - Returns a point interpolated along a line at a fractional location.",
            "doc_url": "https://postgis.net/docs/ST_LineInterpolatePoint.html",
        },
        (str, float): {
            "inst": Geometry,
            "type_hint": Geometry,
            "description": "None",
            "doc_url": "https://postgis.net/docs/ST_LineInterpolatePoint.html",
        },
    },
    "ST_LineInterpolatePoints": {
        (Geometry, float, bool): {
            "inst": Geometry,
            "type_hint": Geometry,
            "description": "args: a_linestring, a_fraction, repeat - Returns points interpolated along a line at a fractional interval.",
            "doc_url": "https://postgis.net/docs/ST_LineInterpolatePoints.html",
        },
        (Geography, float, bool, bool): {
            "inst": Geography,
            "type_hint": Geography,
            "description": "args: a_linestring, a_fraction, use_spheroid = true, repeat = true - Returns points interpolated along a line at a fractional interval.",
            "doc_url": "https://postgis.net/docs/ST_LineInterpolatePoints.html",
        },
        (str, float): {
            "inst": Geometry,
            "type_hint": Geometry,
            "description": "None",
            "doc_url": "https://postgis.net/docs/ST_LineInterpolatePoints.html",
        },
    },
    "ST_LineLocatePoint": {
        (Geometry, Geometry): {
            "inst": float,
            "type_hint": float,
            "description": "args: a_linestring, a_point - Returns the fractional location of the closest point on a line to a point.",
            "doc_url": "https://postgis.net/docs/ST_LineLocatePoint.html",
        },
        (Geography, Geography, bool): {
            "inst": float,
            "type_hint": float,
            "description": "args: a_linestring, a_point, use_spheroid = true - Returns the fractional location of the closest point on a line to a point.",
            "doc_url": "https://postgis.net/docs/ST_LineLocatePoint.html",
        },
        (str, str): {
            "inst": float,
            "type_hint": float,
            "description": "None",
            "doc_url": "https://postgis.net/docs/ST_LineLocatePoint.html",
        },
    },
    "ST_LineMerge": {
        (Geometry,): {
            "inst": Geometry,
            "type_hint": Geometry,
            "description": "args: amultilinestring - Return the lines formed by sewing together a MultiLineString.",
            "doc_url": "https://postgis.net/docs/ST_LineMerge.html",
        },
        (Geometry, bool): {
            "inst": Geometry,
            "type_hint": Geometry,
            "description": "args: amultilinestring, directed - Return the lines formed by sewing together a MultiLineString.",
            "doc_url": "https://postgis.net/docs/ST_LineMerge.html",
        },
    },
    "ST_LineSubstring": {
        (Geometry, float, float): {
            "inst": Geometry,
            "type_hint": Geometry,
            "description": "args: a_linestring, startfraction, endfraction - Returns the part of a line between two fractional locations.",
            "doc_url": "https://postgis.net/docs/ST_LineSubstring.html",
        },
        (Geography, float, float): {
            "inst": Geography,
            "type_hint": Geography,
            "description": "args: a_linestring, startfraction, endfraction - Returns the part of a line between two fractional locations.",
            "doc_url": "https://postgis.net/docs/ST_LineSubstring.html",
        },
        (str, float, float): {
            "inst": Geometry,
            "type_hint": Geometry,
            "description": "None",
            "doc_url": "https://postgis.net/docs/ST_LineSubstring.html",
        },
    },
    "ST_LineToCurve": {
        (Geometry,): {
            "inst": Geometry,
            "type_hint": Geometry,
            "description": "args: geomANoncircular - Converts a linear geometry to a curved geometry.",
            "doc_url": "https://postgis.net/docs/ST_LineToCurve.html",
        }
    },
    "ST_LinestringFromWKB": {
        (bytes, int): {
            "inst": Geometry,
            "type_hint": Geometry,
            "description": "None",
            "doc_url": "https://postgis.net/docs/ST_LinestringFromWKB.html",
        },
        (bytes,): {
            "inst": Geometry,
            "type_hint": Geometry,
            "description": "None",
            "doc_url": "https://postgis.net/docs/ST_LinestringFromWKB.html",
        },
    },
    "ST_LocateAlong": {
        (Geometry, float, float): {
            "inst": Geometry,
            "type_hint": Geometry,
            "description": "args: geom_with_measure, measure, offset = 0 - Returns the point(s) on a geometry that match a measure value.",
            "doc_url": "https://postgis.net/docs/ST_LocateAlong.html",
        }
    },
    "ST_LocateBetween": {
        (Geometry, float, float, float): {
            "inst": Geometry,
            "type_hint": Geometry,
            "description": "args: geom, measure_start, measure_end, offset = 0 - Returns the portions of a geometry that match a measure range.",
            "doc_url": "https://postgis.net/docs/ST_LocateBetween.html",
        }
    },
    "ST_LocateBetweenElevations": {
        (Geometry, float, float): {
            "inst": Geometry,
            "type_hint": Geometry,
            "description": "args: geom, elevation_start, elevation_end - Returns the portions of a geometry that lie in an elevation (Z) range.",
            "doc_url": "https://postgis.net/docs/ST_LocateBetweenElevations.html",
        }
    },
    "ST_LongestLine": {
        (Geometry, Geometry): {
            "inst": Geometry,
            "type_hint": Geometry,
            "description": "args: g1, g2 - Returns the 2D longest line between two geometries.",
            "doc_url": "https://postgis.net/docs/ST_LongestLine.html",
        }
    },
    "ST_M": {
        (Geometry,): {
            "inst": float,
            "type_hint": float,
            "description": "args: a_point - Returns the M coordinate of a Point.",
            "doc_url": "https://postgis.net/docs/ST_M.html",
        }
    },
    "ST_MLineFromText": {
        (str, int): {
            "inst": Geometry,
            "type_hint": Geometry,
            "description": "None",
            "doc_url": "https://postgis.net/docs/ST_MLineFromText.html",
        },
        (str,): {
            "inst": Geometry,
            "type_hint": Geometry,
            "description": "None",
            "doc_url": "https://postgis.net/docs/ST_MLineFromText.html",
        },
    },
    "ST_MPointFromText": {
        (str, int): {
            "inst": Geometry,
            "type_hint": Geometry,
            "description": "None",
            "doc_url": "https://postgis.net/docs/ST_MPointFromText.html",
        },
        (str,): {
            "inst": Geometry,
            "type_hint": Geometry,
            "description": "None",
            "doc_url": "https://postgis.net/docs/ST_MPointFromText.html",
        },
    },
    "ST_MPolyFromText": {
        (str, int): {
            "inst": Geometry,
            "type_hint": Geometry,
            "description": "None",
            "doc_url": "https://postgis.net/docs/ST_MPolyFromText.html",
        },
        (str,): {
            "inst": Geometry,
            "type_hint": Geometry,
            "description": "None",
            "doc_url": "https://postgis.net/docs/ST_MPolyFromText.html",
        },
    },
    "ST_MakeBox2D": {
        (Geometry, Geometry): {
            "inst": Geometry,
            "type_hint": Geometry,
            "description": "args: pointLowLeft, pointUpRight - Creates a BOX2D defined by two 2D point geometries.",
            "doc_url": "https://postgis.net/docs/ST_MakeBox2D.html",
        }
    },
    "ST_MakeEmptyCoverage": {
        (int, int, int, int, float, float, float, float, float, float, int): {
            "inst": Raster,
            "type_hint": List[Raster],
            "description": "args: tilewidth, tileheight, width, height, upperleftx, upperlefty, scalex, scaley, skewx, skewy, srid=unknown - Cover georeferenced area with a grid of empty raster tiles.",
            "doc_url": "https://postgis.net/docs/ST_MakeEmptyCoverage.html",
        }
    },
    "ST_MakeEmptyRaster": {
        (int, int, float, float, float, float, float, float, int): {
            "inst": Raster,
            "type_hint": Raster,
            "description": "args: width, height, upperleftx, upperlefty, scalex, scaley, skewx, skewy, srid=unknown - Returns an empty raster (having no bands) of given dimensions (width & height), upperleft X and Y, pixel size and rotation (scalex, scaley, skewx & skewy) and reference system (srid). If a raster is passed in, returns a new raster with the same size, alignment and SRID. If srid is left out, the spatial ref is set to unknown (0).",
            "doc_url": "https://postgis.net/docs/ST_MakeEmptyRaster.html",
        },
        (int, int, float, float, float): {
            "inst": Raster,
            "type_hint": Raster,
            "description": "args: width, height, upperleftx, upperlefty, pixelsize - Returns an empty raster (having no bands) of given dimensions (width & height), upperleft X and Y, pixel size and rotation (scalex, scaley, skewx & skewy) and reference system (srid). If a raster is passed in, returns a new raster with the same size, alignment and SRID. If srid is left out, the spatial ref is set to unknown (0).",
            "doc_url": "https://postgis.net/docs/ST_MakeEmptyRaster.html",
        },
        (Raster,): {
            "inst": Raster,
            "type_hint": Raster,
            "description": "args: rast - Returns an empty raster (having no bands) of given dimensions (width & height), upperleft X and Y, pixel size and rotation (scalex, scaley, skewx & skewy) and reference system (srid). If a raster is passed in, returns a new raster with the same size, alignment and SRID. If srid is left out, the spatial ref is set to unknown (0).",
            "doc_url": "https://postgis.net/docs/ST_MakeEmptyRaster.html",
        },
    },
    "ST_MakeEnvelope": {
        (float, float, float, float, int): {
            "inst": Geometry,
            "type_hint": Geometry,
            "description": "args: xmin, ymin, xmax, ymax, srid=unknown - Creates a rectangular Polygon from minimum and maximum coordinates.",
            "doc_url": "https://postgis.net/docs/ST_MakeEnvelope.html",
        }
    },
    "ST_MakeLine": {
        (Geometry,): {
            "inst": Geometry,
            "type_hint": Geometry,
            "description": "args: geoms - Creates a LineString from Point, MultiPoint, or LineString geometries.",
            "doc_url": "https://postgis.net/docs/ST_MakeLine.html",
        },
        (List[Geometry],): {
            "inst": Geometry,
            "type_hint": Geometry,
            "description": "args: geoms_array - Creates a LineString from Point, MultiPoint, or LineString geometries.",
            "doc_url": "https://postgis.net/docs/ST_MakeLine.html",
        },
        (Geometry, Geometry): {
            "inst": Geometry,
            "type_hint": Geometry,
            "description": "args: geom1, geom2 - Creates a LineString from Point, MultiPoint, or LineString geometries.",
            "doc_url": "https://postgis.net/docs/ST_MakeLine.html",
        },
    },
    "ST_MakePoint": {
        (float, float): {
            "inst": Geometry,
            "type_hint": Geometry,
            "description": "args: x, y - Creates a 2D, 3DZ or 4D Point.",
            "doc_url": "https://postgis.net/docs/ST_MakePoint.html",
        },
        (float, float, float): {
            "inst": Geometry,
            "type_hint": Geometry,
            "description": "args: x, y, z - Creates a 2D, 3DZ or 4D Point.",
            "doc_url": "https://postgis.net/docs/ST_MakePoint.html",
        },
        (float, float, float, float): {
            "inst": Geometry,
            "type_hint": Geometry,
            "description": "args: x, y, z, m - Creates a 2D, 3DZ or 4D Point.",
            "doc_url": "https://postgis.net/docs/ST_MakePoint.html",
        },
    },
    "ST_MakePointM": {
        (float, float, float): {
            "inst": Geometry,
            "type_hint": Geometry,
            "description": "args: x, y, m - Creates a Point from X, Y and M values.",
            "doc_url": "https://postgis.net/docs/ST_MakePointM.html",
        }
    },
    "ST_MakePolygon": {
        (Geometry, List[Geometry]): {
            "inst": Geometry,
            "type_hint": Geometry,
            "description": "args: outerlinestring, interiorlinestrings - Creates a Polygon from a shell and optional list of holes.",
            "doc_url": "https://postgis.net/docs/ST_MakePolygon.html",
        },
        (Geometry,): {
            "inst": Geometry,
            "type_hint": Geometry,
            "description": "args: linestring - Creates a Polygon from a shell and optional list of holes.",
            "doc_url": "https://postgis.net/docs/ST_MakePolygon.html",
        },
    },
    "ST_MakeValid": {
        (Geometry,): {
            "inst": Geometry,
            "type_hint": Geometry,
            "description": "args: input - Attempts to make an invalid geometry valid without losing vertices.",
            "doc_url": "https://postgis.net/docs/ST_MakeValid.html",
        },
        (Geometry, str): {
            "inst": Geometry,
            "type_hint": Geometry,
            "description": "args: input, params - Attempts to make an invalid geometry valid without losing vertices.",
            "doc_url": "https://postgis.net/docs/ST_MakeValid.html",
        },
    },
    "ST_MapAlgebra": {
        (Raster, str, str, float): {
            "inst": Raster,
            "type_hint": Raster,
            "description": "args: rast, pixeltype, expression, nodataval=NULL - Expression version - Returns a one-band raster given one or two input rasters, band indexes and one or more user-specified SQL expressions.",
            "doc_url": "https://postgis.net/docs/ST_MapAlgebra.html",
        },
        (List[Any], Any, str, str, Raster, int, int, List[Any]): {
            "inst": Raster,
            "type_hint": Raster,
            "description": "args: rastbandargset, callbackfunc, pixeltype=NULL, extenttype=INTERSECTION, customextent=NULL, distancex=0, distancey=0, VARIADIC userargs=NULL - Callback function version - Returns a one-band raster given one or more input rasters, band indexes and one user-specified callback function.",
            "doc_url": "https://postgis.net/docs/ST_MapAlgebra.html",
        },
        (Raster, List[int], Any, str, str, Raster, int, int, List[Any]): {
            "inst": Raster,
            "type_hint": Raster,
            "description": "args: rast, nband, callbackfunc, pixeltype=NULL, extenttype=FIRST, customextent=NULL, distancex=0, distancey=0, VARIADIC userargs=NULL - Callback function version - Returns a one-band raster given one or more input rasters, band indexes and one user-specified callback function.",
            "doc_url": "https://postgis.net/docs/ST_MapAlgebra.html",
        },
        (Raster, int, Any, str, str, Raster, int, int, List[Any]): {
            "inst": Raster,
            "type_hint": Raster,
            "description": "args: rast, nband, callbackfunc, pixeltype=NULL, extenttype=FIRST, customextent=NULL, distancex=0, distancey=0, VARIADIC userargs=NULL - Callback function version - Returns a one-band raster given one or more input rasters, band indexes and one user-specified callback function.",
            "doc_url": "https://postgis.net/docs/ST_MapAlgebra.html",
        },
        (Raster, int, Raster, int, Any, str, str, Raster, int, int, List[Any]): {
            "inst": Raster,
            "type_hint": Raster,
            "description": "args: rast1, nband1, rast2, nband2, callbackfunc, pixeltype=NULL, extenttype=INTERSECTION, customextent=NULL, distancex=0, distancey=0, VARIADIC userargs=NULL - Callback function version - Returns a one-band raster given one or more input rasters, band indexes and one user-specified callback function.",
            "doc_url": "https://postgis.net/docs/ST_MapAlgebra.html",
        },
        (Raster, int, Any, List[float], bool, str, str, Raster, List[Any]): {
            "inst": Raster,
            "type_hint": Raster,
            "description": "args: rast, nband, callbackfunc, mask, weighted, pixeltype=NULL, extenttype=INTERSECTION, customextent=NULL, VARIADIC userargs=NULL - Callback function version - Returns a one-band raster given one or more input rasters, band indexes and one user-specified callback function.",
            "doc_url": "https://postgis.net/docs/ST_MapAlgebra.html",
        },
        (Raster, int, str, str, float): {
            "inst": Raster,
            "type_hint": Raster,
            "description": "args: rast, nband, pixeltype, expression, nodataval=NULL - Expression version - Returns a one-band raster given one or two input rasters, band indexes and one or more user-specified SQL expressions.",
            "doc_url": "https://postgis.net/docs/ST_MapAlgebra.html",
        },
        (Raster, int, Raster, int, str, str, str, str, str, float): {
            "inst": Raster,
            "type_hint": Raster,
            "description": "args: rast1, nband1, rast2, nband2, expression, pixeltype=NULL, extenttype=INTERSECTION, nodata1expr=NULL, nodata2expr=NULL, nodatanodataval=NULL - Expression version - Returns a one-band raster given one or two input rasters, band indexes and one or more user-specified SQL expressions.",
            "doc_url": "https://postgis.net/docs/ST_MapAlgebra.html",
        },
        (Raster, Raster, str, str, str, str, str, float): {
            "inst": Raster,
            "type_hint": Raster,
            "description": "args: rast1, rast2, expression, pixeltype=NULL, extenttype=INTERSECTION, nodata1expr=NULL, nodata2expr=NULL, nodatanodataval=NULL - Expression version - Returns a one-band raster given one or two input rasters, band indexes and one or more user-specified SQL expressions.",
            "doc_url": "https://postgis.net/docs/ST_MapAlgebra.html",
        },
    },
    "ST_MapAlgebraExpr": {
        (Raster, str, str, float): {
            "inst": Raster,
            "type_hint": Raster,
            "description": "args: rast, pixeltype, expression, nodataval=NULL - 1 raster band version: Creates a new one band raster formed by applying a valid PostgreSQL algebraic operation on the input raster band and of pixeltype provided. Band 1 is assumed if no band is specified.",
            "doc_url": "https://postgis.net/docs/ST_MapAlgebraExpr.html",
        },
        (Raster, int, str, str, float): {
            "inst": Raster,
            "type_hint": Raster,
            "description": "args: rast, band, pixeltype, expression, nodataval=NULL - 1 raster band version: Creates a new one band raster formed by applying a valid PostgreSQL algebraic operation on the input raster band and of pixeltype provided. Band 1 is assumed if no band is specified.",
            "doc_url": "https://postgis.net/docs/ST_MapAlgebraExpr.html",
        },
        (Raster, int, Raster, int, str, str, str, str, str, float): {
            "inst": Raster,
            "type_hint": Raster,
            "description": "args: rast1, band1, rast2, band2, expression, pixeltype=same_as_rast1_band, extenttype=INTERSECTION, nodata1expr=NULL, nodata2expr=NULL, nodatanodataval=NULL - 2 raster band version: Creates a new one band raster formed by applying a valid PostgreSQL algebraic operation on the two input raster bands and of pixeltype provided. band 1 of each raster is assumed if no band numbers are specified. The resulting raster will be aligned (scale, skew and pixel corners) on the grid defined by the first raster and have its extent defined by the 'extenttype' parameter. Values for 'extenttype' can be: INTERSECTION, UNION, FIRST, SECOND.",
            "doc_url": "https://postgis.net/docs/ST_MapAlgebraExpr.html",
        },
        (Raster, Raster, str, str, str, str, str, float): {
            "inst": Raster,
            "type_hint": Raster,
            "description": "args: rast1, rast2, expression, pixeltype=same_as_rast1_band, extenttype=INTERSECTION, nodata1expr=NULL, nodata2expr=NULL, nodatanodataval=NULL - 2 raster band version: Creates a new one band raster formed by applying a valid PostgreSQL algebraic operation on the two input raster bands and of pixeltype provided. band 1 of each raster is assumed if no band numbers are specified. The resulting raster will be aligned (scale, skew and pixel corners) on the grid defined by the first raster and have its extent defined by the 'extenttype' parameter. Values for 'extenttype' can be: INTERSECTION, UNION, FIRST, SECOND.",
            "doc_url": "https://postgis.net/docs/ST_MapAlgebraExpr.html",
        },
    },
    "ST_MapAlgebraFct": {
        (Raster, int, str, Any, List[Any]): {
            "inst": Raster,
            "type_hint": Raster,
            "description": "args: rast, band, pixeltype, onerasteruserfunc, VARIADIC args - 1 band version - Creates a new one band raster formed by applying a valid PostgreSQL function on the input raster band and of pixeltype provided. Band 1 is assumed if no band is specified.",
            "doc_url": "https://postgis.net/docs/ST_MapAlgebraFct.html",
        },
        (Raster, int, str, Any): {
            "inst": Raster,
            "type_hint": Raster,
            "description": "args: rast, band, pixeltype, onerasteruserfunc - 1 band version - Creates a new one band raster formed by applying a valid PostgreSQL function on the input raster band and of pixeltype provided. Band 1 is assumed if no band is specified.",
            "doc_url": "https://postgis.net/docs/ST_MapAlgebraFct.html",
        },
        (Raster, int, Any, List[Any]): {
            "inst": Raster,
            "type_hint": Raster,
            "description": "args: rast, band, onerasteruserfunc, VARIADIC args - 1 band version - Creates a new one band raster formed by applying a valid PostgreSQL function on the input raster band and of pixeltype provided. Band 1 is assumed if no band is specified.",
            "doc_url": "https://postgis.net/docs/ST_MapAlgebraFct.html",
        },
        (Raster, int, Any): {
            "inst": Raster,
            "type_hint": Raster,
            "description": "args: rast, band, onerasteruserfunc - 1 band version - Creates a new one band raster formed by applying a valid PostgreSQL function on the input raster band and of pixeltype provided. Band 1 is assumed if no band is specified.",
            "doc_url": "https://postgis.net/docs/ST_MapAlgebraFct.html",
        },
        (Raster, str, Any, List[Any]): {
            "inst": Raster,
            "type_hint": Raster,
            "description": "args: rast, pixeltype, onerasteruserfunc, VARIADIC args - 1 band version - Creates a new one band raster formed by applying a valid PostgreSQL function on the input raster band and of pixeltype provided. Band 1 is assumed if no band is specified.",
            "doc_url": "https://postgis.net/docs/ST_MapAlgebraFct.html",
        },
        (Raster, str, Any): {
            "inst": Raster,
            "type_hint": Raster,
            "description": "args: rast, pixeltype, onerasteruserfunc - 1 band version - Creates a new one band raster formed by applying a valid PostgreSQL function on the input raster band and of pixeltype provided. Band 1 is assumed if no band is specified.",
            "doc_url": "https://postgis.net/docs/ST_MapAlgebraFct.html",
        },
        (Raster, Any, List[Any]): {
            "inst": Raster,
            "type_hint": Raster,
            "description": "args: rast, onerasteruserfunc, VARIADIC args - 1 band version - Creates a new one band raster formed by applying a valid PostgreSQL function on the input raster band and of pixeltype provided. Band 1 is assumed if no band is specified.",
            "doc_url": "https://postgis.net/docs/ST_MapAlgebraFct.html",
        },
        (Raster, Any): {
            "inst": Raster,
            "type_hint": Raster,
            "description": "args: rast, onerasteruserfunc - 1 band version - Creates a new one band raster formed by applying a valid PostgreSQL function on the input raster band and of pixeltype provided. Band 1 is assumed if no band is specified.",
            "doc_url": "https://postgis.net/docs/ST_MapAlgebraFct.html",
        },
        (Raster, int, Raster, int, Any, str, str, List[Any]): {
            "inst": Raster,
            "type_hint": Raster,
            "description": "args: rast1, band1, rast2, band2, tworastuserfunc, pixeltype=same_as_rast1, extenttype=INTERSECTION, VARIADIC userargs - 2 band version - Creates a new one band raster formed by applying a valid PostgreSQL function on the 2 input raster bands and of pixeltype provided. Band 1 is assumed if no band is specified. Extent type defaults to INTERSECTION if not specified.",
            "doc_url": "https://postgis.net/docs/ST_MapAlgebraFct.html",
        },
        (Raster, Raster, Any, str, str, List[Any]): {
            "inst": Raster,
            "type_hint": Raster,
            "description": "args: rast1, rast2, tworastuserfunc, pixeltype=same_as_rast1, extenttype=INTERSECTION, VARIADIC userargs - 2 band version - Creates a new one band raster formed by applying a valid PostgreSQL function on the 2 input raster bands and of pixeltype provided. Band 1 is assumed if no band is specified. Extent type defaults to INTERSECTION if not specified.",
            "doc_url": "https://postgis.net/docs/ST_MapAlgebraFct.html",
        },
    },
    "ST_MapAlgebraFctNgb": {
        (Raster, int, str, int, int, Any, str, List[Any]): {
            "inst": Raster,
            "type_hint": Raster,
            "description": "args: rast, band, pixeltype, ngbwidth, ngbheight, onerastngbuserfunc, nodatamode, VARIADIC args - 1-band version: Map Algebra Nearest Neighbor using user-defined PostgreSQL function. Return a raster which values are the result of a PLPGSQL user function involving a neighborhood of values from the input raster band.",
            "doc_url": "https://postgis.net/docs/ST_MapAlgebraFctNgb.html",
        }
    },
    "ST_Max4ma": {
        (List[float], str, List[Any]): {
            "inst": float,
            "type_hint": float,
            "description": "args: matrix, nodatamode, VARIADIC args - Raster processing function that calculates the maximum pixel value in a neighborhood.",
            "doc_url": "https://postgis.net/docs/ST_Max4ma.html",
        },
        (List[float], List[int], List[Any]): {
            "inst": float,
            "type_hint": float,
            "description": "args: value, pos, VARIADIC userargs - Raster processing function that calculates the maximum pixel value in a neighborhood.",
            "doc_url": "https://postgis.net/docs/ST_Max4ma.html",
        },
    },
    "ST_MaxDistance": {
        (Geometry, Geometry): {
            "inst": float,
            "type_hint": float,
            "description": "args: g1, g2 - Returns the 2D largest distance between two geometries in projected units.",
            "doc_url": "https://postgis.net/docs/ST_MaxDistance.html",
        }
    },
    "ST_MaximumInscribedCircle": {
        (Geometry, Geometry, Geometry, float): {
            "inst": object,
            "type_hint": Any,
            "description": "args: geom - Computes the largest circle contained within a geometry.",
            "doc_url": "https://postgis.net/docs/ST_MaximumInscribedCircle.html",
        }
    },
    "ST_Mean4ma": {
        (List[float], str, List[Any]): {
            "inst": float,
            "type_hint": float,
            "description": "args: matrix, nodatamode, VARIADIC args - Raster processing function that calculates the mean pixel value in a neighborhood.",
            "doc_url": "https://postgis.net/docs/ST_Mean4ma.html",
        },
        (List[float], List[int], List[Any]): {
            "inst": float,
            "type_hint": float,
            "description": "args: value, pos, VARIADIC userargs - Raster processing function that calculates the mean pixel value in a neighborhood.",
            "doc_url": "https://postgis.net/docs/ST_Mean4ma.html",
        },
    },
    "ST_MemSize": {
        (Geometry,): {
            "inst": int,
            "type_hint": int,
            "description": "args: geomA - Returns the amount of memory space a geometry takes.",
            "doc_url": "https://postgis.net/docs/ST_MemSize.html",
        },
        (Raster,): {
            "inst": int,
            "type_hint": int,
            "description": "args: rast - Returns the amount of space (in bytes) the raster takes.",
            "doc_url": "https://postgis.net/docs/ST_MemSize.html",
        },
    },
    "ST_MemUnion": {
        (Geometry,): {
            "inst": Geometry,
            "type_hint": Geometry,
            "description": "args: geomfield - Aggregate function which unions geometries in a memory-efficent but slower way",
            "doc_url": "https://postgis.net/docs/ST_MemUnion.html",
        }
    },
    "ST_MetaData": {
        (Raster, float, float, int, int, float, float, float, float, int, int): {
            "inst": object,
            "type_hint": Any,
            "description": "args: rast - Returns basic meta data about a raster object such as pixel size, rotation (skew), upper, lower left, etc.",
            "doc_url": "https://postgis.net/docs/ST_MetaData.html",
        }
    },
    "ST_Min4ma": {
        (List[float], str, List[Any]): {
            "inst": float,
            "type_hint": float,
            "description": "args: matrix, nodatamode, VARIADIC args - Raster processing function that calculates the minimum pixel value in a neighborhood.",
            "doc_url": "https://postgis.net/docs/ST_Min4ma.html",
        },
        (List[float], List[int], List[Any]): {
            "inst": float,
            "type_hint": float,
            "description": "args: value, pos, VARIADIC userargs - Raster processing function that calculates the minimum pixel value in a neighborhood.",
            "doc_url": "https://postgis.net/docs/ST_Min4ma.html",
        },
    },
    "ST_MinConvexHull": {
        (Raster, int): {
            "inst": Geometry,
            "type_hint": Geometry,
            "description": "args: rast, nband=NULL - Return the convex hull geometry of the raster excluding NODATA pixels.",
            "doc_url": "https://postgis.net/docs/ST_MinConvexHull.html",
        }
    },
    "ST_MinDist4ma": {
        (List[float], List[int], List[Any]): {
            "inst": float,
            "type_hint": float,
            "description": "args: value, pos, VARIADIC userargs - Raster processing function that returns the minimum distance (in number of pixels) between the pixel of interest and a neighboring pixel with value.",
            "doc_url": "https://postgis.net/docs/ST_MinDist4ma.html",
        }
    },
    "ST_MinPossibleValue": {
        (str,): {
            "inst": float,
            "type_hint": float,
            "description": "args: pixeltype - Returns the minimum value this pixeltype can store.",
            "doc_url": "https://postgis.net/docs/ST_MinPossibleValue.html",
        }
    },
    "ST_MinimumBoundingCircle": {
        (Geometry, int): {
            "inst": Geometry,
            "type_hint": Geometry,
            "description": "args: geomA, num_segs_per_qt_circ=48 - Returns the smallest circle polygon that contains a geometry.",
            "doc_url": "https://postgis.net/docs/ST_MinimumBoundingCircle.html",
        }
    },
    "ST_MinimumBoundingRadius": {
        (Geometry, Geometry, float): {
            "inst": object,
            "type_hint": Any,
            "description": "args: geom - Returns the center point and radius of the smallest circle that contains a geometry.",
            "doc_url": "https://postgis.net/docs/ST_MinimumBoundingRadius.html",
        }
    },
    "ST_MinimumClearance": {
        (Geometry,): {
            "inst": float,
            "type_hint": float,
            "description": "args: g - Returns the minimum clearance of a geometry, a measure of a geometry's robustness.",
            "doc_url": "https://postgis.net/docs/ST_MinimumClearance.html",
        }
    },
    "ST_MinimumClearanceLine": {
        (Geometry,): {
            "inst": Geometry,
            "type_hint": Geometry,
            "description": "args: g - Returns the two-point LineString spanning a geometry's minimum clearance.",
            "doc_url": "https://postgis.net/docs/ST_MinimumClearanceLine.html",
        }
    },
    "ST_Multi": {
        (Geometry,): {
            "inst": Geometry,
            "type_hint": Geometry,
            "description": "args: geom - Return the geometry as a MULTI* geometry.",
            "doc_url": "https://postgis.net/docs/ST_Multi.html",
        }
    },
    "ST_NDims": {
        (Geometry,): {
            "inst": int,
            "type_hint": int,
            "description": "args: g1 - Returns the coordinate dimension of a geometry.",
            "doc_url": "https://postgis.net/docs/ST_NDims.html",
        }
    },
    "ST_NPoints": {
        (Geometry,): {
            "inst": int,
            "type_hint": int,
            "description": "args: g1 - Returns the number of points (vertices) in a geometry.",
            "doc_url": "https://postgis.net/docs/ST_NPoints.html",
        }
    },
    "ST_NRings": {
        (Geometry,): {
            "inst": int,
            "type_hint": int,
            "description": "args: geomA - Returns the number of rings in a polygonal geometry.",
            "doc_url": "https://postgis.net/docs/ST_NRings.html",
        }
    },
    "ST_NearestValue": {
        (Raster, int, Geometry, bool): {
            "inst": float,
            "type_hint": float,
            "description": "args: rast, bandnum, pt, exclude_nodata_value=true - Returns the nearest non-NODATA value of a given bands pixel specified by a columnx and rowy or a geometric point expressed in the same spatial reference coordinate system as the raster.",
            "doc_url": "https://postgis.net/docs/ST_NearestValue.html",
        },
        (Raster, Geometry, bool): {
            "inst": float,
            "type_hint": float,
            "description": "args: rast, pt, exclude_nodata_value=true - Returns the nearest non-NODATA value of a given bands pixel specified by a columnx and rowy or a geometric point expressed in the same spatial reference coordinate system as the raster.",
            "doc_url": "https://postgis.net/docs/ST_NearestValue.html",
        },
        (Raster, int, int, int, bool): {
            "inst": float,
            "type_hint": float,
            "description": "args: rast, bandnum, columnx, rowy, exclude_nodata_value=true - Returns the nearest non-NODATA value of a given bands pixel specified by a columnx and rowy or a geometric point expressed in the same spatial reference coordinate system as the raster.",
            "doc_url": "https://postgis.net/docs/ST_NearestValue.html",
        },
        (Raster, int, int, bool): {
            "inst": float,
            "type_hint": float,
            "description": "args: rast, columnx, rowy, exclude_nodata_value=true - Returns the nearest non-NODATA value of a given bands pixel specified by a columnx and rowy or a geometric point expressed in the same spatial reference coordinate system as the raster.",
            "doc_url": "https://postgis.net/docs/ST_NearestValue.html",
        },
    },
    "ST_Neighborhood": {
        (Raster, int, int, int, int, int, bool): {
            "inst": float,
            "type_hint": List[float],
            "description": "args: rast, bandnum, columnX, rowY, distanceX, distanceY, exclude_nodata_value=true - Returns a 2-D double precision array of the non-NODATA values around a given bands pixel specified by either a columnX and rowY or a geometric point expressed in the same spatial reference coordinate system as the raster.",
            "doc_url": "https://postgis.net/docs/ST_Neighborhood.html",
        },
        (Raster, int, int, int, int, bool): {
            "inst": float,
            "type_hint": List[float],
            "description": "args: rast, columnX, rowY, distanceX, distanceY, exclude_nodata_value=true - Returns a 2-D double precision array of the non-NODATA values around a given bands pixel specified by either a columnX and rowY or a geometric point expressed in the same spatial reference coordinate system as the raster.",
            "doc_url": "https://postgis.net/docs/ST_Neighborhood.html",
        },
        (Raster, int, Geometry, int, int, bool): {
            "inst": float,
            "type_hint": List[float],
            "description": "args: rast, bandnum, pt, distanceX, distanceY, exclude_nodata_value=true - Returns a 2-D double precision array of the non-NODATA values around a given bands pixel specified by either a columnX and rowY or a geometric point expressed in the same spatial reference coordinate system as the raster.",
            "doc_url": "https://postgis.net/docs/ST_Neighborhood.html",
        },
        (Raster, Geometry, int, int, bool): {
            "inst": float,
            "type_hint": List[float],
            "description": "args: rast, pt, distanceX, distanceY, exclude_nodata_value=true - Returns a 2-D double precision array of the non-NODATA values around a given bands pixel specified by either a columnX and rowY or a geometric point expressed in the same spatial reference coordinate system as the raster.",
            "doc_url": "https://postgis.net/docs/ST_Neighborhood.html",
        },
    },
    "ST_Node": {
        (Geometry,): {
            "inst": Geometry,
            "type_hint": Geometry,
            "description": "args: geom - Nodes a collection of lines.",
            "doc_url": "https://postgis.net/docs/ST_Node.html",
        }
    },
    "ST_Normalize": {
        (Geometry,): {
            "inst": Geometry,
            "type_hint": Geometry,
            "description": "args: geom - Return the geometry in its canonical form.",
            "doc_url": "https://postgis.net/docs/ST_Normalize.html",
        }
    },
    "ST_NotSameAlignmentReason": {
        (Raster, Raster): {
            "inst": str,
            "type_hint": str,
            "description": "args: rastA, rastB - Returns text stating if rasters are aligned and if not aligned, a reason why.",
            "doc_url": "https://postgis.net/docs/ST_NotSameAlignmentReason.html",
        }
    },
    "ST_NumBands": {
        (Raster,): {
            "inst": int,
            "type_hint": int,
            "description": "args: rast - Returns the number of bands in the raster object.",
            "doc_url": "https://postgis.net/docs/ST_NumBands.html",
        }
    },
    "ST_NumGeometries": {
        (Geometry,): {
            "inst": int,
            "type_hint": int,
            "description": "args: geom - Returns the number of elements in a geometry collection.",
            "doc_url": "https://postgis.net/docs/ST_NumGeometries.html",
        }
    },
    "ST_NumInteriorRing": {
        (Geometry,): {
            "inst": int,
            "type_hint": int,
            "description": "args: a_polygon - Returns the number of interior rings (holes) of a Polygon. Aias for ST_NumInteriorRings",
            "doc_url": "https://postgis.net/docs/ST_NumInteriorRing.html",
        }
    },
    "ST_NumInteriorRings": {
        (Geometry,): {
            "inst": int,
            "type_hint": int,
            "description": "args: a_polygon - Returns the number of interior rings (holes) of a Polygon.",
            "doc_url": "https://postgis.net/docs/ST_NumInteriorRings.html",
        }
    },
    "ST_NumPatches": {
        (Geometry,): {
            "inst": int,
            "type_hint": int,
            "description": "args: g1 - Return the number of faces on a Polyhedral Surface. Will return null for non-polyhedral geometries.",
            "doc_url": "https://postgis.net/docs/ST_NumPatches.html",
        }
    },
    "ST_NumPoints": {
        (Geometry,): {
            "inst": int,
            "type_hint": int,
            "description": "args: g1 - Returns the number of points in a LineString or CircularString.",
            "doc_url": "https://postgis.net/docs/ST_NumPoints.html",
        }
    },
    "ST_OffsetCurve": {
        (Geometry, float, str): {
            "inst": Geometry,
            "type_hint": Geometry,
            "description": "args: line, signed_distance, style_parameters=' - Returns an offset line at a given distance and side from an input line.",
            "doc_url": "https://postgis.net/docs/ST_OffsetCurve.html",
        }
    },
    "ST_OrderingEquals": {
        (Geometry, Geometry): {
            "inst": bool,
            "type_hint": bool,
            "description": "None",
            "doc_url": "https://postgis.net/docs/ST_OrderingEquals.html",
        }
    },
    "ST_OrientedEnvelope": {
        (Geometry,): {
            "inst": Geometry,
            "type_hint": Geometry,
            "description": "args: geom - Returns a minimum-area rectangle containing a geometry.",
            "doc_url": "https://postgis.net/docs/ST_OrientedEnvelope.html",
        }
    },
    "ST_Overlaps": {
        (Geometry, Geometry): {
            "inst": bool,
            "type_hint": bool,
            "description": "None",
            "doc_url": "https://postgis.net/docs/ST_Overlaps.html",
        },
        (Raster, int, Raster, int): {
            "inst": bool,
            "type_hint": bool,
            "description": "args: rastA, nbandA, rastB, nbandB - Return true if raster rastA and rastB intersect but one does not completely contain the other.",
            "doc_url": "https://postgis.net/docs/ST_Overlaps.html",
        },
        (Raster, Raster): {
            "inst": bool,
            "type_hint": bool,
            "description": "args: rastA, rastB - Return true if raster rastA and rastB intersect but one does not completely contain the other.",
            "doc_url": "https://postgis.net/docs/ST_Overlaps.html",
        },
    },
    "ST_PatchN": {
        (Geometry, int): {
            "inst": Geometry,
            "type_hint": Geometry,
            "description": "args: geomA, n - Returns the Nth geometry (face) of a PolyhedralSurface.",
            "doc_url": "https://postgis.net/docs/ST_PatchN.html",
        }
    },
    "ST_Perimeter": {
        (Geometry,): {
            "inst": float,
            "type_hint": float,
            "description": "args: g1 - Returns the length of the boundary of a polygonal geometry or geography.",
            "doc_url": "https://postgis.net/docs/ST_Perimeter.html",
        },
        (Geography, bool): {
            "inst": float,
            "type_hint": float,
            "description": "args: geog, use_spheroid = true - Returns the length of the boundary of a polygonal geometry or geography.",
            "doc_url": "https://postgis.net/docs/ST_Perimeter.html",
        },
    },
    "ST_Perimeter2D": {
        (Geometry,): {
            "inst": float,
            "type_hint": float,
            "description": "args: geomA - Returns the 2D perimeter of a polygonal geometry. Alias for ST_Perimeter.",
            "doc_url": "https://postgis.net/docs/ST_Perimeter2D.html",
        }
    },
    "ST_PixelAsCentroid": {
        (Raster, int, int): {
            "inst": Geometry,
            "type_hint": Geometry,
            "description": "args: rast, x, y - Returns the centroid (point geometry) of the area represented by a pixel.",
            "doc_url": "https://postgis.net/docs/ST_PixelAsCentroid.html",
        }
    },
    "ST_PixelAsCentroids": {
        (Raster, int, bool): {
            "inst": object,
            "type_hint": Any,
            "description": "args: rast, band=1, exclude_nodata_value=TRUE - Returns the centroid (point geometry) for each pixel of a raster band along with the value, the X and the Y raster coordinates of each pixel. The point geometry is the centroid of the area represented by a pixel.",
            "doc_url": "https://postgis.net/docs/ST_PixelAsCentroids.html",
        }
    },
    "ST_PixelAsPoint": {
        (Raster, int, int): {
            "inst": Geometry,
            "type_hint": Geometry,
            "description": "args: rast, columnx, rowy - Returns a point geometry of the pixels upper-left corner.",
            "doc_url": "https://postgis.net/docs/ST_PixelAsPoint.html",
        }
    },
    "ST_PixelAsPoints": {
        (Raster, int, bool): {
            "inst": object,
            "type_hint": Any,
            "description": "args: rast, band=1, exclude_nodata_value=TRUE - Returns a point geometry for each pixel of a raster band along with the value, the X and the Y raster coordinates of each pixel. The coordinates of the point geometry are of the pixels upper-left corner.",
            "doc_url": "https://postgis.net/docs/ST_PixelAsPoints.html",
        }
    },
    "ST_PixelAsPolygon": {
        (Raster, int, int): {
            "inst": Geometry,
            "type_hint": Geometry,
            "description": "args: rast, columnx, rowy - Returns the polygon geometry that bounds the pixel for a particular row and column.",
            "doc_url": "https://postgis.net/docs/ST_PixelAsPolygon.html",
        }
    },
    "ST_PixelAsPolygons": {
        (Raster, int, bool): {
            "inst": object,
            "type_hint": Any,
            "description": "args: rast, band=1, exclude_nodata_value=TRUE - Returns the polygon geometry that bounds every pixel of a raster band along with the value, the X and the Y raster coordinates of each pixel.",
            "doc_url": "https://postgis.net/docs/ST_PixelAsPolygons.html",
        }
    },
    "ST_PixelHeight": {
        (Raster,): {
            "inst": float,
            "type_hint": float,
            "description": "args: rast - Returns the pixel height in geometric units of the spatial reference system.",
            "doc_url": "https://postgis.net/docs/ST_PixelHeight.html",
        }
    },
    "ST_PixelOfValue": {
        (Raster, int, List[float], bool): {
            "inst": object,
            "type_hint": Any,
            "description": "args: rast, nband, search, exclude_nodata_value=true - Get the columnx, rowy coordinates of the pixel whose value equals the search value.",
            "doc_url": "https://postgis.net/docs/ST_PixelOfValue.html",
        },
        (Raster, List[float], bool): {
            "inst": object,
            "type_hint": Any,
            "description": "args: rast, search, exclude_nodata_value=true - Get the columnx, rowy coordinates of the pixel whose value equals the search value.",
            "doc_url": "https://postgis.net/docs/ST_PixelOfValue.html",
        },
        (Raster, int, float, bool): {
            "inst": object,
            "type_hint": Any,
            "description": "args: rast, nband, search, exclude_nodata_value=true - Get the columnx, rowy coordinates of the pixel whose value equals the search value.",
            "doc_url": "https://postgis.net/docs/ST_PixelOfValue.html",
        },
        (Raster, float, bool): {
            "inst": object,
            "type_hint": Any,
            "description": "args: rast, search, exclude_nodata_value=true - Get the columnx, rowy coordinates of the pixel whose value equals the search value.",
            "doc_url": "https://postgis.net/docs/ST_PixelOfValue.html",
        },
    },
    "ST_PixelWidth": {
        (Raster,): {
            "inst": float,
            "type_hint": float,
            "description": "args: rast - Returns the pixel width in geometric units of the spatial reference system.",
            "doc_url": "https://postgis.net/docs/ST_PixelWidth.html",
        }
    },
    "ST_Point": {
        (float, float): {
            "inst": Geometry,
            "type_hint": Geometry,
            "description": "args: x, y - Creates a Point with X, Y and SRID values.",
            "doc_url": "https://postgis.net/docs/ST_Point.html",
        },
        (float, float, int): {
            "inst": Geometry,
            "type_hint": Geometry,
            "description": "args: x, y, srid=unknown - Creates a Point with X, Y and SRID values.",
            "doc_url": "https://postgis.net/docs/ST_Point.html",
        },
    },
    "ST_PointFromGeoHash": {
        (str, int): {
            "inst": Geometry,
            "type_hint": Geometry,
            "description": "None",
            "doc_url": "https://postgis.net/docs/ST_PointFromGeoHash.html",
        }
    },
    "ST_PointFromText": {
        (str,): {
            "inst": Geometry,
            "type_hint": Geometry,
            "description": "None",
            "doc_url": "https://postgis.net/docs/ST_PointFromText.html",
        },
        (str, int): {
            "inst": Geometry,
            "type_hint": Geometry,
            "description": "None",
            "doc_url": "https://postgis.net/docs/ST_PointFromText.html",
        },
    },
    "ST_PointFromWKB": {
        (bytes, int): {
            "inst": Geometry,
            "type_hint": Geometry,
            "description": "None",
            "doc_url": "https://postgis.net/docs/ST_PointFromWKB.html",
        },
        (bytes,): {
            "inst": Geometry,
            "type_hint": Geometry,
            "description": "None",
            "doc_url": "https://postgis.net/docs/ST_PointFromWKB.html",
        },
    },
    "ST_PointInsideCircle": {
        (Geometry, float, float, float): {
            "inst": bool,
            "type_hint": bool,
            "description": "None",
            "doc_url": "https://postgis.net/docs/ST_PointInsideCircle.html",
        }
    },
    "ST_PointM": {
        (float, float, float, int): {
            "inst": Geometry,
            "type_hint": Geometry,
            "description": "args: x, y, m, srid=unknown - Creates a Point with X, Y, M and SRID values.",
            "doc_url": "https://postgis.net/docs/ST_PointM.html",
        }
    },
    "ST_PointN": {
        (Geometry, int): {
            "inst": Geometry,
            "type_hint": Geometry,
            "description": "args: a_linestring, n - Returns the Nth point in the first LineString or circular LineString in a geometry.",
            "doc_url": "https://postgis.net/docs/ST_PointN.html",
        }
    },
    "ST_PointOnSurface": {
        (Geometry,): {
            "inst": Geometry,
            "type_hint": Geometry,
            "description": "args: g1 - Computes a point guaranteed to lie in a polygon, or on a geometry.",
            "doc_url": "https://postgis.net/docs/ST_PointOnSurface.html",
        }
    },
    "ST_PointZ": {
        (float, float, float, int): {
            "inst": Geometry,
            "type_hint": Geometry,
            "description": "args: x, y, z, srid=unknown - Creates a Point with X, Y, Z and SRID values.",
            "doc_url": "https://postgis.net/docs/ST_PointZ.html",
        }
    },
    "ST_PointZM": {
        (float, float, float, float, int): {
            "inst": Geometry,
            "type_hint": Geometry,
            "description": "args: x, y, z, m, srid=unknown - Creates a Point with X, Y, Z, M and SRID values.",
            "doc_url": "https://postgis.net/docs/ST_PointZM.html",
        }
    },
    "ST_Points": {
        (Geometry,): {
            "inst": Geometry,
            "type_hint": Geometry,
            "description": "args: geom - Returns a MultiPoint containing the coordinates of a geometry.",
            "doc_url": "https://postgis.net/docs/ST_Points.html",
        }
    },
    "ST_Polygon": {
        (Geometry, int): {
            "inst": Geometry,
            "type_hint": Geometry,
            "description": "args: lineString, srid - Creates a Polygon from a LineString with a specified SRID.",
            "doc_url": "https://postgis.net/docs/ST_Polygon.html",
        },
        (Raster, int): {
            "inst": Geometry,
            "type_hint": Geometry,
            "description": "args: rast, band_num=1 - Returns a multipolygon geometry formed by the union of pixels that have a pixel value that is not no data value. If no band number is specified, band num defaults to 1.",
            "doc_url": "https://postgis.net/docs/ST_Polygon.html",
        },
    },
    "ST_PolygonFromText": {
        (str, int): {
            "inst": Geometry,
            "type_hint": Geometry,
            "description": "None",
            "doc_url": "https://postgis.net/docs/ST_PolygonFromText.html",
        },
        (str,): {
            "inst": Geometry,
            "type_hint": Geometry,
            "description": "None",
            "doc_url": "https://postgis.net/docs/ST_PolygonFromText.html",
        },
    },
    "ST_Polygonize": {
        (Geometry,): {
            "inst": Geometry,
            "type_hint": Geometry,
            "description": "args: geomfield - Computes a collection of polygons formed from the linework of a set of geometries.",
            "doc_url": "https://postgis.net/docs/ST_Polygonize.html",
        },
        (List[Geometry],): {
            "inst": Geometry,
            "type_hint": Geometry,
            "description": "args: geom_array - Computes a collection of polygons formed from the linework of a set of geometries.",
            "doc_url": "https://postgis.net/docs/ST_Polygonize.html",
        },
    },
    "ST_Project": {
        (Geometry, float, float): {
            "inst": Geometry,
            "type_hint": Geometry,
            "description": "args: g1, distance, azimuth - Returns a point projected from a start point by a distance and bearing (azimuth).",
            "doc_url": "https://postgis.net/docs/ST_Project.html",
        },
        (Geometry, Geometry, float): {
            "inst": Geometry,
            "type_hint": Geometry,
            "description": "args: g1, g2, distance - Returns a point projected from a start point by a distance and bearing (azimuth).",
            "doc_url": "https://postgis.net/docs/ST_Project.html",
        },
        (Geography, Geography, float): {
            "inst": Geography,
            "type_hint": Geography,
            "description": "args: g1, g2, distance - Returns a point projected from a start point by a distance and bearing (azimuth).",
            "doc_url": "https://postgis.net/docs/ST_Project.html",
        },
        (Geography, float, float): {
            "inst": Geography,
            "type_hint": Geography,
            "description": "args: g1, distance, azimuth - Returns a point projected from a start point by a distance and bearing (azimuth).",
            "doc_url": "https://postgis.net/docs/ST_Project.html",
        },
    },
    "ST_Quantile": {
        (Raster, bool, float): {
            "inst": float,
            "type_hint": float,
            "description": "args: rast, exclude_nodata_value, quantile=NULL - Compute quantiles for a raster or raster table coverage in the context of the sample or population. Thus, a value could be examined to be at the rasters 25%, 50%, 75% percentile.",
            "doc_url": "https://postgis.net/docs/ST_Quantile.html",
        },
        (Raster, float): {
            "inst": float,
            "type_hint": float,
            "description": "args: rast, quantile - Compute quantiles for a raster or raster table coverage in the context of the sample or population. Thus, a value could be examined to be at the rasters 25%, 50%, 75% percentile.",
            "doc_url": "https://postgis.net/docs/ST_Quantile.html",
        },
        (Raster, int, bool, List[float], float, float): {
            "inst": object,
            "type_hint": List[Any],
            "description": "args: rast, nband=1, exclude_nodata_value=true, quantiles=NULL - Compute quantiles for a raster or raster table coverage in the context of the sample or population. Thus, a value could be examined to be at the rasters 25%, 50%, 75% percentile.",
            "doc_url": "https://postgis.net/docs/ST_Quantile.html",
        },
        (Raster, int, List[float], float, float): {
            "inst": object,
            "type_hint": List[Any],
            "description": "args: rast, nband, quantiles - Compute quantiles for a raster or raster table coverage in the context of the sample or population. Thus, a value could be examined to be at the rasters 25%, 50%, 75% percentile.",
            "doc_url": "https://postgis.net/docs/ST_Quantile.html",
        },
        (Raster, List[float], float, float): {
            "inst": object,
            "type_hint": List[Any],
            "description": "args: rast, quantiles - Compute quantiles for a raster or raster table coverage in the context of the sample or population. Thus, a value could be examined to be at the rasters 25%, 50%, 75% percentile.",
            "doc_url": "https://postgis.net/docs/ST_Quantile.html",
        },
        (Raster, int, bool, float): {
            "inst": float,
            "type_hint": float,
            "description": "args: rast, nband, exclude_nodata_value, quantile - Compute quantiles for a raster or raster table coverage in the context of the sample or population. Thus, a value could be examined to be at the rasters 25%, 50%, 75% percentile.",
            "doc_url": "https://postgis.net/docs/ST_Quantile.html",
        },
        (Raster, int, float): {
            "inst": float,
            "type_hint": float,
            "description": "args: rast, nband, quantile - Compute quantiles for a raster or raster table coverage in the context of the sample or population. Thus, a value could be examined to be at the rasters 25%, 50%, 75% percentile.",
            "doc_url": "https://postgis.net/docs/ST_Quantile.html",
        },
    },
    "ST_QuantizeCoordinates": {
        (Geometry, int, int, int, int): {
            "inst": Geometry,
            "type_hint": Geometry,
            "description": "args: g, prec_x, prec_y, prec_z, prec_m - Sets least significant bits of coordinates to zero",
            "doc_url": "https://postgis.net/docs/ST_QuantizeCoordinates.html",
        }
    },
    "ST_Range4ma": {
        (List[float], str, List[Any]): {
            "inst": float,
            "type_hint": float,
            "description": "args: matrix, nodatamode, VARIADIC args - Raster processing function that calculates the range of pixel values in a neighborhood.",
            "doc_url": "https://postgis.net/docs/ST_Range4ma.html",
        },
        (List[float], List[int], List[Any]): {
            "inst": float,
            "type_hint": float,
            "description": "args: value, pos, VARIADIC userargs - Raster processing function that calculates the range of pixel values in a neighborhood.",
            "doc_url": "https://postgis.net/docs/ST_Range4ma.html",
        },
    },
    "ST_RastFromHexWKB": {
        (str,): {
            "inst": Raster,
            "type_hint": Raster,
            "description": "args: wkb - Return a raster value from a Hex representation of Well-Known Binary (WKB) raster.",
            "doc_url": "https://postgis.net/docs/ST_RastFromHexWKB.html",
        }
    },
    "ST_RastFromWKB": {
        (bytes,): {
            "inst": Raster,
            "type_hint": Raster,
            "description": "args: wkb - Return a raster value from a Well-Known Binary (WKB) raster.",
            "doc_url": "https://postgis.net/docs/ST_RastFromWKB.html",
        }
    },
    "ST_RasterToWorldCoord": {
        (Raster, int, int, float, float): {
            "inst": object,
            "type_hint": Any,
            "description": "args: rast, xcolumn, yrow - Returns the rasters upper left corner as geometric X and Y (longitude and latitude) given a column and row. Column and row starts at 1.",
            "doc_url": "https://postgis.net/docs/ST_RasterToWorldCoord.html",
        }
    },
    "ST_RasterToWorldCoordX": {
        (Raster, int, int): {
            "inst": float,
            "type_hint": float,
            "description": "args: rast, xcolumn, yrow - Returns the geometric X coordinate upper left of a raster, column and row. Numbering of columns and rows starts at 1.",
            "doc_url": "https://postgis.net/docs/ST_RasterToWorldCoordX.html",
        },
        (Raster, int): {
            "inst": float,
            "type_hint": float,
            "description": "args: rast, xcolumn - Returns the geometric X coordinate upper left of a raster, column and row. Numbering of columns and rows starts at 1.",
            "doc_url": "https://postgis.net/docs/ST_RasterToWorldCoordX.html",
        },
    },
    "ST_RasterToWorldCoordY": {
        (Raster, int, int): {
            "inst": float,
            "type_hint": float,
            "description": "args: rast, xcolumn, yrow - Returns the geometric Y coordinate upper left corner of a raster, column and row. Numbering of columns and rows starts at 1.",
            "doc_url": "https://postgis.net/docs/ST_RasterToWorldCoordY.html",
        },
        (Raster, int): {
            "inst": float,
            "type_hint": float,
            "description": "args: rast, yrow - Returns the geometric Y coordinate upper left corner of a raster, column and row. Numbering of columns and rows starts at 1.",
            "doc_url": "https://postgis.net/docs/ST_RasterToWorldCoordY.html",
        },
    },
    "ST_Reclass": {
        (Raster, List[Any]): {
            "inst": Raster,
            "type_hint": Raster,
            "description": "args: rast, VARIADIC reclassargset - Creates a new raster composed of band types reclassified from original. The nband is the band to be changed. If nband is not specified assumed to be 1. All other bands are returned unchanged. Use case: convert a 16BUI band to a 8BUI and so forth for simpler rendering as viewable formats.",
            "doc_url": "https://postgis.net/docs/ST_Reclass.html",
        },
        (Raster, int, str, str, float): {
            "inst": Raster,
            "type_hint": Raster,
            "description": "args: rast, nband, reclassexpr, pixeltype, nodataval=NULL - Creates a new raster composed of band types reclassified from original. The nband is the band to be changed. If nband is not specified assumed to be 1. All other bands are returned unchanged. Use case: convert a 16BUI band to a 8BUI and so forth for simpler rendering as viewable formats.",
            "doc_url": "https://postgis.net/docs/ST_Reclass.html",
        },
        (Raster, str, str): {
            "inst": Raster,
            "type_hint": Raster,
            "description": "args: rast, reclassexpr, pixeltype - Creates a new raster composed of band types reclassified from original. The nband is the band to be changed. If nband is not specified assumed to be 1. All other bands are returned unchanged. Use case: convert a 16BUI band to a 8BUI and so forth for simpler rendering as viewable formats.",
            "doc_url": "https://postgis.net/docs/ST_Reclass.html",
        },
    },
    "ST_ReducePrecision": {
        (Geometry, float): {
            "inst": Geometry,
            "type_hint": Geometry,
            "description": "args: g, gridsize - Returns a valid geometry with points rounded to a grid tolerance.",
            "doc_url": "https://postgis.net/docs/ST_ReducePrecision.html",
        }
    },
    "ST_Relate": {
        (Geometry, Geometry): {
            "inst": str,
            "type_hint": str,
            "description": "None",
            "doc_url": "https://postgis.net/docs/ST_Relate.html",
        },
        (Geometry, Geometry, int): {
            "inst": str,
            "type_hint": str,
            "description": "None",
            "doc_url": "https://postgis.net/docs/ST_Relate.html",
        },
        (Geometry, Geometry, str): {
            "inst": bool,
            "type_hint": bool,
            "description": "None",
            "doc_url": "https://postgis.net/docs/ST_Relate.html",
        },
    },
    "ST_RelateMatch": {
        (str, str): {
            "inst": bool,
            "type_hint": bool,
            "description": "None",
            "doc_url": "https://postgis.net/docs/ST_RelateMatch.html",
        }
    },
    "ST_RemovePoint": {
        (Geometry, int): {
            "inst": Geometry,
            "type_hint": Geometry,
            "description": "args: linestring, offset - Remove a point from a linestring.",
            "doc_url": "https://postgis.net/docs/ST_RemovePoint.html",
        }
    },
    "ST_RemoveRepeatedPoints": {
        (Geometry, float): {
            "inst": Geometry,
            "type_hint": Geometry,
            "description": "args: geom, tolerance - Returns a version of a geometry with duplicate points removed.",
            "doc_url": "https://postgis.net/docs/ST_RemoveRepeatedPoints.html",
        }
    },
    "ST_Resample": {
        (Raster, float, float, float, float, float, float, str, float): {
            "inst": Raster,
            "type_hint": Raster,
            "description": "args: rast, scalex=0, scaley=0, gridx=NULL, gridy=NULL, skewx=0, skewy=0, algorithm=NearestNeighbor, maxerr=0.125 - Resample a raster using a specified resampling algorithm, new dimensions, an arbitrary grid corner and a set of raster georeferencing attributes defined or borrowed from another raster.",
            "doc_url": "https://postgis.net/docs/ST_Resample.html",
        },
        (Raster, int, int, float, float, float, float, str, float): {
            "inst": Raster,
            "type_hint": Raster,
            "description": "args: rast, width, height, gridx=NULL, gridy=NULL, skewx=0, skewy=0, algorithm=NearestNeighbor, maxerr=0.125 - Resample a raster using a specified resampling algorithm, new dimensions, an arbitrary grid corner and a set of raster georeferencing attributes defined or borrowed from another raster.",
            "doc_url": "https://postgis.net/docs/ST_Resample.html",
        },
        (Raster, Raster, str, float, bool): {
            "inst": Raster,
            "type_hint": Raster,
            "description": "args: rast, ref, algorithm=NearestNeighbor, maxerr=0.125, usescale=true - Resample a raster using a specified resampling algorithm, new dimensions, an arbitrary grid corner and a set of raster georeferencing attributes defined or borrowed from another raster.",
            "doc_url": "https://postgis.net/docs/ST_Resample.html",
        },
        (Raster, Raster, bool, str, float): {
            "inst": Raster,
            "type_hint": Raster,
            "description": "args: rast, ref, usescale, algorithm=NearestNeighbor, maxerr=0.125 - Resample a raster using a specified resampling algorithm, new dimensions, an arbitrary grid corner and a set of raster georeferencing attributes defined or borrowed from another raster.",
            "doc_url": "https://postgis.net/docs/ST_Resample.html",
        },
    },
    "ST_Rescale": {
        (Raster, float, float, str, float): {
            "inst": Raster,
            "type_hint": Raster,
            "description": "args: rast, scalex, scaley, algorithm=NearestNeighbor, maxerr=0.125 - Resample a raster by adjusting only its scale (or pixel size). New pixel values are computed using the NearestNeighbor (english or american spelling), Bilinear, Cubic, CubicSpline, Lanczos, Max or Min resampling algorithm. Default is NearestNeighbor.",
            "doc_url": "https://postgis.net/docs/ST_Rescale.html",
        },
        (Raster, float, str, float): {
            "inst": Raster,
            "type_hint": Raster,
            "description": "args: rast, scalexy, algorithm=NearestNeighbor, maxerr=0.125 - Resample a raster by adjusting only its scale (or pixel size). New pixel values are computed using the NearestNeighbor (english or american spelling), Bilinear, Cubic, CubicSpline, Lanczos, Max or Min resampling algorithm. Default is NearestNeighbor.",
            "doc_url": "https://postgis.net/docs/ST_Rescale.html",
        },
    },
    "ST_Resize": {
        (Raster, str, str, str, float): {
            "inst": Raster,
            "type_hint": Raster,
            "description": "args: rast, width, height, algorithm=NearestNeighbor, maxerr=0.125 - Resize a raster to a new width/height",
            "doc_url": "https://postgis.net/docs/ST_Resize.html",
        },
        (Raster, int, int, str, float): {
            "inst": Raster,
            "type_hint": Raster,
            "description": "args: rast, width, height, algorithm=NearestNeighbor, maxerr=0.125 - Resize a raster to a new width/height",
            "doc_url": "https://postgis.net/docs/ST_Resize.html",
        },
        (Raster, float, float, str, float): {
            "inst": Raster,
            "type_hint": Raster,
            "description": "args: rast, percentwidth, percentheight, algorithm=NearestNeighbor, maxerr=0.125 - Resize a raster to a new width/height",
            "doc_url": "https://postgis.net/docs/ST_Resize.html",
        },
    },
    "ST_Reskew": {
        (Raster, float, float, str, float): {
            "inst": Raster,
            "type_hint": Raster,
            "description": "args: rast, skewx, skewy, algorithm=NearestNeighbor, maxerr=0.125 - Resample a raster by adjusting only its skew (or rotation parameters). New pixel values are computed using the NearestNeighbor (english or american spelling), Bilinear, Cubic, CubicSpline or Lanczos resampling algorithm. Default is NearestNeighbor.",
            "doc_url": "https://postgis.net/docs/ST_Reskew.html",
        },
        (Raster, float, str, float): {
            "inst": Raster,
            "type_hint": Raster,
            "description": "args: rast, skewxy, algorithm=NearestNeighbor, maxerr=0.125 - Resample a raster by adjusting only its skew (or rotation parameters). New pixel values are computed using the NearestNeighbor (english or american spelling), Bilinear, Cubic, CubicSpline or Lanczos resampling algorithm. Default is NearestNeighbor.",
            "doc_url": "https://postgis.net/docs/ST_Reskew.html",
        },
    },
    "ST_Retile": {
        (Any, Any, Geometry, float, float, int, int, str): {
            "inst": Raster,
            "type_hint": List[Raster],
            "description": "args: tab, col, ext, sfx, sfy, tw, th, algo='NearestNeighbor' - Return a set of configured tiles from an arbitrarily tiled raster coverage.",
            "doc_url": "https://postgis.net/docs/ST_Retile.html",
        }
    },
    "ST_Reverse": {
        (Geometry,): {
            "inst": Geometry,
            "type_hint": Geometry,
            "description": "args: g1 - Return the geometry with vertex order reversed.",
            "doc_url": "https://postgis.net/docs/ST_Reverse.html",
        }
    },
    "ST_Rotate": {
        (Geometry, float): {
            "inst": Geometry,
            "type_hint": Geometry,
            "description": "args: geomA, rotRadians - Rotates a geometry about an origin point.",
            "doc_url": "https://postgis.net/docs/ST_Rotate.html",
        },
        (Geometry, float, float, float): {
            "inst": Geometry,
            "type_hint": Geometry,
            "description": "args: geomA, rotRadians, x0, y0 - Rotates a geometry about an origin point.",
            "doc_url": "https://postgis.net/docs/ST_Rotate.html",
        },
        (Geometry, float, Geometry): {
            "inst": Geometry,
            "type_hint": Geometry,
            "description": "args: geomA, rotRadians, pointOrigin - Rotates a geometry about an origin point.",
            "doc_url": "https://postgis.net/docs/ST_Rotate.html",
        },
    },
    "ST_RotateX": {
        (Geometry, float): {
            "inst": Geometry,
            "type_hint": Geometry,
            "description": "args: geomA, rotRadians - Rotates a geometry about the X axis.",
            "doc_url": "https://postgis.net/docs/ST_RotateX.html",
        }
    },
    "ST_RotateY": {
        (Geometry, float): {
            "inst": Geometry,
            "type_hint": Geometry,
            "description": "args: geomA, rotRadians - Rotates a geometry about the Y axis.",
            "doc_url": "https://postgis.net/docs/ST_RotateY.html",
        }
    },
    "ST_RotateZ": {
        (Geometry, float): {
            "inst": Geometry,
            "type_hint": Geometry,
            "description": "args: geomA, rotRadians - Rotates a geometry about the Z axis.",
            "doc_url": "https://postgis.net/docs/ST_RotateZ.html",
        }
    },
    "ST_Rotation": {
        (Raster,): {
            "inst": float,
            "type_hint": float,
            "description": "args: rast - Returns the rotation of the raster in radian.",
            "doc_url": "https://postgis.net/docs/ST_Rotation.html",
        }
    },
    "ST_Roughness": {
        (Raster, int, Raster, str, bool): {
            "inst": Raster,
            "type_hint": Raster,
            "description": "args: rast, nband, customextent, pixeltype='32BF', interpolate_nodata=FALSE - Returns a raster with the calculated 'roughness' of a DEM.",
            "doc_url": "https://postgis.net/docs/ST_Roughness.html",
        },
        (Raster, int, str, bool): {
            "inst": Raster,
            "type_hint": Raster,
            "description": "None",
            "doc_url": "https://postgis.net/docs/ST_Roughness.html",
        },
    },
    "ST_SRID": {
        (Geometry,): {
            "inst": int,
            "type_hint": int,
            "description": "args: g1 - Returns the spatial reference identifier for a geometry.",
            "doc_url": "https://postgis.net/docs/ST_SRID.html",
        },
        (Geography,): {
            "inst": int,
            "type_hint": int,
            "description": "None",
            "doc_url": "https://postgis.net/docs/ST_SRID.html",
        },
        (Raster,): {
            "inst": int,
            "type_hint": int,
            "description": "args: rast - Returns the spatial reference identifier of the raster as defined in spatial_ref_sys table.",
            "doc_url": "https://postgis.net/docs/ST_SRID.html",
        },
    },
    "ST_SameAlignment": {
        (Raster, Raster): {
            "inst": bool,
            "type_hint": bool,
            "description": "args: rastA, rastB - Returns true if rasters have same skew, scale, spatial ref, and offset (pixels can be put on same grid without cutting into pixels) and false if they dont with notice detailing issue.",
            "doc_url": "https://postgis.net/docs/ST_SameAlignment.html",
        },
        (float, float, float, float, float, float, float, float, float, float, float, float): {
            "inst": bool,
            "type_hint": bool,
            "description": "args: ulx1, uly1, scalex1, scaley1, skewx1, skewy1, ulx2, uly2, scalex2, scaley2, skewx2, skewy2 - Returns true if rasters have same skew, scale, spatial ref, and offset (pixels can be put on same grid without cutting into pixels) and false if they dont with notice detailing issue.",
            "doc_url": "https://postgis.net/docs/ST_SameAlignment.html",
        },
        (Raster,): {
            "inst": bool,
            "type_hint": bool,
            "description": "args: rastfield - Returns true if rasters have same skew, scale, spatial ref, and offset (pixels can be put on same grid without cutting into pixels) and false if they dont with notice detailing issue.",
            "doc_url": "https://postgis.net/docs/ST_SameAlignment.html",
        },
    },
    "ST_Scale": {
        (Geometry, float, float): {
            "inst": Geometry,
            "type_hint": Geometry,
            "description": "args: geomA, XFactor, YFactor - Scales a geometry by given factors.",
            "doc_url": "https://postgis.net/docs/ST_Scale.html",
        },
        (Geometry, Geometry): {
            "inst": Geometry,
            "type_hint": Geometry,
            "description": "args: geom, factor - Scales a geometry by given factors.",
            "doc_url": "https://postgis.net/docs/ST_Scale.html",
        },
        (Geometry, Geometry, Geometry): {
            "inst": Geometry,
            "type_hint": Geometry,
            "description": "args: geom, factor, origin - Scales a geometry by given factors.",
            "doc_url": "https://postgis.net/docs/ST_Scale.html",
        },
        (Geometry, float, float, float): {
            "inst": Geometry,
            "type_hint": Geometry,
            "description": "args: geomA, XFactor, YFactor, ZFactor - Scales a geometry by given factors.",
            "doc_url": "https://postgis.net/docs/ST_Scale.html",
        },
    },
    "ST_ScaleX": {
        (Raster,): {
            "inst": float,
            "type_hint": float,
            "description": "args: rast - Returns the X component of the pixel width in units of coordinate reference system.",
            "doc_url": "https://postgis.net/docs/ST_ScaleX.html",
        }
    },
    "ST_ScaleY": {
        (Raster,): {
            "inst": float,
            "type_hint": float,
            "description": "args: rast - Returns the Y component of the pixel height in units of coordinate reference system.",
            "doc_url": "https://postgis.net/docs/ST_ScaleY.html",
        }
    },
    "ST_Scroll": {
        (Geometry, Geometry): {
            "inst": Geometry,
            "type_hint": Geometry,
            "description": "args: linestring, point - Change start point of a closed LineString.",
            "doc_url": "https://postgis.net/docs/ST_Scroll.html",
        }
    },
    "ST_Segmentize": {
        (Geometry, float): {
            "inst": Geometry,
            "type_hint": Geometry,
            "description": "args: geom, max_segment_length - Returns a modified geometry/geography having no segment longer than a given distance.",
            "doc_url": "https://postgis.net/docs/ST_Segmentize.html",
        },
        (Geography, float): {
            "inst": Geography,
            "type_hint": Geography,
            "description": "args: geog, max_segment_length - Returns a modified geometry/geography having no segment longer than a given distance.",
            "doc_url": "https://postgis.net/docs/ST_Segmentize.html",
        },
    },
    "ST_SetBandIndex": {
        (Raster, int, int, bool): {
            "inst": Raster,
            "type_hint": Raster,
            "description": "args: rast, band, outdbindex, force=false - Update the external band number of an out-db band",
            "doc_url": "https://postgis.net/docs/ST_SetBandIndex.html",
        }
    },
    "ST_SetBandIsNoData": {
        (Raster, int): {
            "inst": Raster,
            "type_hint": Raster,
            "description": "args: rast, band=1 - Sets the isnodata flag of the band to TRUE.",
            "doc_url": "https://postgis.net/docs/ST_SetBandIsNoData.html",
        }
    },
    "ST_SetBandNoDataValue": {
        (Raster, int, float, bool): {
            "inst": Raster,
            "type_hint": Raster,
            "description": "args: rast, band, nodatavalue, forcechecking=false - Sets the value for the given band that represents no data. Band 1 is assumed if no band is specified. To mark a band as having no nodata value, set the nodata value = NULL.",
            "doc_url": "https://postgis.net/docs/ST_SetBandNoDataValue.html",
        },
        (Raster, float): {
            "inst": Raster,
            "type_hint": Raster,
            "description": "args: rast, nodatavalue - Sets the value for the given band that represents no data. Band 1 is assumed if no band is specified. To mark a band as having no nodata value, set the nodata value = NULL.",
            "doc_url": "https://postgis.net/docs/ST_SetBandNoDataValue.html",
        },
    },
    "ST_SetBandPath": {
        (Raster, int, str, int, bool): {
            "inst": Raster,
            "type_hint": Raster,
            "description": "args: rast, band, outdbpath, outdbindex, force=false - Update the external path and band number of an out-db band",
            "doc_url": "https://postgis.net/docs/ST_SetBandPath.html",
        }
    },
    "ST_SetEffectiveArea": {
        (Geometry, float, int): {
            "inst": Geometry,
            "type_hint": Geometry,
            "description": "args: geomA, threshold = 0, set_area = 1 - Sets the effective area for each vertex, using the Visvalingam-Whyatt algorithm.",
            "doc_url": "https://postgis.net/docs/ST_SetEffectiveArea.html",
        }
    },
    "ST_SetGeoReference": {
        (Raster, str, str): {
            "inst": Raster,
            "type_hint": Raster,
            "description": "args: rast, georefcoords, format=GDAL - Set Georeference 6 georeference parameters in a single call. Numbers should be separated by white space. Accepts inputs in GDAL or ESRI format. Default is GDAL.",
            "doc_url": "https://postgis.net/docs/ST_SetGeoReference.html",
        },
        (Raster, float, float, float, float, float, float): {
            "inst": Raster,
            "type_hint": Raster,
            "description": "args: rast, upperleftx, upperlefty, scalex, scaley, skewx, skewy - Set Georeference 6 georeference parameters in a single call. Numbers should be separated by white space. Accepts inputs in GDAL or ESRI format. Default is GDAL.",
            "doc_url": "https://postgis.net/docs/ST_SetGeoReference.html",
        },
    },
    "ST_SetM": {
        (Raster, Geometry, str, int): {
            "inst": Geometry,
            "type_hint": Geometry,
            "description": "args: rast, geom, resample=nearest, band=1 - Returns a geometry with the same X/Y coordinates as the input geometry, and values from the raster copied into the M dimension using the requested resample algorithm.",
            "doc_url": "https://postgis.net/docs/ST_SetM.html",
        }
    },
    "ST_SetPoint": {
        (Geometry, int, Geometry): {
            "inst": Geometry,
            "type_hint": Geometry,
            "description": "args: linestring, zerobasedposition, point - Replace point of a linestring with a given point.",
            "doc_url": "https://postgis.net/docs/ST_SetPoint.html",
        }
    },
    "ST_SetRotation": {
        (Raster, float): {
            "inst": Raster,
            "type_hint": Raster,
            "description": "args: rast, rotation - Set the rotation of the raster in radian.",
            "doc_url": "https://postgis.net/docs/ST_SetRotation.html",
        }
    },
    "ST_SetSRID": {
        (Geometry, int): {
            "inst": Geometry,
            "type_hint": Geometry,
            "description": "args: geom, srid - Set the SRID on a geometry.",
            "doc_url": "https://postgis.net/docs/ST_SetSRID.html",
        },
        (Geography, int): {
            "inst": Geography,
            "type_hint": Geography,
            "description": "None",
            "doc_url": "https://postgis.net/docs/ST_SetSRID.html",
        },
        (Raster, int): {
            "inst": Raster,
            "type_hint": Raster,
            "description": "args: rast, srid - Sets the SRID of a raster to a particular integer srid defined in the spatial_ref_sys table.",
            "doc_url": "https://postgis.net/docs/ST_SetSRID.html",
        },
    },
    "ST_SetScale": {
        (Raster, float): {
            "inst": Raster,
            "type_hint": Raster,
            "description": "args: rast, xy - Sets the X and Y size of pixels in units of coordinate reference system. Number units/pixel width/height.",
            "doc_url": "https://postgis.net/docs/ST_SetScale.html",
        },
        (Raster, float, float): {
            "inst": Raster,
            "type_hint": Raster,
            "description": "args: rast, x, y - Sets the X and Y size of pixels in units of coordinate reference system. Number units/pixel width/height.",
            "doc_url": "https://postgis.net/docs/ST_SetScale.html",
        },
    },
    "ST_SetSkew": {
        (Raster, float): {
            "inst": Raster,
            "type_hint": Raster,
            "description": "args: rast, skewxy - Sets the georeference X and Y skew (or rotation parameter). If only one is passed in, sets X and Y to the same value.",
            "doc_url": "https://postgis.net/docs/ST_SetSkew.html",
        },
        (Raster, float, float): {
            "inst": Raster,
            "type_hint": Raster,
            "description": "args: rast, skewx, skewy - Sets the georeference X and Y skew (or rotation parameter). If only one is passed in, sets X and Y to the same value.",
            "doc_url": "https://postgis.net/docs/ST_SetSkew.html",
        },
    },
    "ST_SetUpperLeft": {
        (Raster, float, float): {
            "inst": Raster,
            "type_hint": Raster,
            "description": "args: rast, x, y - Sets the value of the upper left corner of the pixel of the raster to projected X and Y coordinates.",
            "doc_url": "https://postgis.net/docs/ST_SetUpperLeft.html",
        }
    },
    "ST_SetValue": {
        (Raster, int, int, int, float): {
            "inst": Raster,
            "type_hint": Raster,
            "description": "args: rast, bandnum, columnx, rowy, newvalue - Returns modified raster resulting from setting the value of a given band in a given columnx, rowy pixel or the pixels that intersect a particular geometry. Band numbers start at 1 and assumed to be 1 if not specified.",
            "doc_url": "https://postgis.net/docs/ST_SetValue.html",
        },
        (Raster, int, int, float): {
            "inst": Raster,
            "type_hint": Raster,
            "description": "args: rast, columnx, rowy, newvalue - Returns modified raster resulting from setting the value of a given band in a given columnx, rowy pixel or the pixels that intersect a particular geometry. Band numbers start at 1 and assumed to be 1 if not specified.",
            "doc_url": "https://postgis.net/docs/ST_SetValue.html",
        },
        (Raster, int, Geometry, float): {
            "inst": Raster,
            "type_hint": Raster,
            "description": "args: rast, bandnum, geom, newvalue - Returns modified raster resulting from setting the value of a given band in a given columnx, rowy pixel or the pixels that intersect a particular geometry. Band numbers start at 1 and assumed to be 1 if not specified.",
            "doc_url": "https://postgis.net/docs/ST_SetValue.html",
        },
        (Raster, Geometry, float): {
            "inst": Raster,
            "type_hint": Raster,
            "description": "args: rast, geom, newvalue - Returns modified raster resulting from setting the value of a given band in a given columnx, rowy pixel or the pixels that intersect a particular geometry. Band numbers start at 1 and assumed to be 1 if not specified.",
            "doc_url": "https://postgis.net/docs/ST_SetValue.html",
        },
    },
    "ST_SetValues": {
        (Raster, int, int, int, List[float], List[bool], bool): {
            "inst": Raster,
            "type_hint": Raster,
            "description": "args: rast, nband, columnx, rowy, newvalueset, noset=NULL, keepnodata=FALSE - Returns modified raster resulting from setting the values of a given band.",
            "doc_url": "https://postgis.net/docs/ST_SetValues.html",
        },
        (Raster, int, int, int, List[float], float, bool): {
            "inst": Raster,
            "type_hint": Raster,
            "description": "args: rast, nband, columnx, rowy, newvalueset, nosetvalue, keepnodata=FALSE - Returns modified raster resulting from setting the values of a given band.",
            "doc_url": "https://postgis.net/docs/ST_SetValues.html",
        },
        (Raster, int, int, int, int, int, float, bool): {
            "inst": Raster,
            "type_hint": Raster,
            "description": "args: rast, nband, columnx, rowy, width, height, newvalue, keepnodata=FALSE - Returns modified raster resulting from setting the values of a given band.",
            "doc_url": "https://postgis.net/docs/ST_SetValues.html",
        },
        (Raster, int, int, int, int, float, bool): {
            "inst": Raster,
            "type_hint": Raster,
            "description": "args: rast, columnx, rowy, width, height, newvalue, keepnodata=FALSE - Returns modified raster resulting from setting the values of a given band.",
            "doc_url": "https://postgis.net/docs/ST_SetValues.html",
        },
        (Raster, int, List[GeomVal], bool): {
            "inst": Raster,
            "type_hint": Raster,
            "description": "args: rast, nband, geomvalset, keepnodata=FALSE - Returns modified raster resulting from setting the values of a given band.",
            "doc_url": "https://postgis.net/docs/ST_SetValues.html",
        },
    },
    "ST_SetZ": {
        (Raster, Geometry, str, int): {
            "inst": Geometry,
            "type_hint": Geometry,
            "description": "args: rast, geom, resample=nearest, band=1 - Returns a geometry with the same X/Y coordinates as the input geometry, and values from the raster copied into the Z dimension using the requested resample algorithm.",
            "doc_url": "https://postgis.net/docs/ST_SetZ.html",
        }
    },
    "ST_SharedPaths": {
        (Geometry, Geometry): {
            "inst": Geometry,
            "type_hint": Geometry,
            "description": "args: lineal1, lineal2 - Returns a collection containing paths shared by the two input linestrings/multilinestrings.",
            "doc_url": "https://postgis.net/docs/ST_SharedPaths.html",
        }
    },
    "ST_ShiftLongitude": {
        (Geometry,): {
            "inst": Geometry,
            "type_hint": Geometry,
            "description": "args: geom - Shifts the longitude coordinates of a geometry between -180..180 and 0..360.",
            "doc_url": "https://postgis.net/docs/ST_ShiftLongitude.html",
        }
    },
    "ST_ShortestLine": {
        (Geometry, Geometry): {
            "inst": Geometry,
            "type_hint": Geometry,
            "description": "args: geom1, geom2 - Returns the 2D shortest line between two geometries",
            "doc_url": "https://postgis.net/docs/ST_ShortestLine.html",
        },
        (Geography, Geography, bool): {
            "inst": Geography,
            "type_hint": Geography,
            "description": "args: geom1, geom2, use_spheroid = true - Returns the 2D shortest line between two geometries",
            "doc_url": "https://postgis.net/docs/ST_ShortestLine.html",
        },
        (str, str): {
            "inst": Geometry,
            "type_hint": Geometry,
            "description": "None",
            "doc_url": "https://postgis.net/docs/ST_ShortestLine.html",
        },
    },
    "ST_Simplify": {
        (Geometry, float): {
            "inst": Geometry,
            "type_hint": Geometry,
            "description": "args: geomA, tolerance - Returns a simplified version of a geometry, using the Douglas-Peucker algorithm.",
            "doc_url": "https://postgis.net/docs/ST_Simplify.html",
        },
        (Geometry, float, bool): {
            "inst": Geometry,
            "type_hint": Geometry,
            "description": "args: geomA, tolerance, preserveCollapsed - Returns a simplified version of a geometry, using the Douglas-Peucker algorithm.",
            "doc_url": "https://postgis.net/docs/ST_Simplify.html",
        },
    },
    "ST_SimplifyPolygonHull": {
        (Geometry, float, bool): {
            "inst": Geometry,
            "type_hint": Geometry,
            "description": "args: param_geom, vertex_fraction, is_outer = true - Computes a simplified topology-preserving outer or inner hull of a polygonal geometry.",
            "doc_url": "https://postgis.net/docs/ST_SimplifyPolygonHull.html",
        }
    },
    "ST_SimplifyPreserveTopology": {
        (Geometry, float): {
            "inst": Geometry,
            "type_hint": Geometry,
            "description": "args: geomA, tolerance - Returns a simplified and valid version of a geometry, using the Douglas-Peucker algorithm.",
            "doc_url": "https://postgis.net/docs/ST_SimplifyPreserveTopology.html",
        }
    },
    "ST_SimplifyVW": {
        (Geometry, float): {
            "inst": Geometry,
            "type_hint": Geometry,
            "description": "args: geomA, tolerance - Returns a simplified version of a geometry, using the Visvalingam-Whyatt algorithm",
            "doc_url": "https://postgis.net/docs/ST_SimplifyVW.html",
        }
    },
    "ST_SkewX": {
        (Raster,): {
            "inst": float,
            "type_hint": float,
            "description": "args: rast - Returns the georeference X skew (or rotation parameter).",
            "doc_url": "https://postgis.net/docs/ST_SkewX.html",
        }
    },
    "ST_SkewY": {
        (Raster,): {
            "inst": float,
            "type_hint": float,
            "description": "args: rast - Returns the georeference Y skew (or rotation parameter).",
            "doc_url": "https://postgis.net/docs/ST_SkewY.html",
        }
    },
    "ST_Slope": {
        (Raster, int, Raster, str, str, float, bool): {
            "inst": Raster,
            "type_hint": Raster,
            "description": "args: rast, nband, customextent, pixeltype=32BF, units=DEGREES, scale=1.0, interpolate_nodata=FALSE - Returns the slope (in degrees by default) of an elevation raster band. Useful for analyzing terrain.",
            "doc_url": "https://postgis.net/docs/ST_Slope.html",
        },
        (Raster, int, str, str, float, bool): {
            "inst": Raster,
            "type_hint": Raster,
            "description": "args: rast, nband=1, pixeltype=32BF, units=DEGREES, scale=1.0, interpolate_nodata=FALSE - Returns the slope (in degrees by default) of an elevation raster band. Useful for analyzing terrain.",
            "doc_url": "https://postgis.net/docs/ST_Slope.html",
        },
    },
    "ST_Snap": {
        (Geometry, Geometry, float): {
            "inst": Geometry,
            "type_hint": Geometry,
            "description": "args: input, reference, tolerance - Snap segments and vertices of input geometry to vertices of a reference geometry.",
            "doc_url": "https://postgis.net/docs/ST_Snap.html",
        }
    },
    "ST_SnapToGrid": {
        (Geometry, float, float, float, float): {
            "inst": Geometry,
            "type_hint": Geometry,
            "description": "args: geomA, originX, originY, sizeX, sizeY - Snap all points of the input geometry to a regular grid.",
            "doc_url": "https://postgis.net/docs/ST_SnapToGrid.html",
        },
        (Geometry, float, float): {
            "inst": Geometry,
            "type_hint": Geometry,
            "description": "args: geomA, sizeX, sizeY - Snap all points of the input geometry to a regular grid.",
            "doc_url": "https://postgis.net/docs/ST_SnapToGrid.html",
        },
        (Geometry, float): {
            "inst": Geometry,
            "type_hint": Geometry,
            "description": "args: geomA, size - Snap all points of the input geometry to a regular grid.",
            "doc_url": "https://postgis.net/docs/ST_SnapToGrid.html",
        },
        (Geometry, Geometry, float, float, float, float): {
            "inst": Geometry,
            "type_hint": Geometry,
            "description": "args: geomA, pointOrigin, sizeX, sizeY, sizeZ, sizeM - Snap all points of the input geometry to a regular grid.",
            "doc_url": "https://postgis.net/docs/ST_SnapToGrid.html",
        },
        (Raster, float, float, str, float, float, float): {
            "inst": Raster,
            "type_hint": Raster,
            "description": "args: rast, gridx, gridy, algorithm=NearestNeighbor, maxerr=0.125, scalex=DEFAULT 0, scaley=DEFAULT 0 - Resample a raster by snapping it to a grid. New pixel values are computed using the NearestNeighbor (english or american spelling), Bilinear, Cubic, CubicSpline or Lanczos resampling algorithm. Default is NearestNeighbor.",
            "doc_url": "https://postgis.net/docs/ST_SnapToGrid.html",
        },
        (Raster, float, float, float, float, str, float): {
            "inst": Raster,
            "type_hint": Raster,
            "description": "args: rast, gridx, gridy, scalex, scaley, algorithm=NearestNeighbor, maxerr=0.125 - Resample a raster by snapping it to a grid. New pixel values are computed using the NearestNeighbor (english or american spelling), Bilinear, Cubic, CubicSpline or Lanczos resampling algorithm. Default is NearestNeighbor.",
            "doc_url": "https://postgis.net/docs/ST_SnapToGrid.html",
        },
        (Raster, float, float, float, str, float): {
            "inst": Raster,
            "type_hint": Raster,
            "description": "args: rast, gridx, gridy, scalexy, algorithm=NearestNeighbor, maxerr=0.125 - Resample a raster by snapping it to a grid. New pixel values are computed using the NearestNeighbor (english or american spelling), Bilinear, Cubic, CubicSpline or Lanczos resampling algorithm. Default is NearestNeighbor.",
            "doc_url": "https://postgis.net/docs/ST_SnapToGrid.html",
        },
    },
    "ST_Split": {
        (Geometry, Geometry): {
            "inst": Geometry,
            "type_hint": Geometry,
            "description": "args: input, blade - Returns a collection of geometries created by splitting a geometry by another geometry.",
            "doc_url": "https://postgis.net/docs/ST_Split.html",
        }
    },
    "ST_Square": {
        (float, int, int, Geometry): {
            "inst": Geometry,
            "type_hint": Geometry,
            "description": "args: size, cell_i, cell_j, origin - Returns a single square, using the provided edge size and cell coordinate within the square grid space.",
            "doc_url": "https://postgis.net/docs/ST_Square.html",
        }
    },
    "ST_SquareGrid": {
        (float, Geometry, Geometry, int, int): {
            "inst": object,
            "type_hint": List[Any],
            "description": "args: size, bounds - Returns a set of grid squares and cell indices that completely cover the bounds of the geometry argument.",
            "doc_url": "https://postgis.net/docs/ST_SquareGrid.html",
        }
    },
    "ST_StartPoint": {
        (Geometry,): {
            "inst": Geometry,
            "type_hint": Geometry,
            "description": "args: geomA - Returns the first point of a LineString.",
            "doc_url": "https://postgis.net/docs/ST_StartPoint.html",
        }
    },
    "ST_StdDev4ma": {
        (List[float], str, List[Any]): {
            "inst": float,
            "type_hint": float,
            "description": "args: matrix, nodatamode, VARIADIC args - Raster processing function that calculates the standard deviation of pixel values in a neighborhood.",
            "doc_url": "https://postgis.net/docs/ST_StdDev4ma.html",
        },
        (List[float], List[int], List[Any]): {
            "inst": float,
            "type_hint": float,
            "description": "args: value, pos, VARIADIC userargs - Raster processing function that calculates the standard deviation of pixel values in a neighborhood.",
            "doc_url": "https://postgis.net/docs/ST_StdDev4ma.html",
        },
    },
    "ST_Subdivide": {
        (Geometry, int, float): {
            "inst": Geometry,
            "type_hint": List[Geometry],
            "description": "args: geom, max_vertices=256, gridSize = -1 - Computes a rectilinear subdivision of a geometry.",
            "doc_url": "https://postgis.net/docs/ST_Subdivide.html",
        }
    },
    "ST_Sum4ma": {
        (List[float], str, List[Any]): {
            "inst": float,
            "type_hint": float,
            "description": "args: matrix, nodatamode, VARIADIC args - Raster processing function that calculates the sum of all pixel values in a neighborhood.",
            "doc_url": "https://postgis.net/docs/ST_Sum4ma.html",
        },
        (List[float], List[int], List[Any]): {
            "inst": float,
            "type_hint": float,
            "description": "args: value, pos, VARIADIC userargs - Raster processing function that calculates the sum of all pixel values in a neighborhood.",
            "doc_url": "https://postgis.net/docs/ST_Sum4ma.html",
        },
    },
    "ST_Summary": {
        (Geometry,): {
            "inst": str,
            "type_hint": str,
            "description": "args: g - Returns a text summary of the contents of a geometry.",
            "doc_url": "https://postgis.net/docs/ST_Summary.html",
        },
        (Geography,): {
            "inst": str,
            "type_hint": str,
            "description": "args: g - Returns a text summary of the contents of a geometry.",
            "doc_url": "https://postgis.net/docs/ST_Summary.html",
        },
        (Raster,): {
            "inst": str,
            "type_hint": str,
            "description": "args: rast - Returns a text summary of the contents of the raster.",
            "doc_url": "https://postgis.net/docs/ST_Summary.html",
        },
    },
    "ST_SummaryStats": {
        (Raster, int, bool): {
            "inst": SummaryStats,
            "type_hint": SummaryStats,
            "description": "args: rast, nband, exclude_nodata_value - Returns summarystats consisting of count, sum, mean, stddev, min, max for a given raster band of a raster or raster coverage. Band 1 is assumed is no band is specified.",
            "doc_url": "https://postgis.net/docs/ST_SummaryStats.html",
        },
        (Raster, bool): {
            "inst": SummaryStats,
            "type_hint": SummaryStats,
            "description": "args: rast, exclude_nodata_value - Returns summarystats consisting of count, sum, mean, stddev, min, max for a given raster band of a raster or raster coverage. Band 1 is assumed is no band is specified.",
            "doc_url": "https://postgis.net/docs/ST_SummaryStats.html",
        },
    },
    "ST_SummaryStatsAgg": {
        (Raster, int, bool, float): {
            "inst": SummaryStats,
            "type_hint": SummaryStats,
            "description": "args: rast, nband, exclude_nodata_value, sample_percent - Aggregate. Returns summarystats consisting of count, sum, mean, stddev, min, max for a given raster band of a set of raster. Band 1 is assumed is no band is specified.",
            "doc_url": "https://postgis.net/docs/ST_SummaryStatsAgg.html",
        },
        (Raster, bool, float): {
            "inst": SummaryStats,
            "type_hint": SummaryStats,
            "description": "args: rast, exclude_nodata_value, sample_percent - Aggregate. Returns summarystats consisting of count, sum, mean, stddev, min, max for a given raster band of a set of raster. Band 1 is assumed is no band is specified.",
            "doc_url": "https://postgis.net/docs/ST_SummaryStatsAgg.html",
        },
        (Raster, int, bool): {
            "inst": SummaryStats,
            "type_hint": SummaryStats,
            "description": "args: rast, nband, exclude_nodata_value - Aggregate. Returns summarystats consisting of count, sum, mean, stddev, min, max for a given raster band of a set of raster. Band 1 is assumed is no band is specified.",
            "doc_url": "https://postgis.net/docs/ST_SummaryStatsAgg.html",
        },
    },
    "ST_SwapOrdinates": {
        (Geometry, str): {
            "inst": Geometry,
            "type_hint": Geometry,
            "description": "args: geom, ords - Returns a version of the given geometry with given ordinate values swapped.",
            "doc_url": "https://postgis.net/docs/ST_SwapOrdinates.html",
        }
    },
    "ST_SymDifference": {
        (Geometry, Geometry, float): {
            "inst": Geometry,
            "type_hint": Geometry,
            "description": "args: geomA, geomB, gridSize = -1 - Computes a geometry representing the portions of geometries A and B that do not intersect.",
            "doc_url": "https://postgis.net/docs/ST_SymDifference.html",
        }
    },
    "ST_TPI": {
        (Raster, int, str, bool): {
            "inst": Raster,
            "type_hint": Raster,
            "description": "None",
            "doc_url": "https://postgis.net/docs/ST_TPI.html",
        },
        (Raster, int, Raster, str, bool): {
            "inst": Raster,
            "type_hint": Raster,
            "description": "args: rast, nband, customextent, pixeltype='32BF', interpolate_nodata=FALSE - Returns a raster with the calculated Topographic Position Index.",
            "doc_url": "https://postgis.net/docs/ST_TPI.html",
        },
    },
    "ST_Tile": {
        (Raster, List[int], int, int, bool, float): {
            "inst": Raster,
            "type_hint": List[Raster],
            "description": "args: rast, nband, width, height, padwithnodata=FALSE, nodataval=NULL - Returns a set of rasters resulting from the split of the input raster based upon the desired dimensions of the output rasters.",
            "doc_url": "https://postgis.net/docs/ST_Tile.html",
        },
        (Raster, int, int, int, bool, float): {
            "inst": Raster,
            "type_hint": List[Raster],
            "description": "args: rast, nband, width, height, padwithnodata=FALSE, nodataval=NULL - Returns a set of rasters resulting from the split of the input raster based upon the desired dimensions of the output rasters.",
            "doc_url": "https://postgis.net/docs/ST_Tile.html",
        },
        (Raster, int, int, bool, float): {
            "inst": Raster,
            "type_hint": List[Raster],
            "description": "args: rast, width, height, padwithnodata=FALSE, nodataval=NULL - Returns a set of rasters resulting from the split of the input raster based upon the desired dimensions of the output rasters.",
            "doc_url": "https://postgis.net/docs/ST_Tile.html",
        },
    },
    "ST_TileEnvelope": {
        (int, int, int, Geometry, float): {
            "inst": Geometry,
            "type_hint": Geometry,
            "description": "args: tileZoom, tileX, tileY, bounds=SRID=3857;LINESTRING(-20037508.342789 -20037508.342789,20037508.342789 20037508.342789), margin=0.0 - Creates a rectangular Polygon in Web Mercator (SRID:3857) using the XYZ tile system.",
            "doc_url": "https://postgis.net/docs/ST_TileEnvelope.html",
        }
    },
    "ST_Touches": {
        (Geometry, Geometry): {
            "inst": bool,
            "type_hint": bool,
            "description": "None",
            "doc_url": "https://postgis.net/docs/ST_Touches.html",
        },
        (Raster, int, Raster, int): {
            "inst": bool,
            "type_hint": bool,
            "description": "args: rastA, nbandA, rastB, nbandB - Return true if raster rastA and rastB have at least one point in common but their interiors do not intersect.",
            "doc_url": "https://postgis.net/docs/ST_Touches.html",
        },
        (Raster, Raster): {
            "inst": bool,
            "type_hint": bool,
            "description": "args: rastA, rastB - Return true if raster rastA and rastB have at least one point in common but their interiors do not intersect.",
            "doc_url": "https://postgis.net/docs/ST_Touches.html",
        },
    },
    "ST_TransScale": {
        (Geometry, float, float, float, float): {
            "inst": Geometry,
            "type_hint": Geometry,
            "description": "args: geomA, deltaX, deltaY, XFactor, YFactor - Translates and scales a geometry by given offsets and factors.",
            "doc_url": "https://postgis.net/docs/ST_TransScale.html",
        }
    },
    "ST_Transform": {
        (Geometry, int): {
            "inst": Geometry,
            "type_hint": Geometry,
            "description": "args: g1, srid - Return a new geometry with coordinates transformed to a different spatial reference system.",
            "doc_url": "https://postgis.net/docs/ST_Transform.html",
        },
        (Geometry, str): {
            "inst": Geometry,
            "type_hint": Geometry,
            "description": "args: geom, to_proj - Return a new geometry with coordinates transformed to a different spatial reference system.",
            "doc_url": "https://postgis.net/docs/ST_Transform.html",
        },
        (Geometry, str, str): {
            "inst": Geometry,
            "type_hint": Geometry,
            "description": "args: geom, from_proj, to_proj - Return a new geometry with coordinates transformed to a different spatial reference system.",
            "doc_url": "https://postgis.net/docs/ST_Transform.html",
        },
        (Geometry, str, int): {
            "inst": Geometry,
            "type_hint": Geometry,
            "description": "args: geom, from_proj, to_srid - Return a new geometry with coordinates transformed to a different spatial reference system.",
            "doc_url": "https://postgis.net/docs/ST_Transform.html",
        },
        (Raster, int, str, float, float, float): {
            "inst": Raster,
            "type_hint": Raster,
            "description": "args: rast, srid, algorithm=NearestNeighbor, maxerr=0.125, scalex, scaley - Reprojects a raster in a known spatial reference system to another known spatial reference system using specified resampling algorithm. Options are NearestNeighbor, Bilinear, Cubic, CubicSpline, Lanczos defaulting to NearestNeighbor.",
            "doc_url": "https://postgis.net/docs/ST_Transform.html",
        },
        (Raster, int, float, float, str, float): {
            "inst": Raster,
            "type_hint": Raster,
            "description": "args: rast, srid, scalex, scaley, algorithm=NearestNeighbor, maxerr=0.125 - Reprojects a raster in a known spatial reference system to another known spatial reference system using specified resampling algorithm. Options are NearestNeighbor, Bilinear, Cubic, CubicSpline, Lanczos defaulting to NearestNeighbor.",
            "doc_url": "https://postgis.net/docs/ST_Transform.html",
        },
        (Raster, int, float, str, float): {
            "inst": Raster,
            "type_hint": Raster,
            "description": "None",
            "doc_url": "https://postgis.net/docs/ST_Transform.html",
        },
        (Raster, Raster, str, float): {
            "inst": Raster,
            "type_hint": Raster,
            "description": "args: rast, alignto, algorithm=NearestNeighbor, maxerr=0.125 - Reprojects a raster in a known spatial reference system to another known spatial reference system using specified resampling algorithm. Options are NearestNeighbor, Bilinear, Cubic, CubicSpline, Lanczos defaulting to NearestNeighbor.",
            "doc_url": "https://postgis.net/docs/ST_Transform.html",
        },
    },
    "ST_TransformPipeline": {
        (Geometry, str, int): {
            "inst": Geometry,
            "type_hint": Geometry,
            "description": "args: g1, pipeline, to_srid - Return a new geometry with coordinates transformed to a different spatial reference system using a defined coordinate transformation pipeline.",
            "doc_url": "https://postgis.net/docs/ST_TransformPipeline.html",
        }
    },
    "ST_Translate": {
        (Geometry, float, float, float): {
            "inst": Geometry,
            "type_hint": Geometry,
            "description": "args: g1, deltax, deltay, deltaz - Translates a geometry by given offsets.",
            "doc_url": "https://postgis.net/docs/ST_Translate.html",
        },
        (Geometry, float, float): {
            "inst": Geometry,
            "type_hint": Geometry,
            "description": "args: g1, deltax, deltay - Translates a geometry by given offsets.",
            "doc_url": "https://postgis.net/docs/ST_Translate.html",
        },
    },
    "ST_Tri": {
        (Raster, int, Raster, str, bool): {
            "inst": Raster,
            "type_hint": Raster,
            "description": "args: rast, nband, customextent, pixeltype='32BF', interpolate_nodata=FALSE - Returns a raster with the calculated Terrain Ruggedness Index.",
            "doc_url": "https://postgis.net/docs/ST_Tri.html",
        },
        (Raster, int, str, bool): {
            "inst": Raster,
            "type_hint": Raster,
            "description": "None",
            "doc_url": "https://postgis.net/docs/ST_Tri.html",
        },
    },
    "ST_TriangulatePolygon": {
        (Geometry,): {
            "inst": Geometry,
            "type_hint": Geometry,
            "description": "args: geom - Computes the constrained Delaunay triangulation of polygons",
            "doc_url": "https://postgis.net/docs/ST_TriangulatePolygon.html",
        }
    },
    "ST_UnaryUnion": {
        (Geometry, float): {
            "inst": Geometry,
            "type_hint": Geometry,
            "description": "args: geom, gridSize = -1 - Computes the union of the components of a single geometry.",
            "doc_url": "https://postgis.net/docs/ST_UnaryUnion.html",
        }
    },
    "ST_Union": {
        (Geometry,): {
            "inst": Geometry,
            "type_hint": Geometry,
            "description": "args: g1field - Computes a geometry representing the point-set union of the input geometries.",
            "doc_url": "https://postgis.net/docs/ST_Union.html",
        },
        (Geometry, Geometry): {
            "inst": Geometry,
            "type_hint": Geometry,
            "description": "args: g1, g2 - Computes a geometry representing the point-set union of the input geometries.",
            "doc_url": "https://postgis.net/docs/ST_Union.html",
        },
        (Geometry, Geometry, float): {
            "inst": Geometry,
            "type_hint": Geometry,
            "description": "args: g1, g2, gridSize - Computes a geometry representing the point-set union of the input geometries.",
            "doc_url": "https://postgis.net/docs/ST_Union.html",
        },
        (Geometry, float): {
            "inst": Geometry,
            "type_hint": Geometry,
            "description": "args: g1field, gridSize - Computes a geometry representing the point-set union of the input geometries.",
            "doc_url": "https://postgis.net/docs/ST_Union.html",
        },
        (List[Geometry],): {
            "inst": Geometry,
            "type_hint": Geometry,
            "description": "args: g1_array - Computes a geometry representing the point-set union of the input geometries.",
            "doc_url": "https://postgis.net/docs/ST_Union.html",
        },
        (Raster, int, str): {
            "inst": Raster,
            "type_hint": Raster,
            "description": "args: rast, nband, uniontype - Returns the union of a set of raster tiles into a single raster composed of 1 or more bands.",
            "doc_url": "https://postgis.net/docs/ST_Union.html",
        },
        (Raster, List[Any]): {
            "inst": Raster,
            "type_hint": Raster,
            "description": "args: rast, unionargset - Returns the union of a set of raster tiles into a single raster composed of 1 or more bands.",
            "doc_url": "https://postgis.net/docs/ST_Union.html",
        },
        (Raster, int): {
            "inst": Raster,
            "type_hint": Raster,
            "description": "args: rast, nband - Returns the union of a set of raster tiles into a single raster composed of 1 or more bands.",
            "doc_url": "https://postgis.net/docs/ST_Union.html",
        },
        (Raster,): {
            "inst": Raster,
            "type_hint": Raster,
            "description": "args: rast - Returns the union of a set of raster tiles into a single raster composed of 1 or more bands.",
            "doc_url": "https://postgis.net/docs/ST_Union.html",
        },
        (Raster, str): {
            "inst": Raster,
            "type_hint": Raster,
            "description": "args: rast, uniontype - Returns the union of a set of raster tiles into a single raster composed of 1 or more bands.",
            "doc_url": "https://postgis.net/docs/ST_Union.html",
        },
    },
    "ST_UpperLeftX": {
        (Raster,): {
            "inst": float,
            "type_hint": float,
            "description": "args: rast - Returns the upper left X coordinate of raster in projected spatial ref.",
            "doc_url": "https://postgis.net/docs/ST_UpperLeftX.html",
        }
    },
    "ST_UpperLeftY": {
        (Raster,): {
            "inst": float,
            "type_hint": float,
            "description": "args: rast - Returns the upper left Y coordinate of raster in projected spatial ref.",
            "doc_url": "https://postgis.net/docs/ST_UpperLeftY.html",
        }
    },
    "ST_Value": {
        (Raster, int, int, int, bool): {
            "inst": float,
            "type_hint": float,
            "description": "args: rast, band, x, y, exclude_nodata_value=true - Returns the value of a given band in a given columnx, rowy pixel or at a particular geometric point. Band numbers start at 1 and assumed to be 1 if not specified. If exclude_nodata_value is set to false, then all pixels include nodata pixels are considered to intersect and return value. If exclude_nodata_value is not passed in then reads it from metadata of raster.",
            "doc_url": "https://postgis.net/docs/ST_Value.html",
        },
        (Raster, int, Geometry, bool, str): {
            "inst": float,
            "type_hint": float,
            "description": "args: rast, band, pt, exclude_nodata_value=true, resample='nearest' - Returns the value of a given band in a given columnx, rowy pixel or at a particular geometric point. Band numbers start at 1 and assumed to be 1 if not specified. If exclude_nodata_value is set to false, then all pixels include nodata pixels are considered to intersect and return value. If exclude_nodata_value is not passed in then reads it from metadata of raster.",
            "doc_url": "https://postgis.net/docs/ST_Value.html",
        },
        (Raster, int, int, bool): {
            "inst": float,
            "type_hint": float,
            "description": "args: rast, x, y, exclude_nodata_value=true - Returns the value of a given band in a given columnx, rowy pixel or at a particular geometric point. Band numbers start at 1 and assumed to be 1 if not specified. If exclude_nodata_value is set to false, then all pixels include nodata pixels are considered to intersect and return value. If exclude_nodata_value is not passed in then reads it from metadata of raster.",
            "doc_url": "https://postgis.net/docs/ST_Value.html",
        },
        (Raster, Geometry, bool): {
            "inst": float,
            "type_hint": float,
            "description": "args: rast, pt, exclude_nodata_value=true - Returns the value of a given band in a given columnx, rowy pixel or at a particular geometric point. Band numbers start at 1 and assumed to be 1 if not specified. If exclude_nodata_value is set to false, then all pixels include nodata pixels are considered to intersect and return value. If exclude_nodata_value is not passed in then reads it from metadata of raster.",
            "doc_url": "https://postgis.net/docs/ST_Value.html",
        },
    },
    "ST_ValueCount": {
        (Raster, int, bool, List[float], float, float, int): {
            "inst": object,
            "type_hint": List[Any],
            "description": "args: rast, nband=1, exclude_nodata_value=true, searchvalues=NULL, roundto=0, OUT value, OUT count - Returns a set of records containing a pixel band value and count of the number of pixels in a given band of a raster (or a raster coverage) that have a given set of values. If no band is specified defaults to band 1. By default nodata value pixels are not counted. and all other values in the pixel are output and pixel band values are rounded to the nearest integer.",
            "doc_url": "https://postgis.net/docs/ST_ValueCount.html",
        },
        (Raster, int, List[float], float, float, int): {
            "inst": object,
            "type_hint": List[Any],
            "description": "args: rast, nband, searchvalues, roundto=0, OUT value, OUT count - Returns a set of records containing a pixel band value and count of the number of pixels in a given band of a raster (or a raster coverage) that have a given set of values. If no band is specified defaults to band 1. By default nodata value pixels are not counted. and all other values in the pixel are output and pixel band values are rounded to the nearest integer.",
            "doc_url": "https://postgis.net/docs/ST_ValueCount.html",
        },
        (Raster, List[float], float, float, int): {
            "inst": object,
            "type_hint": List[Any],
            "description": "args: rast, searchvalues, roundto=0, OUT value, OUT count - Returns a set of records containing a pixel band value and count of the number of pixels in a given band of a raster (or a raster coverage) that have a given set of values. If no band is specified defaults to band 1. By default nodata value pixels are not counted. and all other values in the pixel are output and pixel band values are rounded to the nearest integer.",
            "doc_url": "https://postgis.net/docs/ST_ValueCount.html",
        },
        (Raster, int, bool, float, float): {
            "inst": int,
            "type_hint": int,
            "description": "args: rast, nband, exclude_nodata_value, searchvalue, roundto=0 - Returns a set of records containing a pixel band value and count of the number of pixels in a given band of a raster (or a raster coverage) that have a given set of values. If no band is specified defaults to band 1. By default nodata value pixels are not counted. and all other values in the pixel are output and pixel band values are rounded to the nearest integer.",
            "doc_url": "https://postgis.net/docs/ST_ValueCount.html",
        },
        (Raster, int, float, float): {
            "inst": int,
            "type_hint": int,
            "description": "args: rast, nband, searchvalue, roundto=0 - Returns a set of records containing a pixel band value and count of the number of pixels in a given band of a raster (or a raster coverage) that have a given set of values. If no band is specified defaults to band 1. By default nodata value pixels are not counted. and all other values in the pixel are output and pixel band values are rounded to the nearest integer.",
            "doc_url": "https://postgis.net/docs/ST_ValueCount.html",
        },
        (Raster, float, float): {
            "inst": int,
            "type_hint": int,
            "description": "args: rast, searchvalue, roundto=0 - Returns a set of records containing a pixel band value and count of the number of pixels in a given band of a raster (or a raster coverage) that have a given set of values. If no band is specified defaults to band 1. By default nodata value pixels are not counted. and all other values in the pixel are output and pixel band values are rounded to the nearest integer.",
            "doc_url": "https://postgis.net/docs/ST_ValueCount.html",
        },
        (str, str, int, bool, List[float], float, float, int): {
            "inst": object,
            "type_hint": List[Any],
            "description": "args: rastertable, rastercolumn, nband=1, exclude_nodata_value=true, searchvalues=NULL, roundto=0, OUT value, OUT count - Returns a set of records containing a pixel band value and count of the number of pixels in a given band of a raster (or a raster coverage) that have a given set of values. If no band is specified defaults to band 1. By default nodata value pixels are not counted. and all other values in the pixel are output and pixel band values are rounded to the nearest integer.",
            "doc_url": "https://postgis.net/docs/ST_ValueCount.html",
        },
        (str, str, int, List[float], float, float, int): {
            "inst": object,
            "type_hint": List[Any],
            "description": "args: rastertable, rastercolumn, nband, searchvalues, roundto=0, OUT value, OUT count - Returns a set of records containing a pixel band value and count of the number of pixels in a given band of a raster (or a raster coverage) that have a given set of values. If no band is specified defaults to band 1. By default nodata value pixels are not counted. and all other values in the pixel are output and pixel band values are rounded to the nearest integer.",
            "doc_url": "https://postgis.net/docs/ST_ValueCount.html",
        },
        (str, str, List[float], float, float, int): {
            "inst": object,
            "type_hint": List[Any],
            "description": "args: rastertable, rastercolumn, searchvalues, roundto=0, OUT value, OUT count - Returns a set of records containing a pixel band value and count of the number of pixels in a given band of a raster (or a raster coverage) that have a given set of values. If no band is specified defaults to band 1. By default nodata value pixels are not counted. and all other values in the pixel are output and pixel band values are rounded to the nearest integer.",
            "doc_url": "https://postgis.net/docs/ST_ValueCount.html",
        },
        (str, str, int, bool, float, float): {
            "inst": int,
            "type_hint": int,
            "description": "args: rastertable, rastercolumn, nband, exclude_nodata_value, searchvalue, roundto=0 - Returns a set of records containing a pixel band value and count of the number of pixels in a given band of a raster (or a raster coverage) that have a given set of values. If no band is specified defaults to band 1. By default nodata value pixels are not counted. and all other values in the pixel are output and pixel band values are rounded to the nearest integer.",
            "doc_url": "https://postgis.net/docs/ST_ValueCount.html",
        },
        (str, str, int, float, float): {
            "inst": int,
            "type_hint": int,
            "description": "args: rastertable, rastercolumn, nband, searchvalue, roundto=0 - Returns a set of records containing a pixel band value and count of the number of pixels in a given band of a raster (or a raster coverage) that have a given set of values. If no band is specified defaults to band 1. By default nodata value pixels are not counted. and all other values in the pixel are output and pixel band values are rounded to the nearest integer.",
            "doc_url": "https://postgis.net/docs/ST_ValueCount.html",
        },
        (str, str, float, float): {
            "inst": int,
            "type_hint": int,
            "description": "args: rastertable, rastercolumn, searchvalue, roundto=0 - Returns a set of records containing a pixel band value and count of the number of pixels in a given band of a raster (or a raster coverage) that have a given set of values. If no band is specified defaults to band 1. By default nodata value pixels are not counted. and all other values in the pixel are output and pixel band values are rounded to the nearest integer.",
            "doc_url": "https://postgis.net/docs/ST_ValueCount.html",
        },
    },
    "ST_VoronoiLines": {
        (Geometry, float, Geometry): {
            "inst": Geometry,
            "type_hint": Geometry,
            "description": "args: geom, tolerance = 0.0, extend_to = NULL - Returns the boundaries of the Voronoi diagram of the vertices of a geometry.",
            "doc_url": "https://postgis.net/docs/ST_VoronoiLines.html",
        }
    },
    "ST_VoronoiPolygons": {
        (Geometry, float, Geometry): {
            "inst": Geometry,
            "type_hint": Geometry,
            "description": "args: geom, tolerance = 0.0, extend_to = NULL - Returns the cells of the Voronoi diagram of the vertices of a geometry.",
            "doc_url": "https://postgis.net/docs/ST_VoronoiPolygons.html",
        }
    },
    "ST_WKBToSQL": {
        (bytes,): {
            "inst": Geometry,
            "type_hint": Geometry,
            "description": "None",
            "doc_url": "https://postgis.net/docs/ST_WKBToSQL.html",
        }
    },
    "ST_WKTToSQL": {
        (str,): {
            "inst": Geometry,
            "type_hint": Geometry,
            "description": "None",
            "doc_url": "https://postgis.net/docs/ST_WKTToSQL.html",
        }
    },
    "ST_Width": {
        (Raster,): {
            "inst": int,
            "type_hint": int,
            "description": "args: rast - Returns the width of the raster in pixels.",
            "doc_url": "https://postgis.net/docs/ST_Width.html",
        }
    },
    "ST_Within": {
        (Geometry, Geometry): {
            "inst": bool,
            "type_hint": bool,
            "description": "None",
            "doc_url": "https://postgis.net/docs/ST_Within.html",
        },
        (Raster, int, Raster, int): {
            "inst": bool,
            "type_hint": bool,
            "description": "args: rastA, nbandA, rastB, nbandB - Return true if no points of raster rastA lie in the exterior of raster rastB and at least one point of the interior of rastA lies in the interior of rastB.",
            "doc_url": "https://postgis.net/docs/ST_Within.html",
        },
        (Raster, Raster): {
            "inst": bool,
            "type_hint": bool,
            "description": "args: rastA, rastB - Return true if no points of raster rastA lie in the exterior of raster rastB and at least one point of the interior of rastA lies in the interior of rastB.",
            "doc_url": "https://postgis.net/docs/ST_Within.html",
        },
    },
    "ST_WorldToRasterCoord": {
        (Raster, float, float, int, int): {
            "inst": object,
            "type_hint": Any,
            "description": "args: rast, longitude, latitude - Returns the upper left corner as column and row given geometric X and Y (longitude and latitude) or a point geometry expressed in the spatial reference coordinate system of the raster.",
            "doc_url": "https://postgis.net/docs/ST_WorldToRasterCoord.html",
        },
        (Raster, Geometry, int, int): {
            "inst": object,
            "type_hint": Any,
            "description": "args: rast, pt - Returns the upper left corner as column and row given geometric X and Y (longitude and latitude) or a point geometry expressed in the spatial reference coordinate system of the raster.",
            "doc_url": "https://postgis.net/docs/ST_WorldToRasterCoord.html",
        },
    },
    "ST_WorldToRasterCoordX": {
        (Raster, float, float): {
            "inst": int,
            "type_hint": int,
            "description": "args: rast, xw, yw - Returns the column in the raster of the point geometry (pt) or a X and Y world coordinate (xw, yw) represented in world spatial reference system of raster.",
            "doc_url": "https://postgis.net/docs/ST_WorldToRasterCoordX.html",
        },
        (Raster, float): {
            "inst": int,
            "type_hint": int,
            "description": "args: rast, xw - Returns the column in the raster of the point geometry (pt) or a X and Y world coordinate (xw, yw) represented in world spatial reference system of raster.",
            "doc_url": "https://postgis.net/docs/ST_WorldToRasterCoordX.html",
        },
        (Raster, Geometry): {
            "inst": int,
            "type_hint": int,
            "description": "args: rast, pt - Returns the column in the raster of the point geometry (pt) or a X and Y world coordinate (xw, yw) represented in world spatial reference system of raster.",
            "doc_url": "https://postgis.net/docs/ST_WorldToRasterCoordX.html",
        },
    },
    "ST_WorldToRasterCoordY": {
        (Raster, float, float): {
            "inst": int,
            "type_hint": int,
            "description": "args: rast, xw, yw - Returns the row in the raster of the point geometry (pt) or a X and Y world coordinate (xw, yw) represented in world spatial reference system of raster.",
            "doc_url": "https://postgis.net/docs/ST_WorldToRasterCoordY.html",
        },
        (Raster, float): {
            "inst": int,
            "type_hint": int,
            "description": "args: rast, xw - Returns the row in the raster of the point geometry (pt) or a X and Y world coordinate (xw, yw) represented in world spatial reference system of raster.",
            "doc_url": "https://postgis.net/docs/ST_WorldToRasterCoordY.html",
        },
        (Raster, Geometry): {
            "inst": int,
            "type_hint": int,
            "description": "args: rast, pt - Returns the row in the raster of the point geometry (pt) or a X and Y world coordinate (xw, yw) represented in world spatial reference system of raster.",
            "doc_url": "https://postgis.net/docs/ST_WorldToRasterCoordY.html",
        },
    },
    "ST_WrapX": {
        (Geometry, float, float): {
            "inst": Geometry,
            "type_hint": Geometry,
            "description": "args: geom, wrap, move - Wrap a geometry around an X value.",
            "doc_url": "https://postgis.net/docs/ST_WrapX.html",
        }
    },
    "ST_X": {
        (Geometry,): {
            "inst": float,
            "type_hint": float,
            "description": "args: a_point - Returns the X coordinate of a Point.",
            "doc_url": "https://postgis.net/docs/ST_X.html",
        }
    },
    "ST_XMax": {
        (Geometry,): {
            "inst": float,
            "type_hint": float,
            "description": "args: aGeomorBox2DorBox3D - Returns the X maxima of a 2D or 3D bounding box or a geometry.",
            "doc_url": "https://postgis.net/docs/ST_XMax.html",
        }
    },
    "ST_XMin": {
        (Geometry,): {
            "inst": float,
            "type_hint": float,
            "description": "args: aGeomorBox2DorBox3D - Returns the X minima of a 2D or 3D bounding box or a geometry.",
            "doc_url": "https://postgis.net/docs/ST_XMin.html",
        }
    },
    "ST_Y": {
        (Geometry,): {
            "inst": float,
            "type_hint": float,
            "description": "args: a_point - Returns the Y coordinate of a Point.",
            "doc_url": "https://postgis.net/docs/ST_Y.html",
        }
    },
    "ST_YMax": {
        (Geometry,): {
            "inst": float,
            "type_hint": float,
            "description": "args: aGeomorBox2DorBox3D - Returns the Y maxima of a 2D or 3D bounding box or a geometry.",
            "doc_url": "https://postgis.net/docs/ST_YMax.html",
        }
    },
    "ST_YMin": {
        (Geometry,): {
            "inst": float,
            "type_hint": float,
            "description": "args: aGeomorBox2DorBox3D - Returns the Y minima of a 2D or 3D bounding box or a geometry.",
            "doc_url": "https://postgis.net/docs/ST_YMin.html",
        }
    },
    "ST_Z": {
        (Geometry,): {
            "inst": float,
            "type_hint": float,
            "description": "args: a_point - Returns the Z coordinate of a Point.",
            "doc_url": "https://postgis.net/docs/ST_Z.html",
        }
    },
    "ST_ZMax": {
        (Geometry,): {
            "inst": float,
            "type_hint": float,
            "description": "args: aGeomorBox2DorBox3D - Returns the Z maxima of a 2D or 3D bounding box or a geometry.",
            "doc_url": "https://postgis.net/docs/ST_ZMax.html",
        }
    },
    "ST_ZMin": {
        (Geometry,): {
            "inst": float,
            "type_hint": float,
            "description": "args: aGeomorBox2DorBox3D - Returns the Z minima of a 2D or 3D bounding box or a geometry.",
            "doc_url": "https://postgis.net/docs/ST_ZMin.html",
        }
    },
    "ST_Zmflag": {
        (Geometry,): {
            "inst": int,
            "type_hint": int,
            "description": "args: geomA - Returns a code indicating the ZM coordinate dimension of a geometry.",
            "doc_url": "https://postgis.net/docs/ST_Zmflag.html",
        }
    },
}
