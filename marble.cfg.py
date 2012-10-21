zfactor=20 # Reduce this when using high resolution data!
azimuth=345

elevation = dict(\
    prototype='datasource.dataset',
    dataset_path='/Users/Kotaimen/proj/geodata/srtm30_new/gtiff/world.vrt',
#    dataset_path='/Users/Kotaimen/proj/geodata/DEM-Tools-patch/source/ned10m/ned10m.vrt',
    cache=dict(prototype='metacache',
        root='./themes/bathymetry/cache/elevation',
        compress=True,
        data_format='gtiff',
        ),
)

marble = dict(\
    prototype='datasource.dataset',
    dataset_path='/Users/Kotaimen/proj/geodata/BlueMarble/bathy.200407.500m.tif',
    cache= dict(prototype='metacache',
       root='./themes/bathymetry/cache/marble',
       compress=True,
       data_format='gtiff',
       ),
)

diffuse = dict(\
    prototype='processing.hillshading',
    sources='elevation',
    zfactor=zfactor,
    scale=1,
    altitude=15,
    azimuth=azimuth,
    )

detail = dict(\
    prototype='processing.hillshading',
    sources='elevation',
    zfactor=1.5,
    scale=1,
    altitude=45,
    azimuth=azimuth,
)

specular = dict(\
    prototype='processing.hillshading',
    sources='elevation',
    zfactor=zfactor,
    scale=1,
    altitude=90,
    azimuth=azimuth,
    )

composer=dict(\
    prototype='composite.imagemagick',
    cache=dict(prototype='metacache',
               root='./themes/bathymetry/cache/composer',
               data_format='jpg',
               ),                  
    sources=['diffuse', 'detail', 'specular', 'marble', ],
    format='jpg',
    command='''   
    (
        ( $1 -fill grey50 -colorize 100% )
        ( $1 ) -compose blend -define compose:args=50% -composite
        ( $2 -brightness-contrast +0%x+30% ) -compose blend -define compose:args=20% -composite    
        ( $3 -gamma 1.8 ) -compose blend -define compose:args=30% -composite     
        -brightness-contrast -10%x-5%
        -gamma 0.7
    )
    
    ( 
        $4 -brightness-contrast +1%x-3%
    ) -compose overlay -composite

#    -brightness-contrast +10%x-12%
    -gamma 1.8
#    -unsharp 0x1+0.3
    -quality 75
    '''
    )

ROOT = dict(\
    renderer='composer',
    metadata=dict(tag='BlueMarble',
                  version='1.0',
                  description='Blue Marble with Bathymetry and Shaded Relief.',
                  attribution='SRTM_new Bathymetry, NASA Blue Marble.',
                  ),
#    cache=dict(prototype='filesystem',
#               root='./themes/bathymetry/cache/export',
#               data_format='jpg',
#               simple=True
#               ),                  
    cache=dict(prototype='mbtiles', database='./themes/bathymetry/cache/export.mbtiles'),
    pyramid=dict(levels=range(3, 8),
                 envelope=(-180,-75,180,75),
                 zoom=5,
                 center=(100, 30),
                 format='jpg',
                 buffer=8,
                 ),
)
