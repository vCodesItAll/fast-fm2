from app.utils.imports import app, router, Base, engine, get_db, ProductSchema, StarletteHTTPException, PlainTextResponse, CORSMiddleware, sys, Path, relationship, Column, Integer, String, Date, ForeignKey, Table, relationship, DateTime, BaseModel, Optional

class PlaylistBase(BaseModel):
    name: str
    user_id: int

class PlaylistCreate(PlaylistBase):
    pass

class Playlist(PlaylistBase):
    id: int

    class Config:
        orm_mode = True
