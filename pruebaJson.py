from pprint import pprint
from io import open
import json
#Unicode is an appropriate type here. The JSONDecoder docs describe the conversion 
#table and state that json string objects are decoded into Unicode objects
#https://docs.python.org/2/library/json.html#encoders-and-decoders

#JSON                    Python
#==================================
#object                  dict
#array                   list
#string                  unicode
#number (int)            int, long
#number (real)           float
#true                    True
#false                   False
#null                    None
#"encoding determines the encoding used to interpret any str objects decoded by 
#this instance (UTF-8 by default)."

datosJson = open("tuits.json") 
leido = json.load(datosJson)
#pprint(leido["tres"]["usuario"])
pprint (leido)

#data.append("cero")
#data.append("uno")
#data.append("dos")
#pprint(data[:])

       