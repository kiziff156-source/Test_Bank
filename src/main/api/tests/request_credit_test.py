import pytest

from src.main.api.classes.api_manager import ApiManager
from src.main.api.fixtures.api_fixtures import api_manager
from src.main.api.generators.model_generator import RandomModelGenerator
from src.main.api.models.admin_models.create_user_request import CreateUserRequest
from src.main.api.models.credit_secret_models.request_credit_request import RequestCreditRequest
from src.main.api.models.credit_secret_models.request_credit_response import RequestCreditResponse
from src.main.api.models.user_models.create_account_response import CreateAccountResponse


@pytest.mark.api
class TestRequestCredit:
    def test_request_credit(
            self,
            api_manager:ApiManager,
            create_credit_secret:CreateUserRequest,
            create_credit_account:CreateAccountResponse
    ):
        request_credit_request=RandomModelGenerator.generate(RequestCreditRequest)
        request_credit_request.accountId = create_credit_account.id

        response = api_manager.credit_steps.create_request_credit(request_credit_request, create_credit_secret)

        assert request_credit_request.amount == response.amount
        assert request_credit_request.termMonths == response.termMonths

    @pytest.mark.xfail (reason="wrong HTTPStatus_code")
    def test_request_credit_invalid(
            self,
            api_manager:ApiManager,
            request_credit:RequestCreditResponse,
            create_credit_secret:CreateUserRequest,
            create_credit_account:CreateAccountResponse
    ):
        request_credit_request = RandomModelGenerator.generate(RequestCreditRequest)
        request_credit_request.accountId = create_credit_account.id
        api_manager.credit_steps.create_request_credit_invalid(request_credit_request, create_credit_secret)
