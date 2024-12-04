from fastapi import APIRouter
from flask_graphql import GraphQLView
from app.schemas.graphql import schema

graphql_router = APIRouter()

graphql_router.add_route("/graphql", GraphQLView.as_view(graphiql=True, schema=schema))
