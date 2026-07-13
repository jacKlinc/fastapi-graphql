from __future__ import annotations
from typing import List

from sqlalchemy.orm import DeclarativeBase, mapped_column, Mapped, relationship

from app.common.types import Cuisine, Course, Diet


class Base(DeclarativeBase):
    pass


class Restaurant(Base):
    __tablename__ = "restaurants"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: str
    cuisine: Cuisine
    menu_id: Mapped[List[MenuItem]] = relationship(back_populates="MenuItem")
    lat: float
    lon: float


class MenuItem(Base):
    __tablename__ = "menu_items"

    name: str
    price: float
    course: Course
    diet: Diet
