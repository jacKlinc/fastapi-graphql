from __future__ import annotations
from typing import List, Optional
from enum import Enum

import strawberry


from app.common.types import Cuisine, Course, Diet


# NOTE: types
@strawberry.type
class Restaurant:
    name: str
    cuisine: Cuisine
    menu: List[MenuItem]
    lat: float
    lon: float


@strawberry.type
class MenuItem:
    name: str
    price: float
    course: Course
    diet: Optional[Diet] = None


# NOTE: queries

# schema = strawberry.Schema(types=[MenuItem, Restaurant])
