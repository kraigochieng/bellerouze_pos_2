from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from datetime import datetime
from sqlalchemy_serializer import SerializerMixin

from .database import Base

class ItemWithCategory(Base, SerializerMixin):
    __tablename__ = "item_with_category"

    id = Column(Integer, primary_key=True)
    item_id = Column(Integer, ForeignKey("item.id"))
    item_category_id = Column(Integer, ForeignKey("item_category.id"))
    created_at = Column(DateTime, default=datetime.now())
    updated_at = Column(DateTime, onupdate=datetime.now())
    is_deleted = Column(Boolean, default=False)

    item = relationship("Item", back_populates="item_with_categories")
    item_category = relationship("ItemCategory", back_populates="item_with_categories")

class Item(Base, SerializerMixin):
    __tablename__ = "item"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    description = Column(String)
    created_at = Column(DateTime, default=datetime.now())
    updated_at = Column(DateTime, onupdate=datetime.now())
    is_deleted = Column(Boolean, default=False)

    item_with_categories = relationship("ItemWithCategory", back_populates="item")
    items_on_orders = relationship("ItemInOrder", back_populates="item")

class ItemCategory(Base, SerializerMixin):
    __tablename__ = "item_category"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    created_at = Column(DateTime, default=datetime.now())
    updated_at = Column(DateTime, onupdate=datetime.now())
    is_deleted = Column(Boolean, default=False) 
    
    item_with_categories = relationship("ItemWithCategory", back_populates="item_category")


class Order(Base, SerializerMixin):
    __tablename__ = "order"

    id = Column(Integer, primary_key=True, index=True)
    created_at = Column(DateTime, default=datetime.now())
    updated_at = Column(DateTime, onupdate=datetime.now())
    is_deleted = Column(Boolean, default=False)

    items = relationship("ItemInOrder", back_populates="order")

class ItemInOrder(Base, SerializerMixin):
    __tablename__ = "item_in_order"

    id = Column(Integer, primary_key=True, index=True)
    order_id = Column(Integer, ForeignKey("order.id"))
    item_id = Column(Integer, ForeignKey("item.id"))
    quantity = Column(Integer)
    created_at = Column(DateTime, default=datetime.now())
    updated_at = Column(DateTime, onupdate=datetime.now())
    is_deleted = Column(Boolean, default=False)

    order = relationship("Order", back_populates="items")
    item = relationship("Item", back_populates="items_on_orders")
