from typing import Optional

from pydantic import BaseModel, ConfigDict


class ItemCreate(BaseModel):
    name: str
    description: str


class ItemRead(BaseModel):
    id: int
    name: str
    description: str


class ItemUpdate(BaseModel):
    name: Optional[str]
    description: Optional[str]


class ItemCategoryCreate(BaseModel):
    name: str


class ItemCategoryRead(BaseModel):
    id: int
    name: str


class ItemCategoryUpdate(BaseModel):
    name: Optional[str]


class ItemWithCategoryCreate(BaseModel):
    item_id: int
    item_category_id: int


class ItemWithCategoryRead(BaseModel):
    item_id: int
    item_category_id: int


class ItemWithCategoryUpdate(BaseModel):
    item_id: Optional[int]
    item_category_id: Optional[int]


class ItemWithCategory(ItemWithCategoryBase):
    model_config = ConfigDict(extra="ignore", from_attributes=True)

    id: int
