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
        encryptor: IEncryptor=Encryptor,
        active: Optional[bool]=True
    ):
        self._uuid = uuid
        self._username = username
        self._password = Password(encryptor, password)
        self._active = active

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

    @property
    def active(self) -> bool:
        return self._active

    @classmethod
    def factory(
        cls,
        username: str,
        password: Optional[str]=None,
        uuid: Optional[UUID]=None,
        active: Optional[bool]=True
    ) -> ICredential:
        uuid = uuid or uuid4()

        if not username:
            raise CredentialValueError("All argments are required")

        return cls(
            uuid=uuid,
            username=username,
            password=password,
            active=active
        )

    def set_password(self, value: str):
        self._password.value = value

    def verify_password(self, value: str) -> bool:
        return self._password == value
    
    def deactivate(self):
        self._active = False
