
import pytest

from src.main.api.generators.model_generator import RandomModelGenerator
from src.main.api.models.admin_models.create_user_request import CreateUserRequest
from src.main.api.models.login_user_request import LoginUserRequest


@pytest.mark.api
class TestUserLogin:
    def test_login_admin(self, api_manager):
        login_user_request = LoginUserRequest(username="admin", password="123456")
        response = api_manager.admin_steps.login_user(login_user_request)

        assert login_user_request.username == response.user.username
        assert response.user.role == "ROLE_ADMIN"

    def test_login_user(self, api_manager, create_user_request):
        response = api_manager.admin_steps.login_user(create_user_request)

        assert create_user_request.username == response.user.username
        assert response.user.role == "ROLE_USER"

    def test_invalid_credentials (self, api_manager):
        unregistered_login = RandomModelGenerator.generate(CreateUserRequest)
        api_manager.user_steps.login_unregistered(unregistered_login)
