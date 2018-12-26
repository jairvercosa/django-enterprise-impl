import abc

from uuid import UUID
from typing import Optional


class ICredential:

    @abc.abstractproperty
    def uuid(self) -> UUID:
        pass

    @abc.abstractproperty
    def user_uuid(self) -> UUID:
        pass

    @abc.abstractproperty
    def username(self) -> str:
        pass

    @abc.abstractproperty
    def password(self) -> str:
        pass

    @abc.abstractclassmethod
    def factory(
        cls,
        user_id: UUID,
        username: str,
        password: str,
        uuid: Optional[UUID]=None
    ) -> 'ICredential':
        pass

    @abc.abstractmethod
    def set_password(self, value: str):
        pass
