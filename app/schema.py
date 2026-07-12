from __future__ import annotations
from typing import List, Optional
from enum import Enum

import strawberry


# NOTE: types
@strawberry.type
class Restaurant:
    name: str
    cuisine: Cuisine
    menu: List[MenuItem]
    lat: float
    lon: float
    # geohash: # TODO


class Cuisine(Enum):
    ITALIAN = "italian"
    INDIAN = "indian"
    # TODO: add more


class Course(Enum):
    STARTER = "starter"
    MAIN = "main"
    DESSERT = "dessert"


class Diet(Enum):
    VEGAN = "vegan"
    VEGGIE = "veggie"


@strawberry.type
class MenuItem:
    name: str
    price: float
    course: Course
    diet: Optional[Diet] = None


# NOTE: queries

# schema = strawberry.Schema(types=[MenuItem, Restaurant])
