from uuid import UUID, uuid4
from typing import Optional

from ..values.password import Password
from ..interfaces.icredential import ICredential
from .encryptor import Encryptor, IEncryptor


class CredentialValueError(Exception):
    pass


class Credential(ICredential):

    def __init__(
        self,
        uuid: UUID,
        username: str,
        password: Optional[str]=None,
        encryptor: IEncryptor=Encryptor
    ):
        self._uuid = uuid
        self._username = username
        self._password = Password(encryptor, password)

    def __eq__(self, value: 'Credencial') -> bool:
        return (
            self.username == value.username and
            self._password.value == value.password
        )

    @property
    def uuid(self) -> UUID:
        return self._uuid

    @property
    def username(self) -> str:
        return self._username

    @property
    def password(self) -> str:
        return self._password.value

    @classmethod
    def factory(
        cls,
        username: str,
        password: Optional[str]=None,
        uuid: Optional[UUID]=None,
    ) -> ICredential:
        uuid = uuid or uuid4()

        if not username:
            raise CredentialValueError("All argments are required")

        return cls(uuid, username, password)

    def set_password(self, value: str):
        self._password.value = value

    def verify_password(self, value: str) -> bool:
        return self._password == value
