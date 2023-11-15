from app.utils.imports import app, router, Base, engine, get_db, ProductSchema, StarletteHTTPException, PlainTextResponse, CORSMiddleware, sys, Path, relationship, Column, Integer, String, Date, ForeignKey, Table, relationship, DateTime, BaseModel, Optional

class AlbumBase(BaseModel):
    title: str
    release_date: Optional[str]

class AlbumCreate(AlbumBase):
    pass

class Album(AlbumBase):
    id: int

    class Config:
        orm_mode = True
