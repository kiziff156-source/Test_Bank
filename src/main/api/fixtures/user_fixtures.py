import pytest

from src.main.api.classes.api_manager import ApiManager
from src.main.api.generators.model_generator import RandomModelGenerator
from src.main.api.models.admin_models.create_user_request import CreateUserRequest
from src.main.api.models.user_models.create_account_response import CreateAccountResponse
from src.main.api.models.user_models.deposit_account_request import DepositAccountRequest


@pytest.fixture
def create_user_request(
        api_manager: ApiManager
):
    user_request = RandomModelGenerator.generate(CreateUserRequest)
    user_request.role = "ROLE_USER"
    api_manager.admin_steps.create_user(user_request)
    return user_request

@pytest.fixture
def create_account_request(
        api_manager: ApiManager,
        create_user_request: CreateUserRequest
):
    account_response = api_manager.user_steps.create_account(create_user_request)
    return account_response

@pytest.fixture
def create_account_second (
        api_manager: ApiManager,
        create_account_request: CreateUserRequest,
        create_user_request: CreateAccountResponse
):
    second_account_response = api_manager.user_steps.create_account(create_user_request)
    return second_account_response

@pytest.fixture
def deposit_account(
        api_manager: ApiManager,
        create_user_request: CreateUserRequest,
        create_account_request: CreateAccountResponse
):
    generated_amount=RandomModelGenerator.generate(DepositAccountRequest)
    generated_amount.accountId = create_account_request.id
    deposit_account_response = api_manager.user_steps.deposit_account(create_user_request, generated_amount)
    return deposit_account_response