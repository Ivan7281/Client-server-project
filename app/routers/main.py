from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from db.session import get_session
from models.main import *
from pydantic_models.main import ProductCreate, OrderCreate, OrderItemCreate


main_router = APIRouter()


@main_router.get("/users", tags=["User"], status_code=200)
def get_users(
        db_session: Annotated[Session, Depends(get_session)]
):
    return db_session.query(UserDBModel).all()


@main_router.get("/buyers", tags=["Buyer"], status_code=200)
def get_buyers(
        db_session: Annotated[Session, Depends(get_session)]
):
    return db_session.query(BuyerDBModel).all()


@main_router.get("/sellers", tags=["Seller"], status_code=200)
def get_sellers(
        db_session: Annotated[Session, Depends(get_session)]
):
    return db_session.query(SellerDBModel).all()


@main_router.post("/add_product", tags=["Product"], status_code=201)
def add_product(
         product: ProductCreate,
        db_session: Annotated[Session, Depends(get_session)]
):
    db_product = ProductDBModel(**dict(product))
    db_session.add(db_product)
    db_session.commit()
    return db_product


@main_router.get("/brands", tags=["Brand"], status_code=200)
def get_brands(
        db_session: Annotated[Session, Depends(get_session)]
):
    return db_session.query(BrandDBModel).all()


@main_router.get("/orders", tags=["Order"], status_code=200)
def get_orders(
        db_session: Annotated[Session, Depends(get_session)]
):
    return db_session.query(OrderDBModel).all()


@main_router.get("/prices", tags=["Price"], status_code=200)
def get_prices(
        db_session: Annotated[Session, Depends(get_session)]
):
    return db_session.query(PriceDBModel).all()


@main_router.get("/discounts", tags=["Discount"], status_code=200)
def get_discounts(
        db_session: Annotated[Session, Depends(get_session)]
):
    return db_session.query(DiscountDBModel).all()



