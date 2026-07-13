# fastapi-graphql
GraphQL API implemented in FastAPI. This [repo's predecessor](https://github.com/jacKlinc/fastapi-hw), aimed to find imaginary climbing routes near Canmore. This repo aims to do the same but for restaurants in Vancouver. 


### Running

```bash
# Start Postgres
docker compose up -d

# Run API (hot reload)
uv run uvicorn app.main:app --reload

# Run GraphQL UI on 8000
uv run strawberry dev app.schema
```

## Design

### Tool choice

Strawberry was chosen instead of graphene due to it being supported out-of-the-box in FastAPI.

Recommended VS Code extension: `vscode-graphql-syntax`

### Schema

`strawberry export-schema app.api.schema:schema > schema.graphql`



---

## GraphQL Theory
### Schema

Structurally the same as an SQL schema where
- Table: type
- Columns: Fields
- Foreign Keys: nested types

```sql
CREATE TABLE users (
    id INT PRIMARY KEY,
    name VARCHAR(100)
);

CREATE TABLE posts (
    id INT PRIMARY KEY,
    title VARCHAR(255),
    user_id INT,
    FOREIGN KEY (user_id) REFERENCES users(id)
);
```
Same as

```graphql
type User {
  id: ID!
  name: String!
  posts: [Post!]! # Direct relationship representation
}

type Post {
  id: ID!
  title: String!
  user: User!
}
```

in FastAPI:
```python
from __future__ import annotations
import strawberry

@strawberry.type
class User:
    id: int
    name: str
    posts: list[Post]


@strawberry.type
class Post:
    id: int
    title: str
    user: User
```


### Query

```graphql
type Query {
    posts: [Post]
    user(id: String!): User
}
```

### Mutation

```graphql
type Mutation {
    createPost(title: String): Post
    deletePost(title: String): String
}
```

### Resolver

Implemented in the programming language of choice. In this case: Python3
```python
def get_posts():
    return [Post(title="New Post", user=User(name="New User"))]

@strawberry.type
class Query:
    posts: List[Post] = strawberry.field(resolver=get_posts)
```

### SDL (Storage Definition Language)

Similar to SQL's DDL where it describes what must be stored in a database table

**Difference**: 
1. SDL describes what the client can request
2. SDL describes graph-like relationships as opposed to DDL's flat, matrix 


Approaches:
1. Schema-first
2. Code-first

**Strawberry only supports code-first**

