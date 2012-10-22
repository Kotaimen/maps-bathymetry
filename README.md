Maps: Blue Marble
=================

Map theme using SRTM250 World Relief and NASA Blue Marble Next Generation.

See http://tiles.mapbox.com/kotaimen/map/BlueMarbleBathymetry

Bathymetry Data
===============
Data Description
----------------
SRTM30_PLUS: SRTM30, COASTAL & RIDGE MULTIBEAM, ESTIMATED TOPOGRAPHY [[Link]](http://topex.ucsd.edu/WWW_html/srtm30_plus.html)
Download
--------
ftp://topex.ucsd.edu/pub/srtm30_plus/

Blue Marble
===========
Download at: http://bluemarble.nasa.gov
Get the 500m resolution one, note they have different image for each month.

Data Import
===========

Bathymetry
----------
A virtual data is a mosaic of the list of input gdal datasets, which makes datasets as one globe  
data. Overlapping data will not be calculated repeatedly.  
`gdalbuildvrt -resolution highest -vrtnodata -32768 world.vrt *.tif`
