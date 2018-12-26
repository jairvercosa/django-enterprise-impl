from auth.business.entities.credential import Credential
from auth.business.use_cases.authenticate_user import AuthenticateUser
from auth.business.interfaces.icredential_repository import (
    ICredentialRepository
)


PASSWORD_TEST = 'P@ssword99'


class CrendentialRepository(ICredentialRepository):

    def find(self, pk):
        pass

    def find_by_username(self, username):
        return Credential.factory(
            username,
            PASSWORD_TEST
        )


class TestExecute:

    def test_when_username_or_password_does_not_match_returns_false(self):
        user_case = AuthenticateUser(
            CrendentialRepository(),
            'johnsmith',
            'P@sssword99'
        )

        assert user_case.execute() is False

    def test_when_username_and_password_match_returns_true(self):
        user_case = AuthenticateUser(
            CrendentialRepository(),
            'johnsmith',
            PASSWORD_TEST
        )

        assert user_case.execute() is True
