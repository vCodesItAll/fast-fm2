# from app.utils.imports import app, router, Base, engine, get_db, StarletteHTTPException, PlainTextResponse, CORSMiddleware, sys, Path, relationship, Column, Integer, String, Date, ForeignKey, Table, relationship, DateTime, BaseModel, Optional, List, Session, database, APIRouter, Depends, SessionLocal,FastAPI, AlbumModel, ArtistModel, GenreModel, PlaylistModel, PlaysModel, SongModel, UserModel, Album, AlbumBase, AlbumCreate, Artist, ArtistBase, ArtistCreate, Genre, GenreBase, GenreCreate, Playlist, PlaylistBase, PlaylistCreate, Plays, PlaysBase, PlaysCreate, Song, SongBase, SongCreate, User, UserBase, UserCreate 
from app.utils.imports import Base, Column, Integer, ForeignKey, relationship, DateTime


class PlaysModel(Base):
    __tablename__ = "plays"

    id = Column(Integer, primary_key=True, index=True)
    song_id = Column(Integer, ForeignKey('songs.id'))  # Reference to the songs table
    user_id = Column(Integer, ForeignKey('users.id'))  # Reference to the users table
    played_at = Column(DateTime)  # Timestamp when the song was played

    song = relationship("Song", back_populates="plays")  # Relationship with songs
    user = relationship("User", back_populates="plays")  # Relationship with users

    # Implement additional functionality, like returning play data as a dictionary
    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}