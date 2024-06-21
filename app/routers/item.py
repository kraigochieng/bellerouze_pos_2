from fastapi import APIRouter, Request, Depends
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import os
from . import api__item
from .. import schemas
from ..database import SessionLocal

router = APIRouter()

# Dependency to get the database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

templates = Jinja2Templates(directory=os.path.join(os.path.dirname(__file__), "../templates"))

@router.get("/", response_class=HTMLResponse)
def get_page(request: Request):
    context = {
        "id": 12,
        "model": None
    }
    return templates.TemplateResponse(request=request, name="item.html", context=context)

@router.post("/", response_class=HTMLResponse)
async def create_item(request: Request, db=Depends(get_db)):
    form = await request.form()
    form_data = dict(form)
    schema = schemas.ItemCreate(**form_data)
    model = api__item.create_item(item=schema, db=db)
    context = {
        "id": 12,
        "model": model
    }
    return templates.TemplateResponse(request=request, name="item.html", context=context)