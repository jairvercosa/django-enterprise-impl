import abc
from uuid import UUID

from ..interfaces.icredential import ICredential


class ICredentialRepository(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def find(self, uuid: UUID) -> ICredential:
        pass

    @abc.abstractmethod
    def find_by_username(self, username: str) -> ICredential:
        pass

    @abc.abstractmethod
    def update_password(self, credential: ICredential) -> ICredential:
        pass
