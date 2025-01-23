from sqlalchemy.orm import Session
from app.models.BookModel import Book
from app.schemas.bookSchema import BookSchema

async def create_book(db: Session, book: BookSchema) -> Book:
    db_book = Book(
        id=book.id,
        name=book.name,
        description=book.description
    )

    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return db_book

async def get_book(db, book_id):
    # Function to retrieve an book entry by its ID
    db_book = db.query(Book).filter(Book.id == book_id).first()
    return db_book

async def update_book(db, book_id, book_data: BookSchema):
    # Function to update an existing example entry
    db_book = db.query(Book).filter(Book.id == book_id).first()
    db_book.name = book_data.name
    db_book.description = book_data.description
    db.commit()
    db.refresh(db_book)
    return db_book


async def delete_book(db, book_id):
    # Function to delete an example entry by its ID
    db_book = db.query(Book).filter(Book.id == book_id).first()
    db.delete(db_book)
    db.commit()
    return True
