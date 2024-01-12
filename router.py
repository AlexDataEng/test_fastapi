from fastapi import APIRouter, HTTPException, Path, Depends
from config import SessionLocal
from sqlalchemy.orm import Session
from schema import BoockSchema, RequestBook, Response
import crud


router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/create")
def create(request:RequestBook, db:Session=Depends(get_db)):
    crud.create_book(db, book=request.parameter)
    return Response(code=200, status="Ok", message="Book Created Successfully").dict(exclude_none=True)
    
@router.get("/")
def get(db:Session = Depends(get_db)):
    _book = crud.get_book(db, 0, 100)
    return Response(code=200, status="Ok", message="Success Fetch all data", result=_book).dict(exclude_none=True)


@router.get("/{id}")
def get_by_id(id:int, db:Session = Depends(get_db)):
    _book = crud.get_book_by_id(db, id)
    return Response(code=200, status="Ok", message="Succes get data", result=_book).dict(exclude_none=True)


@router.put("/update")
def update_book(request: RequestBook, db:Session=Depends(get_db)):
     _book = crud.update_book(db, book_id=request.parameter.id, 
                              title=request.parameter.title, 
                              description=request.parameter.description)
     return Response(code=200, status="Ok", message="Succes update data", result=_book).dict(exclude_none=True)


@router.default("/{id}")
def delete_book(id:int, db:Session=Depends(get_db)):
    crud.remove_book(db, book_id=id)
    return Response(code=200, status="Ok", message="Success delete data").dict(exclude_none=True)


