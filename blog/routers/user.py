from fastapi import APIRouter, Depends, status, Response, HTTPException
from blog import schemas, models, database
import psycopg2
from psycopg2.extras import RealDictCursor
from sqlalchemy.orm import Session
from typing import List
from repository import userRepo


router = APIRouter(
    prefix = "/user",
    tags=['Users']
)


@router.post('/', status_code = status.HTTP_201_CREATED, response_model = schemas.ShowUser)
def create(request: schemas.User, db: Session = Depends(database.get_db)):
    return userRepo.create(request, db)


@router.get('/{id}', response_model = schemas.ShowUser)
def get_By_Id(id: int, response: Response, db: Session = Depends(database.get_db)):
    return userRepo.findById(id, db)