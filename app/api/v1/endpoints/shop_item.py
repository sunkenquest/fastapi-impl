from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.db.connection import get_db
from app.db.models import ShopItem
from app.schemas.shop_item import ShopItemCreate, ShopItemResponse

router = APIRouter()


@router.post("/", response_model=ShopItemResponse)
def create_shop_item(item: ShopItemCreate, db: Session = Depends(get_db)):
    if item.rate < 0 or item.rate > 10:
        raise HTTPException(status_code=400, detail="Rate must be between 0 and 10.")
    if item.price <= 0:
        raise HTTPException(status_code=400, detail="Price must be greater than 0.")

    new_item = ShopItem(
        name=item.name,
        rate=item.rate,
        description=item.description,
        price=item.price,
        image=item.image,
    )
    db.add(new_item)
    db.commit()
    db.refresh(new_item)
    return new_item
