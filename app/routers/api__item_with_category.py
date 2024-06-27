from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from .. import crud, schemas

from ..database import get_db

router = APIRouter()


@router.post("/", response_model=schemas.ItemWithCategoryRead)
def create_item_with_category(item_with_category: schemas.ItemWithCategoryCreate, db: Session = Depends(get_db)):
    return crud.create_item_with_category(db=db, item_with_category=item_with_category)

@router.get("/", response_model=list[schemas.ItemWithCategoryRead])
def read_items_with_categories(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    items_with_categories = crud.read_item_with_categories(db=db, skip=skip, limit=limit)
    return items_with_categories

@router.get("/{item_with_category_id}", response_model=schemas.ItemWithCategoryRead)
def read_item_with_category(item_with_category_id: int, db: Session = Depends(get_db)):
    db_item_with_category = crud.read_item_with_category(db=db, id=item_with_category_id)
    if db_item_with_category is None:
        raise HTTPException(status_code=404, detail="Item with category not found")
    return db_item_with_category

@router.put("/{item_with_category_id}", response_model=schemas.ItemWithCategoryRead)
def update_item_with_category(item_with_category_id: int, item_with_category_update: schemas.ItemWithCategoryUpdate, db: Session = Depends(get_db)):
    db_item_with_category = crud.update_item_with_category(db=db, item_with_category_id=item_with_category_id, item_with_category_update=item_with_category_update)
    if db_item_with_category is None:
        raise HTTPException(status_code=404, detail="Item with category not found")
    return db_item_with_category

@router.delete("/{item_with_category_id}", response_model=schemas.ItemWithCategoryRead)
def delete_item_with_category(item_with_category_id: int, db: Session = Depends(get_db)):
    db_item_with_category = crud.delete_item_with_category(db=db, item_with_category_id=item_with_category_id)
    if db_item_with_category is None:
        raise HTTPException(status_code=404, detail="Item with category not found")
    return db_item_with_category
