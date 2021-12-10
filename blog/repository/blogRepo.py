from sqlalchemy.orm import Session
from blog import models, database, schemas
from fastapi import HTTPException, Response, status


def get_All(db: Session):
    blogs = db.query(models.Blog).all()
    return blogs


def get_ById(id: int, db: Session):
    blog_query = db.query(models.Blog).filter(models.Blog.id == id)
    if blog_query.first() == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog with id: {id} does not exist.")
    return blog_query.first()


def create(request: schemas.Blog, db: Session):
    new_blog = models.Blog(title=request.title, body=request.body,
                           user_id=1)  # conversão do objeto da requisição no objeto modelo.
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog


def destroy(id: int, db: Session):
    blog_query = db.query(models.Blog).filter(models.Blog.id == id)
    if blog_query.first() == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog with id: {id} does not exist.")
    blog_query.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)


def update(id: int,request: schemas.Blog, db: Session):
    blog_query = db.query(models.Blog).filter(models.Blog.id == id)
    blog = blog_query.first()
    if blog == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"blog with id: {id} does not exist.")
    blog_query.update(request.dict(), synchronize_session=False)
    db.commit()
    return blog_query.first()