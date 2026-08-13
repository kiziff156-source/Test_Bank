import pytest
from requests import Session

from src.main.api.classes.api_manager import ApiManager
from src.main.api.models.admin_models.create_user_request import CreateUserRequest
from src.main.api.models.credit_secret_models.repay_ceredit_request import RepayCreditRequest
from src.main.api.models.credit_secret_models.request_credit_response import RequestCreditResponse
from src.main.api.db.crud.credit_crud import CreditCrudDb as Credit


@pytest.mark.api
class TestRepayCredit:
    def test_repay_credit(
            self,
            db_session:Session,
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

        credit_from_db = Credit.get_credit_from_db_by_credit_id(db_session, repay_credit_request.creditId)

        assert credit_from_db.balance == 0 , f"Credit id= {request_credit.creditId} not repaid"





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
            db_session: Session,
            api_manager:ApiManager,
            request_credit:RequestCreditResponse,
            create_credit_secret:CreateUserRequest
    ):
        repay_credit_part_request = RepayCreditRequest(creditId=request_credit.creditId,
                                                       accountId=request_credit.id,
                                                       amount=(request_credit.amount-part))
        api_manager.credit_steps.repay_credit_invalid(repay_credit_part_request, create_credit_secret)

        credit_from_db = Credit.get_credit_from_db_by_credit_id(db_session, repay_credit_part_request.creditId)

        assert credit_from_db.amount == request_credit.balance , f"Credit id= {request_credit.creditId} repaid"
