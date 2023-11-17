# from app.utils.imports import app, router, Base, engine, get_db, StarletteHTTPException, PlainTextResponse, CORSMiddleware, sys, Path, relationship, Column, Integer, String, Date, ForeignKey, Table, relationship, DateTime, BaseModel, Optional, List, Session, database, APIRouter, Depends, SessionLocal,FastAPI, AlbumModel, ArtistModel, GenreModel, PlaylistModel, PlaysModel, SongModel, UserModel, Album, AlbumBase, AlbumCreate, Artist, ArtistBase, ArtistCreate, Genre, GenreBase, GenreCreate, Playlist, PlaylistBase, PlaylistCreate, Plays, PlaysBase, PlaysCreate, Song, SongBase, SongCreate, User, UserBase, UserCreate 
from app.utils.imports import BaseModel, Optional


class PlaysBase(BaseModel):
    song_id: int
    user_id: int
    played_at: Optional[str]

class PlaysCreate(PlaysBase):
    pass

class Plays(PlaysBase):
    id: int

    class Config:
        orm_mode = True
