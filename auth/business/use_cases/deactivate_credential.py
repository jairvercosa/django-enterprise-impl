from uuid import UUID

from ..interfaces.iuse_case import IUseCase
from ..interfaces.icredential_repository import ICredentialRepository


class DeactivateCredential(IUseCase):

    def __init__(
        self,
        credencial_repository: ICredentialRepository,
        credential_uuid: UUID
    ):
        self._repository = credencial_repository
        self._credential_uuid = credential_uuid

    def execute(self):
        credential = self._repository.find(self._credential_uuid)
        credential.deactivate()

        return self._repository.update(credential)
