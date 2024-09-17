import os
from dotenv import load_dotenv
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

# Cargar variables de entorno
load_dotenv()
# Obtener la contraseña de la variable de entorno
db_password = os.getenv('DB_PASSWORD')
uri = f"mongodb+srv://admin:{db_password}@cluster0.rsnsq.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

# Send a ping to confirm a successful connection
try:
    collectionActive ='supermercados'
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
    # Conectar a la base de datos "datosPrueba"
    db = client["datosprueba"]

    # Conectar a la colección "supermercados"
    collection = db[collectionActive]

    print(f"Conectado exitosamente a la base de datos datosprueba y a la colección {collectionActive}")

    
    # Ejemplo: Contar los documentos en la colección
    document_count = collection.count_documents({})
    print(f"Número de documentos en la colección 'supermercados': {document_count}")
    
    '''
    # Ejemplo: Insertar un documento
    nuevo_documento = {"nombre": "Supermercado XYZ", "ubicacion": "Ciudad ABC"}
    resultado_insercion = collection.insert_one(nuevo_documento)
    print(f"Documento insertado con ID: {resultado_insercion.inserted_id}")
    '''

    '''
    # Contar documentos antes de la eliminación
    count_before = collection.count_documents({"nombre": "Supermercado XYZ"})
    print(f"Número de documentos con nombre 'Supermercado XYZ' antes de la eliminación: {count_before}")
    # Eliminar todos los documentos donde nombre es "Supermercado XYZ"
    result = collection.delete_many({"nombre": "Supermercado XYZ"})
    # Imprimir el número de documentos eliminados
    print(f"Número de documentos eliminados: {result.deleted_count}")
    # Contar documentos después de la eliminación
    count_after = collection.count_documents({"nombre": "Supermercado XYZ"})
    print(f"Número de documentos con nombre 'Supermercado XYZ' después de la eliminación: {count_after}")
    '''

    # Ejemplo: Consultar documentos
    print(f"Documentos en la colección {collectionActive}:")
    for documento in collection.find().limit(5):
        #print(documento, end='\n\n')
        super = documento['supermercado']
        fecha = documento['fecha']
        descrip = documento['descrip']
        precio = documento['precio']
        print(f"Fecha: {fecha}, Super: {super}, Descrip.: {descrip}, Precio: {precio} ")

    '''
    #consultar todos los documentos pero en lotes de a diez documentos cada lote.
    batch_size = 10
    for i in range(0, document_count, batch_size):
        for documento in collection.find().skip(i).limit(batch_size):
            print(documento)
    '''
except Exception as e:
    print(e)

finally:
    # Cerrar la conexión al cliente
    client.close()
    print("Conexión cerrada")