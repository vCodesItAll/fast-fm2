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

from database import engine, get_db, SessionLocal
from starlette.exceptions import HTTPException as StarletteHTTPException

# Create instances or objects where necessary
app = FastAPI()
router = APIRouter()
Base = declarative_base()

import sys, models, schemas, app.utils, database
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parent.parent / 'utils'))
from typing import Optional, List
from pytest import Session


# Import all models
from app.models.album_model import AlbumModel
from app.models.artist_model import ArtistModel
from app.models.genre_model import GenreModel
from app.models.playlist_model import PlaylistModel
from app.models.plays_model import PlaysModel
from app.models.song_model import SongModel
from app.models.user_model import UserModel

# Import all schemas
from app.schemas.album_schema import Album, AlbumBase, AlbumCreate
from app.schemas.artist_schema import Artist, ArtistBase, ArtistCreate
from app.schemas.genre_schema import Genre, GenreBase, GenreCreate
from app.schemas.playlist_schema import Playlist, PlaylistBase, PlaylistCreate
from app.schemas.plays_schema import Plays, PlaysBase, PlaysCreate
from app.schemas.song_schema import Song, SongBase, SongCreate
from app.schemas.user_schema import User, UserBase, UserCreate

# Import all routes
from app.utils import creates

# Import all controllers
from app import controllers

# copy this import into other files
# from app.utils.imports import app, router, Base, engine, get_db, StarletteHTTPException, PlainTextResponse, CORSMiddleware, sys, Path, relationship, Column, Integer, String, Date, ForeignKey, Table, relationship, DateTime, BaseModel, Optional, List, Session, database, APIRouter, Depends, SessionLocal,FastAPI, AlbumModel, ArtistModel, GenreModel, PlaylistModel, PlaysModel, SongModel, UserModel, Album, AlbumBase, AlbumCreate, Artist, ArtistBase, ArtistCreate, Genre, GenreBase, GenreCreate, Playlist, PlaylistBase, PlaylistCreate, Plays, PlaysBase, PlaysCreate, Song, SongBase, SongCreate, User, UserBase, UserCreate 

