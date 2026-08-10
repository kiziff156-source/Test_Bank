import pytest

from src.main.api.classes.api_manager import ApiManager
from src.main.api.fixtures.api_fixtures import api_manager
from src.main.api.models.admin_models.create_user_request import CreateUserRequest
from src.main.api.models.user_models.create_account_response import CreateAccountResponse


@pytest.mark.api
class TestCreateAccount:
    def test_create_account(
            self,
            api_manager:ApiManager,
            create_user_request:CreateUserRequest
            ):

        response = api_manager.user_steps.create_account(create_user_request)

        assert response.balance == 0


    def test_create_account_second(
            self,
            api_manager:ApiManager,
            create_user_request:CreateUserRequest,
            create_account_request:CreateAccountResponse
            ):
        account_response = create_account_request
        second_account_response = api_manager.user_steps.create_account(create_user_request)

        assert second_account_response.balance == 0
        assert second_account_response.id != account_response.id
        assert second_account_response.number != account_response.number

    def test_create_account_third_invalid(
            self, api_manager:ApiManager,
            create_user_request:CreateUserRequest,
            create_account_second:CreateAccountResponse
    ):
        api_manager.user_steps.create_account_invalid(create_user_request)
