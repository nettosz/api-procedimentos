from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.models.BookModel import Book
from app.schemas.bookSchema import BookSchema
from app.crud.books import create_book, get_book, update_book, delete_book
from app.database import get_db
router = APIRouter()

@router.post("/create", response_model=BookSchema)
async def create_book_endpoint(book: BookSchema, db: Session = Depends(get_db)):
    return await create_book(db=db, book=book)

@router.get("/get/{book_id}", response_model=BookSchema)
async def read_book(book_id: int, db: Session = Depends(get_db)):
    example = await get_book(book_id=book_id, db=db)
    if example is None:
        raise HTTPException(status_code=404, detail="Book not found")
    return example

@router.put("/update/{book_id}", response_model=BookSchema)
async def update_book_endpoint(book_id: int, book: BookSchema, db: Session = Depends(get_db)):
    updated_example = await update_book(book_id=book_id, book_data=book, db=db)
    if updated_example is None:
        raise HTTPException(status_code=404, detail="Book not found")
    return updated_example

@router.delete("/delete/{book_id}", response_model=dict)
async def delete_book_endpoint(book_id: int, db: Session = Depends(get_db)):
    result = await delete_book(book_id=book_id, db=db)
    if not result:
        raise HTTPException(status_code=404, detail="Book not found")
    return {"detail": "Book deleted successfully"}

