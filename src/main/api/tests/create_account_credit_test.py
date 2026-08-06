import pytest

@pytest.mark.api
class TestCreateAccountCredit:
    def test_create_account_credit(self, api_manager,create_credit_secret):
        response = api_manager.credit_steps.create_account_credit(create_credit_secret)
        assert response.balance == 0

    def test_create_account_credit_second(self, api_manager,create_credit_secret, create_credit_account):
        credit_account=create_credit_account
        credit_account_second_response = api_manager.credit_steps.create_account_credit(create_credit_secret)

        assert credit_account_second_response.balance == 0
        assert credit_account_second_response.id != credit_account.id
        assert credit_account_second_response.number != credit_account.number

    def test_create_credit_account_third_invalid (self, api_manager,create_credit_secret, create_credit_account_second):
        api_manager.credit_steps.create_account_credit_invalid(create_credit_secret)




