from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from datetime import datetime

from .database import Base

class ItemWithCategory(Base):
    __tablename__ = "item_with_category"

    id = Column(Integer, primary_key=True)
    item_id = Column(Integer, ForeignKey("item.id"))
    item_category_id = Column(Integer, ForeignKey("item_category.id"))
    created_at = Column(DateTime, default=datetime.now())
    updated_at = Column(DateTime, onupdate=datetime.now())
    
    item = relationship("Item", back_populates="item_with_categories")
    item_category = relationship("ItemCategory", back_populates="item_with_categories")

class Item(Base):
    __tablename__ = "item"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    description = Column(String)
    created_at = Column(DateTime, default=datetime.now())
    updated_at = Column(DateTime, onupdate=datetime.now())
    is_deleted = Column(Boolean, default=False)
    item_with_categories = relationship("ItemWithCategory", back_populates="item")


class ItemCategory(Base):
    __tablename__ = "item_category"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    created_at = Column(DateTime, default=datetime.now())
    updated_at = Column(DateTime, onupdate=datetime.now())
    is_deleted = Column(Boolean, default=False) 
    item_with_categories = relationship("ItemWithCategory", back_populates="item_category")

