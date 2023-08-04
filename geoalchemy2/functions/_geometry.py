# -*- coding: utf-8 -*-
# flake8: noqa
from geoalchemy2 import types

_FUNCTIONS = [
    (
        "AddAuth",
        None,
        "Adds an authorization token to be used in the current transaction.",
    ),
    (
        "AddGeometryColumn",
        None,
        "Adds a geometry column to an existing table.",
    ),
    (
        "Box2D",
        None,
        "Returns a BOX2D representing the 2D extent of the geometry.",
    ),
    (
        "Box3D",
        None,
        (
            "[geometry] Returns a BOX3D representing the 3D extent of the geometry.\nOR\n[raster] Returns the box 3d representation of the enclosing box of the raster.",
            "Box3D_type",
        ),
    ),
    (
        "CheckAuth",
        None,
        "Creates a trigger on a table to prevent/allow updates and deletes of rows based on authorization token.",
    ),
    (
        "DisableLongTransactions",
        None,
        "Disables long transaction support.",
    ),
    (
        "DropGeometryColumn",
        None,
        "Removes a geometry column from a spatial table.",
    ),
    (
        "DropGeometryTable",
        None,
        "Drops a table and all its references in geometry_columns.",
    ),
    (
        "EnableLongTransactions",
        None,
        "Enables long transaction support.",
    ),
    (
        "Find_SRID",
        None,
        "Returns the SRID defined for a geometry column.",
    ),
    (
        "GeometryType",
        None,
        "Returns the type of a geometry as text.",
    ),
    (
        "LockRow",
        None,
        "Sets lock/authorization for a row in a table.",
    ),
    (
        "Populate_Geometry_Columns",
        None,
        "Ensures geometry columns are defined with type modifiers or have appropriate spatial constraints.",
    ),
    (
        "PostGIS_AddBBox",
        types.Geometry,
        "Add bounding box to the geometry.",
    ),
    (
        "PostGIS_DropBBox",
        types.Geometry,
        "Drop the bounding box cache from the geometry.",
    ),
    (
        "PostGIS_Extensions_Upgrade",
        None,
        "Packages and upgrades postgis extensions (e.g. postgis_raster, postgis_topology, postgis_sfcgal) to latest available version.",
    ),
    (
        "PostGIS_Full_Version",
        None,
        "Reports full postgis version and build configuration infos.",
    ),
    (
        "PostGIS_GEOS_Version",
        None,
        "Returns the version number of the GEOS library.",
    ),
    (
        "PostGIS_HasBBox",
        None,
        "Returns TRUE if the bbox of this geometry is cached, FALSE otherwise.",
    ),
    (
        "PostGIS_LibXML_Version",
        None,
        "Returns the version number of the libxml2 library.",
    ),
    (
        "PostGIS_Lib_Build_Date",
        None,
        "Returns build date of the PostGIS library.",
    ),
    (
        "PostGIS_Lib_Version",
        None,
        "Returns the version number of the PostGIS library.",
    ),
    (
        "PostGIS_Liblwgeom_Version",
        None,
        "Returns the version number of the liblwgeom library. This should match the version of PostGIS.",
    ),
    (
        "PostGIS_PROJ_Version",
        None,
        "Returns the version number of the PROJ4 library.",
    ),
    (
        "PostGIS_Scripts_Build_Date",
        None,
        "Returns build date of the PostGIS scripts.",
    ),
    (
        "PostGIS_Scripts_Installed",
        None,
        "Returns version of the postgis scripts installed in this database.",
    ),
    (
        "PostGIS_Scripts_Released",
        None,
        "Returns the version number of the postgis.sql script released with the installed postgis lib.",
    ),
    (
        "PostGIS_Version",
        None,
        "Returns PostGIS version number and compile-time options.",
    ),
    (
        "PostGIS_Wagyu_Version",
        None,
        "Returns the version number of the internal Wagyu library.",
    ),
    (
        "ST_3DArea",
        None,
        "Computes area of 3D surface geometries. Will return 0 for solids.",
    ),
    (
        "ST_3DClosestPoint",
        types.Geometry,
        "Returns the 3D point on g1 that is closest to g2. This is the first point of the 3D shortest line.",
    ),
    (
        "ST_3DConvexHull",
        types.Geometry,
        "Creates a 3-D Convex Hull from a given geometry.",
    ),
    (
        "ST_3DDFullyWithin",
        None,
        "Returns true if all of the 3D geometries are within the specified distance of one another.",
    ),
    (
        "ST_3DDWithin",
        None,
        "For 3d (z) geometry type Returns true if two geometries 3d distance is within number of units.",
    ),
    (
        "ST_3DDifference",
        types.Geometry,
        "Perform 3D difference",
    ),
    (
        "ST_3DDistance",
        None,
        "Returns the 3D cartesian minimum distance (based on spatial ref) between two geometries in projected units.",
    ),
    (
        "ST_3DExtent",
        None,
        "an aggregate function that returns the 3D bounding box that bounds rows of geometries.",
    ),
    (
        "ST_3DIntersection",
        types.Geometry,
        "Perform 3D intersection",
    ),
    (
        "ST_3DIntersects",
        None,
        'Returns TRUE if the Geometries "spatially intersect" in 3D - only for points, linestrings, polygons, polyhedral surface (area).',
    ),
    (
        "ST_3DLength",
        None,
        "Returns the 3D length of a linear geometry.",
    ),
    (
        "ST_3DLineInterpolatePoint",
        types.Geometry,
        "Returns a point interpolated along a line in 3D. Second argument is a float8 between 0 and 1 representing fraction of total length of linestring the point has to be located.",
    ),
    (
        "ST_3DLongestLine",
        types.Geometry,
        "Returns the 3D longest line between two geometries",
    ),
    (
        "ST_3DMakeBox",
        None,
        "Creates a BOX3D defined by two 3D point geometries.",
    ),
    (
        "ST_3DMaxDistance",
        None,
        "Returns the 3D cartesian maximum distance (based on spatial ref) between two geometries in projected units.",
    ),
    (
        "ST_3DPerimeter",
        None,
        "Returns the 3D perimeter of a polygonal geometry.",
    ),
    (
        "ST_3DShortestLine",
        types.Geometry,
        "Returns the 3D shortest line between two geometries",
    ),
    (
        "ST_3DUnion",
        types.Geometry,
        "Perform 3D union",
    ),
    (
        "ST_AddMeasure",
        types.Geometry,
        "Return a derived geometry with measure elements linearly interpolated between the start and end points.",
    ),
    (
        "ST_AddPoint",
        types.Geometry,
        "Add a point to a LineString.",
    ),
    (
        "ST_Affine",
        types.Geometry,
        "Apply a 3D affine transformation to a geometry.",
    ),
    (
        "ST_AlphaShape",
        types.Geometry,
        "Creates a reconstruction of a shape from a dense unorganized set of data points.",
    ),
    (
        "ST_Angle",
        None,
        "Returns the angle between 3 points, or between 2 vectors (4 points or 2 lines).",
    ),
    (
        "ST_ApproximateMedialAxis",
        types.Geometry,
        "Compute the approximate medial axis of an areal geometry.",
    ),
    (
        "ST_Area",
        None,
        "Returns the area of a polygonal geometry.",
    ),
    (
        "ST_AsBinary",
        None,
        "[gometry] Return the Well-Known Binary (WKB) representation of the geometry/geography without SRID meta data.\nOR\n[raster] Return the Well-Known Binary (WKB) representation of the raster.",
    ),
    (
        "ST_AsEWKB",
        None,
        "Return the Well-Known Binary (WKB) representation of the geometry with SRID meta data.",
    ),
    (
        "ST_AsEWKT",
        None,
        "Return the Well-Known Text (WKT) representation of the geometry with SRID meta data.",
    ),
    (
        "ST_AsEncodedPolyline",
        None,
        "Returns an Encoded Polyline from a LineString geometry.",
    ),
    (
        "ST_AsGML",
        None,
        "Return the geometry as a GML version 2 or 3 element.",
    ),
    (
        "ST_AsGeobuf",
        None,
        "Return a Geobuf representation of a set of rows.",
    ),
    (
        "ST_AsHEXEWKB",
        None,
        "Returns a Geometry in HEXEWKB format (as text) using either little-endian (NDR) or big-endian (XDR) encoding.",
    ),
    (
        "ST_AsKML",
        None,
        "Return the geometry as a KML element. Several variants. Default version=2, default maxdecimaldigits=15",
    ),
    (
        "ST_AsLatLonText",
        None,
        "Return the Degrees, Minutes, Seconds representation of the given point.",
    ),
    (
        "ST_AsMVT",
        None,
        "Aggregate function returning a Mapbox Vector Tile representation of a set of rows.",
    ),
    (
        "ST_AsMVTGeom",
        types.Geometry,
        "Transform a geometry into the coordinate space of a Mapbox Vector Tile.",
    ),
    (
        "ST_AsRaster",
        types.Raster,
        ("Converts a PostGIS geometry to a PostGIS raster.", "RT_ST_AsRaster"),
    ),
    (
        "ST_AsSVG",
        None,
        "Returns SVG path data for a geometry.",
    ),
    (
        "ST_AsTWKB",
        None,
        'Returns the geometry as TWKB, aka "Tiny Well-Known Binary"',
    ),
    (
        "ST_AsText",
        None,
        "Return the Well-Known Text (WKT) representation of the geometry/geography without SRID metadata.",
    ),
    (
        "ST_AsX3D",
        None,
        "Returns a Geometry in X3D xml node element format: ISO-IEC-19776-1.2-X3DEncodings-XML",
    ),
    (
        "ST_Azimuth",
        None,
        "Returns the north-based azimuth as the angle in radians measured clockwise from the vertical on pointA to pointB.",
    ),
    (
        "ST_BdMPolyFromText",
        types.Geometry,
        "Construct a MultiPolygon given an arbitrary collection of closed linestrings as a MultiLineString text representation Well-Known text representation.",
    ),
    (
        "ST_BdPolyFromText",
        types.Geometry,
        "Construct a Polygon given an arbitrary collection of closed linestrings as a MultiLineString Well-Known text representation.",
    ),
    (
        "ST_Boundary",
        types.Geometry,
        "Returns the boundary of a geometry.",
    ),
    (
        "ST_BoundingDiagonal",
        types.Geometry,
        "Returns the diagonal of a geometry's bounding box.",
    ),
    (
        "ST_Box2dFromGeoHash",
        None,
        "Return a BOX2D from a GeoHash string.",
    ),
    (
        "ST_Buffer",
        types.Geometry,
        "(T) Returns a geometry covering all points within a given distance from the input geometry.",
    ),
    (
        "ST_BuildArea",
        types.Geometry,
        "Creates an areal geometry formed by the constituent linework of given geometry",
    ),
    (
        "ST_CPAWithin",
        None,
        "Returns true if the closest point of approach of two trajectories is within the specified distance.",
    ),
    (
        "ST_Centroid",
        types.Geometry,
        "Returns the geometric center of a geometry.",
    ),
    (
        "ST_ChaikinSmoothing",
        types.Geometry,
        'Returns a "smoothed" version of the given geometry using the Chaikin algorithm',
    ),
    (
        "ST_Clip",
        types.Raster,
        (
            "Returns the raster clipped by the input geometry. If band number not is specified, all bands are processed. If crop is not specified or TRUE, the output raster is cropped.",
            "RT_ST_Clip",
        ),
    ),
    (
        "ST_ClipByBox2D",
        types.Geometry,
        "Returns the portion of a geometry falling within a rectangle.",
    ),
    (
        "ST_ClosestPoint",
        types.Geometry,
        "Returns the 2D point on g1 that is closest to g2. This is the first point of the shortest line.",
    ),
    (
        "ST_ClosestPointOfApproach",
        None,
        "Returns the measure at which points interpolated along two trajectories are closest.",
    ),
    (
        "ST_ClusterDBSCAN",
        None,
        "Window function that returns a cluster id for each input geometry using the DBSCAN algorithm.",
    ),
    (
        "ST_ClusterIntersecting",
        types.Geometry,
        "Aggregate function that clusters the input geometries into connected sets.",
    ),
    (
        "ST_ClusterKMeans",
        None,
        "Window function that returns a cluster id for each input geometry using the K-means algorithm.",
    ),
    (
        "ST_ClusterWithin",
        types.Geometry,
        "Aggregate function that clusters the input geometries by separation distance.",
    ),
    (
        "ST_Collect",
        types.Geometry,
        "Creates a GeometryCollection or Multi* geometry from a set of geometries.",
    ),
    (
        "ST_CollectionExtract",
        types.Geometry,
        "Given a (multi)geometry, return a (multi)geometry consisting only of elements of the specified type.",
    ),
    (
        "ST_CollectionHomogenize",
        types.Geometry,
        'Given a geometry collection, return the "simplest" representation of the contents.',
    ),
    (
        "ST_ConcaveHull",
        types.Geometry,
        "The concave hull of a geometry represents a possibly concave geometry that encloses all geometries within the set. You can think of it as shrink wrapping.",
    ),
    (
        "ST_ConstrainedDelaunayTriangles",
        types.Geometry,
        "Return a constrained Delaunay triangulation around the given input geometry.",
    ),
    (
        "ST_Contains",
        None,
        "[geometry] Returns true if and only if no points of B lie in the exterior of A, and at least one point of the interior of B lies in the interior of A.\nOR\n[raster] Return true if no points of raster rastB lie in the exterior of raster rastA and at least one point of the interior of rastB lies in the interior of rastA.",
    ),
    (
        "ST_ContainsProperly",
        None,
        "[geometry] Returns true if B intersects the interior of A but not the boundary (or exterior). A does not contain properly itself, but does contain itself.\nOR\n[raster] Return true if rastB intersects the interior of rastA but not the boundary or exterior of rastA.",
    ),
    (
        "ST_ConvexHull",
        types.Geometry,
        "[geometry] Computes the convex hull of a geometry.\nOR\n[raster] Return the convex hull geometry of the raster including pixel values equal to BandNoDataValue. For regular shaped and non-skewed rasters, this gives the same result as ST_Envelope so only useful for irregularly shaped or skewed rasters.",
    ),
    (
        "ST_CoordDim",
        None,
        "Return the coordinate dimension of a geometry.",
    ),
    (
        "ST_CoveredBy",
        None,
        "[geometry] Returns 1 (TRUE) if no point in Geometry/Geography A is outside Geometry/Geography B\nOR\n[raster] Return true if no points of raster rastA lie outside raster rastB.",
    ),
    (
        "ST_Covers",
        None,
        "[geometry] Returns 1 (TRUE) if no point in Geometry B is outside Geometry A\nOR\n[raster] Return true if no points of raster rastB lie outside raster rastA.",
    ),
    (
        "ST_Crosses",
        None,
        "Returns TRUE if the supplied geometries have some, but not all, interior points in common.",
    ),
    (
        "ST_CurveToLine",
        types.Geometry,
        "Converts a CIRCULARSTRING/CURVEPOLYGON/MULTISURFACE to a LINESTRING/POLYGON/MULTIPOLYGON",
    ),
    (
        "ST_DFullyWithin",
        None,
        "[geometry] Returns true if all of the geometries are within the specified distance of one another\nOR\n[raster] Return true if rasters rastA and rastB are fully within the specified distance of each other.",
    ),
    (
        "ST_DWithin",
        None,
        "[geometry] Returns true if the geometries are within the specified distance of one another. For geometry units are in those of spatial reference and for geography units are in meters and measurement is defaulted to use_spheroid=true (measure around spheroid), for faster check, use_spheroid=false to measure along sphere.\nOR\n[raster] Return true if rasters rastA and rastB are within the specified distance of each other.",
    ),
    (
        "ST_DelaunayTriangles",
        types.Geometry,
        "Return a Delaunay triangulation around the given input points.",
    ),
    (
        "ST_Difference",
        types.Geometry,
        "Returns a geometry that represents that part of geometry A that does not intersect with geometry B.",
    ),
    (
        "ST_Dimension",
        None,
        "Returns the topological dimension of a geometry.",
    ),
    (
        "ST_Disjoint",
        None,
        '[geometry] Returns TRUE if the Geometries do not "spatially intersect" - if they do not share any space together.\nOR\n[raster] Return true if raster rastA does not spatially intersect rastB.',
    ),
    (
        "ST_Distance",
        None,
        "Returns the distance between two geometry or geography values.",
    ),
    (
        "ST_DistanceCPA",
        None,
        "Returns the distance between the closest point of approach of two trajectories.",
    ),
    (
        "ST_DistanceSphere",
        None,
        "Returns minimum distance in meters between two lon/lat geometries using a spherical earth model.",
    ),
    (
        "ST_DistanceSpheroid",
        None,
        "Returns the minimum distance between two lon/lat geometries using a spheroidal earth model.",
    ),
    (
        "ST_Dump",
        types.GeometryDump,
        "Returns a set of geometry_dump rows for the components of a geometry.",
    ),
    (
        "ST_DumpPoints",
        types.GeometryDump,
        "Returns a set of geometry_dump rows for the points in a geometry.",
    ),
    (
        "ST_DumpRings",
        types.GeometryDump,
        "Returns a set of geometry_dump rows for the exterior and interior rings of a Polygon.",
    ),
    (
        "ST_DumpSegments",
        types.GeometryDump,
        "A set-returning function (SRF) that extracts the segments of a geometry. It returns a set of geometry_dump rows, each containing a geometry (geom field) and an array of integers (path field).",
    ),
    (
        "ST_EndPoint",
        types.Geometry,
        "Returns the last point of a LineString or CircularLineString.",
    ),
    (
        "ST_Envelope",
        types.Geometry,
        "[geometry] Returns a geometry representing the bounding box of a geometry.\nOR\n[raster] Returns the polygon representation of the extent of the raster.",
    ),
    (
        "ST_Equals",
        None,
        "Returns true if the given geometries represent the same geometry. Directionality is ignored.",
    ),
    (
        "ST_EstimatedExtent",
        None,
        "Return the 'estimated' extent of a spatial table.",
    ),
    (
        "ST_Expand",
        types.Geometry,
        "Returns a bounding box expanded from another bounding box or a geometry.",
    ),
    (
        "ST_Extent",
        None,
        "an aggregate function that returns the bounding box that bounds rows of geometries.",
    ),
    (
        "ST_ExteriorRing",
        types.Geometry,
        "Returns a LineString representing the exterior ring of a Polygon.",
    ),
    (
        "ST_Extrude",
        types.Geometry,
        "Extrude a surface to a related volume",
    ),
    (
        "ST_FilterByM",
        types.Geometry,
        "Filters vertex points based on their m-value",
    ),
    (
        "ST_FlipCoordinates",
        types.Geometry,
        "Returns a version of the given geometry with X and Y axis flipped. Useful for people who have built latitude/longitude features and need to fix them.",
    ),
    (
        "ST_Force2D",
        types.Geometry,
        'Force the geometries into a "2-dimensional mode".',
    ),
    (
        "ST_Force3D",
        types.Geometry,
        "Force the geometries into XYZ mode. This is an alias for ST_Force3DZ.",
    ),
    (
        "ST_Force3DM",
        types.Geometry,
        "Force the geometries into XYM mode.",
    ),
    (
        "ST_Force3DZ",
        types.Geometry,
        "Force the geometries into XYZ mode.",
    ),
    (
        "ST_Force4D",
        types.Geometry,
        "Force the geometries into XYZM mode.",
    ),
    (
        "ST_ForceCollection",
        types.Geometry,
        "Convert the geometry into a GEOMETRYCOLLECTION.",
    ),
    (
        "ST_ForceCurve",
        types.Geometry,
        "Upcast a geometry into its curved type, if applicable.",
    ),
    (
        "ST_ForceLHR",
        types.Geometry,
        "Force LHR orientation",
    ),
    (
        "ST_ForcePolygonCCW",
        types.Geometry,
        "Orients all exterior rings counter-clockwise and all interior rings clockwise.",
    ),
    (
        "ST_ForcePolygonCW",
        types.Geometry,
        "Orients all exterior rings clockwise and all interior rings counter-clockwise.",
    ),
    (
        "ST_ForceRHR",
        types.Geometry,
        "Force the orientation of the vertices in a polygon to follow the Right-Hand-Rule.",
    ),
    (
        "ST_ForceSFS",
        types.Geometry,
        "Force the geometries to use SFS 1.1 geometry types only.",
    ),
    (
        "ST_FrechetDistance",
        None,
        "Returns the Fréchet distance between two geometries.",
    ),
    (
        "ST_GMLToSQL",
        types.Geometry,
        "Return a specified ST_Geometry value from GML representation. This is an alias name for ST_GeomFromGML",
    ),
    (
        "ST_GeneratePoints",
        types.Geometry,
        "Converts a polygon or multi-polygon into a multi-point composed of randomly location points within the original areas.",
    ),
    (
        "ST_GeoHash",
        None,
        "Return a GeoHash representation of the geometry.",
    ),
    (
        "ST_GeogFromText",
        types.Geography,
        "Return a specified geography value from Well-Known Text representation or extended (WKT).",
    ),
    (
        "ST_GeogFromWKB",
        types.Geography,
        "Creates a geography instance from a Well-Known Binary geometry representation (WKB) or extended Well Known Binary (EWKB).",
    ),
    (
        "ST_GeographyFromText",
        types.Geography,
        "Return a specified geography value from Well-Known Text representation or extended (WKT).",
    ),
    (
        "ST_GeomCollFromText",
        types.Geometry,
        "Makes a collection Geometry from collection WKT with the given SRID. If SRID is not given, it defaults to 0.",
    ),
    (
        "ST_GeomFromEWKB",
        types.Geometry,
        "Return a specified ST_Geometry value from Extended Well-Known Binary representation (EWKB).",
    ),
    (
        "ST_GeomFromEWKT",
        types.Geometry,
        "Return a specified ST_Geometry value from Extended Well-Known Text representation (EWKT).",
    ),
    (
        "ST_GeomFromGML",
        types.Geometry,
        "Takes as input GML representation of geometry and outputs a PostGIS geometry object",
    ),
    (
        "ST_GeomFromGeoHash",
        types.Geometry,
        "Return a geometry from a GeoHash string.",
    ),
    (
        "ST_GeomFromGeoJSON",
        types.Geometry,
        "Takes as input a geojson representation of a geometry and outputs a PostGIS geometry object",
    ),
    (
        "ST_GeomFromKML",
        types.Geometry,
        "Takes as input KML representation of geometry and outputs a PostGIS geometry object",
    ),
    (
        "ST_GeomFromTWKB",
        types.Geometry,
        'Creates a geometry instance from a TWKB ("Tiny Well-Known Binary") geometry representation.',
    ),
    (
        "ST_GeomFromText",
        types.Geometry,
        "Return a specified ST_Geometry value from Well-Known Text representation (WKT).",
    ),
    (
        "ST_GeomFromWKB",
        types.Geometry,
        "Creates a geometry instance from a Well-Known Binary geometry representation (WKB) and optional SRID.",
    ),
    (
        "ST_GeometricMedian",
        types.Geometry,
        "Returns the geometric median of a MultiPoint.",
    ),
    (
        "ST_GeometryFromText",
        types.Geometry,
        "Return a specified ST_Geometry value from Well-Known Text representation (WKT). This is an alias name for ST_GeomFromText",
    ),
    (
        "ST_GeometryN",
        types.Geometry,
        "Return the Nth geometry element of a geometry collection.",
    ),
    (
        "ST_GeometryType",
        None,
        "Returns the SQL-MM type of a geometry as text.",
    ),
    (
        "ST_HasArc",
        None,
        "Tests if a geometry contains a circular arc",
    ),
    (
        "ST_HausdorffDistance",
        None,
        "Returns the Hausdorff distance between two geometries.",
    ),
    (
        "ST_Hexagon",
        types.Geometry,
        "Uses the same hexagon tiling concept as ST_HexagonGrid, but generates just one hexagon at the desired cell coordinate. Optionally, can adjust origin coordinate of the tiling, the default origin is at 0,0.",
    ),
    (
        "ST_HexagonGrid",
        types.GeometryDump,
        "Returns hexagons in a given Tiling(SRS, Size) that overlap with a given bounds.",
    ),
    (
        "ST_InteriorRingN",
        types.Geometry,
        "Returns the Nth interior ring (hole) of a Polygon.",
    ),
    (
        "ST_InterpolatePoint",
        None,
        "Return the value of the measure dimension of a geometry at the point closed to the provided point.",
    ),
    (
        "ST_Intersection",
        types.Geometry,
        "[geometry] (T) Returns a geometry that represents the shared portion of geomA and geomB.\nOR\n[raster] Returns a raster or a set of geometry-pixelvalue pairs representing the shared portion of two rasters or the geometrical intersection of a vectorization of the raster and a geometry.",
    ),
    (
        "ST_Intersects",
        None,
        '[geometry] Returns TRUE if the Geometries/Geography "spatially intersect in 2D" - (share any portion of space) and FALSE if they don\'t (they are Disjoint). For geography tolerance is 0.00001 meters (so any points that close are considered to intersect)\nOR\n[raster] Return true if raster rastA spatially intersects raster rastB.',
    ),
    (
        "ST_IsClosed",
        None,
        "Tests if a LineStrings's start and end points are coincident. For a PolyhedralSurface tests if it is closed (volumetric).",
    ),
    (
        "ST_IsCollection",
        None,
        "Tests if a geometry is a geometry collection type.",
    ),
    (
        "ST_IsEmpty",
        None,
        "[geometry] Tests if a geometry is empty.\nOR\n[raster] Returns true if the raster is empty (width = 0 and height = 0). Otherwise, returns false.",
    ),
    (
        "ST_IsPlanar",
        None,
        "Check if a surface is or not planar",
    ),
    (
        "ST_IsPolygonCCW",
        None,
        "Tests if Polygons have exterior rings oriented counter-clockwise and interior rings oriented clockwise.",
    ),
    (
        "ST_IsPolygonCW",
        None,
        "Tests if Polygons have exterior rings oriented clockwise and interior rings oriented counter-clockwise.",
    ),
    (
        "ST_IsRing",
        None,
        "Tests if a LineString is closed and simple.",
    ),
    (
        "ST_IsSimple",
        None,
        "Tests if a geometry has no points of self-intersection or self-tangency.",
    ),
    (
        "ST_IsSolid",
        None,
        "Test if the geometry is a solid. No validity check is performed.",
    ),
    (
        "ST_IsValid",
        None,
        "Tests if a geometry is well-formed in 2D.",
    ),
    (
        "ST_IsValidDetail",
        None,
        "Returns a valid_detail row stating if a geometry is valid, and if not a reason why and a location.",
    ),
    (
        "ST_IsValidReason",
        None,
        "Returns text stating if a geometry is valid, or a reason for invalidity.",
    ),
    (
        "ST_IsValidTrajectory",
        None,
        "Returns true if the geometry is a valid trajectory.",
    ),
    (
        "ST_Length",
        None,
        "Returns the 2D length of a linear geometry.",
    ),
    (
        "ST_Length2D",
        None,
        "Returns the 2D length of a linear geometry. Alias for ST_Length",
    ),
    (
        "ST_LengthSpheroid",
        None,
        "Returns the 2D or 3D length/perimeter of a lon/lat geometry on a spheroid.",
    ),
    (
        "ST_Letters",
        types.Geometry,
        "Uses a built-in font to render out a string as a multipolygon geometry. The default text height is 100.0, the distance from the bottom of a descender to the top of a capital. The default start position places the start of the baseline at the origin. Over-riding the font involves passing in a json map, with a character as the key, and base64 encoded TWKB for the font shape, with the fonts having a height of 1000 units from the bottom of the descenders to the tops of the capitals.",
    ),
    (
        "ST_LineCrossingDirection",
        None,
        "Given 2 linestrings, returns a number between -3 and 3 denoting what kind of crossing behavior. 0 is no crossing.",
    ),
    (
        "ST_LineFromEncodedPolyline",
        types.Geometry,
        "Creates a LineString from an Encoded Polyline.",
    ),
    (
        "ST_LineFromMultiPoint",
        types.Geometry,
        "Creates a LineString from a MultiPoint geometry.",
    ),
    (
        "ST_LineFromText",
        types.Geometry,
        "Makes a Geometry from WKT representation with the given SRID. If SRID is not given, it defaults to 0.",
    ),
    (
        "ST_LineFromWKB",
        types.Geometry,
        "Makes a LINESTRING from WKB with the given SRID",
    ),
    (
        "ST_LineInterpolatePoint",
        types.Geometry,
        "Returns a point interpolated along a line. Second argument is a float8 between 0 and 1 representing fraction of total length of linestring the point has to be located.",
    ),
    (
        "ST_LineInterpolatePoints",
        types.Geometry,
        "Returns one or more points interpolated along a line.",
    ),
    (
        "ST_LineLocatePoint",
        None,
        "Returns a float between 0 and 1 representing the location of the closest point on LineString to the given Point, as a fraction of total 2d line length.",
    ),
    (
        "ST_LineMerge",
        types.Geometry,
        "Return a (set of) LineString(s) formed by sewing together a MULTILINESTRING.",
    ),
    (
        "ST_LineSubstring",
        types.Geometry,
        "Return a linestring being a substring of the input one starting and ending at the given fractions of total 2d length. Second and third arguments are float8 values between 0 and 1.",
    ),
    (
        "ST_LineToCurve",
        types.Geometry,
        "Converts a LINESTRING/POLYGON to a CIRCULARSTRING, CURVEPOLYGON",
    ),
    (
        "ST_LinestringFromWKB",
        types.Geometry,
        "Makes a geometry from WKB with the given SRID.",
    ),
    (
        "ST_LocateAlong",
        types.Geometry,
        "Return a derived geometry collection value with elements that match the specified measure. Polygonal elements are not supported.",
    ),
    (
        "ST_LocateBetween",
        types.Geometry,
        "Return a derived geometry collection value with elements that match the specified range of measures inclusively.",
    ),
    (
        "ST_LocateBetweenElevations",
        types.Geometry,
        "Return a derived geometry (collection) value with elements that intersect the specified range of elevations inclusively.",
    ),
    (
        "ST_LongestLine",
        types.Geometry,
        "Returns the 2D longest line between two geometries.",
    ),
    (
        "ST_M",
        None,
        "Returns the M coordinate of a Point.",
    ),
    (
        "ST_MLineFromText",
        types.Geometry,
        "Return a specified ST_MultiLineString value from WKT representation.",
    ),
    (
        "ST_MPointFromText",
        types.Geometry,
        "Makes a Geometry from WKT with the given SRID. If SRID is not given, it defaults to 0.",
    ),
    (
        "ST_MPolyFromText",
        types.Geometry,
        "Makes a MultiPolygon Geometry from WKT with the given SRID. If SRID is not given, it defaults to 0.",
    ),
    (
        "ST_MakeBox2D",
        None,
        "Creates a BOX2D defined by two 2D point geometries.",
    ),
    (
        "ST_MakeEnvelope",
        types.Geometry,
        "Creates a rectangular Polygon from minimum and maximum coordinates.",
    ),
    (
        "ST_MakeLine",
        types.Geometry,
        "Creates a Linestring from Point, MultiPoint, or LineString geometries.",
    ),
    (
        "ST_MakePoint",
        types.Geometry,
        "Creates a 2D, 3DZ or 4D Point.",
    ),
    (
        "ST_MakePointM",
        types.Geometry,
        "Creates a Point from X, Y and M values.",
    ),
    (
        "ST_MakePolygon",
        types.Geometry,
        "Creates a Polygon from a shell and optional list of holes.",
    ),
    (
        "ST_MakeSolid",
        types.Geometry,
        "Cast the geometry into a solid. No check is performed. To obtain a valid solid, the input geometry must be a closed Polyhedral Surface or a closed TIN.",
    ),
    (
        "ST_MakeValid",
        types.Geometry,
        "Attempts to make an invalid geometry valid without losing vertices.",
    ),
    (
        "ST_MaxDistance",
        None,
        "Returns the 2D largest distance between two geometries in projected units.",
    ),
    (
        "ST_MaximumInscribedCircle",
        types.Geometry,
        "Finds the largest circle that is contained within a (multi)polygon, or which does not overlap any lines and points.",
    ),
    (
        "ST_MemSize",
        None,
        "[geometry] Returns the amount of memory space a geometry takes.\nOR\n[raster] Returns the amount of space (in bytes) the raster takes.",
    ),
    (
        "ST_MemUnion",
        types.Geometry,
        "Same as ST_Union, only memory-friendly (uses less memory and more processor time).",
    ),
    (
        "ST_MinConvexHull",
        types.Geometry,
        (
            "Return the convex hull geometry of the raster excluding NODATA pixels.",
            "RT_ST_MinConvexHull",
        ),
    ),
    (
        "ST_MinPossibleValue",
        None,
        "Returns the minimum value this pixeltype can store.",
    ),
    (
        "ST_MinimumBoundingCircle",
        types.Geometry,
        "Returns the smallest circle polygon that can fully contain a geometry. Default uses 48 segments per quarter circle.",
    ),
    (
        "ST_MinimumBoundingRadius",
        None,
        "Returns the center point and radius of the smallest circle that can fully contain a geometry.",
    ),
    (
        "ST_MinimumClearance",
        None,
        "Returns the minimum clearance of a geometry, a measure of a geometry's robustness.",
    ),
    (
        "ST_MinimumClearanceLine",
        types.Geometry,
        "Returns the two-point LineString spanning a geometry's minimum clearance.",
    ),
    (
        "ST_MinkowskiSum",
        types.Geometry,
        "Performs Minkowski sum",
    ),
    (
        "ST_Multi",
        types.Geometry,
        "Return the geometry as a MULTI* geometry.",
    ),
    (
        "ST_NDims",
        None,
        "Returns the coordinate dimension of a geometry.",
    ),
    (
        "ST_NPoints",
        None,
        "Returns the number of points (vertices) in a geometry.",
    ),
    (
        "ST_NRings",
        None,
        "Returns the number of rings in a polygonal geometry.",
    ),
    (
        "ST_Node",
        types.Geometry,
        "Node a set of linestrings.",
    ),
    (
        "ST_Normalize",
        types.Geometry,
        "Return the geometry in its canonical form.",
    ),
    (
        "ST_NumGeometries",
        None,
        "Returns the number of elements in a geometry collection.",
    ),
    (
        "ST_NumInteriorRing",
        None,
        "Returns the number of interior rings (holes) of a Polygon. Aias for ST_NumInteriorRings",
    ),
    (
        "ST_NumInteriorRings",
        None,
        "Returns the number of interior rings (holes) of a Polygon.",
    ),
    (
        "ST_NumPatches",
        None,
        "Return the number of faces on a Polyhedral Surface. Will return null for non-polyhedral geometries.",
    ),
    (
        "ST_NumPoints",
        None,
        "Returns the number of points in a LineString or CircularString.",
    ),
    (
        "ST_OffsetCurve",
        types.Geometry,
        "Return an offset line at a given distance and side from an input line. Useful for computing parallel lines about a center line",
    ),
    (
        "ST_OptimalAlphaShape",
        types.Geometry,
        'Computes the "optimal" alpha-shapes of the set of geometry. CGAL can automatically find the optimal value of alpha. This version uses it to find an "optimal" alpha-shape. The result is a single polygon. It will not contain holes unless the optional param_allow_holes argument is specified as true. The result will be generated such that the number of solid component of the alpha shape is equal to or smaller than param_nb_components.',
    ),
    (
        "ST_OrderingEquals",
        None,
        "Returns true if the given geometries represent the same geometry and points are in the same directional order.",
    ),
    (
        "ST_Orientation",
        None,
        "Determine surface orientation",
    ),
    (
        "ST_OrientedEnvelope",
        types.Geometry,
        "Returns a minimum rotated rectangle enclosing a geometry.",
    ),
    (
        "ST_Overlaps",
        None,
        "[geometry] Returns TRUE if the Geometries share space, are of the same dimension, but are not completely contained by each other.\nOR\n[raster] Return true if raster rastA and rastB intersect but one does not completely contain the other.",
    ),
    (
        "ST_PatchN",
        types.Geometry,
        "Returns the Nth geometry (face) of a PolyhedralSurface.",
    ),
    (
        "ST_Perimeter",
        None,
        "Returns the length of the boundary of a polygonal geometry or geography.",
    ),
    (
        "ST_Perimeter2D",
        None,
        "Returns the 2D perimeter of a polygonal geometry. Alias for ST_Perimeter.",
    ),
    (
        "ST_PixelAsCentroid",
        types.Geometry,
        (
            "Returns the centroid (point geometry) of the area represented by a pixel.",
            "RT_ST_PixelAsCentroid",
        ),
    ),
    (
        "ST_PixelAsPoint",
        types.Geometry,
        (
            "Returns a point geometry of the pixel's upper-left corner.",
            "RT_ST_PixelAsPoint",
        ),
    ),
    (
        "ST_PixelAsPolygon",
        types.Geometry,
        (
            "Returns the polygon geometry that bounds the pixel for a particular row and column.",
            "RT_ST_PixelAsPolygon",
        ),
    ),
    (
        "ST_Point",
        types.Geometry,
        "Creates a Point with the given coordinate values. Alias for ST_MakePoint.",
    ),
    (
        "ST_PointFromGeoHash",
        types.Geometry,
        "Return a point from a GeoHash string.",
    ),
    (
        "ST_PointFromText",
        types.Geometry,
        "Makes a point Geometry from WKT with the given SRID. If SRID is not given, it defaults to unknown.",
    ),
    (
        "ST_PointFromWKB",
        types.Geometry,
        "Makes a geometry from WKB with the given SRID",
    ),
    (
        "ST_PointInsideCircle",
        None,
        "Is the point geometry inside the circle defined by center_x, center_y, radius",
    ),
    (
        "ST_PointM",
        types.Geometry,
        "Returns an Point with the given X, Y and M coordinate values, and optionally an SRID number.",
    ),
    (
        "ST_PointN",
        types.Geometry,
        "Returns the Nth point in the first LineString or circular LineString in a geometry.",
    ),
    (
        "ST_PointOnSurface",
        types.Geometry,
        "Returns a POINT guaranteed to lie on the surface.",
    ),
    (
        "ST_PointZM",
        types.Geometry,
        "Returns an Point with the given X, Y, Z and M coordinate values, and optionally an SRID number.",
    ),
    (
        "ST_Points",
        types.Geometry,
        "Returns a MultiPoint containing all the coordinates of a geometry.",
    ),
    (
        "ST_Polygon",
        types.Geometry,
        "[geometry] Creates a Polygon from a LineString with a specified SRID.\nOR\n[raster] Returns a multipolygon geometry formed by the union of pixels that have a pixel value that is not no data value. If no band number is specified, band num defaults to 1.",
    ),
    (
        "ST_PolygonFromText",
        types.Geometry,
        "Makes a Geometry from WKT with the given SRID. If SRID is not given, it defaults to 0.",
    ),
    (
        "ST_Polygonize",
        types.Geometry,
        "Aggregate. Creates a GeometryCollection containing possible polygons formed from the constituent linework of a set of geometries.",
    ),
    (
        "ST_Project",
        types.Geography,
        "Returns a point projected from a start point by a distance and bearing (azimuth).",
    ),
    (
        "ST_QuantizeCoordinates",
        types.Geometry,
        "Sets least significant bits of coordinates to zero",
    ),
    (
        "ST_ReducePrecision",
        types.Geometry,
        "Returns a valid geometry with all points rounded to the provided grid tolerance, and features below the tolerance removed. Unlike ST_SnapToGrid the returned geometry will be valid, with no ring self-intersections or collapsed components.",
    ),
    (
        "ST_Relate",
        None,
        "Returns true if this Geometry is spatially related to anotherGeometry, by testing for intersections between the Interior, Boundary and Exterior of the two geometries as specified by the values in the intersectionMatrixPattern. If no intersectionMatrixPattern is passed in, then returns the maximum intersectionMatrixPattern that relates the 2 geometries.",
    ),
    (
        "ST_RelateMatch",
        None,
        "Returns true if intersectionMattrixPattern1 implies intersectionMatrixPattern2",
    ),
    (
        "ST_RemovePoint",
        types.Geometry,
        "Remove point from a linestring.",
    ),
    (
        "ST_RemoveRepeatedPoints",
        types.Geometry,
        "Returns a version of the given geometry with duplicated points removed.",
    ),
    (
        "ST_Reverse",
        types.Geometry,
        "Return the geometry with vertex order reversed.",
    ),
    (
        "ST_Rotate",
        types.Geometry,
        "Rotates a geometry about an origin point.",
    ),
    (
        "ST_RotateX",
        types.Geometry,
        "Rotates a geometry about the X axis.",
    ),
    (
        "ST_RotateY",
        types.Geometry,
        "Rotates a geometry about the Y axis.",
    ),
    (
        "ST_RotateZ",
        types.Geometry,
        "Rotates a geometry about the Z axis.",
    ),
    (
        "ST_SRID",
        None,
        "[geometry] Returns the spatial reference identifier for the ST_Geometry as defined in spatial_ref_sys table.\nOR\n[raster] Returns the spatial reference identifier of the raster as defined in spatial_ref_sys table.",
    ),
    (
        "ST_Scale",
        types.Geometry,
        "Scales a geometry by given factors.",
    ),
    (
        "ST_Scroll",
        types.Geometry,
        "Changes the start/end point of a closed LineString to the given vertex point.",
    ),
    (
        "ST_Segmentize",
        types.Geometry,
        "Return a modified geometry/geography having no segment longer than the given distance.",
    ),
    (
        "ST_SetEffectiveArea",
        types.Geometry,
        "Sets the effective area for each vertex, storing the value in the M ordinate. A simplified geometry can then be generated by filtering on the M ordinate.",
    ),
    (
        "ST_SetPoint",
        types.Geometry,
        "Replace point of a linestring with a given point.",
    ),
    (
        "ST_SetSRID",
        types.Geometry,
        "[geometry] Set the SRID on a geometry to a particular integer value.\nOR\n[raster] Sets the SRID of a raster to a particular integer srid defined in the spatial_ref_sys table.",
    ),
    (
        "ST_SharedPaths",
        types.Geometry,
        "Returns a collection containing paths shared by the two input linestrings/multilinestrings.",
    ),
    (
        "ST_ShiftLongitude",
        types.Geometry,
        "Toggle geometry coordinates between -180..180 and 0..360 ranges.",
    ),
    (
        "ST_ShortestLine",
        types.Geometry,
        "Returns the 2D shortest line between two geometries",
    ),
    (
        "ST_Simplify",
        types.Geometry,
        'Returns a "simplified" version of the given geometry using the Douglas-Peucker algorithm.',
    ),
    (
        "ST_SimplifyPolygonHull",
        types.Geometry,
        "Computes a simplified topology-preserving outer or inner hull of a polygonal geometry. An outer hull completely covers the input geometry. An inner hull is completely covered by the input geometry. The result is a polygonal geometry formed by a subset of the input vertices. MultiPolygons and holes are handled and produce a result with the same structure as the input.",
    ),
    (
        "ST_SimplifyPreserveTopology",
        types.Geometry,
        'Returns a "simplified" version of the given geometry using the Douglas-Peucker algorithm. Will avoid creating derived geometries (polygons in particular) that are invalid.',
    ),
    (
        "ST_SimplifyVW",
        types.Geometry,
        'Returns a "simplified" version of the given geometry using the Visvalingam-Whyatt algorithm',
    ),
    (
        "ST_Snap",
        types.Geometry,
        "Snap segments and vertices of input geometry to vertices of a reference geometry.",
    ),
    (
        "ST_SnapToGrid",
        types.Geometry,
        "[geometry] Snap all points of the input geometry to a regular grid.\nOR\n[raster] Resample a raster by snapping it to a grid. New pixel values are computed using the NearestNeighbor (english or american spelling), Bilinear, Cubic, CubicSpline or Lanczos resampling algorithm. Default is NearestNeighbor.",
    ),
    (
        "ST_Split",
        types.Geometry,
        "Returns a collection of geometries resulting by splitting a geometry.",
    ),
    (
        "ST_Square",
        types.Geometry,
        "Uses the same square tiling concept as ST_SquareGrid, but generates just one square at the desired cell coordinate. Optionally, can adjust origin coordinate of the tiling, the default origin is at 0,0.",
    ),
    (
        "ST_SquareGrid",
        types.GeometryDump,
        "Starts with the concept of a square tiling of the plane. For a given planar SRS, and a given edge size, starting at the origin of the SRS, there is one unique square tiling of the plane, Tiling(SRS, Size). This function answers the question: what grids in a given Tiling(SRS, Size) overlap with a given bounds.",
    ),
    (
        "ST_StartPoint",
        types.Geometry,
        "Returns the first point of a LineString.",
    ),
    (
        "ST_StraightSkeleton",
        types.Geometry,
        "Compute a straight skeleton from a geometry",
    ),
    (
        "ST_Subdivide",
        types.Geometry,
        "Returns a set of geometry where no geometry in the set has more than the specified number of vertices.",
    ),
    (
        "ST_Summary",
        None,
        "[geometry] Returns a text summary of the contents of a geometry.\nOR\n[raster] Returns a text summary of the contents of the raster.",
    ),
    (
        "ST_SummaryStatsAgg",
        types.SummaryStats,
        (
            "Aggregate. Returns summarystats consisting of count, sum, mean, stddev, min, max for a given raster band of a set of raster. Band 1 is assumed is no band is specified.",
            "RT_ST_SummaryStatsAgg",
        ),
    ),
    (
        "ST_SwapOrdinates",
        types.Geometry,
        "Returns a version of the given geometry with given ordinate values swapped.",
    ),
    (
        "ST_SymDifference",
        types.Geometry,
        "Returns a geometry that represents the portions of A and B that do not intersect. It is called a symmetric difference because ST_SymDifference(A,B) = ST_SymDifference(B,A).",
    ),
    (
        "ST_Tesselate",
        types.Geometry,
        "Perform surface Tessellation of a polygon or polyhedralsurface and returns as a TIN or collection of TINS",
    ),
    (
        "ST_TileEnvelope",
        types.Geometry,
        "Creates a rectangular Polygon in Web Mercator (SRID:3857) using the XYZ tile system.",
    ),
    (
        "ST_Touches",
        None,
        "[geometry] Returns TRUE if the geometries have at least one point in common, but their interiors do not intersect.\nOR\n[raster] Return true if raster rastA and rastB have at least one point in common but their interiors do not intersect.",
    ),
    (
        "ST_TransScale",
        types.Geometry,
        "Translates and scales a geometry by given offsets and factors.",
    ),
    (
        "ST_Transform",
        types.Geometry,
        "[geometry] Return a new geometry with its coordinates transformed to a different spatial reference system.\nOR\n[raster] Reprojects a raster in a known spatial reference system to another known spatial reference system using specified resampling algorithm. Options are NearestNeighbor, Bilinear, Cubic, CubicSpline, Lanczos defaulting to NearestNeighbor.",
    ),
    (
        "ST_Translate",
        types.Geometry,
        "Translates a geometry by given offsets.",
    ),
    (
        "ST_TriangulatePolygon",
        types.Geometry,
        'Computes the constrained Delaunay triangulation of polygons. Holes and Multipolygons are supported. The "constrained Delaunay triangulation" of a polygon is a set of triangles formed from the vertices of the polygon, and covering it exactly, with the maximum total interior angle over all possible triangulations. It provides the "best quality" triangulation of the polygon.',
    ),
    (
        "ST_UnaryUnion",
        types.Geometry,
        "Like ST_Union, but working at the geometry component level.",
    ),
    (
        "ST_Union",
        types.Geometry,
        "[geometry] Returns a geometry that represents the point set union of the Geometries.\nOR\n[raster] Returns the union of a set of raster tiles into a single raster composed of 1 or more bands.",
    ),
    (
        "ST_Volume",
        None,
        "Computes the volume of a 3D solid. If applied to surface (even closed) geometries will return 0.",
    ),
    (
        "ST_VoronoiLines",
        types.Geometry,
        "Returns the boundaries between the cells of the Voronoi diagram constructed from the vertices of a geometry.",
    ),
    (
        "ST_VoronoiPolygons",
        types.Geometry,
        "Returns the cells of the Voronoi diagram constructed from the vertices of a geometry.",
    ),
    (
        "ST_WKBToSQL",
        types.Geometry,
        "Return a specified ST_Geometry value from Well-Known Binary representation (WKB). This is an alias name for ST_GeomFromWKB that takes no srid",
    ),
    (
        "ST_WKTToSQL",
        types.Geometry,
        "Return a specified ST_Geometry value from Well-Known Text representation (WKT). This is an alias name for ST_GeomFromText",
    ),
    (
        "ST_Within",
        None,
        "[geometry] Returns true if the geometry A is completely inside geometry B\nOR\n[raster] Return true if no points of raster rastA lie in the exterior of raster rastB and at least one point of the interior of rastA lies in the interior of rastB.",
    ),
    (
        "ST_WorldToRasterCoordX",
        None,
        (
            "Returns the column in the raster of the point geometry (pt) or a X and Y world coordinate (xw, yw) represented in world spatial reference system of raster.",
            "RT_ST_WorldToRasterCoordX",
        ),
    ),
    (
        "ST_WorldToRasterCoordY",
        None,
        (
            "Returns the row in the raster of the point geometry (pt) or a X and Y world coordinate (xw, yw) represented in world spatial reference system of raster.",
            "RT_ST_WorldToRasterCoordY",
        ),
    ),
    (
        "ST_WrapX",
        types.Geometry,
        "Wrap a geometry around an X value.",
    ),
    (
        "ST_X",
        None,
        "Returns the X coordinate of a Point.",
    ),
    (
        "ST_XMax",
        None,
        "Returns the X maxima of a 2D or 3D bounding box or a geometry.",
    ),
    (
        "ST_XMin",
        None,
        "Returns the X minima of a 2D or 3D bounding box or a geometry.",
    ),
    (
        "ST_Y",
        None,
        "Returns the Y coordinate of a Point.",
    ),
    (
        "ST_YMax",
        None,
        "Returns the Y maxima of a 2D or 3D bounding box or a geometry.",
    ),
    (
        "ST_YMin",
        None,
        "Returns the Y minima of a 2D or 3D bounding box or a geometry.",
    ),
    (
        "ST_Z",
        None,
        "Returns the Z coordinate of a Point.",
    ),
    (
        "ST_ZMax",
        None,
        "Returns the Z maxima of a 2D or 3D bounding box or a geometry.",
    ),
    (
        "ST_ZMin",
        None,
        "Returns the Z minima of a 2D or 3D bounding box or a geometry.",
    ),
    (
        "ST_Zmflag",
        None,
        "Returns a code indicating the ZM coordinate dimension of a geometry.",
    ),
    (
        "UnlockRows",
        None,
        "Removes all locks held by an authorization token.",
    ),
    (
        "UpdateGeometrySRID",
        None,
        "Updates the SRID of all features in a geometry column, and the table metadata.",
    ),
    (
        "postgis_sfcgal_version",
        None,
        "Returns the version of SFCGAL in use",
    ),
]
