from app.utils.imports import app, router, Base, engine, get_db, ProductSchema, StarletteHTTPException, PlainTextResponse, CORSMiddleware, sys, Path, relationship, Column, Integer, String, Date, ForeignKey, Table, relationship, DateTime, BaseModel, Optional
class ArtistBase(BaseModel):
    name: str
    genre: str

class ArtistCreate(ArtistBase):
    pass

class Artist(ArtistBase):
    id: int

    class Config:
        orm_mode = True