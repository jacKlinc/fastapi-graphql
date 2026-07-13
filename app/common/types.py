from enum import Enum


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
