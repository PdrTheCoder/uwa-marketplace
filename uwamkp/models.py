from datetime import timezone
from sqlalchemy.dialects.sqlite import (
    BOOLEAN,
    DATETIME,
    DECIMAL,
    SMALLINT,
    TEXT,
    VARCHAR,
)
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
from werkzeug.security import check_password_hash


def format_local_time(some_datetime):
    """Format the datetime to local time str"""
    return some_datetime.replace(tzinfo=timezone.utc).astimezone().strftime("%m/%d/%Y, %H:%M:%S")


class Base(DeclarativeBase):
    pass


db = SQLAlchemy(model_class=Base)


class User(UserMixin, db.Model):
    __tablename__ = 'user'
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    email: Mapped[str] = mapped_column(unique=True, nullable=False)
    username: Mapped[str] = mapped_column(unique=True, nullable=False)
    password: Mapped[str] = mapped_column(nullable=False)
    created_at: Mapped[str] = mapped_column(DATETIME, nullable=False)
    is_admin: Mapped[bool] = mapped_column(BOOLEAN, nullable=False)
    deleted: Mapped[bool] = mapped_column(BOOLEAN, nullable=False)

    def verify_password(self, password):
        return check_password_hash(self.password, password)


class Listing(Base):
    __tablename__ = 'listing'
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    title: Mapped[str] = mapped_column(VARCHAR(60), nullable=False)
    condition: Mapped[int] = mapped_column(SMALLINT, nullable=False)
    price: Mapped[float] = mapped_column(DECIMAL, nullable=False)
    description: Mapped[str] = mapped_column(TEXT, nullable=False)
    seller_id: Mapped[int] = mapped_column(ForeignKey(
        'user.id', ondelete='CASCADE'), nullable=False)
    suspended: Mapped[bool] = mapped_column(BOOLEAN, nullable=False)
    sold: Mapped[bool] = mapped_column(BOOLEAN, nullable=False)
    deleted: Mapped[bool] = mapped_column(BOOLEAN, nullable=False)
    created_at: Mapped[str] = mapped_column(DATETIME, nullable=False)
    updated_at: Mapped[str] = mapped_column(DATETIME, nullable=True)
    category_id: Mapped[int] = mapped_column(
        ForeignKey('category.id', ondelete='SET NULL'), nullable=True)
    seller = relationship("User")
    image_path: Mapped[str] = mapped_column(VARCHAR, nullable=False)

    def to_dict(self):
        condition_mapping = {
            0: "New",
            1: "Used - Like New",
            2: "Used - Good",
            3: "Used - Fair"
        }
        return {
            "id": self.id,
            "title": self.title,
            "condition": condition_mapping[self.condition],
            "price": round(self.price, 2),
            "description": self.description,
            "seller_id": self.seller_id,
            "seller_username": self.seller.username,
            "suspended": self.suspended,
            "sold": self.sold,
            "deleted": self.deleted,
            # TODO better render utc time and let client side determine timezone
            "created_at": format_local_time(self.created_at),
            "updated_at": format_local_time(self.updated_at) if self.updated_at else None,
            "image_path": self.image_path
        }


class Reply(Base):
    __tablename__ = 'reply'
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    message: Mapped[str] = mapped_column(TEXT, nullable=False)
    from_user_id: Mapped[int] = mapped_column(
        ForeignKey('user.id'), nullable=False)
    created_at: Mapped[str] = mapped_column(DATETIME, nullable=False)
    listing_id: Mapped[int] = mapped_column(
        ForeignKey('listing.id'), nullable=False)
    user = relationship("User") #add user relationship

    def to_dict(self):
        return {
            "id": self.id,
            "message": self.message,
            "from_user_id": self.from_user_id,
            # TODO better render utc time and let client side determine timezone
            "created_at": format_local_time(self.created_at),
            "listing_id": self.listing_id,
            "from_username": self.user.username,
            "from_user_email": self.user.email
        }


class Category(Base):
    __tablename__ = 'category'
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    category_name: Mapped[str] = mapped_column(VARCHAR(50), unique=True)
    desc: Mapped[str] = mapped_column(TEXT)
    created_at: Mapped[str] = mapped_column(DATETIME, nullable=False)
