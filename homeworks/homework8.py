import sqlite3

DB_NAME = "library.db"

def reset_database():
    """Удаляет старые таблицы, если они существуют."""
    with sqlite3.connect(DB_NAME) as conn:
        cur = conn.cursor()
        cur.execute("DROP TABLE IF EXISTS books")
        cur.execute("DROP TABLE IF EXISTS genres")
        conn.commit()

def create_tables():
    """Создает таблицы genres и books."""
    with sqlite3.connect(DB_NAME) as conn:
        cur = conn.cursor()
        cur.execute("""
        CREATE TABLE genres (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT UNIQUE
        )
        """)
        cur.execute("""
        CREATE TABLE books (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            author TEXT,
            publication_year INTEGER,
            number_of_pages INTEGER,
            number_of_copies INTEGER,
            genre_id INTEGER,
            UNIQUE(name, author, publication_year),
            FOREIGN KEY (genre_id) REFERENCES genres(id)
        )
        """)
        conn.commit()

def insert_genres():
    """Заполняет таблицу жанров."""
    genres = [("Роман",), ("Роман в стихах",), ("Фантастика",), ("Детектив",)]
    with sqlite3.connect(DB_NAME) as conn:
        cur = conn.cursor()
        cur.executemany("INSERT INTO genres (name) VALUES (?)", genres)
        conn.commit()

def insert_books():
    """Заполняет таблицу книг с правильными genre_id."""
    with sqlite3.connect(DB_NAME) as conn:
        cur = conn.cursor()
        cur.execute("SELECT id, name FROM genres")
        genre_map = {name: id for id, name in cur.fetchall()}

        books = [
            ("Преступление и наказание", "Ф.М. Достоевский", 1866, 545, 3, "Роман"),
            ("Мастер и Маргарита", "М.А. Булгаков", 1967, 480, 5, "Роман"),
            ("Война и мир", "Л.Н. Толстой", 1869, 1225, 2, "Роман"),
            ("Анна Каренина", "Л.Н. Толстой", 1877, 864, 4, "Роман"),
            ("Евгений Онегин", "А.С. Пушкин", 1833, 384, 7, "Роман в стихах"),
        ]

        books_prepared = [
            (name, author, year, pages, copies, genre_map[genre])
            for name, author, year, pages, copies, genre in books
        ]

        cur.executemany("""
            INSERT INTO books
            (name, author, publication_year, number_of_pages, number_of_copies, genre_id)
            VALUES (?, ?, ?, ?, ?, ?)
        """, books_prepared)
        conn.commit()

def fetch_books_with_genres():
    """Выводит книги с названиями жанров через JOIN."""
    with sqlite3.connect(DB_NAME) as conn:
        cur = conn.cursor()
        cur.execute("""
            SELECT books.id, books.name, books.author, books.publication_year,
                   books.number_of_pages, books.number_of_copies, genres.name
            FROM books
            JOIN genres ON books.genre_id = genres.id
            ORDER BY books.publication_year
        """)
        return cur.fetchall()

if __name__ == "__main__":
    reset_database()
    create_tables()
    insert_genres()
    insert_books()
    books = fetch_books_with_genres()
    print("📚 Список книг с жанрами:")
    for b in books:
        print(f"ID: {b[0]} | Название: {b[1]} | Автор: {b[2]} | Год: {b[3]} | "
              f"Страниц: {b[4]} | Копий: {b[5]} | Жанр: {b[6]}")


