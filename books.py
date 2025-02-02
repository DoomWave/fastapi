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


@app.get("/books")
async def read_all_books():
    return BOOKS

@app.get("/books/{dynamic_param}")
async def read_all_books(dynamic_param):
    return{'dynamic_param': dynamic_param}
