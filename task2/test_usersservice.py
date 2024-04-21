import unittest
from unittest.mock import AsyncMock, Mock
from task2.task2_usersservice import UsersService
from task2.models import UserDTO


class TestUserService(unittest.IsolatedAsyncioTestCase):
    async def test_get_user(self):
        user_service = UsersService()
        user = await user_service.get(1)

        self.assertEqual(user.id, 1)
        self.assertEqual(user.username, 'john_doe')
        self.assertEqual(user.email, 'john@example.com')

    async def test_add_user(self):
        # request_mock = AsyncMock()
        # request_mock.__aenter__.return_value = request_mock
        # request_mock.json.return_value = { 'hello' : 'world'}
        #
        # session = Mock()
        # session.get.return_value = request_mock

        user_id = 1000

        user_data = {'id': user_id, 'username': 'new_user', 'email': 'new@example.com'}
        user = UserDTO(**user_data)

        user_service = UsersService()
        await user_service.add(user)

        user = await user_service.get(user_id)
        self.assertTrue(user)

        await user_service.destroy(user_id)

        # db_session.add.assert_called_once()
        # db_session.commit.assert_called_once()


if __name__ == "__main__":
    unittest.main()
