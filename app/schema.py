from typing import List

import strawberry


def get_books():
    return [Book(title="War & Peace", author="Leo Tolstoy")]


@strawberry.type
class Book:
    title: str
    author: str


@strawberry.type
class Query:
    # this the resolver
    books: List[Book] = strawberry.field(resolver=get_books)


schema = strawberry.Schema(query=Query)
