from fastapi import FastAPI
from app.api.v1.endpoints import book

app = FastAPI()

app.include_router(book.router, prefix="/api/v1/doc", tags=["example"])

@app.get("/")
def read_root():
    return {"message": "Hello World"}
