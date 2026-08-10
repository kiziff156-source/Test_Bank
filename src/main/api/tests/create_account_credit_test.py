import pytest

from src.main.api.classes.api_manager import ApiManager
from src.main.api.models.admin_models.create_user_request import CreateUserRequest
from src.main.api.models.user_models.create_account_response import CreateAccountResponse


@pytest.mark.api
class TestCreateAccountCredit:
    def test_create_account_credit(
            self,
            api_manager:ApiManager,
            create_credit_secret:CreateUserRequest
            ):
        response = api_manager.credit_steps.create_account_credit(create_credit_secret)
        assert response.balance == 0

    def test_create_account_credit_second(
            self,
            api_manager:ApiManager,
            create_credit_secret:CreateUserRequest,
            create_credit_account:CreateAccountResponse
    ):
        credit_account=create_credit_account
        credit_account_second_response = api_manager.credit_steps.create_account_credit(create_credit_secret)

        assert credit_account_second_response.balance == 0
        assert credit_account_second_response.id != credit_account.id
        assert credit_account_second_response.number != credit_account.number

    def test_create_credit_account_third_invalid (
            self,
            api_manager:ApiManager,
            create_credit_secret:CreateUserRequest,
            create_credit_account_second:CreateAccountResponse
    ):
        api_manager.credit_steps.create_account_credit_invalid(create_credit_secret)




