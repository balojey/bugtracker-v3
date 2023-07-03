from backend.models import User
from backend.roles import Role


async def test_create_user():
    """Test create user"""

    user = await User.create(
        email="testuser1@test.com",
        password="testpassword1",
        first_name="Test",
        last_name="User1",
        role=Role.admin,
    )
    assert user.email == "testuser1@test.com"