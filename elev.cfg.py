#
# Standard hill shading and gtiff tiles
#

# Default elevation, use PostGIS2 as data source
elevation = dict(\
    prototype='datasource.dataset',
    dataset_path='/Users/Kotaimen/proj/geodata/srtm30_new/gtiff/world.vrt',
    cache= dict(prototype='metacache',
         root='./themes/bathymetry/cache/elevation',
         compress=True,
         data_format='gtiff',
         ),
)

# Simple relief for preview
relief = dict(\
    prototype='processing.hillshading',
    sources='elevation',
    zfactor=3,
    scale=1,
    altitude=45,
    azimuth=315,
    )

composer=dict(\
    prototype='composite.imagemagick',
    cache=None,
    sources=['relief',],
    format='png',
    command='''
    $1
    -brightness-contrast +10%x-33% -gamma 1.2
    '''
    )

ROOT = dict(\
    renderer='elevation',
    metadata=dict(tag='hills'),
    pyramid=dict(levels=range(4, 8),
                 envelope=(-180,-85,180,85),
                 zoom=7,
                 center=(0, 0),
                 format='png',
                 buffer=0,
                 ),
)
