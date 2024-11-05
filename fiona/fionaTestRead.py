import fiona

# Abrir el archivo Shapefile
with fiona.open('./datos/shapefile/calles_posgar.shp') as src:
    # Imprimir información sobre el archivo
    print(src.driver)
    print(src.crs)
    print(src.schema)
    
    # Leer todos los features
    features = list(src)
    
    # Mostrar el primer feature
    first_feature = features[0]
    print(first_feature['geometry'])
    print(first_feature['properties'])

# Cerrar automáticamente el archivo al salir del bloque 'with'
 