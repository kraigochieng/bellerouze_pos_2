from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import crud, schemas
from app.database import SessionLocal

router = APIRouter()

# Dependency to get the database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/", response_model=schemas.ItemCategory)
def create_item_category(item_category: schemas.ItemCategoryCreate, db: Session = Depends(get_db)):
    return crud.create_item_category(db=db, item_category=item_category)


@router.get("/", response_model=list[schemas.ItemCategory])
def read_item_categories(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    item_categories = crud.read_item_categories(db=db, skip=skip, limit=limit)
    return item_categories

@router.get("/{item_category_id}", response_model=schemas.ItemCategory)
def read_item_category(item_category_id: int, db: Session = Depends(get_db)):
    db_item_category = crud.read_item_category(db=db, id=item_category_id)
    if db_item_category is None:
        raise HTTPException(status_code=404, detail="Item category not found")
    return db_item_category

@router.put("/{item_category_id}", response_model=schemas.ItemCategory)
def update_item_category(item_category_id: int, item_category_update: schemas.ItemCategoryUpdate, db: Session = Depends(get_db)):
    db_item_category = crud.update_item_category(db=db, item_category_id=item_category_id, item_category_update=item_category_update)
    if db_item_category is None:
        raise HTTPException(status_code=404, detail="Item category not found")
    return db_item_category

@router.delete("/{item_category_id}", response_model=schemas.ItemCategory)
def delete_item_category(item_category_id: int, db: Session = Depends(get_db)):
    db_item_category = crud.delete_item_category(db=db, item_category_id=item_category_id)
    if db_item_category is None:
        raise HTTPException(status_code=404, detail="Item category not found")
    return db_item_category
