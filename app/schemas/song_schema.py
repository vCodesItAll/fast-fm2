# from app.utils.imports import app, router, Base, engine, get_db, StarletteHTTPException, PlainTextResponse, CORSMiddleware, sys, Path, relationship, Column, Integer, String, Date, ForeignKey, Table, relationship, DateTime, BaseModel, Optional, List, Session, database, APIRouter, Depends, SessionLocal,FastAPI, AlbumModel, ArtistModel, GenreModel, PlaylistModel, PlaysModel, SongModel, UserModel, Album, AlbumBase, AlbumCreate, Artist, ArtistBase, ArtistCreate, Genre, GenreBase, GenreCreate, Playlist, PlaylistBase, PlaylistCreate, Plays, PlaysBase, PlaysCreate, Song, SongBase, SongCreate, User, UserBase, UserCreate 
from app.utils.imports import BaseModel, Optional, List


class SongBase(BaseModel):
    title: str
    duration_seconds: int
    release_date: Optional[str]
    album_id: Optional[int]

class SongCreate(SongBase):
    pass

class Song(SongBase):
    id: int
    artists: List[int] = []
    playlists: List[int] = []
    genres: List[int] = []

    class Config:
        orm_mode = True
