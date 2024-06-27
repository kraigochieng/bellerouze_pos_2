from sqlalchemy import not_
from sqlalchemy.orm import Session

from . import models, schemas


# Item
def create_item(db: Session, item: schemas.ItemCreate):
    db_item = models.Item(**item.model_dump())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item


def read_item(db: Session, id: int):
    return (
        db.query(models.Item)
        .filter(models.Item.id == id, not_(models.Item.is_deleted))
        .first()
    )


def read_items(db: Session, skip: int = 0, limit: int = 10):
    return (
        db.query(models.Item)
        .filter(not_(models.Item.is_deleted))
        .offset(skip)
        .limit(limit)
        .all()
    )


def update_item(db: Session, id: int, update_model=schemas.ItemUpdate):
    model_in_db = read_item(db=db, id=id)
    if model_in_db:
        for key, value in update_model.model_dump().items():
            setattr(model_in_db, key, value)

        db.commit()
        db.refresh(model_in_db)
        return model_in_db
    else:
        return None


def delete_item(db: Session, id: int):
    db_item = read_item(db=db, id=id)
    if db_item:
        db_item.is_deleted = True
        db.commit()
        db.refresh(db_item)
        return db_item
    else:
        return None


# Item Category
def create_item_category(db: Session, item_category: schemas.ItemCategoryCreate):
    db_item_category = models.ItemCategory(**item_category.model_dump())
    db.add(db_item_category)
    db.commit()
    db.refresh(db_item_category)
    return db_item_category


def read_item_category(db: Session, id: int):
    return (
        db.query(models.ItemCategory)
        .filter(models.ItemCategory.id == id, not_(models.ItemCategory.is_deleted))
        .first()
    )


def read_item_categories(db: Session, skip: int = 0, limit: int = 10):
    return (
        db.query(models.ItemCategory)
        .filter(not_(models.ItemCategory.is_deleted))
        .offset(skip)
        .limit(limit)
        .all()
    )


def update_item_category(db: Session, id: int, update_model=schemas.ItemCategoryUpdate):
    model_in_db = read_item_category(db=db, id=id)
    if model_in_db:
        for key, value in update_model.model_dump().items():
            setattr(model_in_db, key, value)

        db.commit()
        db.refresh(model_in_db)
        return model_in_db
    else:
        return None


def delete_item_category(db: Session, id: int):
    db_item = read_item_category(db=db, id=id)
    if db_item:
        db_item.is_deleted = True
        db.commit()
        db.refresh(db_item)
        return db_item
    else:
        return None


# Item With Category
def create_item_with_category(
    db: Session, item_with_category: schemas.ItemWithCategoryCreate
):
    db_item_with_category = models.ItemWithCategory(**item_with_category.model_dump())
    db.add(db_item_with_category)
    db.commit()
    db.refresh(db_item_with_category)
    return db_item_with_category


def read_item_with_category(db: Session, id: int):
    return (
        db.query(models.ItemWithCategory)
        .filter(
            models.ItemWithCategory.id == id,
            not_(models.ItemWithCategory.is_deleted),
        )
        .first()
    )


def read_item_with_categories(db: Session, skip: int = 0, limit: int = 10):
    return (
        db.query(models.ItemWithCategory)
        .filter(not_(models.ItemWithCategory.is_deleted))
        .offset(skip)
        .limit(limit)
        .all()
    )


def update_item_with_category(
    db: Session, id: int, update_model=schemas.ItemWithCategoryUpdate
):
    model_in_db = read_item_with_category(db=db, id=id)
    if model_in_db:
        for key, value in update_model.model_dump().items():
            setattr(model_in_db, key, value)

        db.commit()
        db.refresh(model_in_db)
        return model_in_db
    else:
        return None


def delete_item_with_category(db: Session, id: int):
    db_item = read_item_with_category(db=db, id=id)
    if db_item:
        db_item.is_deleted = True
        db.commit()
        db.refresh(db_item)
        return db_item
    else:
        return None
