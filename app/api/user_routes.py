from app.utils.imports import app, router, Base, engine, get_db, StarletteHTTPException, PlainTextResponse, CORSMiddleware, sys, Path, relationship, Column, Integer, String, Date, ForeignKey, Table, relationship, DateTime, BaseModel, Optional, List, Session, schemas, models, controllers, utils, database, APIRouter, Depends, SessionLocal
from app.utils import creates
from app.schemas.user_schema import User, UserCreate

router = APIRouter()

router.include_router(creates.router)


