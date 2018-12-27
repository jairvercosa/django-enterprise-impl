from auth.business.entities.credential import Credential
from auth.business.use_cases.check_credential import CheckCredential
from auth.business.interfaces.icredential_repository import (
    ICredentialRepository
)


USERNAME_TEST = 'johnsmith'
PASSWORD_TEST = 'P@ssword99'


class AbstractRepository(ICredentialRepository):
    
    def find(self, uuid):
        pass

    def update_password(self, credential):
        pass

    def update(self, credential):
        pass

    def create(self, credential):
        pass


class CredentialRepository(AbstractRepository):

    def find_by_username(self, username):
        return Credential.factory(
            USERNAME_TEST,
            PASSWORD_TEST
        )


class CredentialRepositoryDeactivated(AbstractRepository):

    def find_by_username(self, username):
        return Credential.factory(
            USERNAME_TEST,
            PASSWORD_TEST,
            active=False
        )


class TestExecute:

    def test_when_username_does_not_match_returns_false(self):
        use_case = CheckCredential(
            CredentialRepository(),
            'john',
            PASSWORD_TEST
        )

        assert use_case.execute() is False

    def test_when_password_does_not_match_returns_false(self):
        use_case = CheckCredential(
            CredentialRepository(),
            USERNAME_TEST,
            'P@sssword999'
        )

        assert use_case.execute() is False

    def test_when_credential_is_not_active_returns_false(self):
        use_case = CheckCredential(
            CredentialRepositoryDeactivated(),
            USERNAME_TEST,
            PASSWORD_TEST
        )

        assert use_case.execute() is False

    def test_when_username_and_password_match_and_credential_is_active_returns_true(self):
        use_case = CheckCredential(
            CredentialRepository(),
            USERNAME_TEST,
            PASSWORD_TEST
        )

        assert use_case.execute() is True
