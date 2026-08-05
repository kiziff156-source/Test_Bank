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
