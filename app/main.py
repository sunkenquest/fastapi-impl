from fastapi import FastAPI
import strawberry
from app.db.connection import engine, Base
from app.api.v1.endpoints import users, message
from strawberry.fastapi import GraphQLRouter

from app.graphql.graphql import Query

Base.metadata.create_all(bind=engine)

app = FastAPI()

# rest api
app.include_router(users.router, prefix="/api/v1/users", tags=["Users"])
app.include_router(message.router, prefix="/api/v1/sms", tags=["Message"])


# graphql
schema = strawberry.Schema(Query)
graphql_app = GraphQLRouter(schema)
app.include_router(graphql_app, prefix="/graphql")
