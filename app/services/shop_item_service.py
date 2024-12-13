from sqlalchemy.orm import Session

from app.db.models import ShopItem
from app.schemas.shop_item import ShopItemCreate


def create_shop_item_service(db: Session, item: ShopItemCreate):
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


def get_all_items_service(db: Session):
    items = db.query(ShopItem).all()
    return items if items else []
