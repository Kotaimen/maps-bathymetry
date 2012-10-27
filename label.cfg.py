import os


datadir = '/Users/Kotaimen/proj/geodata'
themedir= './themes/bathymetry'
cachedir= os.path.join(themedir, 'cache')
tag = 'Label'

labels = dict(\
    prototype='datasource.mapnik',
    cache=dict(prototype='metacache',
           root=os.path.join(cachedir, '%s' % tag),
           data_format='png',
           ),   
    theme=os.path.join(themedir, 'label.xml'),
    image_type='png',
    buffer_size=64,
    scale_factor=1,
    )

ROOT = dict(\
    prototype='root',
    renderer='labels',
    metadata=dict(
        tag='Labels',
    ),
    pyramid=dict(
        levels=range(2, 9),
        format='png',
        buffer=0,
        tile_size=256,
        zoom=5,
        center=(35, 0),
        ),
    cache=dict(prototype='filesystem',
           root=os.path.join(cachedir, 'export', '%s' % tag),
           data_format='png',
           simple=True
           ),   
    )

