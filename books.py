from fastapi import FastAPI

app = FastAPI()


BOOKS = [
    {"title": "Dune", "author": "Frank Herbert", "category":"science fiction"},
    {"title": "Divine Comedy", "author": "Dante Aligheri", "category":"Fiction"},
    {"title": "Harry Potter", "author": "J.K Rowling", "category":"Fantasy"},
    {"title": "Lord of the Rings", "author": "J.R.R Tolkien", "category":"Fantasy"},
    {"title": "The Alchemist", "author": "Paulo Coelho", "category":"Philosophy"},
    {"title": "IT", "author": "Stephen King", "category":"Horror"},
]


@app.get("/Books")
async def read_all_books():
    return BOOKS


@app.get("/books/{book_title}")
async def read_book(book_title: str):
    for book in BOOKS:
        if book.get("title").casefold() == book_title.casefold():
            return book


@app.get("/books/")
async def read_category_by_query(category: str):
    books_to_return = []
    for book in BOOKS:
        if book.get('category').casefold() == category.casefold():
            books_to_return.append(book)
    return books_to_return


@app.get("/books/{books_author}/")
async def read_author_category_by_query(book_author: str, category: str):
    books_to_return = []
    for book in BOOKS:
        if book.get('author').casefold() == book_author.casefold() and \
                book.get('category').casefold() == category.casefold():
            books_to_return.append(book)

            
    return books_to_return
