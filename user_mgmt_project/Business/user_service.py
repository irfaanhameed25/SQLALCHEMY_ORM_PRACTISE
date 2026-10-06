# business/user_service.py
from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from Data_Access import repository
from Schemas.user_schema import UserCreate

def register_new_user(db: Session, user: UserCreate):
    # Business rule: Email must be unique
    existing = repository.get_user_by_email(db, email=user.email)
    if existing:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, 
            detail="Email already registered"
        )
    return repository.create_user(db=db, user=user)

def fetch_user_by_id(db: Session, user_id: int):
    user = repository.get_user_by_id(db, user_id=user_id)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, 
            detail="User not found"
        )
    return user

def fetch_users(db: Session, skip: int, limit: int):
    return repository.get_users(db, skip=skip, limit=limit)

def remove_user(db: Session, user_id: int):
    user = fetch_user_by_id(db, user_id)
    repository.delete_user(db, user)
    return None