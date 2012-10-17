import copy

zfactor=16
azimuth=315
    
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
    sources='elevation',
    zfactor=zfactor,
    scale=1,
    altitude=30,
    azimuth=azimuth,
    )

specular = dict(\
    prototype='processing.hillshading',
    sources='elevation',
    zfactor=zfactor,
    scale=1,
    altitude=85,
    azimuth=azimuth,
    )

ocean = dict(\
    prototype='processing.colorrelief',
    sources='elevation',
    color_context='themes/bathymetry/ocean.txt',
    )

warm_humid = dict(\
    prototype='processing.colorrelief',
    sources='elevation',
    color_context='themes/bathymetry/warm-humid.txt',
    )

cold_humid = dict(\
    prototype='processing.colorrelief',
    sources='elevation',
    color_context='themes/bathymetry/cold-humid.txt',
    )
    
arid = dict(\
    prototype='processing.colorrelief',
    sources='elevation',
    color_context='themes/bathymetry/arid.txt',
    )
    
polar = dict(\
    prototype='processing.colorrelief',
    sources='elevation',
    color_context='themes/bathymetry/polar.txt',
    )


mtemp = dict(\
    prototype='datasource.dataset',
    dataset_path='/Users/Kotaimen/proj/geodata/natualearth/tmean_5m_bil/tmean_5m.vrt',
    cache= dict(prototype='metacache',
         root='./themes/bathymetry/cache/tmean',
         compress=True,
         data_format='gtiff',
         ),
)

mtemp_mask = dict(\
    prototype='processing.colorrelief',
    sources='mtemp',
    color_context='themes/bathymetry/mtemp.txt',
    )
    
prec = dict(\
    prototype='datasource.dataset',
    dataset_path='/Users/Kotaimen/proj/geodata/natualearth/prec_5m_bil/prec_5m.vrt',
    cache= dict(prototype='metacache',
         root='./themes/bathymetry/cache/prec',
         compress=True,
         data_format='gtiff',
         ),
)

prec_mask = dict(\
    prototype='processing.colorrelief',
    sources='prec',
    color_context='themes/bathymetry/prec.txt',
    )

polar_mask = dict(\
    prototype='datasource.mapnik',
    theme=r'./themes/bathymetry/polar-mask.xml',
    image_type='png',
    buffer_size=0,
    )
    
land_fill = dict(\
    prototype='datasource.mapnik',
    theme=r'./themes/bathymetry/land-fill.xml',
    image_type='png',
    buffer_size=0,
    )

land_mask = dict(\
    prototype='datasource.mapnik',
    theme=r'./themes/bathymetry/land-mask.xml',
    image_type='png',
    buffer_size=0,
    )

    
composer = dict(\
     prototype='composite.imagemagick',
#      cache=dict(prototype='metacache',
#               root='./themes/bathymetry/cache/bathmetry',
#               data_format='jpg',
#               ),
     sources=['diffuse', 'specular', 'ocean',
              'warm_humid', 'cold_humid', 'arid', 'polar', 
              'mtemp_mask', 'prec_mask', 'polar_mask', 
              'land_fill', 'land_mask'
             ],
     format='jpg',
     command='''
     
    (
        $1 -fill grey50 -colorize 100%
        ( $1 ) -compose blend -define compose:args=55% -composite
        ( $2 -gamma 4.5 ) -compose blend -define compose:args=45% -composite     
        -brightness-contrast -13%x-6%
        -gamma 0.7
    )
    ( 
        
        $3
        $11 -compose over -composite
        ( 
            $4
            $6
            $9 -compose over -composite 
            $5
            $8 -compose over -composite 
            $7
            $10 -compose over -composite 
        ) $12  -compose over -composite  
    )   -compose overlay -composite
    
    -brightness-contrast -7%x-6%
    
    -adaptive-sharpen 2.5
    -quality 100
     ''',

     )

ROOT = dict(\
    metadata=dict(tag='world'),
    renderer='composer',    
    pyramid=dict(levels=range(3, 10),
                 format='jpg',
                 buffer=16,
                 tile_size=256, 
                 envelope=(-180, -85, 180, 85),
                 zoom=5,
                 center=(126, 27),
                 ),
#    cache=dict(prototype='filesystem',
#               root='./themes/bathymetry/cache/export',
#               data_format='jpg',
#               ),
    )
