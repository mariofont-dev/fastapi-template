from uuid import UUID
from app.contexts.user.domain.entities.user import User


class TestUser:

    def test_success(self):
        user = User(first_name="Mario", last_name="Font", age=27)

        assert user.id
        assert isinstance(user.id, UUID)
        assert user.first_name == "Mario"
        assert user.last_name == "Font"
        assert user.age == 27
