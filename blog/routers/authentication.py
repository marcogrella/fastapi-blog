from fastapi import APIRouter, Depends, status, HTTPException
from blog import schemas, database, models, hashing, tokengenerator
from sqlalchemy.orm import Session
from blog.hashing import Hash
from fastapi.security import OAuth2PasswordRequestForm




router = APIRouter()


router = APIRouter(
    prefix="/login",
     tags=['Authentication']
)

# o login não utiliza o login e senha no formulário de requisição.

@router.post('/')
def login(request: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(database.get_db)):
    user = db.query(models.User).filter(models.User.email == request.username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"User {request.username} not found.")
    if not Hash.verify(user.password, request.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"The password is incorrect.")

    access_token = tokengenerator.create_access_token(data={"sub": user.email})

    return {"access_token": access_token, "token_type": "bearer"}

