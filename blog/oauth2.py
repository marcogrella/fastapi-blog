from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from blog import tokengenerator


# nesse arquivo fazemos a validação do token


# login é roteamento no qual o usuário captura o token, no caso é o login.
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")


async def get_current_user(token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )

    return tokengenerator.verify_token(token, credentials_exception)
