import pytest
from uuid import uuid4

from auth.business.entities.credential import Credential
from auth.business.interfaces.icredential_repository import (
    ICredentialRepository
)
from auth.business.use_cases.set_new_password import (
    OldPasswordDoesNotMatch,
    SetNewPassword,
)
    

PASSWORD_TEST = 'P@ssword99'


class CredentialRepository(ICredentialRepository):

    def find(self, uuid):
        credential = Credential.factory(
            username='johnsmith',
            uuid=uuid
        )
        credential.set_password(PASSWORD_TEST)
        return credential

    def find_by_username(self, username):
        pass

    def update_password(self, credential):
        return Credential.factory(
            username='johnsmith',
            password=credential.password,
            uuid=credential.uuid
        )

    def update(self, credential):
        pass


class TestExecute:

    def test_when_old_password_does_not_match_raise_exception(self):
        with pytest.raises(OldPasswordDoesNotMatch):
            use_case = SetNewPassword(
                CredentialRepository(),
                uuid4(),
                '',
                None
            )

            use_case.execute()

    def test_when_old_password_perform_update(self):
        new_password = 'P@sssword99'

        use_case = SetNewPassword(
            CredentialRepository(),
            uuid4(),
            PASSWORD_TEST,
            new_password
        )

        credential = use_case.execute()
        assert credential.verify_password(new_password) is True

    def test_persist_new_password(self, mocker):
        credentail_uuid = uuid4()
        new_password = 'P@sssword99'

        CredentialRepository.update_password = mocker.MagicMock(
            return_value=Credential.factory(
                uuid=credentail_uuid,
                username='johnsmith',
                active=True
            )
        )

        use_case = SetNewPassword(
            CredentialRepository(),
            uuid4(),
            PASSWORD_TEST,
            new_password
        )
        use_case.execute()
        assert CredentialRepository.update_password.called is True
