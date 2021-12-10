from sqlalchemy.orm import Session
from blog import models, database, schemas
from fastapi import HTTPException, Response, status
from blog.hashing import Hash


def create(request: schemas.User, db: Session):
    hashed_password = Hash.cript(request.password)
    new_user = models.User(name=request.name, email=request.email, password=hashed_password)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


def findById(id: int, db: Session):
    user = db.query(models.User).filter(models.User.id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"User with id {id} is not available")
    return user