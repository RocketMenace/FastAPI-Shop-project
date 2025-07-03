from pydantic import BaseModel, ConfigDict, Field


class OrderLine(BaseModel):
    model_config = ConfigDict(frozen=True)
    order_id: int = Field(default=..., title="order_id")
    sku: str = Field(default=..., title="sku")
    qty: int = Field(default=..., title="qty")
