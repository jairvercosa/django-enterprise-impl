import abc

from auth.business.interfaces.icredential import ICredential


class ICredentialRepository(metaclass=abc.ABCMeta):

    def find(self, pk: int) -> ICredential:
        pass

    def find_by_username(self, username: str) -> ICredential:
        pass
