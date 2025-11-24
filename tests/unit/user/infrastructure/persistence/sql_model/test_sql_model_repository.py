from dependency_injector.wiring import Provide, inject

from app.contexts.user.domain.entities.user_entity import UserEntity
from app.contexts.user.domain.persistence.user_repository import UserRepositoryInterface
from app.shared.container.container import Container


class TestSQLModelRepository:
    @classmethod
    def setup_class(cls):
        cls.container = Container()

    def test_create_and_get(self):
        entity = UserEntity(first_name="Mario", last_name="Font", age=27)

        user_repository = self.container.user_container().user_repository()
        created_user = user_repository.create(user=entity)
        assert entity == created_user

        got_user = user_repository.get_by_id(identifier=entity.id)
        assert entity == got_user
