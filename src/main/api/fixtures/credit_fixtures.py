import pytest

from src.main.api.generators.model_generator import RandomModelGenerator
from src.main.api.models.create_user_request import CreateUserRequest


@pytest.fixture
def create_credit_secret(api_manager):
    generated_credit_secret = RandomModelGenerator.generate(CreateUserRequest)
    generated_credit_secret.role = "ROLE_CREDIT_SECRET"
    api_manager.admin_steps.create_user(generated_credit_secret)
    return generated_credit_secret

@pytest.fixture
def create_credit_account(api_manager, create_credit_secret):
    response = api_manager.credit_steps.create_account_credit(create_credit_secret)
    return response
