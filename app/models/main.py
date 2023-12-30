import datetime

from sqlalchemy import String, DateTime, ForeignKey, Float
from sqlalchemy.orm import Mapped, mapped_column, relationship


from db import Base
from models.common import CreateUpdateDate


class UserDBModel(Base, CreateUpdateDate):
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(String(255), nullable=False)
    password: Mapped[str] = mapped_column(String(255), nullable=False)
    is_admin: Mapped[bool] = mapped_column(default=False, server_default='false')

class BuyerDBModel(Base, CreateUpdateDate):
    __tablename__ = 'buyers'

    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey('users.id'), nullable=False)
    user: Mapped[UserDBModel] = relationship('UserDBModel', back_populates='buyer', uselist=False)


class SellerDBModel(Base, CreateUpdateDate):
    __tablename__ = 'sellers'

    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey('users.id'), nullable=False)
    user: Mapped[UserDBModel] = relationship('UserDBModel', back_populates='seller', uselist=False)


class BrandDBModel(Base):
    __tablename__ = 'brands'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    # Add other brand-specific fields


class ProductDBModel(Base):
    __tablename__ = 'products'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    brand_id: Mapped[int] = mapped_column(ForeignKey('brands.id'), nullable=False)
    brand: Mapped[BrandDBModel] = relationship('BrandDBModel', back_populates='products')
    price: Mapped[float] = mapped_column(Float, nullable=False)


class OrderDBModel(Base, CreateUpdateDate):
    __tablename__ = 'orders'

    id: Mapped[int] = mapped_column(primary_key=True)
    buyer_id: Mapped[int] = mapped_column(ForeignKey('buyers.id'), nullable=False)
    buyer: Mapped[BuyerDBModel] = relationship('BuyerDBModel', back_populates='orders')


class PriceDBModel(Base):
    __tablename__ = 'prices'

    id: Mapped[int] = mapped_column(primary_key=True)
    product_id: Mapped[int] = mapped_column(ForeignKey('products.id'), nullable=False)
    product: Mapped[ProductDBModel] = relationship('ProductDBModel', back_populates='prices')
    price: Mapped[float] = mapped_column(Float, nullable=False)
    start_date: Mapped[datetime.date] = mapped_column(DateTime, nullable=False)
    end_date: Mapped[datetime.date] = mapped_column(DateTime, nullable=False)


class DiscountDBModel(Base):
    __tablename__ = 'discounts'

    id: Mapped[int] = mapped_column(primary_key=True)
    product_id: Mapped[int] = mapped_column(ForeignKey('products.id'), nullable=False)
    product: Mapped[ProductDBModel] = relationship('ProductDBModel', back_populates='discounts')
    discount_percentage: Mapped[float] = mapped_column(Float, nullable=False)
    start_date: Mapped[datetime.date] = mapped_column(DateTime, nullable=False)
    end_date: Mapped[datetime.date] = mapped_column(DateTime, nullable=False)

