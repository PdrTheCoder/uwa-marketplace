from datetime import datetime
from datetime import timezone
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from models import User, Listing
from utils import get_salt_and_password

engine = create_engine("sqlite:///../instance/uwamkp.db", echo=True)


def add_user(
        email,
        username,
        password,
        is_admin):

    # get salt and password
    hashed, salt = get_salt_and_password(password=password)
    created_at = datetime.now(timezone.utc)

    with Session(engine) as session:
        new_user = User(
            email=email,
            username=username,
            salt=salt,
            password=hashed,
            created_at=created_at,
            is_admin=is_admin,
            deleted=False
        )
        session.add(new_user)
        session.commit()


def add_listing(
        title,
        price,
        description,
        seller_id,
        condition=0,
        suspended=False,
        sold=False,
        deleted=False,
        created_at=datetime.now(timezone.utc)):

    with Session(engine) as session:
        new_listing = Listing(
            title=title,
            condition=condition,
            price=price,
            description=description,
            seller_id=seller_id,
            suspended=suspended,
            sold=sold,
            deleted=deleted,
            created_at=created_at,
        )
        session.add(new_listing)
        session.commit()


if __name__ == "__main__":
    # add a use to start
    # ==================
    # add_user("00000000@student.uwa.edu.au", "test", "test", True)
    # ==================

    # add a listing to start
    # ==================
    # add_listing(
    #     "Used bicycle for sell",
    #     343.99,
    #     "Good condition, easy to use, well maintained.",
    #     1
    # )
    # ==================

    pass
