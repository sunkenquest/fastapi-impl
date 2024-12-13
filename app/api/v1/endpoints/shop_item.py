from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.db.connection import get_db
from app.schemas.shop_item import ShopItemCreate, ShopItemResponse
from app.services.shop_item_service import (
    create_shop_item_service,
    get_all_items_service,
)

router = APIRouter()


@router.post("/", response_model=ShopItemResponse)
def post_shop_item(item: ShopItemCreate, db: Session = Depends(get_db)):
    if item.price <= 0:
        raise HTTPException(status_code=400, detail="Price must be greater than 0.")

    db_item = create_shop_item_service(db, item)
    return db_item


@router.get("/all", response_model=list[ShopItemResponse])
def get_all_items(db: Session = Depends(get_db)):
    items = get_all_items_service(db)
    return items
