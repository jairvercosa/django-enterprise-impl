from uuid import UUID, uuid4
from typing import Optional

from ..values.password import Password
from .encryptor import Encryptor, IEncryptor


class CredentialValueError(Exception):
    pass


class Credential:

    def __init__(
        self,
        uuid: UUID,
        user_uuid: UUID,
        username: str,
        password: str,
        encryptor: IEncryptor=Encryptor
    ):
        self._uuid = uuid
        self._user_uuid = user_uuid
        self._username = username
        self._password = Password(encryptor)
        self._password.value = password

    def __eq__(self, value: 'Credencial') -> bool:
        return (
            self.username == value.username and
            self._password.value == value.password
        )

    @property
    def uuid(self) -> UUID:
        return self._uuid

    @property
    def user_uuid(self) -> UUID:
        return self._user_uuid

    @property
    def username(self) -> str:
        return self._username

    @property
    def password(self) -> str:
        return self._password.value

    @classmethod
    def factory(
        cls,
        user_uuid: UUID,
        username: str,
        password: str,
        uuid: Optional[UUID]=None,
    ):
        uuid = uuid or uuid4()

        if not all([user_uuid, username, password]):
            raise CredentialValueError("All argments are required")

        return cls(uuid, user_uuid, username, password)

    def set_password(self, value: str):
        self._password.value = value
