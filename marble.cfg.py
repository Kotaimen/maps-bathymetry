zfactor=22
azimuth=315
    

elevation = dict(\
    prototype='datasource.dataset',
    dataset_path='/Users/Kotaimen/proj/geodata/srtm30_new/gtiff/world.vrt',
    cache= dict(prototype='metacache',
         root='./themes/BlueMarble/cache/elevation',
         compress=True,
         data_format='gtiff',
         ),
)


marble = dict(\
    prototype='datasource.dataset',
    dataset_path='/Users/Kotaimen//proj/geodata/BlueMarble/world.topo.bathy.tif',
#    cache= dict(prototype='metacache',
#         root='./themes/BlueMarble/cache/elevation',
#         compress=True,
#         data_format='gtiff',
#         ),
)

diffuse = dict(\
    prototype='processing.hillshading',
    sources='elevation',
    zfactor=zfactor,
    scale=1,
    altitude=20,
    azimuth=azimuth,
    )

specular = dict(\
    prototype='processing.hillshading',
    sources='elevation',
    zfactor=zfactor,
    scale=1,
    altitude=89,
    azimuth=azimuth,
    )

composer=dict(\
    prototype='composite.imagemagick',
    cache=None,
    sources=['elevation', 'marble', 'diffuse', 'specular', ],
    format='jpg',
    command='''   
    (
        $3 -fill grey50 -colorize 100%
        ( $3 ) -compose blend -define compose:args=55% -composite
        ( $4 -gamma 4.5 ) -compose blend -define compose:args=45% -composite     
        -brightness-contrast -10%x-1%
        -gamma 0.8
    )
    
    $2 -compose overlay -composite
    #-brightness-contrast +15%x-%
    -gamma 1.5
#     -adaptive-sharpen 2.2
    
    
    -quality 99
    '''
    )

ROOT = dict(\
    renderer='composer',
    metadata=dict(tag='BlueMarble',
                  version='1.0',
                  description='Blue Marble with Bathymetry and Shaded Relief',
                  attribution='',
                  ),
    pyramid=dict(levels=range(3, 8),
                 envelope=(-180,-85,180,85),
                 zoom=5,
                 center=(100, 30),
                 format='jpg',
                 buffer=0,
                 ),
)
