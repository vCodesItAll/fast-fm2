from app.utils.imports import app, router, Base, engine, get_db, ProductSchema, StarletteHTTPException, PlainTextResponse, CORSMiddleware, sys, Path, relationship, Column, Integer, String, Date, ForeignKey, Table, relationship, DateTime, BaseModel, Optional

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
