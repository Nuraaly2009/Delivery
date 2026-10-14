from pydantic import BaseModel, EmailStr
from .models import OrderStatusChoices
from datetime import date, datetime


class UserLoginSchema(BaseModel):
    username: str
    password: str


class UserOutSchema(BaseModel):
    id: int
    username: str
    email: EmailStr
    registered_date: date


class UserInputSchema(BaseModel):
    username: str
    email: EmailStr
    password: str


class ProductOutSchema(BaseModel):
    id: int
    product_name: str
    price: int
    description: str
    created_date: datetime


class ProductInputSchema(BaseModel):
    product_name: str
    price: int
    description: str


class OrderOutSchema(BaseModel):
    id: int
    user_id: int
    product_id: int
    quantity: int
    total_price: int
    order_status: OrderStatusChoices
    created_date: datetime


class OrderInputSchema(BaseModel):
    user_id: int
    product_id: int
    quantity: int = 1
    total_price: int
    order_status: OrderStatusChoices = OrderStatusChoices.pending
