
#------------------
#pip install tweepy
#------------------
import json
import tweepy
from tweepy import OAuthHandler
#from tweepy import request_oauthlib

consumer_key = 'ylJw9EP47UvNE2OBzeuhDD9Dn'
consumer_secret = 'GzESceqtXVlY6YEAfgbIYwE1XW8VOvju367T251CSsP3C3k6Tp'
access_token = '20507804-dJmZz2FzMO8oZiiMNO5wbPzTcx0qMfW5L65DpxWmB'
access_secret = 'GTZvwNgoc4gabk1h9rBchawqejHQMRLQbkOXDe3XwbOPX'

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth)

# Los APImétodos se pueden agrupar en las siguientes categorías:
# 1)  Métodos para las líneas de tiempo del usuario
# 2)  Métodos para tweets. Los tweets aparecen como Status
# 3)  Métodos para usuarios
# 4)  Métodos para seguidores
# 5)  Métodos para tu cuenta
# 6)  Métodos para Me gusta
# 7)  Métodos para bloquear usuarios
# 8)  Métodos para búsquedas
# 9)  Métodos para tendencias
# 10) Métodos para transmitir

#favorite es un like <-------------------------------------------------------------------------
#status es un tweet: <-------------------------------------------------------------------------


# 1) LINEAS DE TIEMPO
"""
for status in tweepy.Cursor(api.home_timeline).items(10):
    print("texto: " + status.text + "\n")
listaObjetosStatus = api.home_timeline()
untuit = listaObjetosStatus[0]
pepe = json.dumps(untuit._json)
print(untuit[0])
"""

#friendship es una relación seguido-seguidor:
for friend in tweepy.Cursor(api.get_friends).items(1):
    print(friend._json)


#for tweet in tweepy.Cursor(api.user_timeline).items(1):
#    print(tweet)


#Lineas de tiempo del usuario: Estos métodos se ocupan de leer tweets, menciones y retuits de su línea de tiempo
#o de la línea de tiempo o de la línea de tiempo de cualquier otro usuario siempre que sea público
"""
timeline = api.home_timeline()
i=0
for tweet in timeline:
	i=i+1
	print(f"{i}) - El usuario {tweet.user.name} DIJO:\n {tweet.text}\n")
"""

#Métodos para Tweets: tienen que ver con crear, buscar y retuitear tweets.
#api.update_status("Probando tweetear desde una aplicación Python. Ahora son las 18:38 del jueves 10 de octubre de 2019")   

#Métodos para usuarios: Permiten buscar usuarios con un criterio de filtro, buscar detalles de usuarios y 
#enumerar los seguidores de cualquier usuario, siempre que sea público
#Ejemplo: buscar mi usuario, @mhosan, y luego imprimir sus detalles, así como sus 20 seguidores más recientes:
"""
user = api.get_user("mhosan")
print("Usuario detlles: ")
print(user.name)
print(user.description)
print(user.location)
print("Ultimos 20 seguidores:")
for follower in user.followers():
	print(follower.name)
"""

#Métodos para seguidores: Se ocupa de seguir y dejar de seguir a los usuarios, consultar a los seguidores de un
# usuario y enumerar las cuentas que sigue cualquier usuario
#Este código muestra como comenzar a seguir a @realpython:
#api.create_friendship("realpython")

#Métodos para su cuenta: Manejar los detalles del perfil.
#Ejemplo: el siguiente código actualiza la descripción del perfil:
#api.update_profile(description="I like Python")

#Métodos para likes: Sirve para marcar cualquier tweet como liked o remover la marca de liked
"""
tweets = api.home_timeline(count=1)
tweet = tweets[0]
print(f"Liking tweet {tweet.id} of {tweet.author.name}")
api.create_favorite(tweet.id)
"""

#Métodos para bloquear usuarios: 
"""
for block in api.blocks():
    print(block.name)
"""

# ---------------------------------------------------------------------------------------
# 8) METODOS PARA BUSQUEDAS 
# ---------------------------------------------------------------------------------------
#Métodos para busquedas: Buscar tweets con texto, idioma y otros filtros:
#Ejemplo: Buscar los 10 tweets públicos mas recientes que estan en español y que contienen
#la palabra Fernandez:
"""
for tweet in api.search(q="*", lang="es", rpp=10):
#for tweet in api.search(q="*", lang="es", rpp=10, geocode="-34.921188, -57.954596, 1500km"):
    print(f"{tweet.user.name}:{tweet.text}")
    print("  ")
    print("----------------------------")
"""


# ---------------------------------------------------------------------------------------
# 9) METODOS PARA TENDENCIAS  
# ---------------------------------------------------------------------------------------
#Métodos para tendencias: Enumerar las tendencias actuales para cualquier
#ubicación geográfica.
#Ejemplo: Como enumerar temas de tendencias mundiales:
"""
trends_result = api.trends_place(1)
for trend in trends_result[0]["trends"]:
    print(trend["name"])
"""
#Utilizando trends_place(), se obtiene la lista de tendencias para cualquier lugar, 
# pasando como único argumento el id del lugar. Aquí, 1 significa en todo el mundo. 
# Se puede ver la lista completa de ubicaciones disponibles usando api.trends_available().


# ---------------------------------------------------------------------------------------
# 10) METODOS PARA STREAMING (transmitir)  
# ---------------------------------------------------------------------------------------
#Métodos para Streaming (transmisión): un kilombo...


# ---------------------------------------------------------------------------------------
# CURSORES   
# ---------------------------------------------------------------------------------------
#Cursores: 
#lista=[]
#for tweet in tweepy.Cursor(api.home_timeline).items(100):
    #print(f"El usuario {tweet.user.name} DIJO:\n {tweet.text}\n")
#	lista.append()

