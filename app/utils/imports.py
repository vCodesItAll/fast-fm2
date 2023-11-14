# Import FastAPI and related modules
from fastapi import FastAPI, APIRouter, Depends, Response, status
from fastapi.responses import JSONResponse, PlainTextResponse
from fastapi.encoders import jsonable_encoder
from fastapi.middleware.cors import CORSMiddleware

# Import SQLAlchemy modules for database operations
from sqlalchemy import create_engine, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session

# Import Pydantic modules for data validation and serialization
from pydantic import BaseModel

# Other necessary imports used across your project
import models
from schemas import ProductSchema
from database import engine, get_db
from starlette.exceptions import HTTPException as StarletteHTTPException

# Create instances or objects where necessary
app = FastAPI()
router = APIRouter()
Base = declarative_base()


