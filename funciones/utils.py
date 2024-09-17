import readCsv


def get_population(country_dict):
  population_dict = {
    '2022': int(country_dict['2022 Population']),
    '2020': int(country_dict['2020 Population']),
    '2015': int(country_dict['2015 Population']),
    '2010': int(country_dict['2010 Population']),
    '2000': int(country_dict['2000 Population']),
    '1990': int(country_dict['1990 Population']),
    '1980': int(country_dict['1980 Population']),
    '1970': int(country_dict['1970 Population'])
  }
  return population_dict.keys(), population_dict.values()

def population_by_country(data, country):
  #print(type(data))
  #if isinstance(data, list) and len(data) > 0:
  #  print(type(data[0]))
  #result = list(filter(lambda item: item['Country/Territory'] == country, data))
  result = list(filter(lambda item: item.get('Country/Territory') == country, data))
  #print (result)
  return result

if __name__ == '__main__':
  data = readCsv.read_csv('world_population.csv')
  print(f"data[42]: {data[42]}")
  country = input('Type country => ')
  population_by_country(data, country)
