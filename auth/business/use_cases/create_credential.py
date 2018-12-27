from typing import Optional
from uuid import UUID, uuid4

from ..entities.credential import Credential
from ..interfaces.iuse_case import IUseCase
from ..interfaces.icredential_repository import ICredentialRepository


class CredentialAlreadyExistError(Exception):
    pass


class CreateCredential(IUseCase):

    def __init__(
        self,
        credential_repository: ICredentialRepository,
        username: str,
        password: str,
        uuid: Optional[UUID]=None
    ):
        self._repository = credential_repository
        self._username = username
        self._password = password
        self._uuid = uuid

    def execute(self):
        credential = self._repository.find_by_username(self._username)

        if credential is not None:
            raise CredentialAlreadyExistError

        credential = Credential.factory(
            username=self._username,
            uuid=self._uuid
        )
        credential.set_password(self._password)
        return self._repository.create(credential)
