# presentation/endpoints.py
from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from typing import Annotated, List

from Core.database import get_db
from Schemas.user_schema import UserCreate, UserResponse
from Business import user_service

router = APIRouter(prefix="/users", tags=["Users"])

@router.post("/", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
def create_user(user: UserCreate, db: Annotated[Session, Depends(get_db)]):
    return user_service.register_new_user(db=db, user=user)

@router.get("/", response_model=List[UserResponse])
def get_users(db: Annotated[Session, Depends(get_db)],skip: int = 0, limit: int = 10,):
    return user_service.fetch_users(db=db, skip=skip, limit=limit)

@router.get("/{user_id}", response_model=UserResponse)
def get_user(user_id: int, db: Annotated[Session, Depends(get_db)]):
    return user_service.fetch_user_by_id(db=db, user_id=user_id)

@router.delete("/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_user(user_id: int, db: Annotated[Session, Depends(get_db)]):
    return user_service.remove_user(db=db, user_id=user_id)