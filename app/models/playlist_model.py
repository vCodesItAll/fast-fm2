# from app.utils.imports import app, router, Base, engine, get_db, StarletteHTTPException, PlainTextResponse, CORSMiddleware, sys, Path, relationship, Column, Integer, String, Date, ForeignKey, Table, relationship, DateTime, BaseModel, Optional, List, Session, database, APIRouter, Depends, SessionLocal,FastAPI, AlbumModel, ArtistModel, GenreModel, PlaylistModel, PlaysModel, SongModel, UserModel, Album, AlbumBase, AlbumCreate, Artist, ArtistBase, ArtistCreate, Genre, GenreBase, GenreCreate, Playlist, PlaylistBase, PlaylistCreate, Plays, PlaysBase, PlaysCreate, Song, SongBase, SongCreate, User, UserBase, UserCreate 
from app.utils.imports import Base, Column, Integer, String, Date, ForeignKey, Table, relationship


class PlaylistModel(Base):
    __tablename__ = "playlists"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    # Reference to the users table
    user_id = Column(Integer, ForeignKey('users.id'))  
    # Relationship with users
    user = relationship("User", back_populates="playlists")  
    # Relationship with songs via playlist_songs
    songs = relationship("Song", secondary="playlist_songs", back_populates="playlists")  

    # Implement additional functionality, like returning playlist data as a dictionary
    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}
