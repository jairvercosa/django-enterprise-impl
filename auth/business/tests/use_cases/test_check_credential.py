from auth.business.entities.credential import Credential
from auth.business.use_cases.check_credential import CheckCredential
from auth.business.interfaces.icredential_repository import (
    ICredentialRepository
)


PASSWORD_TEST = 'P@ssword99'


class CrendentialRepository(ICredentialRepository):

    def find(self, uuid):
        pass

    def find_by_username(self, username):
        return Credential.factory(
            username,
            PASSWORD_TEST
        )

    def update_password(self, credential):
        pass


class TestExecute:

    def test_when_username_or_password_does_not_match_returns_false(self):
        use_case = CheckCredential(
            CrendentialRepository(),
            'johnsmith',
            'P@sssword99'
        )

        assert use_case.execute() is False

    def test_when_username_and_password_match_returns_true(self):
        use_case = CheckCredential(
            CrendentialRepository(),
            'johnsmith',
            PASSWORD_TEST
        )

        assert use_case.execute() is True
