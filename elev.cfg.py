#
# Standard hill shading and gtiff tiles
#



# Default elevation, use PostGIS2 as data source
elevation = dict(\
    name='elevation',
    prototype='datasource.postgis',
    server='postgresql://postgres:123456@172.26.183.198:5432/srtm30_new',
    table='srtm30_3857',
    cache=
    #None,
    dict(prototype='metacache',
               root='./themes/bathymetry/cache/elevation',
               compress=True,
               data_format='gtiff',
               ),
)

# Simple relief for preview
relief = dict(\
    name='relief',
    prototype='processing.hillshading',
    sources=(elevation,),
    zfactor=3,
    scale=1,
    altitude=45,
    azimuth=315,
    )

composer=dict(\
    name='composer',
    prototype='composite.imagemagick',
    cache=None,
    sources=[relief,],
    format='png',
    command='''
    $1
    -brightness-contrast +10%x-33% -gamma 1.2
    '''
    )

ROOT = dict(\
    renderer=composer,
    metadata=dict(tag='hills'),
    pyramid=dict(levels=range(6, 9),
                 envelope=(-180,-85,180,85),
                 zoom=7,
                 center=(0, 0),
                 format='png',
                 buffer=16,
                 ),
)
