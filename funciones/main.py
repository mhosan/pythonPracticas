'''
import collections
import sys
import time

print(sys.version)
timestamp = time.time()
print(f"timestamp: {timestamp}")
local = time.localtime()
result = time.asctime(local)
print(f"en formato normal: {result}")
numbers = [12,3,23,4,5,6,7,3,3,3,12,12,12,8,8,8,8,8,8,8,9,10,11,12,13,14,15]
counter = collections.Counter(numbers)
print(counter)
'''

#file = open('./readme.txt')
#print(file.read())
#print(file.readline())
#for line in file:
#  print(line)  
#file.close() 

#con with no hace falta cerrar el archivo, lo cierra el propio with:
#el open es readonly por default. El permiso r+ es para leer y
#escribir y el permiso w+ es para leer y sobreescribir.
'''
with open('./readme.txt', 'r+') as file:  
  for line in file:
    print(line)    
  file.write('Algo nuevo en este archivo... \n')
'''


import utils
import readCsv
import charts
import pandas as pd


def run():
  df = pd.read_csv('world_population.csv')
  df = df[df['Continent'] == 'South America']
  countries = df['Country/Territory'].values
  percentages = df['World Population Percentage'].values
  charts.generate_pie_chart(countries, percentages)

  data = readCsv.read_csv('world_population.csv')
  country = input('Type country => ')
  result = utils.population_by_country(data, country)
  if len(result) > 0:
    country = result[0]
    labels, values = utils.get_population(country)
    charts.generate_bar_chart(labels, values)
  else:
    print("result = 0")

if __name__ == '__main__':
  run()
























