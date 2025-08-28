import sqlite3

DB_NAME = "library.db"

def create_table():
    with sqlite3.connect(DB_NAME) as conn:
        cur = conn.cursor()
        cur.execute("""
        CREATE TABLE IF NOT EXISTS books (
            name TEXT,
            author TEXT,
            publication_year INTEGER,
            genre TEXT,
            number_of_pages INTEGER,
            number_of_copies INTEGER,
            -- чтобы не плодить дубли при повторных запусках
            UNIQUE(name, author, publication_year)
        )
        """)
        conn.commit()

def insert_books():
    books_data = [
        ("Преступление и наказание", "Ф.М. Достоевский", 1866, "Роман", 545, 3),
        ("Мастер и Маргарита", "М.А. Булгаков", 1967, "Роман", 480, 5),
        ("Война и мир", "Л.Н. Толстой", 1869, "Роман", 1225, 2),
        ("Анна Каренина", "Л.Н. Толстой", 1877, "Роман", 864, 4),
        ("Отцы и дети", "И.С. Тургенев", 1862, "Роман", 320, 6),
        ("Герой нашего времени", "М.Ю. Лермонтов", 1840, "Роман", 230, 3),
        ("Евгений Онегин", "А.С. Пушкин", 1833, "Роман в стихах", 384, 7),
        ("Доктор Живаго", "Б.Л. Пастернак", 1957, "Роман", 592, 2),
        ("Идиот", "Ф.М. Достоевский", 1869, "Роман", 768, 4),
        ("Белая гвардия", "М.А. Булгаков", 1925, "Роман", 432, 5),
    ]
    with sqlite3.connect(DB_NAME) as conn:
        cur = conn.cursor()
        cur.executemany("""
            INSERT OR IGNORE INTO books
            (name, author, publication_year, genre, number_of_pages, number_of_copies)
            VALUES (?, ?, ?, ?, ?, ?)
        """, books_data)
        conn.commit()

def delete_book(book_name: str):
    with sqlite3.connect(DB_NAME) as conn:
        cur = conn.cursor()
        cur.execute("DELETE FROM books WHERE name = ?", (book_name,))
        conn.commit()

# Вспомогательные функции для наглядной проверки
def count_books() -> int:
    with sqlite3.connect(DB_NAME) as conn:
        cur = conn.cursor()
        cur.execute("SELECT COUNT(*) FROM books")
        return cur.fetchone()[0]

def fetch_all():
    with sqlite3.connect(DB_NAME) as conn:
        cur = conn.cursor()
        cur.execute("""SELECT name, author, publication_year, genre,
                              number_of_pages, number_of_copies
                       FROM books ORDER BY publication_year""")
        return cur.fetchall()

if __name__ == "__main__":
    create_table()
    insert_books()
    before = count_books()
    delete_book("Идиот")        # демонстрация удаления
    after = count_books()

    print(f"✅ Таблица создана. До удаления: {before} записей. После удаления: {after}.")
    print("Первые 5 записей:")
    for row in fetch_all()[:5]:
        print(row)

