from pydantic import BaseModel, ConfigDict


class ItemBase(BaseModel):
    name: str
    description: str


class ItemCreate(ItemBase):
    pass


class ItemUpdate(ItemBase):
    pass


class Item(ItemBase):
    model_config = ConfigDict(extra="ignore", from_attributes=True)

    id: int


class ItemCategoryBase(BaseModel):
    name: str


class ItemCategoryCreate(ItemCategoryBase):
    pass


class ItemCategoryUpdate(ItemCategoryBase):
    pass


class ItemCategory(ItemCategoryBase):
    model_config = ConfigDict(extra="ignore", from_attributes=True)

    id: int


class ItemWithCategoryBase(BaseModel):
    item_id: int
    item_category_id: int


class ItemWithCategoryCreate(ItemWithCategoryBase):
    pass


class ItemWithCategoryUpdate(ItemWithCategoryBase):
    pass


class ItemWithCategory(ItemWithCategoryBase):
    model_config = ConfigDict(extra="ignore", from_attributes=True)

    id: int
