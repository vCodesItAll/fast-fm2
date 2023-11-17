from typing import List
from typing import Optional

from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, text, Table, TIMESTAMP
from database import Base

class ProductModel (Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, nullable=False)
    title = Column(String, nullable=False)
    description = Column(String, nullable=False)
    at_sale = Column(Boolean, server_default=text('false'))
    inventory = Column(Integer, server_default=text('0'), nullable=False)
    added_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('Now()'))

# from sqlalchemy.orm import relationship, declarative_base
# from sqlalchemy import Column, ForeignKey, Integer, String, Float

# Base = declarative_base()

# class Category(Base):
#     __tablename__ = "categories"

#     id = Column(Integer, primary_key=True, index=True)
#     name = Column(String)

# class Cuisine(Base):
#     __tablename__ = "cuisines"

#     id = Column(Integer, primary_key=True, index=True)
#     name = Column(String)

# class MenuItem(Base):
#     __tablename__ = "menu_items"

#     id = Column(Integer, primary_key=True, index=True)
#     title = Column(String)
#     description = Column(String)
#     price = Column(Float)
#     spicy_level = Column(Integer)
#     category_id = Column(Integer, ForeignKey("categories.id"))
#     cuisine_id = Column(Integer, ForeignKey("cuisines.id"))

#     category = relationship("Category", back_populates="menu_items")
#     cuisine = relationship("Cuisine", back_populates="menu_items")

# Category.menu_items = relationship("MenuItem", back_populates="category")
# Cuisine.menu_items = relationship("MenuItem", back_populates="cuisine")

