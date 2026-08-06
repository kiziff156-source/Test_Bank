import pytest
from src.main.api.fixtures.api_fixtures import api_manager
from src.main.api.generators.model_generator import RandomModelGenerator
from src.main.api.models.credit_secret_models.request_credit_request import RequestCreditRequest


@pytest.mark.api
class TestRequestCredit:
    def test_request_credit(self, api_manager, create_credit_secret, create_credit_account):
        request_credit_request=RandomModelGenerator.generate(RequestCreditRequest)
        request_credit_request.accountId = create_credit_account.id

        response = api_manager.credit_steps.create_request_credit(request_credit_request, create_credit_secret)

        assert request_credit_request.amount == response.amount
        assert request_credit_request.termMonths == response.termMonths

    @pytest.mark.xfail (reason="wrong HTTPStatus_code")
    def test_request_credit_invalid(self, api_manager, request_credit, create_credit_secret, create_credit_account):
        request_credit_request = RandomModelGenerator.generate(RequestCreditRequest)
        request_credit_request.accountId = create_credit_account.id
        api_manager.credit_steps.create_request_credit_invalid(request_credit_request, create_credit_secret)
