# -*- coding: utf-8 -*-
# flake8: noqa
from geoalchemy2 import types

_FUNCTIONS = [
    ("AddGeometryColumn", None, """Adds a geometry column to an existing table."""),
    ("DropGeometryColumn", None, """Removes a geometry column from a spatial table."""),
    (
        "DropGeometryTable",
        None,
        """Drops a table and all its references in geometry_columns.""",
    ),
    ("Find_SRID", None, """Returns the SRID defined for a geometry column."""),
    (
        "Populate_Geometry_Columns",
        None,
        """Ensures geometry columns are defined with type modifiers or have appropriate spatial constraints.""",
    ),
    (
        "UpdateGeometrySRID",
        None,
        """Updates the SRID of all features in a geometry column, and the table metadata.""",
    ),
    (
        "ST_Collect",
        types.Geometry,
        """Creates a GeometryCollection or Multi* geometry from a set of geometries.""",
    ),
    (
        "ST_LineFromMultiPoint",
        types.Geometry,
        """Creates a LineString from a MultiPoint geometry.""",
    ),
    (
        "ST_MakeEnvelope",
        types.Geometry,
        """Creates a rectangular Polygon from minimum and maximum coordinates.""",
    ),
    (
        "ST_MakeLine",
        types.Geometry,
        """Creates a Linestring from Point, MultiPoint, or LineString geometries.""",
    ),
    ("ST_MakePoint", types.Geometry, """Creates a 2D, 3DZ or 4D Point."""),
    ("ST_MakePointM", types.Geometry, """Creates a Point from X, Y and M values."""),
    (
        "ST_MakePolygon",
        types.Geometry,
        """Creates a Polygon from a shell and optional list of holes.""",
    ),
    (
        "ST_Point",
        types.Geometry,
        """Creates a Point with the given coordinate values. Alias for ST_MakePoint.""",
    ),
    (
        "ST_Polygon",
        types.Geometry,
        """[geometry] Creates a Polygon from a LineString with a specified SRID.\nOR\n[raster] Returns a multipolygon geometry formed by the union of pixels that have a pixel value that is not no data value. If no band number is specified, band num defaults to 1.""",
    ),
    (
        "ST_TileEnvelope",
        types.Geometry,
        """Creates a rectangular Polygon in Web Mercator (SRID:3857) using the XYZ tile system.""",
    ),
    ("GeometryType", None, """Returns the type of a geometry as text."""),
    ("ST_Boundary", types.Geometry, """Returns the boundary of a geometry."""),
    ("ST_CoordDim", None, """Return the coordinate dimension of a geometry."""),
    ("ST_Dimension", None, """Returns the topological dimension of a geometry."""),
    (
        "ST_Dump",
        types.GeometryDump,
        """Returns a set of geometry_dump rows for the components of a geometry.""",
    ),
    (
        "ST_DumpPoints",
        types.GeometryDump,
        """Returns a set of geometry_dump rows for the points in a geometry.""",
    ),
    (
        "ST_DumpRings",
        types.GeometryDump,
        """Returns a set of geometry_dump rows for the exterior and interior rings of a Polygon.""",
    ),
    (
        "ST_EndPoint",
        types.Geometry,
        """Returns the last point of a LineString or CircularLineString.""",
    ),
    (
        "ST_Envelope",
        types.Geometry,
        """[geometry] Returns a geometry representing the bounding box of a geometry.\nOR\n[raster] Returns the polygon representation of the extent of the raster.""",
    ),
    (
        "ST_BoundingDiagonal",
        types.Geometry,
        """Returns the diagonal of a geometry's bounding box.""",
    ),
    (
        "ST_ExteriorRing",
        types.Geometry,
        """Returns a LineString representing the exterior ring of a Polygon.""",
    ),
    (
        "ST_GeometryN",
        types.Geometry,
        """Return the Nth geometry element of a geometry collection.""",
    ),
    ("ST_GeometryType", None, """Returns the SQL-MM type of a geometry as text."""),
    ("ST_HasArc", None, """Tests if a geometry contains a circular arc"""),
    (
        "ST_InteriorRingN",
        types.Geometry,
        """Returns the Nth interior ring (hole) of a Polygon.""",
    ),
    (
        "ST_IsPolygonCCW",
        None,
        """Tests if Polygons have exterior rings oriented counter-clockwise and interior rings oriented clockwise.""",
    ),
    (
        "ST_IsPolygonCW",
        None,
        """Tests if Polygons have exterior rings oriented clockwise and interior rings oriented counter-clockwise.""",
    ),
    (
        "ST_IsClosed",
        None,
        """Tests if a LineStrings's start and end points are coincident. For a PolyhedralSurface tests if it is closed (volumetric).""",
    ),
    ("ST_IsCollection", None, """Tests if a geometry is a geometry collection type."""),
    (
        "ST_IsEmpty",
        None,
        """[geometry] Tests if a geometry is empty.\nOR\n[raster] Returns true if the raster is empty (width = 0 and height = 0). Otherwise, returns false.""",
    ),
    ("ST_IsRing", None, """Tests if a LineString is closed and simple."""),
    (
        "ST_IsSimple",
        None,
        """Tests if a geometry has no points of self-intersection or self-tangency.""",
    ),
    ("ST_M", None, """Returns the M coordinate of a Point."""),
    (
        "ST_MemSize",
        None,
        """[geometry] Returns the amount of memory space a geometry takes.\nOR\n[raster] Returns the amount of space (in bytes) the raster takes.""",
    ),
    ("ST_NDims", None, """Returns the coordinate dimension of a geometry."""),
    ("ST_NPoints", None, """Returns the number of points (vertices) in a geometry."""),
    ("ST_NRings", None, """Returns the number of rings in a polygonal geometry."""),
    (
        "ST_NumGeometries",
        None,
        """Returns the number of elements in a geometry collection.""",
    ),
    (
        "ST_NumInteriorRings",
        None,
        """Returns the number of interior rings (holes) of a Polygon.""",
    ),
    (
        "ST_NumInteriorRing",
        None,
        """Returns the number of interior rings (holes) of a Polygon. Aias for ST_NumInteriorRings""",
    ),
    (
        "ST_NumPatches",
        None,
        """Return the number of faces on a Polyhedral Surface. Will return null for non-polyhedral geometries.""",
    ),
    (
        "ST_NumPoints",
        None,
        """Returns the number of points in a LineString or CircularString.""",
    ),
    (
        "ST_PatchN",
        types.Geometry,
        """Returns the Nth geometry (face) of a PolyhedralSurface.""",
    ),
    (
        "ST_PointN",
        types.Geometry,
        """Returns the Nth point in the first LineString or circular LineString in a geometry.""",
    ),
    (
        "ST_Points",
        types.Geometry,
        """Returns a MultiPoint containing all the coordinates of a geometry.""",
    ),
    ("ST_StartPoint", types.Geometry, """Returns the first point of a LineString."""),
    (
        "ST_Summary",
        None,
        """[geometry] Returns a text summary of the contents of a geometry.\nOR\n[raster] Returns a text summary of the contents of the raster.""",
    ),
    ("ST_X", None, """Returns the X coordinate of a Point."""),
    ("ST_Y", None, """Returns the Y coordinate of a Point."""),
    ("ST_Z", None, """Returns the Z coordinate of a Point."""),
    (
        "ST_Zmflag",
        None,
        """Returns a code indicating the ZM coordinate dimension of a geometry.""",
    ),
    ("ST_AddPoint", types.Geometry, """Add a point to a LineString."""),
    (
        "ST_CollectionExtract",
        types.Geometry,
        """Given a (multi)geometry, return a (multi)geometry consisting only of elements of the specified type.""",
    ),
    (
        "ST_CollectionHomogenize",
        types.Geometry,
        """Given a geometry collection, return the \"simplest\" representation of the contents.""",
    ),
    (
        "ST_Force2D",
        types.Geometry,
        """Force the geometries into a \"2-dimensional mode\".""",
    ),
    (
        "ST_Force3D",
        types.Geometry,
        (
            """Force the geometries into XYZ mode. This is an alias for ST_Force3DZ.""",
            "ST_Force_3D",
        ),
    ),
    (
        "ST_Force3DZ",
        types.Geometry,
        ("""Force the geometries into XYZ mode.""", "ST_Force_3DZ"),
    ),
    (
        "ST_Force3DM",
        types.Geometry,
        ("""Force the geometries into XYM mode.""", "ST_Force_3DZ"),
    ),
    (
        "ST_Force4D",
        types.Geometry,
        ("""Force the geometries into XYZM mode.""", "ST_Force_4D"),
    ),
    (
        "ST_ForcePolygonCCW",
        types.Geometry,
        """Orients all exterior rings counter-clockwise and all interior rings clockwise.""",
    ),
    (
        "ST_ForceCollection",
        types.Geometry,
        ("""Convert the geometry into a GEOMETRYCOLLECTION.""", "ST_Force_Collection"),
    ),
    (
        "ST_ForcePolygonCW",
        types.Geometry,
        """Orients all exterior rings clockwise and all interior rings counter-clockwise.""",
    ),
    (
        "ST_ForceSFS",
        types.Geometry,
        """Force the geometries to use SFS 1.1 geometry types only.""",
    ),
    (
        "ST_ForceRHR",
        types.Geometry,
        """Force the orientation of the vertices in a polygon to follow the Right-Hand-Rule.""",
    ),
    (
        "ST_ForceCurve",
        types.Geometry,
        """Upcast a geometry into its curved type, if applicable.""",
    ),
    (
        "ST_LineMerge",
        types.Geometry,
        """Return a (set of) LineString(s) formed by sewing together a MULTILINESTRING.""",
    ),
    ("ST_Multi", types.Geometry, """Return the geometry as a MULTI* geometry."""),
    ("ST_Normalize", types.Geometry, """Return the geometry in its canonical form."""),
    (
        "ST_QuantizeCoordinates",
        types.Geometry,
        """Sets least significant bits of coordinates to zero""",
    ),
    ("ST_RemovePoint", types.Geometry, """Remove point from a linestring."""),
    (
        "ST_Reverse",
        types.Geometry,
        """Return the geometry with vertex order reversed.""",
    ),
    (
        "ST_Segmentize",
        types.Geometry,
        """Return a modified geometry/geography having no segment longer than the given distance.""",
    ),
    (
        "ST_SetPoint",
        types.Geometry,
        """Replace point of a linestring with a given point.""",
    ),
    (
        "ST_SnapToGrid",
        types.Geometry,
        """[geometry] Snap all points of the input geometry to a regular grid.\nOR\n[raster] Resample a raster by snapping it to a grid. New pixel values are computed using the NearestNeighbor (english or american spelling), Bilinear, Cubic, CubicSpline or Lanczos resampling algorithm. Default is NearestNeighbor.""",
    ),
    (
        "ST_Snap",
        types.Geometry,
        """Snap segments and vertices of input geometry to vertices of a reference geometry.""",
    ),
    (
        "ST_SwapOrdinates",
        types.Geometry,
        """Returns a version of the given geometry with given ordinate values swapped.""",
    ),
    ("ST_IsValid", None, """Tests if a geometry is well-formed in 2D."""),
    (
        "ST_IsValidDetail",
        None,
        """Returns a valid_detail row stating if a geometry is valid, and if not a reason why and a location.""",
    ),
    (
        "ST_IsValidReason",
        None,
        """Returns text stating if a geometry is valid, or a reason for invalidity.""",
    ),
    (
        "ST_SetSRID",
        types.Geometry,
        """[geometry] Set the SRID on a geometry to a particular integer value.\nOR\n[raster] Sets the SRID of a raster to a particular integer srid defined in the spatial_ref_sys table.""",
    ),
    (
        "ST_SRID",
        None,
        """[geometry] Returns the spatial reference identifier for the ST_Geometry as defined in spatial_ref_sys table.\nOR\n[raster] Returns the spatial reference identifier of the raster as defined in spatial_ref_sys table.""",
    ),
    (
        "ST_Transform",
        types.Geometry,
        """[geometry] Return a new geometry with its coordinates transformed to a different spatial reference system.\nOR\n[raster] Reprojects a raster in a known spatial reference system to another known spatial reference system using specified resampling algorithm. Options are NearestNeighbor, Bilinear, Cubic, CubicSpline, Lanczos defaulting to NearestNeighbor.""",
    ),
    (
        "ST_BdPolyFromText",
        types.Geometry,
        """Construct a Polygon given an arbitrary collection of closed linestrings as a MultiLineString Well-Known text representation.""",
    ),
    (
        "ST_BdMPolyFromText",
        types.Geometry,
        """Construct a MultiPolygon given an arbitrary collection of closed linestrings as a MultiLineString text representation Well-Known text representation.""",
    ),
    (
        "ST_GeogFromText",
        types.Geography,
        """Return a specified geography value from Well-Known Text representation or extended (WKT).""",
    ),
    (
        "ST_GeographyFromText",
        types.Geography,
        """Return a specified geography value from Well-Known Text representation or extended (WKT).""",
    ),
    (
        "ST_GeomCollFromText",
        types.Geometry,
        """Makes a collection Geometry from collection WKT with the given SRID. If SRID is not given, it defaults to 0.""",
    ),
    (
        "ST_GeomFromEWKT",
        types.Geometry,
        """Return a specified ST_Geometry value from Extended Well-Known Text representation (EWKT).""",
    ),
    (
        "ST_GeometryFromText",
        types.Geometry,
        """Return a specified ST_Geometry value from Well-Known Text representation (WKT). This is an alias name for ST_GeomFromText""",
    ),
    (
        "ST_GeomFromText",
        types.Geometry,
        """Return a specified ST_Geometry value from Well-Known Text representation (WKT).""",
    ),
    (
        "ST_LineFromText",
        types.Geometry,
        """Makes a Geometry from WKT representation with the given SRID. If SRID is not given, it defaults to 0.""",
    ),
    (
        "ST_MLineFromText",
        types.Geometry,
        """Return a specified ST_MultiLineString value from WKT representation.""",
    ),
    (
        "ST_MPointFromText",
        types.Geometry,
        """Makes a Geometry from WKT with the given SRID. If SRID is not given, it defaults to 0.""",
    ),
    (
        "ST_MPolyFromText",
        types.Geometry,
        """Makes a MultiPolygon Geometry from WKT with the given SRID. If SRID is not given, it defaults to 0.""",
    ),
    (
        "ST_PointFromText",
        types.Geometry,
        """Makes a point Geometry from WKT with the given SRID. If SRID is not given, it defaults to unknown.""",
    ),
    (
        "ST_PolygonFromText",
        types.Geometry,
        """Makes a Geometry from WKT with the given SRID. If SRID is not given, it defaults to 0.""",
    ),
    (
        "ST_WKTToSQL",
        types.Geometry,
        """Return a specified ST_Geometry value from Well-Known Text representation (WKT). This is an alias name for ST_GeomFromText""",
    ),
    (
        "ST_GeogFromWKB",
        types.Geography,
        """Creates a geography instance from a Well-Known Binary geometry representation (WKB) or extended Well Known Binary (EWKB).""",
    ),
    (
        "ST_GeomFromEWKB",
        types.Geometry,
        """Return a specified ST_Geometry value from Extended Well-Known Binary representation (EWKB).""",
    ),
    (
        "ST_GeomFromWKB",
        types.Geometry,
        """Creates a geometry instance from a Well-Known Binary geometry representation (WKB) and optional SRID.""",
    ),
    (
        "ST_LineFromWKB",
        types.Geometry,
        """Makes a LINESTRING from WKB with the given SRID""",
    ),
    (
        "ST_LinestringFromWKB",
        types.Geometry,
        """Makes a geometry from WKB with the given SRID.""",
    ),
    (
        "ST_PointFromWKB",
        types.Geometry,
        """Makes a geometry from WKB with the given SRID""",
    ),
    (
        "ST_WKBToSQL",
        types.Geometry,
        """Return a specified ST_Geometry value from Well-Known Binary representation (WKB). This is an alias name for ST_GeomFromWKB that takes no srid""",
    ),
    (
        "ST_Box2dFromGeoHash",
        None,  # return an unsupported Box2d object
        """Return a BOX2D from a GeoHash string.""",
    ),
    (
        "ST_GeomFromGeoHash",
        types.Geometry,
        """Return a geometry from a GeoHash string.""",
    ),
    (
        "ST_GeomFromGML",
        types.Geometry,
        """Takes as input GML representation of geometry and outputs a PostGIS geometry object""",
    ),
    (
        "ST_GeomFromGeoJSON",
        types.Geometry,
        """Takes as input a geojson representation of a geometry and outputs a PostGIS geometry object""",
    ),
    (
        "ST_GeomFromKML",
        types.Geometry,
        """Takes as input KML representation of geometry and outputs a PostGIS geometry object""",
    ),
    (
        "ST_GeomFromTWKB",
        types.Geometry,
        """Creates a geometry instance from a TWKB (\"Tiny Well-Known Binary\") geometry representation.""",
    ),
    (
        "ST_GMLToSQL",
        types.Geometry,
        """Return a specified ST_Geometry value from GML representation. This is an alias name for ST_GeomFromGML""",
    ),
    (
        "ST_LineFromEncodedPolyline",
        types.Geometry,
        """Creates a LineString from an Encoded Polyline.""",
    ),
    (
        "ST_PointFromGeoHash",
        types.Geometry,
        """Return a point from a GeoHash string.""",
    ),
    (
        "ST_AsEWKT",
        None,
        """Return the Well-Known Text (WKT) representation of the geometry with SRID meta data.""",
    ),
    (
        "ST_AsText",
        None,
        """Return the Well-Known Text (WKT) representation of the geometry/geography without SRID metadata.""",
    ),
    (
        "ST_AsBinary",
        None,
        """[gometry] Return the Well-Known Binary (WKB) representation of the geometry/geography without SRID meta data.\nOR\n[raster] Return the Well-Known Binary (WKB) representation of the raster.""",
    ),
    (
        "ST_AsEWKB",
        None,
        """Return the Well-Known Binary (WKB) representation of the geometry with SRID meta data.""",
    ),
    (
        "ST_AsHEXEWKB",
        None,
        """Returns a Geometry in HEXEWKB format (as text) using either little-endian (NDR) or big-endian (XDR) encoding.""",
    ),
    (
        "ST_AsEncodedPolyline",
        None,
        """Returns an Encoded Polyline from a LineString geometry.""",
    ),
    ("ST_AsGeobuf", None, """Return a Geobuf representation of a set of rows."""),
    ("ST_AsGML", None, """Return the geometry as a GML version 2 or 3 element."""),
    (
        "ST_AsKML",
        None,
        """Return the geometry as a KML element. Several variants. Default version=2, default maxdecimaldigits=15""",
    ),
    (
        "ST_AsLatLonText",
        None,
        """Return the Degrees, Minutes, Seconds representation of the given point.""",
    ),
    (
        "ST_AsMVTGeom",
        types.Geometry,
        """Transform a geometry into the coordinate space of a Mapbox Vector Tile.""",
    ),
    (
        "ST_AsMVT",
        None,
        """Aggregate function returning a Mapbox Vector Tile representation of a set of rows.""",
    ),
    ("ST_AsSVG", None, """Returns SVG path data for a geometry."""),
    (
        "ST_AsTWKB",
        None,
        '''Returns the geometry as TWKB, aka \"Tiny Well-Known Binary\"''',
    ),
    (
        "ST_AsX3D",
        None,
        """Returns a Geometry in X3D xml node element format: ISO-IEC-19776-1.2-X3DEncodings-XML""",
    ),
    ("ST_GeoHash", None, """Return a GeoHash representation of the geometry."""),
    (
        "ST_3DIntersects",
        None,
        """Returns TRUE if the Geometries \"spatially intersect\" in 3D - only for points, linestrings, polygons, polyhedral surface (area).""",
    ),
    (
        "ST_Contains",
        None,
        """[geometry] Returns true if and only if no points of B lie in the exterior of A, and at least one point of the interior of B lies in the interior of A.\nOR\n[raster] Return true if no points of raster rastB lie in the exterior of raster rastA and at least one point of the interior of rastB lies in the interior of rastA.""",
    ),
    (
        "ST_ContainsProperly",
        None,
        """[geometry] Returns true if B intersects the interior of A but not the boundary (or exterior). A does not contain properly itself, but does contain itself.\nOR\n[raster] Return true if rastB intersects the interior of rastA but not the boundary or exterior of rastA.""",
    ),
    (
        "ST_Covers",
        None,
        """[geometry] Returns 1 (TRUE) if no point in Geometry B is outside Geometry A\nOR\n[raster] Return true if no points of raster rastB lie outside raster rastA.""",
    ),
    (
        "ST_CoveredBy",
        None,
        """[geometry] Returns 1 (TRUE) if no point in Geometry/Geography A is outside Geometry/Geography B\nOR\n[raster] Return true if no points of raster rastA lie outside raster rastB.""",
    ),
    (
        "ST_Crosses",
        None,
        """Returns TRUE if the supplied geometries have some, but not all, interior points in common.""",
    ),
    (
        "ST_LineCrossingDirection",
        None,
        """Given 2 linestrings, returns a number between -3 and 3 denoting what kind of crossing behavior. 0 is no crossing.""",
    ),
    (
        "ST_Disjoint",
        None,
        """[geometry] Returns TRUE if the Geometries do not \"spatially intersect\" - if they do not share any space together.\nOR\n[raster] Return true if raster rastA does not spatially intersect rastB.""",
    ),
    (
        "ST_Equals",
        None,
        """Returns true if the given geometries represent the same geometry. Directionality is ignored.""",
    ),
    (
        "ST_Intersects",
        None,
        """[geometry] Returns TRUE if the Geometries/Geography \"spatially intersect in 2D\" - (share any portion of space) and FALSE if they don't (they are Disjoint). For geography tolerance is 0.00001 meters (so any points that close are considered to intersect)\nOR\n[raster] Return true if raster rastA spatially intersects raster rastB.""",
    ),
    (
        "ST_OrderingEquals",
        None,
        """Returns true if the given geometries represent the same geometry and points are in the same directional order.""",
    ),
    (
        "ST_Overlaps",
        None,
        """[geometry] Returns TRUE if the Geometries share space, are of the same dimension, but are not completely contained by each other.\nOR\n[raster] Return true if raster rastA and rastB intersect but one does not completely contain the other.""",
    ),
    (
        "ST_PointInsideCircle",
        None,
        """Is the point geometry inside the circle defined by center_x, center_y, radius""",
    ),
    (
        "ST_Relate",
        None,
        """Returns true if this Geometry is spatially related to anotherGeometry, by testing for intersections between the Interior, Boundary and Exterior of the two geometries as specified by the values in the intersectionMatrixPattern. If no intersectionMatrixPattern is passed in, then returns the maximum intersectionMatrixPattern that relates the 2 geometries.""",
    ),
    (
        "ST_RelateMatch",
        None,
        """Returns true if intersectionMattrixPattern1 implies intersectionMatrixPattern2""",
    ),
    (
        "ST_Touches",
        None,
        """[geometry] Returns TRUE if the geometries have at least one point in common, but their interiors do not intersect.\nOR\n[raster] Return true if raster rastA and rastB have at least one point in common but their interiors do not intersect.""",
    ),
    (
        "ST_Within",
        None,
        """[geometry] Returns true if the geometry A is completely inside geometry B\nOR\n[raster] Return true if no points of raster rastA lie in the exterior of raster rastB and at least one point of the interior of rastA lies in the interior of rastB.""",
    ),
    (
        "ST_3DDWithin",
        None,
        """For 3d (z) geometry type Returns true if two geometries 3d distance is within number of units.""",
    ),
    (
        "ST_3DDFullyWithin",
        None,
        """Returns true if all of the 3D geometries are within the specified distance of one another.""",
    ),
    (
        "ST_DFullyWithin",
        None,
        """[geometry] Returns true if all of the geometries are within the specified distance of one another\nOR\n[raster] Return true if rasters rastA and rastB are fully within the specified distance of each other.""",
    ),
    (
        "ST_DWithin",
        None,
        """[geometry] Returns true if the geometries are within the specified distance of one another. For geometry units are in those of spatial reference and for geography units are in meters and measurement is defaulted to use_spheroid=true (measure around spheroid), for faster check, use_spheroid=false to measure along sphere.\nOR\n[raster] Return true if rasters rastA and rastB are within the specified distance of each other.""",
    ),
    ("ST_Area", None, """Returns the area of a polygonal geometry."""),
    (
        "ST_Azimuth",
        None,
        """Returns the north-based azimuth as the angle in radians measured clockwise from the vertical on pointA to pointB.""",
    ),
    (
        "ST_Angle",
        None,
        """Returns the angle between 3 points, or between 2 vectors (4 points or 2 lines).""",
    ),
    (
        "ST_ClosestPoint",
        types.Geometry,
        """Returns the 2D point on g1 that is closest to g2. This is the first point of the shortest line.""",
    ),
    (
        "ST_3DClosestPoint",
        types.Geometry,
        """Returns the 3D point on g1 that is closest to g2. This is the first point of the 3D shortest line.""",
    ),
    (
        "ST_Distance",
        None,
        """Returns the distance between two geometry or geography values.""",
    ),
    (
        "ST_3DDistance",
        None,
        """Returns the 3D cartesian minimum distance (based on spatial ref) between two geometries in projected units.""",
    ),
    (
        "ST_DistanceSphere",
        None,
        """Returns minimum distance in meters between two lon/lat geometries using a spherical earth model.""",
    ),
    (
        "ST_DistanceSpheroid",
        None,
        """Returns the minimum distance between two lon/lat geometries using a spheroidal earth model.""",
    ),
    (
        "ST_FrechetDistance",
        None,
        """Returns the Fréchet distance between two geometries.""",
    ),
    (
        "ST_HausdorffDistance",
        None,
        """Returns the Hausdorff distance between two geometries.""",
    ),
    ("ST_Length", None, """Returns the 2D length of a linear geometry."""),
    (
        "ST_Length2D",
        None,
        """Returns the 2D length of a linear geometry. Alias for ST_Length""",
    ),
    ("ST_3DLength", None, """Returns the 3D length of a linear geometry."""),
    (
        "ST_LengthSpheroid",
        None,
        """Returns the 2D or 3D length/perimeter of a lon/lat geometry on a spheroid.""",
    ),
    (
        "ST_LongestLine",
        types.Geometry,
        """Returns the 2D longest line between two geometries.""",
    ),
    (
        "ST_3DLongestLine",
        types.Geometry,
        """Returns the 3D longest line between two geometries""",
    ),
    (
        "ST_MaxDistance",
        None,
        """Returns the 2D largest distance between two geometries in projected units.""",
    ),
    (
        "ST_3DMaxDistance",
        None,
        """Returns the 3D cartesian maximum distance (based on spatial ref) between two geometries in projected units.""",
    ),
    (
        "ST_MinimumClearance",
        None,
        """Returns the minimum clearance of a geometry, a measure of a geometry's robustness.""",
    ),
    (
        "ST_MinimumClearanceLine",
        types.Geometry,
        """Returns the two-point LineString spanning a geometry's minimum clearance.""",
    ),
    (
        "ST_Perimeter",
        None,
        """Returns the length of the boundary of a polygonal geometry or geography.""",
    ),
    (
        "ST_Perimeter2D",
        None,
        """Returns the 2D perimeter of a polygonal geometry. Alias for ST_Perimeter.""",
    ),
    ("ST_3DPerimeter", None, """Returns the 3D perimeter of a polygonal geometry."""),
    (
        "ST_Project",
        types.Geography,
        """Returns a point projected from a start point by a distance and bearing (azimuth).""",
    ),
    (
        "ST_ShortestLine",
        types.Geometry,
        """Returns the 2D shortest line between two geometries""",
    ),
    (
        "ST_3DShortestLine",
        types.Geometry,
        """Returns the 3D shortest line between two geometries""",
    ),
    (
        "ST_Buffer",
        types.Geometry,
        """(T) Returns a geometry covering all points within a given distance from the input geometry.""",
    ),
    (
        "ST_BuildArea",
        types.Geometry,
        """Creates an areal geometry formed by the constituent linework of given geometry""",
    ),
    ("ST_Centroid", types.Geometry, """Returns the geometric center of a geometry."""),
    (
        "ST_ClipByBox2D",
        types.Geometry,
        """Returns the portion of a geometry falling within a rectangle.""",
    ),
    (
        "ST_ConcaveHull",
        types.Geometry,
        """The concave hull of a geometry represents a possibly concave geometry that encloses all geometries within the set. You can think of it as shrink wrapping.""",
    ),
    (
        "ST_ConvexHull",
        types.Geometry,
        """[geometry] Computes the convex hull of a geometry.\nOR\n[raster] Return the convex hull geometry of the raster including pixel values equal to BandNoDataValue. For regular shaped and non-skewed rasters, this gives the same result as ST_Envelope so only useful for irregularly shaped or skewed rasters.""",
    ),
    (
        "ST_CurveToLine",
        types.Geometry,
        """Converts a CIRCULARSTRING/CURVEPOLYGON/MULTISURFACE to a LINESTRING/POLYGON/MULTIPOLYGON""",
    ),
    (
        "ST_DelaunayTriangles",
        types.Geometry,
        """Return a Delaunay triangulation around the given input points.""",
    ),
    (
        "ST_Difference",
        types.Geometry,
        """Returns a geometry that represents that part of geometry A that does not intersect with geometry B.""",
    ),
    (
        "ST_FlipCoordinates",
        types.Geometry,
        """Returns a version of the given geometry with X and Y axis flipped. Useful for people who have built latitude/longitude features and need to fix them.""",
    ),
    (
        "ST_GeneratePoints",
        types.Geometry,
        """Converts a polygon or multi-polygon into a multi-point composed of randomly location points within the original areas.""",
    ),
    (
        "ST_GeometricMedian",
        types.Geometry,
        """Returns the geometric median of a MultiPoint.""",
    ),
    (
        "ST_Intersection",
        types.Geometry,
        """[geometry] (T) Returns a geometry that represents the shared portion of geomA and geomB.\nOR\n[raster] Returns a raster or a set of geometry-pixelvalue pairs representing the shared portion of two rasters or the geometrical intersection of a vectorization of the raster and a geometry.""",
    ),
    (
        "ST_LineToCurve",
        types.Geometry,
        """Converts a LINESTRING/POLYGON to a CIRCULARSTRING, CURVEPOLYGON""",
    ),
    (
        "ST_MakeValid",
        types.Geometry,
        """Attempts to make an invalid geometry valid without losing vertices.""",
    ),
    (
        "ST_MemUnion",
        types.Geometry,
        """Same as ST_Union, only memory-friendly (uses less memory and more processor time).""",
    ),
    (
        "ST_MinimumBoundingCircle",
        types.Geometry,
        """Returns the smallest circle polygon that can fully contain a geometry. Default uses 48 segments per quarter circle.""",
    ),
    (
        "ST_MinimumBoundingRadius",
        None,
        """Returns the center point and radius of the smallest circle that can fully contain a geometry.""",
    ),
    (
        "ST_OrientedEnvelope",
        types.Geometry,
        """Returns a minimum rotated rectangle enclosing a geometry.""",
    ),
    (
        "ST_Polygonize",
        types.Geometry,
        """Aggregate. Creates a GeometryCollection containing possible polygons formed from the constituent linework of a set of geometries.""",
    ),
    ("ST_Node", types.Geometry, """Node a set of linestrings."""),
    (
        "ST_OffsetCurve",
        types.Geometry,
        """Return an offset line at a given distance and side from an input line. Useful for computing parallel lines about a center line""",
    ),
    (
        "ST_PointOnSurface",
        types.Geometry,
        """Returns a POINT guaranteed to lie on the surface.""",
    ),
    (
        "ST_RemoveRepeatedPoints",
        types.Geometry,
        """Returns a version of the given geometry with duplicated points removed.""",
    ),
    (
        "ST_SharedPaths",
        types.Geometry,
        """Returns a collection containing paths shared by the two input linestrings/multilinestrings.""",
    ),
    (
        "ST_ShiftLongitude",
        types.Geometry,
        (
            """Toggle geometry coordinates between -180..180 and 0..360 ranges.""",
            "ST_Shift_Longitude",
        ),
    ),
    ("ST_WrapX", types.Geometry, """Wrap a geometry around an X value."""),
    (
        "ST_Simplify",
        types.Geometry,
        """Returns a \"simplified\" version of the given geometry using the Douglas-Peucker algorithm.""",
    ),
    (
        "ST_SimplifyPreserveTopology",
        types.Geometry,
        """Returns a \"simplified\" version of the given geometry using the Douglas-Peucker algorithm. Will avoid creating derived geometries (polygons in particular) that are invalid.""",
    ),
    (
        "ST_SimplifyVW",
        types.Geometry,
        """Returns a \"simplified\" version of the given geometry using the Visvalingam-Whyatt algorithm""",
    ),
    (
        "ST_ChaikinSmoothing",
        types.Geometry,
        """Returns a \"smoothed\" version of the given geometry using the Chaikin algorithm""",
    ),
    (
        "ST_FilterByM",
        types.Geometry,
        """Filters vertex points based on their m-value""",
    ),
    (
        "ST_SetEffectiveArea",
        types.Geometry,
        """Sets the effective area for each vertex, storing the value in the M ordinate. A simplified geometry can then be generated by filtering on the M ordinate.""",
    ),
    (
        "ST_Split",
        types.Geometry,
        """Returns a collection of geometries resulting by splitting a geometry.""",
    ),
    (
        "ST_SymDifference",
        types.Geometry,
        """Returns a geometry that represents the portions of A and B that do not intersect. It is called a symmetric difference because ST_SymDifference(A,B) = ST_SymDifference(B,A).""",
    ),
    (
        "ST_Subdivide",
        types.Geometry,
        """Returns a set of geometry where no geometry in the set has more than the specified number of vertices.""",
    ),
    (
        "ST_Union",
        types.Geometry,
        """[geometry] Returns a geometry that represents the point set union of the Geometries.\nOR\n[raster] Returns the union of a set of raster tiles into a single raster composed of 1 or more bands.""",
    ),
    (
        "ST_UnaryUnion",
        types.Geometry,
        """Like ST_Union, but working at the geometry component level.""",
    ),
    (
        "ST_VoronoiLines",
        types.Geometry,
        """Returns the boundaries between the cells of the Voronoi diagram constructed from the vertices of a geometry.""",
    ),
    (
        "ST_VoronoiPolygons",
        types.Geometry,
        """Returns the cells of the Voronoi diagram constructed from the vertices of a geometry.""",
    ),
    (
        "ST_Affine",
        types.Geometry,
        """Apply a 3D affine transformation to a geometry.""",
    ),
    ("ST_Rotate", types.Geometry, """Rotates a geometry about an origin point."""),
    ("ST_RotateX", types.Geometry, """Rotates a geometry about the X axis."""),
    ("ST_RotateY", types.Geometry, """Rotates a geometry about the Y axis."""),
    ("ST_RotateZ", types.Geometry, """Rotates a geometry about the Z axis."""),
    ("ST_Scale", types.Geometry, """Scales a geometry by given factors."""),
    ("ST_Translate", types.Geometry, """Translates a geometry by given offsets."""),
    (
        "ST_TransScale",
        types.Geometry,
        """Translates and scales a geometry by given offsets and factors.""",
    ),
    (
        "ST_ClusterDBSCAN",
        None,
        """Window function that returns a cluster id for each input geometry using the DBSCAN algorithm.""",
    ),
    (
        "ST_ClusterIntersecting",
        types.Geometry,
        """Aggregate function that clusters the input geometries into connected sets.""",
    ),
    (
        "ST_ClusterKMeans",
        None,
        """Window function that returns a cluster id for each input geometry using the K-means algorithm.""",
    ),
    (
        "ST_ClusterWithin",
        types.Geometry,
        """Aggregate function that clusters the input geometries by separation distance.""",
    ),
    (
        "Box2D",
        None,  # return an unsupported Box2d object
        (
            """Returns a BOX2D representing the 2D extent of the geometry.""",
            "Box2D_type",
        ),
    ),
    (
        "Box3D",
        None,  # return an unsupported Box3d object
        (
            """[geometry] Returns a BOX3D representing the 3D extent of the geometry.\nOR\n[raster] Returns the box 3d representation of the enclosing box of the raster.""",
            "Box3D_type",
        ),
    ),
    (
        "ST_EstimatedExtent",
        None,  # return an unsupported Box2d object
        """Return the 'estimated' extent of a spatial table.""",
    ),
    (
        "ST_Expand",
        types.Geometry,
        """Returns a bounding box expanded from another bounding box or a geometry.""",
    ),
    (
        "ST_Extent",
        None,  # return an unsupported Box2d object
        """an aggregate function that returns the bounding box that bounds rows of geometries.""",
    ),
    (
        "ST_3DExtent",
        None,  # return an unsupported Box3d object
        """an aggregate function that returns the 3D bounding box that bounds rows of geometries.""",
    ),
    (
        "ST_MakeBox2D",
        None,  # return an unsupported Box2d object
        """Creates a BOX2D defined by two 2D point geometries.""",
    ),
    (
        "ST_3DMakeBox",
        None,  # return an unsupported Box3d object
        """Creates a BOX3D defined by two 3D point geometries.""",
    ),
    (
        "ST_XMax",
        None,
        """Returns the X maxima of a 2D or 3D bounding box or a geometry.""",
    ),
    (
        "ST_XMin",
        None,
        """Returns the X minima of a 2D or 3D bounding box or a geometry.""",
    ),
    (
        "ST_YMax",
        None,
        """Returns the Y maxima of a 2D or 3D bounding box or a geometry.""",
    ),
    (
        "ST_YMin",
        None,
        """Returns the Y minima of a 2D or 3D bounding box or a geometry.""",
    ),
    (
        "ST_ZMax",
        None,
        """Returns the Z maxima of a 2D or 3D bounding box or a geometry.""",
    ),
    (
        "ST_ZMin",
        None,
        """Returns the Z minima of a 2D or 3D bounding box or a geometry.""",
    ),
    (
        "ST_LineInterpolatePoint",
        types.Geometry,
        """Returns a point interpolated along a line. Second argument is a float8 between 0 and 1 representing fraction of total length of linestring the point has to be located.""",
    ),
    (
        "ST_3DLineInterpolatePoint",
        types.Geometry,
        """Returns a point interpolated along a line in 3D. Second argument is a float8 between 0 and 1 representing fraction of total length of linestring the point has to be located.""",
    ),
    (
        "ST_LineInterpolatePoints",
        types.Geometry,
        """Returns one or more points interpolated along a line.""",
    ),
    (
        "ST_LineLocatePoint",
        None,
        """Returns a float between 0 and 1 representing the location of the closest point on LineString to the given Point, as a fraction of total 2d line length.""",
    ),
    (
        "ST_LineSubstring",
        types.Geometry,
        """Return a linestring being a substring of the input one starting and ending at the given fractions of total 2d length. Second and third arguments are float8 values between 0 and 1.""",
    ),
    (
        "ST_LocateAlong",
        types.Geometry,
        """Return a derived geometry collection value with elements that match the specified measure. Polygonal elements are not supported.""",
    ),
    (
        "ST_LocateBetween",
        types.Geometry,
        """Return a derived geometry collection value with elements that match the specified range of measures inclusively.""",
    ),
    (
        "ST_LocateBetweenElevations",
        types.Geometry,
        """Return a derived geometry (collection) value with elements that intersect the specified range of elevations inclusively.""",
    ),
    (
        "ST_InterpolatePoint",
        None,
        """Return the value of the measure dimension of a geometry at the point closed to the provided point.""",
    ),
    (
        "ST_AddMeasure",
        types.Geometry,
        """Return a derived geometry with measure elements linearly interpolated between the start and end points.""",
    ),
    (
        "ST_IsValidTrajectory",
        None,
        """Returns true if the geometry is a valid trajectory.""",
    ),
    (
        "ST_ClosestPointOfApproach",
        None,
        """Returns the measure at which points interpolated along two trajectories are closest.""",
    ),
    (
        "ST_DistanceCPA",
        None,
        """Returns the distance between the closest point of approach of two trajectories.""",
    ),
    (
        "ST_CPAWithin",
        None,
        """Returns true if the closest point of approach of two trajectories is within the specified distance.""",
    ),
    ("postgis_sfcgal_version", None, """Returns the version of SFCGAL in use"""),
    ("ST_Extrude", types.Geometry, """Extrude a surface to a related volume"""),
    (
        "ST_StraightSkeleton",
        types.Geometry,
        """Compute a straight skeleton from a geometry""",
    ),
    (
        "ST_ApproximateMedialAxis",
        types.Geometry,
        """Compute the approximate medial axis of an areal geometry.""",
    ),
    ("ST_IsPlanar", None, """Check if a surface is or not planar"""),
    ("ST_Orientation", None, """Determine surface orientation"""),
    ("ST_ForceLHR", types.Geometry, """Force LHR orientation"""),
    ("ST_MinkowskiSum", types.Geometry, """Performs Minkowski sum"""),
    (
        "ST_ConstrainedDelaunayTriangles",
        types.Geometry,
        """Return a constrained Delaunay triangulation around the given input geometry.""",
    ),
    ("ST_3DIntersection", types.Geometry, """Perform 3D intersection"""),
    ("ST_3DDifference", types.Geometry, """Perform 3D difference"""),
    ("ST_3DUnion", types.Geometry, """Perform 3D union"""),
    (
        "ST_3DArea",
        None,
        """Computes area of 3D surface geometries. Will return 0 for solids.""",
    ),
    (
        "ST_Tesselate",
        types.Geometry,
        """Perform surface Tessellation of a polygon or polyhedralsurface and returns as a TIN or collection of TINS""",
    ),
    (
        "ST_Volume",
        None,
        """Computes the volume of a 3D solid. If applied to surface (even closed) geometries will return 0.""",
    ),
    (
        "ST_MakeSolid",
        types.Geometry,
        """Cast the geometry into a solid. No check is performed. To obtain a valid solid, the input geometry must be a closed Polyhedral Surface or a closed TIN.""",
    ),
    (
        "ST_IsSolid",
        None,
        """Test if the geometry is a solid. No validity check is performed.""",
    ),
    (
        "AddAuth",
        None,
        """Adds an authorization token to be used in the current transaction.""",
    ),
    (
        "CheckAuth",
        None,
        """Creates a trigger on a table to prevent/allow updates and deletes of rows based on authorization token.""",
    ),
    ("DisableLongTransactions", None, """Disables long transaction support."""),
    ("EnableLongTransactions", None, """Enables long transaction support."""),
    ("LockRow", None, """Sets lock/authorization for a row in a table."""),
    ("UnlockRows", None, """Removes all locks held by an authorization token."""),
    (
        "PostGIS_Extensions_Upgrade",
        None,
        """Packages and upgrades postgis extensions (e.g. postgis_raster, postgis_topology, postgis_sfcgal) to latest available version.""",
    ),
    (
        "PostGIS_Full_Version",
        None,
        """Reports full postgis version and build configuration infos.""",
    ),
    (
        "PostGIS_GEOS_Version",
        None,
        """Returns the version number of the GEOS library.""",
    ),
    (
        "PostGIS_Liblwgeom_Version",
        None,
        """Returns the version number of the liblwgeom library. This should match the version of PostGIS.""",
    ),
    (
        "PostGIS_LibXML_Version",
        None,
        """Returns the version number of the libxml2 library.""",
    ),
    ("PostGIS_Lib_Build_Date", None, """Returns build date of the PostGIS library."""),
    (
        "PostGIS_Lib_Version",
        None,
        """Returns the version number of the PostGIS library.""",
    ),
    (
        "PostGIS_PROJ_Version",
        None,
        """Returns the version number of the PROJ4 library.""",
    ),
    (
        "PostGIS_Wagyu_Version",
        None,
        """Returns the version number of the internal Wagyu library.""",
    ),
    (
        "PostGIS_Scripts_Build_Date",
        None,
        """Returns build date of the PostGIS scripts.""",
    ),
    (
        "PostGIS_Scripts_Installed",
        None,
        """Returns version of the postgis scripts installed in this database.""",
    ),
    (
        "PostGIS_Scripts_Released",
        None,
        """Returns the version number of the postgis.sql script released with the installed postgis lib.""",
    ),
    (
        "PostGIS_Version",
        None,
        """Returns PostGIS version number and compile-time options.""",
    ),
    ("PostGIS_AddBBox", types.Geometry, """Add bounding box to the geometry."""),
    (
        "PostGIS_DropBBox",
        types.Geometry,
        """Drop the bounding box cache from the geometry.""",
    ),
    (
        "PostGIS_HasBBox",
        None,
        """Returns TRUE if the bbox of this geometry is cached, FALSE otherwise.""",
    ),
    (
        "ST_AddBand",
        types.Raster,
        (
            """Returns a raster with the new band(s) of given type added with given initial value in the given index location. If no index is specified, the band is added to the end.""",
            "RT_ST_AddBand",
        ),
    ),
    (
        "ST_AsRaster",
        types.Raster,
        ("""Converts a PostGIS geometry to a PostGIS raster.""", "RT_ST_AsRaster"),
    ),
    (
        "ST_Band",
        types.Raster,
        (
            """Returns one or more bands of an existing raster as a new raster. Useful for building new rasters from existing rasters.""",
            "RT_ST_Band",
        ),
    ),
    (
        "ST_MakeEmptyCoverage",
        types.Raster,
        (
            """Cover georeferenced area with a grid of empty raster tiles.""",
            "RT_ST_MakeEmptyCoverage",
        ),
    ),
    (
        "ST_MakeEmptyRaster",
        types.Raster,
        (
            """Returns an empty raster (having no bands) of given dimensions (width & height), upperleft X and Y, pixel size and rotation (scalex, scaley, skewx & skewy) and reference system (srid). If a raster is passed in, returns a new raster with the same size, alignment and SRID. If srid is left out, the spatial ref is set to unknown (0).""",
            "RT_ST_MakeEmptyRaster",
        ),
    ),
    (
        "ST_Tile",
        types.Raster,
        (
            """Returns a set of rasters resulting from the split of the input raster based upon the desired dimensions of the output rasters.""",
            "RT_ST_Tile",
        ),
    ),
    (
        "ST_Retile",
        types.Raster,
        (
            """Return a set of configured tiles from an arbitrarily tiled raster coverage.""",
            "RT_ST_Retile",
        ),
    ),
    (
        "ST_FromGDALRaster",
        types.Raster,
        (
            """Returns a raster from a supported GDAL raster file.""",
            "RT_ST_FromGDALRaster",
        ),
    ),
    (
        "ST_GeoReference",
        None,
        (
            """Returns the georeference meta data in GDAL or ESRI format as commonly seen in a world file. Default is GDAL.""",
            "RT_ST_GeoReference",
        ),
    ),
    (
        "ST_Height",
        None,
        ("""Returns the height of the raster in pixels.""", "RT_ST_Height"),
    ),
    (
        "ST_MetaData",
        None,
        (
            """Returns basic meta data about a raster object such as pixel size, rotation (skew), upper, lower left, etc.""",
            "RT_ST_MetaData",
        ),
    ),
    (
        "ST_NumBands",
        None,
        ("""Returns the number of bands in the raster object.""", "RT_ST_NumBands"),
    ),
    (
        "ST_PixelHeight",
        None,
        (
            """Returns the pixel height in geometric units of the spatial reference system.""",
            "RT_ST_PixelHeight",
        ),
    ),
    (
        "ST_PixelWidth",
        None,
        (
            """Returns the pixel width in geometric units of the spatial reference system.""",
            "RT_ST_PixelWidth",
        ),
    ),
    (
        "ST_ScaleX",
        None,
        (
            """Returns the X component of the pixel width in units of coordinate reference system.""",
            "RT_ST_ScaleX",
        ),
    ),
    (
        "ST_ScaleY",
        None,
        (
            """Returns the Y component of the pixel height in units of coordinate reference system.""",
            "RT_ST_ScaleY",
        ),
    ),
    (
        "ST_RasterToWorldCoord",
        None,
        (
            """Returns the raster's upper left corner as geometric X and Y (longitude and latitude) given a column and row. Column and row starts at 1.""",
            "RT_ST_RasterToWorldCoord",
        ),
    ),
    (
        "ST_RasterToWorldCoordX",
        None,
        (
            """Returns the geometric X coordinate upper left of a raster, column and row. Numbering of columns and rows starts at 1.""",
            "RT_ST_RasterToWorldCoordX",
        ),
    ),
    (
        "ST_RasterToWorldCoordY",
        None,
        (
            """Returns the geometric Y coordinate upper left corner of a raster, column and row. Numbering of columns and rows starts at 1.""",
            "RT_ST_RasterToWorldCoordY",
        ),
    ),
    (
        "ST_Rotation",
        None,
        ("""Returns the rotation of the raster in radian.""", "RT_ST_Rotation"),
    ),
    (
        "ST_SkewX",
        None,
        ("""Returns the georeference X skew (or rotation parameter).""", "RT_ST_SkewX"),
    ),
    (
        "ST_SkewY",
        None,
        ("""Returns the georeference Y skew (or rotation parameter).""", "RT_ST_SkewY"),
    ),
    (
        "ST_UpperLeftX",
        None,
        (
            """Returns the upper left X coordinate of raster in projected spatial ref.""",
            "RT_ST_UpperLeftX",
        ),
    ),
    (
        "ST_UpperLeftY",
        None,
        (
            """Returns the upper left Y coordinate of raster in projected spatial ref.""",
            "RT_ST_UpperLeftY",
        ),
    ),
    (
        "ST_Width",
        None,
        ("""Returns the width of the raster in pixels.""", "RT_ST_Width"),
    ),
    (
        "ST_WorldToRasterCoord",
        None,
        (
            """Returns the upper left corner as column and row given geometric X and Y (longitude and latitude) or a point geometry expressed in the spatial reference coordinate system of the raster.""",
            "RT_ST_WorldToRasterCoord",
        ),
    ),
    (
        "ST_WorldToRasterCoordX",
        None,
        (
            """Returns the column in the raster of the point geometry (pt) or a X and Y world coordinate (xw, yw) represented in world spatial reference system of raster.""",
            "RT_ST_WorldToRasterCoordX",
        ),
    ),
    (
        "ST_WorldToRasterCoordY",
        None,
        (
            """Returns the row in the raster of the point geometry (pt) or a X and Y world coordinate (xw, yw) represented in world spatial reference system of raster.""",
            "RT_ST_WorldToRasterCoordY",
        ),
    ),
    (
        "ST_BandMetaData",
        None,
        (
            """Returns basic meta data for a specific raster band. band num 1 is assumed if none-specified.""",
            "RT_ST_BandMetaData",
        ),
    ),
    (
        "ST_BandNoDataValue",
        None,
        (
            """Returns the value in a given band that represents no data. If no band num 1 is assumed.""",
            "RT_ST_BandNoDataValue",
        ),
    ),
    (
        "ST_BandIsNoData",
        None,
        (
            """Returns true if the band is filled with only nodata values.""",
            "RT_ST_BandIsNoData",
        ),
    ),
    (
        "ST_BandPath",
        None,
        (
            """Returns system file path to a band stored in file system. If no bandnum specified, 1 is assumed.""",
            "RT_ST_BandPath",
        ),
    ),
    (
        "ST_BandFileSize",
        None,
        (
            """Returns the file size of a band stored in file system. If no bandnum specified, 1 is assumed.""",
            "RT_ST_BandFileSize",
        ),
    ),
    (
        "ST_BandFileTimestamp",
        None,
        (
            """Returns the file timestamp of a band stored in file system. If no bandnum specified, 1 is assumed.""",
            "RT_ST_BandFileTimestamp",
        ),
    ),
    (
        "ST_BandPixelType",
        None,
        (
            """Returns the type of pixel for given band. If no bandnum specified, 1 is assumed.""",
            "RT_ST_BandPixelType",
        ),
    ),
    (
        "ST_MinPossibleValue",
        None,
        """Returns the minimum value this pixeltype can store.""",
    ),
    (
        "ST_HasNoBand",
        None,
        (
            """Returns true if there is no band with given band number. If no band number is specified, then band number 1 is assumed.""",
            "RT_ST_HasNoBand",
        ),
    ),
    (
        "ST_PixelAsPolygon",
        types.Geometry,
        (
            """Returns the polygon geometry that bounds the pixel for a particular row and column.""",
            "RT_ST_PixelAsPolygon",
        ),
    ),
    (
        "ST_PixelAsPolygons",
        None,
        (
            """Returns the polygon geometry that bounds every pixel of a raster band along with the value, the X and the Y raster coordinates of each pixel.""",
            "RT_ST_PixelAsPolygons",
        ),
    ),
    (
        "ST_PixelAsPoint",
        types.Geometry,
        (
            """Returns a point geometry of the pixel's upper-left corner.""",
            "RT_ST_PixelAsPoint",
        ),
    ),
    (
        "ST_PixelAsPoints",
        None,
        (
            """Returns a point geometry for each pixel of a raster band along with the value, the X and the Y raster coordinates of each pixel. The coordinates of the point geometry are of the pixel's upper-left corner.""",
            "RT_ST_PixelAsPoints",
        ),
    ),
    (
        "ST_PixelAsCentroid",
        types.Geometry,
        (
            """Returns the centroid (point geometry) of the area represented by a pixel.""",
            "RT_ST_PixelAsCentroid",
        ),
    ),
    (
        "ST_PixelAsCentroids",
        None,
        (
            """Returns the centroid (point geometry) for each pixel of a raster band along with the value, the X and the Y raster coordinates of each pixel. The point geometry is the centroid of the area represented by a pixel.""",
            "RT_ST_PixelAsCentroids",
        ),
    ),
    (
        "ST_Value",
        None,
        (
            """Returns the value of a given band in a given columnx, rowy pixel or at a particular geometric point. Band numbers start at 1 and assumed to be 1 if not specified. If exclude_nodata_value is set to false, then all pixels include nodata pixels are considered to intersect and return value. If exclude_nodata_value is not passed in then reads it from metadata of raster.""",
            "RT_ST_Value",
        ),
    ),
    (
        "ST_NearestValue",
        None,
        (
            """Returns the nearest non-NODATA value of a given band's pixel specified by a columnx and rowy or a geometric point expressed in the same spatial reference coordinate system as the raster.""",
            "RT_ST_NearestValue",
        ),
    ),
    (
        "ST_Neighborhood",
        None,
        (
            """Returns a 2-D double precision array of the non-NODATA values around a given band's pixel specified by either a columnX and rowY or a geometric point expressed in the same spatial reference coordinate system as the raster.""",
            "RT_ST_Neighborhood",
        ),
    ),
    (
        "ST_SetValue",
        types.Raster,
        (
            """Returns modified raster resulting from setting the value of a given band in a given columnx, rowy pixel or the pixels that intersect a particular geometry. Band numbers start at 1 and assumed to be 1 if not specified.""",
            "RT_ST_SetValue",
        ),
    ),
    (
        "ST_SetValues",
        types.Raster,
        (
            """Returns modified raster resulting from setting the values of a given band.""",
            "RT_ST_SetValues",
        ),
    ),
    (
        "ST_DumpValues",
        None,
        (
            """Get the values of the specified band as a 2-dimension array.""",
            "RT_ST_DumpValues",
        ),
    ),
    (
        "ST_PixelOfValue",
        None,
        (
            """Get the columnx, rowy coordinates of the pixel whose value equals the search value.""",
            "RT_ST_PixelOfValue",
        ),
    ),
    (
        "ST_SetGeoReference",
        types.Raster,
        (
            """Set Georeference 6 georeference parameters in a single call. Numbers should be separated by white space. Accepts inputs in GDAL or ESRI format. Default is GDAL.""",
            "RT_ST_SetGeoReference",
        ),
    ),
    (
        "ST_SetRotation",
        types.Raster,
        ("""Set the rotation of the raster in radian.""", "RT_ST_SetRotation"),
    ),
    (
        "ST_SetScale",
        types.Raster,
        (
            """Sets the X and Y size of pixels in units of coordinate reference system. Number units/pixel width/height.""",
            "RT_ST_SetScale",
        ),
    ),
    (
        "ST_SetSkew",
        types.Raster,
        (
            """Sets the georeference X and Y skew (or rotation parameter). If only one is passed in, sets X and Y to the same value.""",
            "RT_ST_SetSkew",
        ),
    ),
    (
        "ST_SetUpperLeft",
        types.Raster,
        (
            """Sets the value of the upper left corner of the pixel of the raster to projected X and Y coordinates.""",
            "RT_ST_SetUpperLeft",
        ),
    ),
    (
        "ST_Resample",
        types.Raster,
        (
            """Resample a raster using a specified resampling algorithm, new dimensions, an arbitrary grid corner and a set of raster georeferencing attributes defined or borrowed from another raster.""",
            "RT_ST_Resample",
        ),
    ),
    (
        "ST_Rescale",
        types.Raster,
        (
            """Resample a raster by adjusting only its scale (or pixel size). New pixel values are computed using the NearestNeighbor (english or american spelling), Bilinear, Cubic, CubicSpline or Lanczos resampling algorithm. Default is NearestNeighbor.""",
            "RT_ST_Rescale",
        ),
    ),
    (
        "ST_Reskew",
        types.Raster,
        (
            """Resample a raster by adjusting only its skew (or rotation parameters). New pixel values are computed using the NearestNeighbor (english or american spelling), Bilinear, Cubic, CubicSpline or Lanczos resampling algorithm. Default is NearestNeighbor.""",
            "RT_ST_Reskew",
        ),
    ),
    (
        "ST_Resize",
        types.Raster,
        ("""Resize a raster to a new width/height""", "RT_ST_Resize"),
    ),
    (
        "ST_SetBandNoDataValue",
        types.Raster,
        (
            """Sets the value for the given band that represents no data. Band 1 is assumed if no band is specified. To mark a band as having no nodata value, set the nodata value = NULL.""",
            "RT_ST_SetBandNoDataValue",
        ),
    ),
    (
        "ST_SetBandIsNoData",
        types.Raster,
        ("""Sets the isnodata flag of the band to TRUE.""", "RT_ST_SetBandIsNoData"),
    ),
    (
        "ST_SetBandPath",
        types.Raster,
        (
            """Update the external path and band number of an out-db band""",
            "RT_ST_SetBandPath",
        ),
    ),
    (
        "ST_SetBandIndex",
        types.Raster,
        ("""Update the external band number of an out-db band""", "RT_ST_SetBandIndex"),
    ),
    (
        "ST_Count",
        None,
        (
            """Returns the number of pixels in a given band of a raster or raster coverage. If no band is specified defaults to band 1. If exclude_nodata_value is set to true, will only count pixels that are not equal to the nodata value.""",
            "RT_ST_Count",
        ),
    ),
    (
        "ST_CountAgg",
        None,
        (
            """Aggregate. Returns the number of pixels in a given band of a set of rasters. If no band is specified defaults to band 1. If exclude_nodata_value is set to true, will only count pixels that are not equal to the NODATA value.""",
            "RT_ST_CountAgg",
        ),
    ),
    (
        "ST_Histogram",
        None,
        (
            """Returns a set of record summarizing a raster or raster coverage data distribution separate bin ranges. Number of bins are autocomputed if not specified.""",
            "RT_ST_Histogram",
        ),
    ),
    (
        "ST_Quantile",
        None,
        (
            """Compute quantiles for a raster or raster table coverage in the context of the sample or population. Thus, a value could be examined to be at the raster's 25%, 50%, 75% percentile.""",
            "RT_ST_Quantile",
        ),
    ),
    (
        "ST_SummaryStats",
        None,
        (
            """Returns summarystats consisting of count, sum, mean, stddev, min, max for a given raster band of a raster or raster coverage. Band 1 is assumed is no band is specified.""",
            "RT_ST_SummaryStats",
        ),
    ),
    (
        "ST_SummaryStatsAgg",
        types.SummaryStats,
        (
            """Aggregate. Returns summarystats consisting of count, sum, mean, stddev, min, max for a given raster band of a set of raster. Band 1 is assumed is no band is specified.""",
            "RT_ST_SummaryStatsAgg",
        ),
    ),
    (
        "ST_ValueCount",
        None,
        (
            """Returns a set of records containing a pixel band value and count of the number of pixels in a given band of a raster (or a raster coverage) that have a given set of values. If no band is specified defaults to band 1. By default nodata value pixels are not counted. and all other values in the pixel are output and pixel band values are rounded to the nearest integer.""",
            "RT_ST_ValueCount",
        ),
    ),
    (
        "ST_RastFromWKB",
        types.Raster,
        (
            """Return a raster value from a Well-Known Binary (WKB) raster.""",
            "RT_ST_RastFromWKB",
        ),
    ),
    (
        "ST_RastFromHexWKB",
        types.Raster,
        (
            """Return a raster value from a Hex representation of Well-Known Binary (WKB) raster.""",
            "RT_ST_RastFromHexWKB",
        ),
    ),
    (
        "ST_AsWKB",
        None,
        (
            """Return the Well-Known Binary (WKB) representation of the raster.""",
            "RT_ST_AsBinary",
        ),
    ),
    (
        "ST_AsHexWKB",
        None,
        (
            """Return the Well-Known Binary (WKB) in Hex representation of the raster.""",
            "RT_ST_AsHexWKB",
        ),
    ),
    (
        "ST_AsGDALRaster",
        None,
        (
            """Return the raster tile in the designated GDAL Raster format. Raster formats are one of those supported by your compiled library. Use ST_GDALDrivers() to get a list of formats supported by your library.""",
            "RT_ST_AsGDALRaster",
        ),
    ),
    (
        "ST_AsJPEG",
        None,
        (
            """Return the raster tile selected bands as a single Joint Photographic Exports Group (JPEG) image (byte array). If no band is specified and 1 or more than 3 bands, then only the first band is used. If only 3 bands then all 3 bands are used and mapped to RGB.""",
            "RT_ST_AsJPEG",
        ),
    ),
    (
        "ST_AsPNG",
        None,
        (
            """Return the raster tile selected bands as a single portable network graphics (PNG) image (byte array). If 1, 3, or 4 bands in raster and no bands are specified, then all bands are used. If more 2 or more than 4 bands and no bands specified, then only band 1 is used. Bands are mapped to RGB or RGBA space.""",
            "RT_ST_AsPNG",
        ),
    ),
    (
        "ST_AsTIFF",
        None,
        (
            """Return the raster selected bands as a single TIFF image (byte array). If no band is specified or any of specified bands does not exist in the raster, then will try to use all bands.""",
            "RT_ST_AsTIFF",
        ),
    ),
    (
        "ST_Clip",
        types.Raster,
        (
            """Returns the raster clipped by the input geometry. If band number not is specified, all bands are processed. If crop is not specified or TRUE, the output raster is cropped.""",
            "RT_ST_Clip",
        ),
    ),
    (
        "ST_ColorMap",
        types.Raster,
        (
            """Creates a new raster of up to four 8BUI bands (grayscale, RGB, RGBA) from the source raster and a specified band. Band 1 is assumed if not specified.""",
            "RT_ST_ColorMap",
        ),
    ),
    (
        "ST_Grayscale",
        types.Raster,
        (
            """Creates a new one-8BUI band raster from the source raster and specified bands representing Red, Green and Blue""",
            "RT_ST_Grayscale",
        ),
    ),
    (
        "ST_MapAlgebra",
        None,
        (
            """[raster] Callback function version - Returns a one-band raster given one or more input rasters, band indexes and one user-specified callback function.\nOR\n[raster] Expression version - Returns a one-band raster given one or two input rasters, band indexes and one or more user-specified SQL expressions.""",
            "RT_ST_MapAlgebra",
        ),
    ),
    (
        "ST_MapAlgebraExpr",
        types.Raster,
        (
            """[raster] 1 raster band version: Creates a new one band raster formed by applying a valid PostgreSQL algebraic operation on the input raster band and of pixeltype provided. Band 1 is assumed if no band is specified.\nOR\n[raster] 2 raster band version: Creates a new one band raster formed by applying a valid PostgreSQL algebraic operation on the two input raster bands and of pixeltype provided. band 1 of each raster is assumed if no band numbers are specified. The resulting raster will be aligned (scale, skew and pixel corners) on the grid defined by the first raster and have its extent defined by the \"extenttype\" parameter. Values for \"extenttype\" can be: INTERSECTION, UNION, FIRST, SECOND.""",
            "RT_ST_MapAlgebraExpr",
        ),
    ),
    (
        "ST_MapAlgebraFct",
        types.Raster,
        (
            """[raster] 1 band version - Creates a new one band raster formed by applying a valid PostgreSQL function on the input raster band and of pixeltype prodived. Band 1 is assumed if no band is specified.\nOR\n[raster] 2 band version - Creates a new one band raster formed by applying a valid PostgreSQL function on the 2 input raster bands and of pixeltype prodived. Band 1 is assumed if no band is specified. Extent type defaults to INTERSECTION if not specified.""",
            "RT_ST_MapAlgebraFct",
        ),
    ),
    (
        "ST_MapAlgebraFctNgb",
        types.Raster,
        (
            """1-band version: Map Algebra Nearest Neighbor using user-defined PostgreSQL function. Return a raster which values are the result of a PLPGSQL user function involving a neighborhood of values from the input raster band.""",
            "RT_ST_MapAlgebraFctNgb",
        ),
    ),
    (
        "ST_Reclass",
        types.Raster,
        (
            """Creates a new raster composed of band types reclassified from original. The nband is the band to be changed. If nband is not specified assumed to be 1. All other bands are returned unchanged. Use case: convert a 16BUI band to a 8BUI and so forth for simpler rendering as viewable formats.""",
            "RT_ST_Reclass",
        ),
    ),
    (
        "ST_Distinct4ma",
        None,
        (
            """Raster processing function that calculates the number of unique pixel values in a neighborhood.""",
            "RT_ST_Distinct4ma",
        ),
    ),
    (
        "ST_InvDistWeight4ma",
        None,
        (
            """Raster processing function that interpolates a pixel's value from the pixel's neighborhood.""",
            "RT_ST_InvDistWeight4ma",
        ),
    ),
    (
        "ST_Max4ma",
        None,
        (
            """Raster processing function that calculates the maximum pixel value in a neighborhood.""",
            "RT_ST_Max4ma",
        ),
    ),
    (
        "ST_Mean4ma",
        None,
        (
            """Raster processing function that calculates the mean pixel value in a neighborhood.""",
            "RT_ST_Mean4ma",
        ),
    ),
    (
        "ST_Min4ma",
        None,
        (
            """Raster processing function that calculates the minimum pixel value in a neighborhood.""",
            "RT_ST_Min4ma",
        ),
    ),
    (
        "ST_MinDist4ma",
        None,
        (
            """Raster processing function that returns the minimum distance (in number of pixels) between the pixel of interest and a neighboring pixel with value.""",
            "RT_ST_MinDist4ma",
        ),
    ),
    (
        "ST_Range4ma",
        None,
        (
            """Raster processing function that calculates the range of pixel values in a neighborhood.""",
            "RT_ST_Range4ma",
        ),
    ),
    (
        "ST_StdDev4ma",
        None,
        (
            """Raster processing function that calculates the standard deviation of pixel values in a neighborhood.""",
            "RT_ST_StdDev4ma",
        ),
    ),
    (
        "ST_Sum4ma",
        None,
        (
            """Raster processing function that calculates the sum of all pixel values in a neighborhood.""",
            "RT_ST_Sum4ma",
        ),
    ),
    (
        "ST_Aspect",
        types.Raster,
        (
            """Returns the aspect (in degrees by default) of an elevation raster band. Useful for analyzing terrain.""",
            "RT_ST_Aspect",
        ),
    ),
    (
        "ST_HillShade",
        types.Raster,
        (
            """Returns the hypothetical illumination of an elevation raster band using provided azimuth, altitude, brightness and scale inputs.""",
            "RT_ST_HillShade",
        ),
    ),
    (
        "ST_Roughness",
        types.Raster,
        (
            """Returns a raster with the calculated \"roughness\" of a DEM.""",
            "RT_ST_Roughness",
        ),
    ),
    (
        "ST_Slope",
        types.Raster,
        (
            """Returns the slope (in degrees by default) of an elevation raster band. Useful for analyzing terrain.""",
            "RT_ST_Slope",
        ),
    ),
    (
        "ST_TPI",
        types.Raster,
        (
            """Returns a raster with the calculated Topographic Position Index.""",
            "RT_ST_TPI",
        ),
    ),
    (
        "ST_TRI",
        types.Raster,
        (
            """Returns a raster with the calculated Terrain Ruggedness Index.""",
            "RT_ST_TRI",
        ),
    ),
    (
        "ST_DumpAsPolygons",
        None,
        (
            """Returns a set of geomval (geom,val) rows, from a given raster band. If no band number is specified, band num defaults to 1.""",
            "RT_ST_DumpAsPolygons",
        ),
    ),
    (
        "ST_MinConvexHull",
        types.Geometry,
        (
            """Return the convex hull geometry of the raster excluding NODATA pixels.""",
            "RT_ST_MinConvexHull",
        ),
    ),
    (
        "ST_SameAlignment",
        None,
        (
            """Returns true if rasters have same skew, scale, spatial ref, and offset (pixels can be put on same grid without cutting into pixels) and false if they don't with notice detailing issue.""",
            "RT_ST_SameAlignment",
        ),
    ),
    (
        "ST_NotSameAlignmentReason",
        None,
        (
            """Returns text stating if rasters are aligned and if not aligned, a reason why.""",
            "RT_ST_NotSameAlignmentReason",
        ),
    ),
    (
        "ST_Distance_Sphere",
        None,
        """Returns minimum distance in meters between two lon/lat geometries. Uses a spherical earth and radius of 6370986 meters. Faster than ``ST_Distance_Spheroid``, but less accurate. PostGIS versions prior to 1.5 only implemented for points.""",
    ),
]

