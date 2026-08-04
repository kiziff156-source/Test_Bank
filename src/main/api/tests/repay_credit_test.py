import pytest

from src.main.api.models.repay_ceredit_request import RepayCreditRequest


@pytest.mark.api
class TestRepayCredit:
    def test_repay_credit(self, api_manager, request_credit, create_credit_secret):

        repay_credit_request = RepayCreditRequest(creditId=request_credit.creditId, accountId=request_credit.id, amount=request_credit.amount)
        response = api_manager.credit_steps.repay_credit(repay_credit_request, create_credit_secret)

        assert repay_credit_request.creditId == response.creditId
        assert repay_credit_request.amount == response.amountDeposited