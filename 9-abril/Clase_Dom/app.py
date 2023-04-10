
import os
import sqlite3
from dotenv import load_dotenv

load_dotenv()  

DB_NAME = os.getenv('DB_NAME')

def connect_to_database(db):
    con = sqlite3.connect(db)
    return con, con.cursor()

# para crear a base de datos:
con, cursor = connect_to_database(DB_NAME)

# movie -> nombre de la tabla
def create_table():
    cursor.execute("CREATE TABLE IF NOT EXISTS movie(title TEXT NOT NULL, year INTEGER NOT NULL, score REAL)")

def save_movie(title, year, score): # variables GLOBALES
     # lo de adentro -> variables LOCALES
    cursor.execute("""INSERT INTO movie 
                (title, year, score) VALUES 
                (?, ?, ?)
            """, (title, year, score))
    con.commit()


def select_all_movies():
    cursor.execute("SELECT * FROM movie")
    lista_movies = cursor.fetchall()
    return lista_movies

save_movie("Top Gun", 2022 , 9.99)

lista_movies = select_all_movies()


# hacer e recorrido en for -> para mostrar una Lista(mas bonita)
for movie in lista_movies:
    print(movie)









#---------------------------------------------------------------

# Paso 1 -> en Consola: (Crear el ENTORNO VIRTUAL -> venv), url -> https://docs.python.org/3/library/venv.html
# comando -> [python3 -m venv venv], se crear la carpeta -> [venv]

#---------------------------------------------------------------

# Paso 2 -> crear e archivo -> [.env]
# Y poner esot (DB_NAME = "database.db") IMPORTANTE

#---------------------------------------------------------------

# Paso 3 -> activar el modo virtual en consola:
# comando -> [source venv/bin/activate]

#---------------------------------------------------------------

# Paso 4 -> Instalar (python-dotenv)
# comando -> [pip install python-dotenv]

#---------------------------------------------------------------

# # Paso 5 -> Para guardar todas las LIBRERIAS Instaladas.
# comando -> [pip freeze > requirements.txt]

# En el caso de una nueva carpta para tener ya las librerias instalads que dio LA OTRA PERSONA:
# comando -> [pip install -r requirements.txt]

#---------------------------------------------------------------


# Fallas:-------------------------------------------------------
# -> en el caso de fallas con conexion python 3.10.10(venv)
# https://www.youtube.com/watch?v=P9wR8STuygk&ab_channel=willjw3
# ( Ctrl+Shift+P ), comando Python: Create Environment
#---------------------------------------------------------------