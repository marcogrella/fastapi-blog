from fastapi import APIRouter, Depends, status, Response, HTTPException
from blog import schemas, models, database, oauth2
import psycopg2
from psycopg2.extras import RealDictCursor
from sqlalchemy.orm import Session
from typing import List
from repository import blogRepo


router = APIRouter(
    prefix="/blog",
     tags=['Blogs']
)
# OBS: o current_user: schemas.User = Depends(oauth2.get_current_user)) faz com que a cada requisição seja verificada
# o usuário, se possui token, se está expirado. Faz uso do método get_current_user em oauth2

# o objeto db: Session é um objeto do sqlalchemy, mas que depende da implementação da sessão que vem da base de dados.

@router.post('/', status_code = status.HTTP_201_CREATED)
def create(request: schemas.Blog, db: Session = Depends(database.get_db),
           current_user: schemas.User = Depends(oauth2.get_current_user)):
   return blogRepo.create(request, db)


@router.get('/', response_model=List[schemas.ShowBlog])
def get_all(db: Session = Depends(database.get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return blogRepo.get_All(db)


@router.get('/{id}', status_code = status.HTTP_200_OK, response_model=schemas.ShowBlog)
def get_by_id(id: int, response: Response, db: Session = Depends(database.get_db),
              current_user: schemas.User = Depends(oauth2.get_current_user)):
    return blogRepo.get_ById(id, db)


@router.delete('/{id}', status_code = status.HTTP_204_NO_CONTENT)
def delete(id: int, db: Session = Depends(database.get_db),
           current_user: schemas.User = Depends(oauth2.get_current_user)):
    return blogRepo.destroy(id, db)


@router.put('/{id}', status_code = status.HTTP_202_ACCEPTED)
def update(id: int, request: schemas.Blog, db: Session = Depends(database.get_db),
           current_user: schemas.User = Depends(oauth2.get_current_user)):
    return blogRepo.update(id, request, db)
