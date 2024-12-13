from pydantic import BaseModel


class ShopItemBase(BaseModel):
    name: str
    rate: int
    description: str
    price: float
    image: str


class ShopItemCreate(ShopItemBase):
    pass


class ShopItemResponse(ShopItemBase):
    id: int

    class Config:
        orm_mode = True
