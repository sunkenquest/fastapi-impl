from pydantic import BaseModel, Field


class ShopItemBase(BaseModel):
    name: str
    rate: int | None = Field(None, description="Rating of the product, optional")
    description: str
    price: float
    image: str


class ShopItemCreate(ShopItemBase):
    pass


class ShopItemResponse(ShopItemBase):
    id: int

    class Config:
        orm_mode = True
