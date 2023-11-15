from app.utils.imports import app, router, Base, engine, get_db, ProductSchema, StarletteHTTPException, PlainTextResponse, CORSMiddleware, sys, Path, relationship, Column, Integer, String, Date, ForeignKey, Table, relationship, DateTime

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, index=True)
    email = Column(String, unique=True, index=True)
    # Other user attributes here

    playlists = relationship("Playlist", back_populates="user")  # Relationship with playlists
    plays = relationship("Play", back_populates="user")  # Relationship with plays

    # Implement additional functionality, like returning user data as a dictionary
    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}
