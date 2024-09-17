import pymongo
from pymongo import MongoClient

cMongo = MongoClient('localhost', 27017)
db = cMongo.dbPrueba
#coleccion = db.ifttttuiteos
coleccion = db.pruebas
#coleccionArchiver = db.archivertuiteos
#cursorArchiver = coleccionArchiver.find()

cursor = coleccion.find()
#print(cursorArchiver.next())
for unTuit in cursor:
    #post_id = coleccion.insert_one(unTuit).inserted_id
    
    j=0
#for tuits in cursorCoordenadas:
    registro = {"usuario" : unTuit['usuario'],
                "fecha" : unTuit['fecha'],
                "texto" : unTuit['texto'],
                "urlTweet" : unTuit['url']
                }
#                "urlGoogleMaps" : tuits['urlGoogleMaps'],
#                "latitud" : float(tuits['latitud']),
#                "longuitud" : float(tuits['longuitud'])
#            }
    print ("Registro       : "  + str(j)  + "\n" \
           "Fecha          : "  + registro['fecha'] + "\n" \
           "Usuario        : "  + registro['usuario'] + "\n" \
           "Texto          : "  + registro['texto']   + "\n" \
           "Url Tweet      : "  + registro['urlTweet']   + "\n" )
#           "Url Google Maps: "  + registro['urlGoogleMaps'] + "\n" \
#           "latitud        : "  + str(registro['latitud']) + "\n" \
#           "longuitud      : "  + str(registro['longuitud']) + "\n" )
#    post_id = coleccionPruebas.insert_one(tuits).inserted_id
    j = j + 1 

# =============================================================================
# cursor = coleccion.aggregate(
#  [
#     {
#         '$group': {
#             '_id': '$usuario', 
#             'cantidad': {
#                 '$sum': 1
#             }
#         }
#     }, {
#         '$match': {
#             'cantidad': {
#                 '$gt': 25
#             }
#         }
#     }
#     , {
#         '$sort': {
#             'cantidad': -1
#         }
#     }, {
#         '$limit': 100
#     }
# ]
# )
# =============================================================================
#print(cursor.next())
#for grupos in cursor:
        #print('usuario {0}, cantidad de tweets {1}'.format(grupos['_id'],grupos['cantidad']))
        #print(grupos)



#status = db.command("serverStatus")  #estado del servidor
#print(status)

# Retrieve the value of a certain cell

#print("\n\nFecha: " + sheet['A2'].value + "\n\n" \
#      "Usuario: "  + sheet['B2'].value + "\n\n" \
#      "Texto: " + sheet['C2'].value + "\n\n" \
#      "Url tweet:" + sheet['D2'].value + "\n\n" \
#      "Coords: " + sheet['E2'].value)

# Get currently active sheet
#anotherSheet = wb.active

# Check `anotherSheet` 
#anotherSheet

# Retrieve the value of a certain cell
#sheet['A1'].value

# Select element 'B2' of your sheet 
#c = sheet['B2']

# Retrieve the row number of your element
#c.row

# Retrieve the column letter of your element
#c.column

# Retrieve the coordinates of the cell 
#c.coordinate

# Retrieve cell value 
#sheet.cell(row=1, column=2).value

# Print out values in column 2 
#for i in range(1, 4):
#     print(i, sheet.cell(row=i, column=2).value)
# Import relevant modules from `openpyxl.utils`
#from openpyxl.utils import get_column_letter, column_index_from_string

# Return 'A'
#get_column_letter(1)

# Return '1'
#column_index_from_string('A')

# Print row per row
#for cellObj in sheet['A1':'C3']:
#      for cell in cellObj:
#              print(cells.coordinate, cells.value)
#      print('--- END ---')

# Retrieve the maximum amount of rows 
#sheet.max_row

# Retrieve the maximum amount of columns
#sheet.max_column







































        
    
        
        
        
        
