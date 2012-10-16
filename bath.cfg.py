import copy

zfactor=20
azimuth=315

# elevation = dict(\
#     name='dem',
#     prototype='datasource.storage',
#     storage_type='metacache',
#     stride=1,
#     root='./themes/bathymetry/cache/elevation',
#     )
    
elevation = dict(\
    prototype='datasource.dataset',
    dataset_path='/Users/Kotaimen/proj/geodata/srtm30_new/gtiff/world.vrt',
    cache= dict(prototype='metacache',
         root='./themes/bathymetry/cache/elevation',
         compress=True,
         data_format='gtiff',
         ),
)


diffuse = dict(\
    prototype='processing.hillshading',
    cache=None,
    sources='elevation',
    zfactor=zfactor,
    scale=1,
    altitude=30,
    azimuth=azimuth,
    )

specular = dict(\
    prototype='processing.hillshading',
    cache=None,
    sources='elevation',
    zfactor=zfactor,
    scale=1,
    altitude=85,
    azimuth=azimuth,
    )

color = dict(\
    prototype='processing.colorrelief',
    cache=None,
    sources='elevation',
    color_context='themes/bathymetry/hypsometric-map-ocean.txt',
    )

composer = dict(\
     prototype='composite.imagemagick',
     cache=dict(prototype='metacache',
               root='./themes/bathymetry/cache/bathmetry',
               data_format='jpg',
               ),
     sources=['diffuse', 'specular', 'color'],
     format='jpg',
     command=''' 
    $1 -fill grey50 -colorize 100%
    ( $1 ) -compose blend -define compose:args=55% -composite
    ( $2 -gamma 3.1 ) -compose blend -define compose:args=45% -composite     
    -brightness-contrast -15%x-2%
    -gamma 0.75
    $3 -compose overlay -composite
#   -unsharp 2x1+0.3
    -adaptive-sharpen 2
#     -sharpen 0.6
    -quality 100
     ''',

     )

ROOT = dict(\
    metadata=dict(tag='world'),
    renderer='composer',    
    pyramid=dict(levels=range(4, 10),
                 format='jpg',
                 buffer=16,
                 envelope=(-180, -85, 180, 85),
                 zoom=5,
                 center=(126, 27),
                 ),
    cache=dict(prototype='filesystem',
               root='./themes/bathymetry/cache/export',
               data_format='jpg',
               ),
    )
