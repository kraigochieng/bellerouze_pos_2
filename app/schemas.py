from datetime import datetime
from typing import Optional

from pydantic import BaseModel, ConfigDict


class ItemBase(BaseModel):
    name: str
    description: str


class ItemCreate(ItemBase):
    pass


class ItemRead(ItemBase):
    pass


class ItemUpdate(ItemBase):
    pass


class Item(ItemBase):
    id: int

    class Config(ConfigDict):
        from_attributes = True
        extra = "ignore"


class ItemCategoryBase(BaseModel):
    name: str


class ItemCategoryCreate(ItemCategoryBase):
    pass


class ItemCategoryUpdate(ItemCategoryBase):
    pass


class ItemCategory(ItemCategoryBase):
    id: int

    class Config(ConfigDict):
        from_attributes = True
        extra = "ignore"


class ItemWithCategoryBase(BaseModel):
    item_id: int
    item_category_id: int


class ItemWithCategoryCreate(ItemWithCategoryBase):
    pass


class ItemWithCategoryUpdate(ItemWithCategoryBase):
    pass


class ItemWithCategory(ItemWithCategoryBase):
    id: int

    class Config(ConfigDict):
        from_attributes = True
        extra = "ignore"
