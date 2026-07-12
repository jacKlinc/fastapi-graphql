from __future__ import annotations
from typing import List

import strawberry


def get_author_for_book(root: Book) -> Author:
    return Author(name=root.author_name)


def get_books_for_author(root: Author) -> List[Book]:
    return [book for book in books if book.author_name == root.name]


def get_authors() -> List[Author]:
    author_names = {book.author_name for book in books}
    return [Author(name=name) for name in author_names]


def get_books() -> List[Book]:
    return books


@strawberry.type
class Book:
    title: str
    author_name: strawberry.Private[str]
    author: Author = strawberry.field(resolver=get_author_for_book)


@strawberry.type
class Author:
    name: str
    books: List[Book] = strawberry.field(resolver=get_books_for_author)


books: List[Book] = [
    Book(title="War & Peace", author_name="Leo Tolstoy"),
    Book(title="A Tale of Two Cities", author_name="Charles Dickens"),
]


@strawberry.type
class Query:
    authors: List[Author] = strawberry.field(resolver=get_authors)
    books: List[Book] = strawberry.field(resolver=get_books)


@strawberry.type
class Mutation:
    @strawberry.mutation
    def add_book(self, title: str, author: str) -> Book:
        book = Book(title=title, author_name=author)
        books.append(book)
        return book


schema = strawberry.Schema(query=Query, mutation=Mutation, types=[Book])

"""
# Gets all books, their titles and author's name
query {
  books {
    title
    author {
      name
    }
  }
}

# Adds a new book and returns its title
mutation {
  addBook(title: "testTitle", author: "testTitle") {
    title
  }
}
"""