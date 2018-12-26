from typing import Optional

from ..interfaces.icredential_repository import ICredentialRepository
from ..entities.credential import Credential


class AuthenticateUser:

    def __init__(
        self,
        credential_repository: ICredentialRepository,
        username: str,
        password: str
    ):
        self._repository = credential_repository
        self._credential = Credential.factory(username, password)

    def execute(self) -> (bool, Optional[str]):
        user_credential = self._repository.find_by_username(
            self._credential.username
        )

        return user_credential == self._credential
