from app.utils.imports import app, router, Base, engine, get_db, StarletteHTTPException, PlainTextResponse, CORSMiddleware, sys, Path, relationship, Column, Integer, String, Date, ForeignKey, Table, relationship, DateTime, BaseModel, Optional, List, Session, schemas, models, controllers, utils, database, APIRouter, Depends, SessionLocal
class UserBase(BaseModel):
    username: str
    email: str

class UserCreate(UserBase):
    password: str
    email: str

class User(UserBase):
    id: int

    class Config:
        orm_mode = True
