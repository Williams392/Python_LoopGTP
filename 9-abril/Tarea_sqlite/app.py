import os
import sqlite3
from dotenv import load_dotenv

load_dotenv()  

DB_NAME = os.getenv('DB_NAME')


class Movie:
    def __init__(self, title, year, score):
        self.title = title
        self.year = year
        self.score = score

    def save(self):
        con, cursor = Database.connect()
        cursor.execute("""INSERT INTO movie 
                    (title, year, score) VALUES 
                    (?, ?, ?)
                """, (self.title, self.year, self.score))
        con.commit()
        con.close()

    @staticmethod
    def select_all():
        con, cursor = Database.connect()
        cursor.execute("SELECT * FROM movie")
        movies = cursor.fetchall()
        con.close()
        return [Movie(*movie) for movie in movies]

    def __str__(self):
        return f"Title: {self.title}, Year: {self.year}, Score: {self.score}"


class Database:
    @staticmethod
    def connect():
        con = sqlite3.connect(DB_NAME)
        return con, con.cursor()

    @staticmethod
    def create_table():
        con, cursor = Database.connect()
        cursor.execute("CREATE TABLE IF NOT EXISTS movie(title TEXT NOT NULL, year INTEGER NOT NULL, score REAL)")
        con.close()


# Crear la tabla si no existe
Database.create_table()

# Crear películas y guardarlas en la base de datos
movies = [
    Movie("Top Gun", 2022, 9.99),
    Movie("Batman", 2022, 9.5),
    Movie("Rápido y furioso", 2021, 8.9),
]

for movie in movies:
    movie.save()

# Seleccionar todas las películas de la base de datos
movies = Movie.select_all()

# Imprimir las películas
for movie in movies:
    print(movie)

