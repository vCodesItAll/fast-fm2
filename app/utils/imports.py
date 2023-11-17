# Import FastAPI and related modules
from fastapi import FastAPI, APIRouter, Depends, Response, status
from fastapi.responses import JSONResponse, PlainTextResponse
from fastapi.encoders import jsonable_encoder
from fastapi.middleware.cors import CORSMiddleware

# Import SQLAlchemy modules for database operations
from sqlalchemy import create_engine, MetaData, Column, Integer, String, Date, ForeignKey, Table, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session, relationship

# Import Pydantic modules for data validation and serialization
from pydantic import BaseModel

# Other necessary imports used across your project
from schemas import ProductSchema
from database import engine, get_db
from starlette.exceptions import HTTPException as StarletteHTTPException

# Create instances or objects where necessary
app = FastAPI()
router = APIRouter()
Base = declarative_base()

import sys, models, schemas, controllers_formerly_crud, utils, database
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parent.parent / 'utils'))
from typing import Optional, List
from pytest import Session


# copy this import into other files
# from app.utils.imports import app, router, Base, engine, get_db, ProductSchema, StarletteHTTPException, PlainTextResponse, CORSMiddleware, sys, Path, relationship
from app.utils.imports import app, router, Base, engine, get_db, ProductSchema, StarletteHTTPException, PlainTextResponse, CORSMiddleware, sys, Path, relationship, Column, Integer, String, Date, ForeignKey, Table, relationship, DateTime, BaseModel, Optional, List, Session, schemas, models, controllers_formerly_crud, utils, database