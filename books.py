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

@app.get("/api-endpoint")
async def first_api():
    return BOOKS
