from fastapi import FastAPI, HTTPException, Depends, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from app.models import Book
from app.cassandra_db import insert_book, get_book
from app.cache import get_cached_book, set_cached_book
from app.auth import create_access_token, get_current_user
from app.users import verify_user

app = FastAPI()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

@app.post("/login")
def login(form_data: OAuth2PasswordRequestForm = Depends()):
    user = verify_user(form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token = create_access_token(data={"sub": user.username})
    return {"access_token": access_token, "token_type": "bearer"}

@app.post("/books/")
def add_book(book: Book, current_user: str = Depends(get_current_user)):
    insert_book(book.book_id, book.title)
    return {"status": "Book Added"}

@app.get("/books/{book_id}")
def read_book(book_id: str, current_user: str = Depends(get_current_user)):
    cached = get_cached_book(book_id)
    if cached:
        return {"book_id": book_id, "title": cached, "cached": True}
    book = get_book(book_id)
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    
    set_cached_book(book.book_id, book.title)
    return {"book_id": book.book_id, "title": book.title, "cached": False}