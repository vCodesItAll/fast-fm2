from app.utils.imports import app, router, Base, engine, get_db, ProductSchema, StarletteHTTPException, PlainTextResponse, CORSMiddleware, sys, Path, relationship, Column, Integer, String, Date, ForeignKey, Table, relationship, DateTime, BaseModel, Optional

class PlayBase(BaseModel):
    song_id: int
    user_id: int
    played_at: Optional[str]

class PlayCreate(PlayBase):
    pass

class Play(PlayBase):
    id: int

    class Config:
        orm_mode = True
