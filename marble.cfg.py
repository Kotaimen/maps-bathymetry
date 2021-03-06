import os

zfactor=24 # Reduce this when using high resolution data!
azimuth=345

datadir = '/Users/Kotaimen/proj/geodata'
themedir= './themes/bathymetry'
cachedir= os.path.join(themedir, 'cache')
tag = 'BlueMarble_June'

marble = dict(\
    prototype='datasource.dataset',
    dataset_path=os.path.join(datadir, 'BlueMarble/bathy.200406.tif'),
    )


land_mask = dict(\
    prototype='datasource.mapnik',
    theme=os.path.join(themedir, 'land_mask.xml'),
    image_type='png',
    buffer_size=0,
    )

elevation = dict(\
    prototype='datasource.dataset',
    dataset_path=os.path.join(datadir, 'srtm30_new/world_tiled.tif'),
    cache=dict(prototype='metacache',
        root=os.path.join(cachedir, 'elevation'),
        compress=True,
        data_format='gtiff',
        ),
    )

bathymetry = dict(\
    prototype='processing.colorrelief',
    sources='elevation',
    color_context=os.path.join(themedir, 'ocean.txt'),
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
               root=os.path.join(cachedir, '%s' % tag),
               data_format='jpg',
               ),                  
    sources=['diffuse', 'detail', 'specular', 'marble'],
    format='jpg',
    command='''   
    (
        ( $1 -fill grey50 -colorize 100% )
        ( $1 ) -compose blend -define compose:args=50% -composite
        ( $2 -brightness-contrast +0%x+30% ) -compose blend -define compose:args=20% -composite    
        ( $3 -gamma 1.9 ) -compose blend -define compose:args=30% -composite     
        -brightness-contrast -5%x-5%
        -gamma 0.8
    )
    (   

        ( $4 -gamma 2.2 -gaussian-blur 0x0.4 ) 
    ) -compose overlay -composite
    -quality 85
    '''
    )

ROOT = dict(\
    renderer='composer',
    metadata=dict(tag=tag,
                  version='1.0',
                  description='NASA Blue Marbels with Bathymetry and Shaded Relief',
                  attribution='',
                  ),
    cache=dict(prototype='filesystem',
               root=os.path.join(cachedir, 'export', '%s' % tag),
               data_format='jpg',
               simple=True
               ),                  
    pyramid=dict(levels=range(2, 9),
                 envelope=(-180,-85,180,85),
                 zoom=5,
                 center=(100, 30),
                 format='jpg',
                 buffer=8,
                 ),
)
