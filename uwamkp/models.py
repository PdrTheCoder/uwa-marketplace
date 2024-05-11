from sqlalchemy.dialects.sqlite import (
    BLOB,
    BOOLEAN,
    DATETIME,
    DECIMAL,
    INTEGER,
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
from werkzeug.security import check_password_hash


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
    #
    condition: Mapped[int] = mapped_column(SMALLINT, nullable=False)
    price: Mapped[float] = mapped_column(DECIMAL, nullable=False)
    description: Mapped[str] = mapped_column(TEXT, nullable=False)
    # image = Column(BLOB) # TODO later
    seller_id: Mapped[int] = mapped_column(ForeignKey(
        'user.id', ondelete='CASCADE'), nullable=False)
    suspended: Mapped[bool] = mapped_column(BOOLEAN, nullable=False)
    sold: Mapped[bool] = mapped_column(BOOLEAN, nullable=False)
    deleted: Mapped[bool] = mapped_column(BOOLEAN, nullable=False)
    created_at: Mapped[str] = mapped_column(DATETIME, nullable=False)
    updated_at: Mapped[str] = mapped_column(DATETIME, nullable=True)
    category_id: Mapped[int] = mapped_column(
        ForeignKey('category.id', ondelete='SET NULL'), nullable=True)


class Reply(Base):
    __tablename__ = 'reply'
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    message: Mapped[str] = mapped_column(TEXT, nullable=False)
    from_user_id: Mapped[int] = mapped_column(
        ForeignKey('user.id'), nullable=False)
    created_at: Mapped[str] = mapped_column(DATETIME, nullable=False)
    listing_id: Mapped[int] = mapped_column(
        ForeignKey('listing.id'), nullable=False)


class Category(Base):
    __tablename__ = 'category'
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    category_name: Mapped[str] = mapped_column(VARCHAR(50), unique=True)
    desc: Mapped[str] = mapped_column(TEXT)
    created_at: Mapped[str] = mapped_column(DATETIME, nullable=False)
