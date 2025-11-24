from dependency_injector import containers, providers

from app.contexts.user.infrastructure.persistence.sql_model.user_repository import (
    SQLModelRepository,
)
from app.shared.infrastructure.database.connection import DatabaseConnection


class UserContainer(containers.DeclarativeContainer):
    database = providers.Dependency(instance_of=DatabaseConnection)

    user_repository = providers.Factory(SQLModelRepository, database=database)
