from fastapi import FastAPI,HTTPException
from app.models import Book
from app.cassandra_db import insert_book,get_book
from app.cache import get_cached_book,set_cached_book

app = FastAPI()

@app.post("/books/")
def add_book(book:Book):
    insert_book(book.book_id,book.title)
    return {"status":"Book Added"}

@app.get("/books/{book_id}")
def read_book(book_id:str):
    cached = get_cached_book(book_id)
    if cached:
        return {"book_id":book_id,"title":cached,"cached":True}
    book= get_book(book_id)
    if not book:
        raise HTTPException(status_code=404,detail="Book not found")
    
    set_cached_book(book.book_id,book.title)
    return {"book_id":book.book_id,"title":book.title,"cached":False}

