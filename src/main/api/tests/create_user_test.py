import pytest

from src.main.api.models.create_user_request import CreateUserRequest
from src.main.api.generators.model_generator import RandomModelGenerator


@pytest.mark.api
class TestCreateUser:
    @pytest.mark.parametrize(
        "generated_user",
        [RandomModelGenerator.generate(CreateUserRequest)]
    )
    def test_create_user_valid(self, api_manager, generated_user):
        generated_user.role = "ROLE_USER"
        response = api_manager.admin_steps.create_user(generated_user)

        assert generated_user.username == response.username
        assert generated_user.role == response.role

    @pytest.mark.parametrize(
        "username, password",
        [
            ("абв", "Pas!sw0rd"),
            ("ab", "Pas!sw0rd"),
            ("ab!", "Pas!sw0rd"),
            ("Maxx1", "Pas!sw0rд"),
            ("Maxx2", "Pas!sw0"),
            ("Maxx3", "pas!sw0rd"),
            ("Maxx4", "PAS!SW0RD"),
            ("Maxx5", "Passsw0rd"),
            ("Maxx6", "Pas!sword")
        ]
    )

    def test_create_user_invalid(self, username, password, api_manager):
        create_user_request = CreateUserRequest(username=username, password=password, role="ROLE_USER")

        api_manager.admin_steps.create_invalid_user(create_user_request)

