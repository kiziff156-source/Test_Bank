import pytest


from src.main.api.classes.api_manager import ApiManager
from src.main.api.models.admin_models.create_user_request import CreateUserRequest
from src.main.api.models.credit_secret_models.repay_ceredit_request import RepayCreditRequest
from src.main.api.models.credit_secret_models.request_credit_response import RequestCreditResponse


@pytest.mark.api
class TestRepayCredit:
    def test_repay_credit(
            self,
            api_manager:ApiManager,
            request_credit:RequestCreditResponse,
            create_credit_secret:CreateUserRequest
    ):

        repay_credit_request = RepayCreditRequest(creditId=request_credit.creditId,
                                                  accountId=request_credit.id,
                                                  amount=request_credit.amount)
        response = api_manager.credit_steps.repay_credit(repay_credit_request, create_credit_secret)

        assert repay_credit_request.creditId == response.creditId
        assert repay_credit_request.amount == response.amountDeposited

    @pytest.mark.parametrize(
        "part",
        [
            0.01,
            -0.01,
        ]
    )
    def test_repay_credit_part(
            self,
            part: float,
            api_manager:ApiManager,
            request_credit:RequestCreditResponse,
            create_credit_secret:CreateUserRequest
    ):
        repay_credit_part_request = RepayCreditRequest(creditId=request_credit.creditId,
                                                       accountId=request_credit.id,
                                                       amount=(request_credit.amount-part))
        api_manager.credit_steps.repay_credit_invalid(repay_credit_part_request, create_credit_secret)
