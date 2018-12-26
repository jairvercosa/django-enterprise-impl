import abc


class IEncryptor(metaclass=abc.ABCMeta):

    @abc.abstractclassmethod
    def encrypt(cls, value: str) -> str:
        pass

    @abc.abstractclassmethod
    def verify(cls, valeu: str, encrypted: str) -> bool:
        pass