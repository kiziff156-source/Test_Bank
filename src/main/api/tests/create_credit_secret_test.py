import pytest

from src.main.api.generators.model_generator import RandomModelGenerator
from src.main.api.models.admin_models.create_user_request import CreateUserRequest


@pytest.mark.api
class TestCreateCreditSecret:
    @pytest.mark.parametrize(
        "generated_credit_secret",
        [RandomModelGenerator.generate(CreateUserRequest)]
    )
    def test_create_credit_secret(self, api_manager, generated_credit_secret):
        generated_credit_secret.role = "ROLE_CREDIT_SECRET"
        response = api_manager.admin_steps.create_user(generated_credit_secret)
        assert generated_credit_secret.username == response.username
        assert generated_credit_secret.role == response.role

    @pytest.mark.parametrize(
        "password",
        [
            "Pas!sw0rд"
            "Pas!sw0",
            "PAS!SW0RD",
            "Passsw0rd",
            "Pas!sword"
        ]
    )
    def test_create_credit_secret_invalid_password (self, api_manager, password):
        create_credit_secret_invalid_password = CreateUserRequest(username= "Max", password=password, role= "ROLE_CREDIT_SECRET")
        api_manager.admin_steps.create_invalid_user(create_credit_secret_invalid_password)

    @pytest.mark.parametrize(
        "username",
            [
                "абв",
                "ab",
                "ab!"
            ]
        )
    def test_create_credit_secret_invalid_username(self, api_manager, username):
        create_credit_secret_invalid_username = CreateUserRequest(username=username, password="Pas!sw0rd",role="ROLE_CREDIT_SECRET")
        api_manager.admin_steps.create_invalid_user(create_credit_secret_invalid_username)
