import pytest

from src.main.api.models.create_account_response import CreateAccountResponse
from src.main.api.models.create_user_request import CreateUserRequest
from  src.main.api.generators.model_generator import RandomModelGenerator

@pytest.fixture
def create_user_request(api_manager):
    user_request = RandomModelGenerator.generate(CreateUserRequest)
    api_manager.admin_steps.create_user(user_request)
    return user_request

@pytest.fixture
def create_account_request(api_manager, create_user_request):
    account_response = api_manager.user_steps.create_account(create_user_request)
    return account_response

@pytest.fixture
def create_account_second (api_manager, create_account_request, create_user_request):
    account_response = create_account_request
    second_account_response = api_manager.user_steps.create_account(create_user_request)
    return account_response, second_account_response

@pytest.fixture
def deposit_account_request(api_manager, create_user_request):...
