from typing import Optional
from uuid import UUID

from ..entities.credential import Credential
from ..interfaces.icredential_repository import ICredentialRepository
from ..interfaces.iuse_case import IUseCase


class OldPasswordDoesNotMatch(Exception):
    pass


class SetNewPassword(IUseCase):

    def __init__(
        self,
        credential_repository: ICredentialRepository,
        credential_uuid: UUID,
        old_password: str,
        new_password: str
    ):
        self._repository = credential_repository
        self._credential_uuid = credential_uuid
        self._old_password = old_password
        self._new_password = new_password

    def execute(self) -> (bool, Credential):
        credential = self._repository.find(self._credential_uuid)
        
        if credential.verify_password(self._old_password):
            credential.set_password(self._new_password)
            credential = self._repository.update_password(credential)
            return credential
        else:
            raise OldPasswordDoesNotMatch(
                "Old password must be the same as the credential"
            )
