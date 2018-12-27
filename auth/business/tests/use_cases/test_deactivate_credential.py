from uuid import uuid4

from auth.business.interfaces.icredential_repository import (
    ICredentialRepository
)
from auth.business.entities.credential import Credential
from auth.business.use_cases.deactivate_credential import DeactivateCredential


class CredentialRepository(ICredentialRepository):

    def find(self, uuid):
        return Credential.factory(
            uuid=uuid,
            username='johnsmith',
            active=True
        )
    
    def find_by_username(self, username):
        pass

    def update_password(self, credential):
        pass

    def update(self, credential):
        return credential


class TestExecute:

    def test_update_credential_active_status(self):
        credentail_uuid = uuid4()
        usecase = DeactivateCredential(
            CredentialRepository(),
            credentail_uuid
        )

        credential = usecase.execute()
        assert credential.active is False

    def test_persit_deactivated_status(self, mocker):
        credentail_uuid = uuid4()
        CredentialRepository.update = mocker.MagicMock(
            return_value=Credential.factory(
                uuid=credentail_uuid,
                username='johnsmith',
                active=True
            )
        )

        usecase = DeactivateCredential(CredentialRepository(), credentail_uuid)
        usecase.execute()
        assert CredentialRepository.update.called is True
