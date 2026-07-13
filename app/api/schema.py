from __future__ import annotations
from typing import List, Optional

import strawberry


from app.common.types import Cuisine, Course, Diet


# NOTE: types
@strawberry.type
class Restaurant:
    """A restaurant on the platform."""  # NOTE: strawberry will add this to the schema docs

    # TODO: add ID
    name: str
    cuisine: Cuisine
    menu: List[MenuItem]
    lat: float
    lon: float


@strawberry.type
class MenuItem:
    """A menu in a restaurant."""

    # TODO: add ID
    name: str
    price: float
    course: Course
    diet: Optional[Diet] = None


def get_restaurants() -> List[Restaurant]:
    return [
        Restaurant(
            name="Dummy Diner",
            cuisine=Cuisine.ITALIAN,
            menu=[
                MenuItem(name="Spaghetti", price=12.5, course=Course.MAIN, diet=None)
            ],
            lat=49.2827,
            lon=-123.1207,
        )
    ]


# NOTE: queries
@strawberry.type
class Query:
    restaurants: List[Restaurant] = strawberry.field(resolver=get_restaurants)


schema = strawberry.Schema(query=Query, types=[MenuItem, Restaurant])
