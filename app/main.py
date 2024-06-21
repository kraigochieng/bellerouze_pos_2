from fastapi import FastAPI
from .routers import api__item, api__item_category, api__item_with_category, item
from .database import engine
from .models import Base

# Create FastAPI instance
app = FastAPI()

# Create the database tables
Base.metadata.create_all(bind=engine)

# Prefix the routers and register them
app.include_router(item.router, prefix="/items", tags=["items"])
app.include_router(api__item.router, prefix="/api/items", tags=["API: items"])
app.include_router(api__item_category.router, prefix="/api/item_categories", tags=["API: item categories"])
app.include_router(api__item_with_category.router, prefix="/api/item_with_categories", tags=["API: items with categories"])


# Optional: Define a root route
@app.get("/")
def read_root():
    return {"message": "Welcome to the API!"}
