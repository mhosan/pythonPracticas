import fiona
import os

# Definir el esquema y el sistema de coordenadas
schema = {'geometry': 'Point', 'properties': [('id', 'int')]}
crs = {'init': 'epsg:4326'}

# Crear una lista de features
features = [
    {'type': 'Feature',
     'geometry': {'type': 'Point', 'coordinates': [125.6, 10.1]},
     'properties': {'id': 0}},
    {'type': 'Feature',
     'geometry': {'type': 'Point', 'coordinates': [125.7, 10.2]},
     'properties': {'id': 1}}
]

# Obtener la ruta del escritorio
#desktop_path = os.path.join(os.environ['USERPROFILE'], 'Desktop')
desktop_path = 'C:/Users/marcelo.hosan/Desktop/'
print(desktop_path)
'''
# Crear la ruta completa hasta la carpeta final
gis_folder = os.path.join(desktop_path, 'GIS')
carpetaUnicaDistribuir = os.path.join(gis_folder, 'carpetaUnicaDistribuir')
datos = os.path.join(carpetaUnicaDistribuir, 'datos')
final_folder = os.path.join(datos, 'shapeFilesPython')

# Crear todas las carpetas necesarias si no existen
os.makedirs(final_folder, exist_ok=True)

# Construir la ruta completa para el nuevo archivo
output_file = os.path.join(final_folder, 'nuevo_archivo.shp')

# Escribir el nuevo archivo Shapefile
with fiona.open(output_file, 'w', 
                driver='ESRI Shapefile', 
                schema=schema,
                crs=crs) as sink:
    sink.writerecords(features)

print(f"Archivo creado correctamente en {output_file}")
'''