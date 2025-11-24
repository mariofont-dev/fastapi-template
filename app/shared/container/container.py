from dependency_injector import containers, providers

from app.config.settings import settings
from app.contexts.user.container.user_container import UserContainer
from app.shared.infrastructure.database.sql_model_connection import SQLModelConnection


class Container(containers.DeclarativeContainer):
    sql_model_database = providers.Singleton(
        SQLModelConnection,
        database_url=settings.database_url,
    )

    database = sql_model_database

    user_container = providers.Container(UserContainer, database=database.provided)