# TODO (Reconcile this list from http://postgis.net/docs/manual-3.3/PostGIS_Special_Functions_Index.html#PostGIS_TypeFunctionMatrix with the previous list above)
# Box2D
# Box3D
# GeometryType
# PostGIS_AddBBox
# PostGIS_DropBBo
# PostGIS_HasBBo
# ST_3DArea
# ST_3DClosestPoint
# ST_3DConvexHull
# ST_3DDifference
# ST_3DDistance
# ST_3DExtent
# ST_3DIntersection
# ST_3DLength
# ST_3DLineInterpolatePoint
# ST_3DLongestLine
# ST_3DMakeBox
# ST_3DMaxDistance
# ST_3DPerimeter
# ST_3DShortestLine
# ST_3DUnion
# ST_AddMeasure
# ST_AddPoint
# ST_Affine
# ST_AlphaShape
# ST_Angle
# ST_ApproximateMedialAxis
# ST_Area
# ST_Azimuth
# ST_Boundary
# ST_BoundingDiagonal
# ST_Buffer
# ST_BuildArea
# ST_CPAWithin
# ST_Centroid
# ST_ChaikinSmoothing
# ST_ClipByBox2D
# ST_ClosestPoint
# ST_ClosestPointOfApproach
# ST_ClusterDBSCAN
# ST_ClusterIntersecting
# ST_ClusterKMeans
# ST_ClusterWithin
# ST_Collect
# ST_CollectionExtract
# ST_CollectionHomogenize
# ST_ConcaveHull
# ST_ConstrainedDelaunayTriangles
# ST_ConvexHull
# ST_CoordDim
# ST_CurveToLine
# ST_DelaunayTriangles
# ST_Difference
# ST_Dimension
# ST_Distance
# ST_DistanceCPA
# ST_DistanceSphere
# ST_DistanceSpheroid
# ST_Dump
# ST_DumpPoints
# ST_DumpRings
# ST_DumpSegments
# ST_EndPoint
# ST_Envelope
# ST_EstimatedExtent
# ST_Expand
# ST_Extent
# ST_ExteriorRing
# ST_Extrude
# ST_FilterByM
# ST_FlipCoordinates
# ST_Force2D
# ST_Force3D
# ST_Force3DM
# ST_Force3DZ
# ST_Force4D
# ST_ForceCollection
# ST_ForceCurve
# ST_ForceLHR
# ST_ForcePolygonCCW
# ST_ForcePolygonCW
# ST_ForceRHR
# ST_ForceSFS
# ST_FrechetDistance
# ST_GeneratePoints
# ST_GeometricMedian
# ST_GeometryN
# ST_GeometryType
# ST_HasArc
# ST_HausdorffDistance
# ST_Hexagon
# ST_HexagonGrid
# ST_InteriorRingN
# ST_InterpolatePoint
# ST_Intersection
# ST_IsClosed
# ST_IsCollection
# ST_IsEmpty
# ST_IsPlanar
# ST_IsPolygonCCW
# ST_IsPolygonCW
# ST_IsRing
# ST_IsSimple
# ST_IsSolid
# ST_IsValid
# ST_IsValidDetail
# ST_IsValidReason
# ST_IsValidTrajectory
# ST_Length
# ST_Length2D
# ST_LengthSpheroid
# ST_Letters
# ST_LineFromMultiPoint
# ST_LineInterpolatePoint
# ST_LineInterpolatePoints
# ST_LineLocatePoint
# ST_LineMerge
# ST_LineSubstring
# ST_LineToCurve
# ST_LocateAlong
# ST_LocateBetween
# ST_LocateBetweenElevations
# ST_LongestLine
# ST_M
# ST_MakeBox2D
# ST_MakeEnvelope
# ST_MakeLine
# ST_MakePoint
# ST_MakePointM
# ST_MakePolygon
# ST_MakeSolid
# ST_MakeValid
# ST_MaxDistance
# ST_MaximumInscribedCircle
# ST_MemSize
# ST_MemUnion
# ST_MinimumBoundingCircle
# ST_MinimumBoundingRadius
# ST_MinimumClearance
# ST_MinimumClearanceLine
# ST_MinkowskiSum
# ST_Multi
# ST_NDims
# ST_NPoints
# ST_NRings
# ST_Node
# ST_Normalize
# ST_NumGeometries
# ST_NumInteriorRing
# ST_NumInteriorRings
# ST_NumPatches
# ST_NumPoints
# ST_OffsetCurve
# ST_OptimalAlphaShape
# ST_Orientation
# ST_OrientedEnvelope
# ST_PatchN
# ST_Perimeter
# ST_Perimeter2D
# ST_Point
# ST_PointM
# ST_PointN
# ST_PointOnSurface
# ST_PointZ
# ST_PointZM
# ST_Points
# ST_Polygon
# ST_Polygoniz
# ST_QuantizeCoordinates
# ST_ReducePrecision
# ST_RemovePoint
# ST_RemoveRepeatedPoints
# ST_Reverse
# ST_Rotate
# ST_RotateX
# ST_RotateY
# ST_RotateZ
# ST_SRID
# ST_Scale
# ST_Scroll
# ST_Segmentize
# ST_SetEffectiveArea
# ST_SetPoint
# ST_SetSRID
# ST_SharedPaths
# ST_ShiftLongitude
# ST_ShortestLine
# ST_Simplify
# ST_SimplifyPolygonHull
# ST_SimplifyPreserveTopology
# ST_SimplifyVW
# ST_Snap
# ST_SnapToGrid
# ST_Split
# ST_Square
# ST_SquareGrid
# ST_StartPoint
# ST_StraightSkeleton
# ST_Subdivide
# ST_Summary
# ST_SwapOrdinates
# ST_SymDifference
# ST_Tesselate
# ST_TileEnvelope
# ST_TransScale
# ST_Transform
# ST_Translate
# ST_TriangulatePolygon
# ST_UnaryUnion
# ST_Union
# ST_Volume
# ST_VoronoiLines
# ST_VoronoiPolygons
# ST_WrapX
# ST_X
# ST_XMax
# ST_XMin
# ST_Y
# ST_YMax
# ST_YMin
# ST_Z
# ST_ZMax
# ST_ZMin
# ST_Zmflag
