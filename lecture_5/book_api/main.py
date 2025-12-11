from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from database import engine, get_db, Base
import models
import schemas

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Book API",
    description="API for book managment",
    version="1.0.0"
)

# api endpoint
@app.get("/")
def read_root():
    return {"message": "Добро пожаловать в Book API!"}


@app.post("/books/", response_model=schemas.BookResponse)
def create_book(book: schemas.BookCreate, db: Session = Depends(get_db)):

    db_book = models.Book(**book.dict())
    
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    
    return db_book

# for all books
@app.get("/books/", response_model=List[schemas.BookResponse])
def read_books(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    books = db.query(models.Book).offset(skip).limit(limit).all()
    return books

# endpoint to get one book
@app.get("/books/{book_id}", response_model=schemas.BookResponse)
def read_book(book_id: int, db: Session = Depends(get_db)):
    book = db.query(models.Book).filter(models.Book.id == book_id).first()
    
    if book is None:
        raise HTTPException(status_code=404, detail="Книга не найдена")
    
    return book

# update
@app.put("/books/{book_id}", response_model=schemas.BookResponse)
def update_book(book_id: int, book_update: schemas.BookUpdate, db: Session = Depends(get_db)):
    # seacrh a book
    db_book = db.query(models.Book).filter(models.Book.id == book_id).first()
    
    if db_book is None:
        raise HTTPException(status_code=404, detail="Книга не найдена")
    
    update_data = book_update.dict(exclude_unset=True)
    
    for field, value in update_data.items():
        setattr(db_book, field, value)
    
    db.commit()
    db.refresh(db_book)
    
    return db_book

# for delete
@app.delete("/books/{book_id}")
def delete_book(book_id: int, db: Session = Depends(get_db)):
    
    db_book = db.query(models.Book).filter(models.Book.id == book_id).first()
    
    if db_book is None:
        raise HTTPException(status_code=404, detail="Книга не найдена")
    
    db.delete(db_book)
    db.commit()
    
    return {"message": "Книга успешно удалена"}