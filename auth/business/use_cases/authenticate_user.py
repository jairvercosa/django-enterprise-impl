from ..entities.credential import Credential
from ..interfaces.icredential_repository import ICredentialRepository
from ..interfaces.iuse_case import IUseCase


class AuthenticateUser(IUseCase):

    def __init__(
        self,
        credential_repository: ICredentialRepository,
        username: str,
        password: str
    ):
        self._repository = credential_repository
        self._credential = Credential.factory(username, password)

    def execute(self) -> bool:
        user_credential = self._repository.find_by_username(
            self._credential.username
        )

        return user_credential == self._credential
