# -*- coding: utf-8 -*-
# flake8: noqa
from geoalchemy2 import types

_FUNCTIONS = [
    (
        "Box3D",
        None,
        (
            """Returns the box 3d representation of the enclosing box of the raster.""",
            "RT_Box3D",
        ),
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
        "ST_AsBinary",
        None,
        (
            """Return the Well-Known Binary (WKB) representation of the raster.""",
            "RT_ST_AsBinary",
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
        "ST_AsHexWKB",
        None,
        (
            """Return the Well-Known Binary (WKB) in Hex representation of the raster.""",
            "RT_ST_AsHexWKB",
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
        "ST_AsRaster",
        types.Raster,
        ("""Converts a PostGIS geometry to a PostGIS raster.""", "RT_ST_AsRaster"),
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
        "ST_AsWKB",
        None,
        (
            """Return the Well-Known Binary (WKB) representation of the raster.""",
            "RT_ST_AsWKB",
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
        "ST_Band",
        types.Raster,
        (
            """Returns one or more bands of an existing raster as a new raster. Useful for building new rasters from existing rasters.""",
            "RT_ST_Band",
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
        "ST_BandIsNoData",
        None,
        (
            """Returns true if the band is filled with only nodata values.""",
            "RT_ST_BandIsNoData",
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
        "ST_BandPath",
        None,
        (
            """Returns system file path to a band stored in file system. If no bandnum specified, 1 is assumed.""",
            "RT_ST_BandPath",
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
        "ST_Contains",
        None,
        (
            """Return true if no points of raster rastB lie in the exterior of raster rastA and at least one point of the interior of rastB lies in the interior of rastA.""",
            "RT_ST_Contains",
        ),
    ),
    (
        "ST_ContainsProperly",
        None,
        (
            """Return true if rastB intersects the interior of rastA but not the boundary or exterior of rastA.""",
            "RT_ST_ContainsProperly",
        ),
    ),
    (
        "ST_Contour",
        None,
        (
            """Generates a set of vector contours from the provided raster band, using the GDAL contouring algorithm.""",
            "RT_ST_Contour",
        ),
    ),
    (
        "ST_ConvexHull",
        None,
        (
            """Return the convex hull geometry of the raster including pixel values equal to BandNoDataValue. For regular shaped and non-skewed rasters, this gives the same result as ST_Envelope so only useful for irregularly shaped or skewed rasters.""",
            "RT_ST_ConvexHull",
        ),
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
        "ST_CoveredBy",
        None,
        (
            """Return true if no points of raster rastA lie outside raster rastB.""",
            "RT_ST_CoveredBy",
        ),
    ),
    (
        "ST_Covers",
        None,
        (
            """Return true if no points of raster rastB lie outside raster rastA.""",
            "RT_ST_Covers",
        ),
    ),
    (
        "ST_DFullyWithin",
        None,
        (
            """Return true if rasters rastA and rastB are fully within the specified distance of each other.""",
            "RT_ST_DFullyWithin",
        ),
    ),
    (
        "ST_DWithin",
        None,
        (
            """Return true if rasters rastA and rastB are within the specified distance of each other.""",
            "RT_ST_DWithin",
        ),
    ),
    (
        "ST_Disjoint",
        None,
        (
            """Return true if raster rastA does not spatially intersect rastB.""",
            "RT_ST_Disjoint",
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
        "ST_DumpValues",
        None,
        (
            """Get the values of the specified band as a 2-dimension array.""",
            "RT_ST_DumpValues",
        ),
    ),
    (
        "ST_Envelope",
        None,
        (
            """Returns the polygon representation of the extent of the raster.""",
            "RT_ST_Envelope",
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
        "ST_Grayscale",
        types.Raster,
        (
            """Creates a new one-8BUI band raster from the source raster and specified bands representing Red, Green and Blue""",
            "RT_ST_Grayscale",
        ),
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
        "ST_Height",
        None,
        ("""Returns the height of the raster in pixels.""", "RT_ST_Height"),
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
        "ST_Histogram",
        None,
        (
            """Returns a set of record summarizing a raster or raster coverage data distribution separate bin ranges. Number of bins are autocomputed if not specified.""",
            "RT_ST_Histogram",
        ),
    ),
    (
        "ST_InterpolateRaster",
        None,
        (
            """Interpolates a gridded surface based on an input set of 3-d points, using the X- and Y-values to position the points on the grid and the Z-value of the points as the surface elevation.""",
            "RT_ST_InterpolateRaster",
        ),
    ),
    (
        "ST_Intersection",
        None,
        (
            """Returns a raster or a set of geometry-pixelvalue pairs representing the shared portion of two rasters or the geometrical intersection of a vectorization of the raster and a geometry.""",
            "RT_ST_Intersection",
        ),
    ),
    (
        "ST_Intersects",
        None,
        (
            """Return true if raster rastA spatially intersects raster rastB.""",
            "RT_ST_Intersects",
        ),
    ),
    (
        "ST_IsEmpty",
        None,
        (
            """Returns true if the raster is empty (width = 0 and height = 0). Otherwise, returns false.""",
            "RT_ST_IsEmpty",
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
        "ST_MapAlgebra",
        types.Raster,
        (
            """Callback function version -- Returns a one-band raster given one or more input rasters, band indexes and one user-specified callback function.\nOR\nExpression version -- Returns a one-band raster given one or two input rasters, band indexes and one or more user-specified SQL expressions.""",
            "RT_ST_MapAlgebra",
        ),
    ),
    (
        "ST_MapAlgebraExpr",
        types.Raster,
        (
            """1 raster band version: Creates a new one band raster formed by applying a valid PostgreSQL algebraic operation on the input raster band and of pixeltype provided. Band 1 is assumed if no band is specified.\nOR\n2 raster band version: Creates a new one band raster formed by applying a valid PostgreSQL algebraic operation on the two input raster bands and of pixeltype provided. band 1 of each raster is assumed if no band numbers are specified. The resulting raster will be aligned (scale, skew and pixel corners) on the grid defined by the first raster and have its extent defined by the "extenttype" parameter. Values for "extenttype" can be: INTERSECTION, UNION, FIRST, SECOND.""",
            "RT_ST_MapAlgebraExpr",
        ),
    ),
    (
        "ST_MapAlgebraFct",
        types.Raster,
        (
            """1 band version -- Creates a new one band raster formed by applying a valid PostgreSQL function on the input raster band and of pixeltype prodived. Band 1 is assumed if no band is specified.\nOR\n2 band version -- Creates a new one band raster formed by applying a valid PostgreSQL function on the 2 input raster bands and of pixeltype prodived. Band 1 is assumed if no band is specified. Extent type defaults to INTERSECTION if not specified.""",
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
        "ST_MemSize",
        None,
        (
            """Returns the amount of space (in bytes) the raster takes.""",
            "RT_ST_MemSize",
        ),
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
        "ST_MinConvexHull",
        None,
        (
            """Return the convex hull geometry of the raster excluding NODATA pixels.""",
            "RT_ST_MinConvexHull",
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
        "ST_NotSameAlignmentReason",
        None,
        (
            """Returns text stating if rasters are aligned and if not aligned, a reason why.""",
            "RT_ST_NotSameAlignmentReason",
        ),
    ),
    (
        "ST_NumBands",
        None,
        ("""Returns the number of bands in the raster object.""", "RT_ST_NumBands"),
    ),
    (
        "ST_Overlaps",
        None,
        (
            """Return true if raster rastA and rastB intersect but one does not completely contain the other.""",
            "RT_ST_Overlaps",
        ),
    ),
    (
        "ST_PixelAsCentroid",
        None,
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
        "ST_PixelAsPoint",
        None,
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
        "ST_PixelAsPolygon",
        None,
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
        "ST_PixelHeight",
        None,
        (
            """Returns the pixel height in geometric units of the spatial reference system.""",
            "RT_ST_PixelHeight",
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
        "ST_PixelWidth",
        None,
        (
            """Returns the pixel width in geometric units of the spatial reference system.""",
            "RT_ST_PixelWidth",
        ),
    ),
    (
        "ST_Polygon",
        None,
        (
            """Returns a multipolygon geometry formed by the union of pixels that have a pixel value that is not no data value. If no band number is specified, band num defaults to 1.""",
            "RT_ST_Polygon",
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
        "ST_RastFromHexWKB",
        types.Raster,
        (
            """Return a raster value from a Hex representation of Well-Known Binary (WKB) raster.""",
            "RT_ST_RastFromHexWKB",
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
        "ST_Reclass",
        types.Raster,
        (
            """Creates a new raster composed of band types reclassified from original. The nband is the band to be changed. If nband is not specified assumed to be 1. All other bands are returned unchanged. Use case: convert a 16BUI band to a 8BUI and so forth for simpler rendering as viewable formats.""",
            "RT_ST_Reclass",
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
        "ST_Resize",
        types.Raster,
        ("""Resize a raster to a new width/height""", "RT_ST_Resize"),
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
        "ST_Retile",
        types.Raster,
        (
            """Return a set of configured tiles from an arbitrarily tiled raster coverage.""",
            "RT_ST_Retile",
        ),
    ),
    (
        "ST_Rotation",
        None,
        ("""Returns the rotation of the raster in radian.""", "RT_ST_Rotation"),
    ),
    (
        "ST_Roughness",
        types.Raster,
        (
            """Returns a raster with the calculated "roughness" of a DEM.""",
            "RT_ST_Roughness",
        ),
    ),
    (
        "ST_SRID",
        None,
        (
            """Returns the spatial reference identifier of the raster as defined in spatial_ref_sys table.""",
            "RT_ST_SRID",
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
        "ST_SetBandIndex",
        types.Raster,
        ("""Update the external band number of an out-db band""", "RT_ST_SetBandIndex"),
    ),
    (
        "ST_SetBandIsNoData",
        types.Raster,
        ("""Sets the isnodata flag of the band to TRUE.""", "RT_ST_SetBandIsNoData"),
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
        "ST_SetBandPath",
        types.Raster,
        (
            """Update the external path and band number of an out-db band""",
            "RT_ST_SetBandPath",
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
        "ST_SetM",
        None,
        (
            """Returns a geometry with the same X/Y coordinates as the input geometry, and values from the raster copied into the Z dimension using the requested resample algorithm.""",
            "RT_ST_SetM",
        ),
    ),
    (
        "ST_SetRotation",
        types.Raster,
        ("""Set the rotation of the raster in radian.""", "RT_ST_SetRotation"),
    ),
    (
        "ST_SetSRID",
        types.Raster,
        (
            """Sets the SRID of a raster to a particular integer srid defined in the spatial_ref_sys table.""",
            "RT_ST_SetSRID",
        ),
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
        "ST_SetZ",
        None,
        (
            """Returns a geometry with the same X/Y coordinates as the input geometry, and values from the raster copied into the Z dimension using the requested resample algorithm.""",
            "RT_ST_SetZ",
        ),
    ),
    (
        "ST_SkewX",
        types.Raster,
        ("""Returns the georeference X skew (or rotation parameter).""", "RT_ST_SkewX"),
    ),
    (
        "ST_SkewY",
        types.Raster,
        ("""Returns the georeference Y skew (or rotation parameter).""", "RT_ST_SkewY"),
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
        "ST_SnapToGrid",
        types.Raster,
        (
            """Resample a raster by snapping it to a grid. New pixel values are computed using the NearestNeighbor (english or american spelling), Bilinear, Cubic, CubicSpline or Lanczos resampling algorithm. Default is NearestNeighbor.""",
            "RT_ST_SnapToGrid",
        ),
    ),
    (
        "ST_Summary",
        None,
        ("""Returns a text summary of the contents of the raster.""", "RT_ST_Summary"),
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
        "ST_Tile",
        types.Raster,
        (
            """Returns a set of rasters resulting from the split of the input raster based upon the desired dimensions of the output rasters.""",
            "RT_ST_Tile",
        ),
    ),
    (
        "ST_Touches",
        None,
        (
            """Return true if raster rastA and rastB have at least one point in common but their interiors do not intersect.""",
            "RT_ST_Touches",
        ),
    ),
    (
        "ST_Transform",
        types.Raster,
        (
            """Reprojects a raster in a known spatial reference system to another known spatial reference system using specified resampling algorithm. Options are NearestNeighbor, Bilinear, Cubic, CubicSpline, Lanczos defaulting to NearestNeighbor.""",
            "RT_ST_Transform",
        ),
    ),
    (
        "ST_Union",
        types.Raster,
        (
            """Returns the union of a set of raster tiles into a single raster composed of 1 or more bands.""",
            "RT_ST_Union",
        ),
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
        "ST_Value",
        None,
        (
            """Returns the value of a given band in a given columnx, rowy pixel or at a particular geometric point. Band numbers start at 1 and assumed to be 1 if not specified. If exclude_nodata_value is set to false, then all pixels include nodata pixels are considered to intersect and return value. If exclude_nodata_value is not passed in then reads it from metadata of raster.""",
            "RT_ST_Value",
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
        "ST_Width",
        None,
        ("""Returns the width of the raster in pixels.""", "RT_ST_Width"),
    ),
    (
        "ST_Within",
        None,
        (
            """Return true if no points of raster rastA lie in the exterior of raster rastB and at least one point of the interior of rastA lies in the interior of rastB.""",
            "RT_ST_Within",
        ),
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
        "UpdateRasterSRID",
        None,
        (
            """Change the SRID of all rasters in the user-specified column and table.""",
            "RT_UpdateRasterSRID",
        ),
    ),
]
