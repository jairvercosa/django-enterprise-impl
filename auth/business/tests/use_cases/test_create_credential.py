import pytest
from uuid import uuid4

from auth.business.entities.credential import Credential
from auth.business.interfaces.icredential_repository import (
    ICredentialRepository
)

from auth.business.use_cases.create_credential import (
    CreateCredential,
    CredentialAlreadyExistError
)


class CredentialRepositoryFind(ICredentialRepository):

    def find(self, uuid):
        pass

    def find_by_username(self, username):
        return Credential.factory(username='johnmatt')

    def update_password(self, credential):
        pass

    def update(self, credential):
        pass

    def create(self, credential):
        pass


class CredentialRepositoryCreate(ICredentialRepository):

    def find(self, uuid):
        pass

    def find_by_username(self, username):
        return None

    def update_password(self, credential):
        pass

    def update(self, credential):
        pass

    def create(self, credential):
        return credential


class TestExecute:

    def test_when_credential_already_exist_raise_exception(self):
        with pytest.raises(CredentialAlreadyExistError):
            usecase = CreateCredential(
                credential_repository=CredentialRepositoryFind(),
                username='johnsmith',
                password='P@sswordD99'
            )
            usecase.execute()

    def test_when_credential_does_not_exist_returns_new_credential(self):
        usecase = CreateCredential(
            credential_repository=CredentialRepositoryCreate(),
            username='johnsmith',
            password='P@sswordD99'
        )
        credential = usecase.execute()
        assert isinstance(credential, Credential)

    def test_persist_new_credential(self, mocker):
        credentail_uuid = uuid4()
        mocker.patch.object(
            CredentialRepositoryCreate,
            'create',
            return_value=None
        )

        usecase = CreateCredential(
            CredentialRepositoryCreate(),
            username='johnsmith',
            password='P@sswordD99'
        )
        usecase.execute()
        assert CredentialRepositoryCreate.create.called is True
