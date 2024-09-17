import csv
import os

def read_csv(path):
  os.system('cls')
  with open(path, 'r') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')   #devuelve un iterable
    header = next(reader) #el primer registro del iterable, obtener el encabezado en formato lista
    #print(f"Esto es una lista con el encabezado (titulos) del csv: {header}")
    data=[]
    i=0
    for row in reader: #cada registro del csv es una lista
      i +=1
      iterable = zip(header, row) #<--- zip une los dos arrays en un array de tuplas
      #print('***' * 25,"fila -->", i)
      #print(row)
      #print(list(iterable))
      #-------------------------------------------------
      #crea un diccionario con los valores de cada tupla
      country_dict = {key: value for key, value in iterable} 
      data.append(country_dict)
    return data
   
if __name__ == '__main__':
  data = read_csv('world_population.csv')
  #print(data)
  #print(data[42])
  
  