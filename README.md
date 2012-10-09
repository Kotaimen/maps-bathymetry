Maps-Bathymetry
===============

Map Theme for SRTM250 World Relief (including ocean bathymetry)

Bathymetry Data
---------------
- **Data Description**  
SRTM30_PLUS: SRTM30, COASTAL & RIDGE MULTIBEAM, ESTIMATED TOPOGRAPHY [[Link]](http://topex.ucsd.edu/WWW_html/srtm30_plus.html)
- **Data Download**  
ftp://topex.ucsd.edu/pub/srtm30_plus/

Data Import
-----------
- **Bulid Virtual Data**  
A virtual data is a mosaic of the list of input gdal datasets, which makes datasets as one globe  
data. Overlapping data will not be calculated repeatedly.  
`gdalbuildvrt -resolution highest -vrtnodata -32768 world.vrt *.tif`

- **Reprojection**  
Project the dataset to EPSG:3857(google mercator).  
It it better to use cubicspline as to get a smooth resample result.  
Work memory can be increased to improve the performance if you have large memory.
`gdalwarp -t_srs EPSG:3857 -dstnodata -32768 -r cubicspline -wm 1024mb -multi world.vrt world_3857.tif`

- **Import Into PostgreSQL**  
Use `raster2psql` to import raster data into PostgreSQL WITH PostGIS(2.0.0+).   
`raster2psql -s 3857 -t 512x512 -I -M -C -Y -N -32768 world_3857.tif table_name > import.sql`
`psql -d database_name -f import.sql`