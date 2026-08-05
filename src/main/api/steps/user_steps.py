
from src.main.api.foundation.endpoint import Endpoint
from src.main.api.foundation.requesters.crud_requester import CrudRequester
from src.main.api.foundation.requesters.validate_crud_requester import ValidateCrudRequester
from src.main.api.models.admin_models.create_user_request import CreateUserRequest
from src.main.api.models.user_models.deposit_account_request import DepositAccountRequest
from src.main.api.specs.request_specs import RequestSpecs
from src.main.api.specs.response_specs import ResponseSpecs
from src.main.api.steps.base_steps import BaseSteps


class UserSteps(BaseSteps):

    def login_unregistered(self, unregistered_login: CreateUserRequest):
        CrudRequester(
            RequestSpecs.unauth_headers(),
            Endpoint.LOGIN_USER,
            ResponseSpecs.request_bad_login()
        ).post(unregistered_login)

    def create_account(self, create_user_request: CreateUserRequest):
        response = ValidateCrudRequester(
            RequestSpecs.auth_headers(username=create_user_request.username, password=create_user_request.password),
            Endpoint.CREATE_ACCOUNT,
            ResponseSpecs.request_created()
        ).post()
        return response

    def create_account_invalid(self, create_user_request: CreateUserRequest):
        response = CrudRequester(
            RequestSpecs.auth_headers(username=create_user_request.username, password=create_user_request.password),
            Endpoint.CREATE_ACCOUNT,
            ResponseSpecs.request_no_more_account()
        ).post(create_user_request)




    def deposit_account(self,  create_user_request: CreateUserRequest, deposit_account_request: DepositAccountRequest):
        response = ValidateCrudRequester(
            RequestSpecs.auth_headers(username=create_user_request.username, password=create_user_request.password),
            Endpoint.DEPOSIT_ACCOUNT,
            ResponseSpecs.request_ok()
        ).post(deposit_account_request)
        return response

    def transfer_amount (self,create_user_request, transfer_amount_request):
        response = ValidateCrudRequester(
            RequestSpecs.auth_headers(username=create_user_request.username, password=create_user_request.password),
            Endpoint.TRANSFER_AMOUNT,
            ResponseSpecs.request_ok()
        ).post(transfer_amount_request)
        return response


