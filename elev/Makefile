all: t1 t2 t3 t4 t5 t6 t7 t8
	gdalbuildvrt -resolution highest -overwrite world.vrt *.tif
	gdalwarp -t_srs "epsg:3857" -te -20037508.342 -20037508.342 20037508.342 20037508.342 -wo "SOURCE_EXTRA=120" -r cubic -wm 1024 -multi -of gtiff -co "TILED=YES" -co "JPEG_QUALITY=85" -co "COMPRESS=JPEG" -co "BLOCKXSIZE=512" -co "BLOCKYSIZE=512" -overwrite world.vrt world.3857.tif 
    #gdalwarp -t_srs "epsg:3857" -te -20037508.342 -20037508.342 20037508.342 20037508.342 -wo "SOURCE_EXTRA=120" -r cubic -wm 1024 -multi -of gtiff -co "TILED=YES" -co "ZLEVEL=5" -co "COMPRESS=DEFLATE" -co "BLOCKXSIZE=512" -co "BLOCKYSIZE=512" -overwrite world.vrt world_tiled.tif

t1:
	gdal_translate -of gtiff -co "TILED=YES" -a_srs epsg:4326 -a_ullr -180 90 -90 0  world.topo.200406.3x21600x21600.A1.jpg A1.tif
t2:
	gdal_translate -of gtiff -co "TILED=YES" -a_srs epsg:4326 -a_ullr -180 0 -90 -90  world.topo.200406.3x21600x21600.A2.jpg A2.tif
t3:
	gdal_translate -of gtiff -co "TILED=YES" -a_srs epsg:4326 -a_ullr -90 90 0 0  world.topo.200406.3x21600x21600.B1.jpg B1.tif
t4:
	gdal_translate -of gtiff -co "TILED=YES" -a_srs epsg:4326 -a_ullr -90 0 0 -90  world.topo.200406.3x21600x21600.B2.jpg B2.tif
t5:
	gdal_translate -of gtiff -co "TILED=YES" -a_srs epsg:4326 -a_ullr 0 90 90 0  world.topo.200406.3x21600x21600.C1.jpg C1.tif
t6:
	gdal_translate -of gtiff -co "TILED=YES" -a_srs epsg:4326 -a_ullr 0 0 90 -90  world.topo.200406.3x21600x21600.C2.jpg C2.tif
t7:
	gdal_translate -of gtiff -co "TILED=YES" -a_srs epsg:4326 -a_ullr 90 90 180 0  world.topo.200406.3x21600x21600.D1.jpg D1.tif
t8:
	gdal_translate -of gtiff -co "TILED=YES" -a_srs epsg:4326 -a_ullr 90 0 180 -90  world.topo.200406.3x21600x21600.D2.jpg D2.tif
