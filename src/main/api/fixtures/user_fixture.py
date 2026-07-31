import pytest

from src.main.api.models import deposit_account_response
from src.main.api.models.create_account_response import CreateAccountResponse
from src.main.api.models.create_user_request import CreateUserRequest
from  src.main.api.generators.model_generator import RandomModelGenerator
from src.main.api.models.deposit_account_request import DepositAccountRequest

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
    second_account_response = api_manager.user_steps.create_account(create_user_request)
    return second_account_response

@pytest.fixture
def deposit_account(api_manager, create_user_request, create_account_request):
    generated_amount=RandomModelGenerator.generate(DepositAccountRequest)
    generated_amount.accountId = create_account_request.id
    deposit_account_response = api_manager.user_steps.deposit_account(create_user_request, generated_amount)
    return deposit_account_response