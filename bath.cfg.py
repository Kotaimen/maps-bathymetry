import copy

zfactor=16
azimuth=315

dem1 = dict(\
    name='dem',
    prototype='datasource.storage',
    storage_type='metacache',
    stride=1,
    root='./themes/bathymetry/cache/elevation',
    )
    
dem1 = dict(\
    name='elevation',
    prototype='datasource.postgis',
    server='postgresql://postgres:123456@172.26.183.198:5432/srtm30_new',
    table='srtm30_3857',
    cache=dict(prototype='metacache',
               root='./themes/bathymetry/cache/elevation',
               compress=True,
               data_format='gtiff',
               ),
)


dem2 = copy.deepcopy(dem1)
dem3 = copy.deepcopy(dem1)
dem4 = copy.deepcopy(dem1)
dem5 = copy.deepcopy(dem1)

diffuse = dict(\
    name='diffuse',
    prototype='processing.hillshading',
    cache=None,
    sources=(dem1,),
    zfactor=zfactor,
    scale=1,
    altitude=30,
    azimuth=azimuth,
    )
    
detail = dict(\
    name='diffuse',
    prototype='processing.hillshading',
    cache=None,
    sources=(dem2,),
    zfactor=1,
    scale=1,
    altitude=40,
    azimuth=azimuth,
)

specular = dict(\
    name='specular',
    prototype='processing.hillshading',
    cache=None,
    sources=(dem3,),
    zfactor=zfactor,
    scale=1,
    altitude=85,
    azimuth=azimuth,
    )

color = dict(\
    name='color',
    prototype='processing.colorrelief',
    cache=None,
    sources=(dem4,),
    color_context='themes/bathymetry/hypsometric-map-ocean.txt',
    )


composer = dict(\
     name='imagemagick_composer',
     prototype='composite.imagemagick',
     cache=dict(prototype='metacache',
               root='./themes/bathymetry/cache/bathmetry',
               data_format='jpg',
               ),
     sources=[diffuse, specular, color, detail, dem5],
     format='jpg',
     command=''' 
    $1 -fill grey50 -colorize 100%
    ( $1 ) -compose blend -define compose:args=30% -composite
    ( $4 -brightness-contrast +0%x+40% ) -compose blend -define compose:args=20% -composite    
    ( $2 -gamma 4 ) -compose blend -define compose:args=50% -composite     
    -brightness-contrast -15%x+2%
    -gamma 0.75
    $3 -compose overlay -composite
#   -unsharp 2x1+0.3
#   -adaptive-sharpen 2
    -sharpen 0.6
    -quality 85
     ''',

     )



ROOT = dict(\
    metadata=dict(tag='world'),
    pyramid=dict(levels=range(5, 9),
                 format='jpg',
                 buffer=0,
                 envelope=(-180, -85, 180, 85),
                 zoom=7,
                 center=(0, 0),
                 ),
    cache=dict(prototype='filesystem',
               root='./themes/bathymetry/cache/export',
               data_format='jpg',
               ),
    renderer=composer,
    )
