from uuid import UUID
from app.contexts.user.domain.entities.user_entity import UserEntity


class TestUser:

    def test_success(self):
        user = UserEntity(first_name="Mario", last_name="Font", age=27)

        assert user.id
        assert isinstance(user.id, UUID)
        assert user.first_name == "Mario"
        assert user.last_name == "Font"
        assert user.age == 27
