# main.py
from fastapi import FastAPI
from Core.database import engine, Base
from Presentation.endpoints import router as user_router

# Automatically create database tables on startup
Base.metadata.create_all(bind=engine)

app = FastAPI(title="User Management API - SQL ALCHEMY ORM")

# Register presentation routing
app.include_router(user_router)