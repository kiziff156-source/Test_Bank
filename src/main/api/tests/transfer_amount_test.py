import pytest
from requests import Session

from src.main.api.classes.api_manager import ApiManager
from src.main.api.models.admin_models.create_user_request import CreateUserRequest
from src.main.api.models.user_models.create_account_response import CreateAccountResponse
from src.main.api.models.user_models.deposit_account_response import DepositAccountResponse
from src.main.api.models.user_models.transfer_amount_request import TransferAmountRequest
from src.main.api.db.crud.transaction_crud import TransactionCrud as Transaction
from src.main.api.db.crud.account_crud import AccountCRUD as Account

@pytest.mark.api.xfail(reason="BUG: to_account_id stores fromAccountId in DB")
class TestTransferAmount:

    def test_transfer_amount(
            self,
            db_session: Session,
            api_manager:ApiManager,
            create_user_request:CreateUserRequest,
            create_account_second:CreateAccountResponse,
            deposit_account:DepositAccountResponse
    ):
        first_account = deposit_account
        second_account = create_account_second
        amount = first_account.balance/2


        transfer_amount_request=TransferAmountRequest(fromAccountId=first_account.id,toAccountId=second_account.id,amount=amount)
        transfer_amount_response = api_manager.user_steps.transfer_amount(create_user_request, transfer_amount_request)

        transfer_amount_from_db = Transaction.get_transaction_by_from_account_id(db_session, first_account.id)
        second_account_balance_from_db = Account.get_balance_by_account_id(db_session, second_account.id)

        assert transfer_amount_response.fromAccountIdBalance == first_account.balance - transfer_amount_request.amount
        assert transfer_amount_response.fromAccountId == first_account.id
        assert transfer_amount_response.toAccountId == second_account.id

        assert transfer_amount_from_db.to_account_id == second_account.id, f"Wrong transaction to account, expect {second_account.id}"
        assert transfer_amount_from_db.amount == amount, f"Wrong transaction amount, expect {amount}"
        assert second_account_balance_from_db.balance == amount, f"Wrong transaction to account, expect to_account balance {amount}"


    @pytest.mark.parametrize(
        "amount", [
        499.00,
        10000.01
    ]
    )

    def test_transfer_amount_invalid(
            self,
            db_session: Session,
            api_manager:ApiManager,
            create_user_request:CreateUserRequest,
            create_account_second:CreateAccountResponse,
            deposit_account:DepositAccountResponse,
            amount):
        first_account = deposit_account
        second_account = create_account_second
        transfer_amount_request = TransferAmountRequest(fromAccountId=first_account.id, toAccountId=second_account.id, amount=amount)

        api_manager.user_steps.transfer_amount_invalid(create_user_request, transfer_amount_request)

        transfer_amount_from_db = Transaction.get_transaction_by_from_account_id(db_session, first_account.id)

        assert transfer_amount_from_db == None, f"Transaction id='{transfer_amount_from_db.id}' created, error"