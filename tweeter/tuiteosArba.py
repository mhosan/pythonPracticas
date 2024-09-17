#import json

#leer = json.loads(open('cafe.json').read())
#algo = leer[0]
#print (algo)
print ("|---------------------------|")
print ("|                           |")
print ("|                           |")
print ("|                           |")
print ("|---------------------------|")

#import pprint
import pymongo
from pymongo import MongoClient
cMongo = MongoClient('localhost', 27017)
db = cMongo.datos
coleccion = db.ifttttuiteos

planilla = "./p.xlsx"

from openpyxl import load_workbook
wb = load_workbook(planilla)
sheet = wb.get_sheet_by_name('Hoja 1')

j = 1
k = 1
for i in sheet:
    celdaA = 'A' + str(j)
    celdaB = 'B' + str(j)
    celdaC = 'C' + str(j)
    celdaD = 'D' + str(j)
    usuario = sheet[celdaB].value
    fecha = sheet[celdaA].value
    texto = sheet[celdaC].value
    url = sheet[celdaD].value
    if usuario != "@arba_h1231" \
    and usuario != "@arba_bot" \
    and usuario != "@Dadaaaaaaang" \
    and usuario != "@Samir_islam2013" \
    and usuario != "@alexander1LT" \
    and usuario != "@_matar_114" \
    and usuario != "@Awadhi_Al" \
    and usuario != "@moouunim" \
    and usuario != "@heru_arba" \
    and usuario != "@DrStrangesStore" \
    and usuario != "@Arba_93" \
    and usuario != "@Michelle_commu" \
    and usuario != "@cookie_03n" \
    and usuario != "@min080809" \
    and usuario != "@7_arba" \
    and usuario != "@minasketch" \
    and usuario != "@KTN_Headlines" \
    and usuario != "@Sindh_Times005" \
    and usuario != "@TerI_YaD_A" \
    and usuario != "@arba_putra" \
    and usuario != "@Zawar_News110" \
    and usuario != "@YourNeighbor_P" \
    and usuario != "@AWAZ_E_MEHRAN" \
    and usuario != "@nohoomeday" \
    and usuario != "@ARBA__":
        texto
        print ("Registro del Excel       :" + str(j) + "\n" \
              "Registro planilla limpia :" + str(k) + "\n" \
              "Fecha                    :" + fecha + "\n" \
              "Usuario                  :"  + usuario + "\n" \
              "Texto                    :"  + texto   + "\n" \
              "Url Tweet                :"  + url   + "\n" )
        k = k + 1
        registro = ""
        registro = {"usuario" : usuario,
                "fecha" : fecha,
                "texto" : texto,
                "urlTweet" : url
                #"urlGoogleMaps" : coords
                }
        #post_id = coleccion.insert_one(registro).inserted_id
    j = j + 1





















































        
    
        
        
        
        
