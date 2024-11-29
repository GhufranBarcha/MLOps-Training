from fastapi import FastAPI, HTTPException
from pydantic import BaseModel , Field
from uuid import UUID , uuid4


app = FastAPI()

class BOOK(BaseModel):
    id: UUID
    title: str = Field(min_length=1)
    author: str = Field(min_length=1 , max_length=100)
    description: str = Field(min_length=1 ,max_length=100)
    rating: int = Field(gt = -1 , lt = 5)

BOOKS = []

@app.get("/")
def read_api():
    return BOOKS



@app.post("/")
def create_book(book: BOOK):
    BOOKS.append(book)
    return  book


@app.put("/{book_id}")
def update_book(book_id: UUID, book: BOOK):
    counter = 0

    for x in BOOKS:
        counter += 1
        if x.id == book_id:
            BOOKS[counter - 1] = book
            return BOOKS[counter - 1]
    raise HTTPException(
        status_code=404,
        detail=f"ID {book_id} not found",
    ) 

@app.delete("/{book_id}")
def delete_book(book_id: UUID):
    counter = 0

    for x in BOOKS:
        counter += 1
        if x.id == book_id:
            del BOOKS[counter - 1]
            return f"ID {book_id} deleted"
    raise HTTPException(
        status_code=404,
        detail=f"ID {book_id} not found",    
    )
