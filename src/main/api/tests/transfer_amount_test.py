import pytest

from src.main.api.models.user_models.transfer_amount_request import TransferAmountRequest


@pytest.mark.api
class TestTransferAmount:

    def test_transfer_amount(self, api_manager, create_user_request, create_account_second,deposit_account):
        first_account = deposit_account
        second_account = create_account_second
        amount = first_account.balance/2


        transfer_amount_request=TransferAmountRequest(fromAccountId=first_account.id,toAccountId=second_account.id,amount=amount)
        transfer_amount_response = api_manager.user_steps.transfer_amount(create_user_request, transfer_amount_request)

        assert transfer_amount_response.fromAccountIdBalance == first_account.balance - transfer_amount_request.amount
        assert transfer_amount_response.fromAccountId == first_account.id
        assert transfer_amount_response.toAccountId == second_account.id

    def test_transfer_in(self):
        pass
    def test_transfer_out(self):
        pass
