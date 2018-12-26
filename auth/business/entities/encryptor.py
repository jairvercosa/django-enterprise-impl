from passlib.hash import argon2

from ..interfaces.iencryptor import IEncryptor


class EncryptorExpectedTypeError(Exception):
    pass


class Encryptor(IEncryptor):
    __salt = "492MIj$M"

    @classmethod
    def encrypt(cls, value: str) -> str:
        if not isinstance(value, str):
            raise EncryptorExpectedTypeError("value should be a string")

        salt = str.encode(cls.__salt)
        return argon2.using(rounds=4, salt=salt).hash(value)

    @classmethod
    def verify(cls, value: str, encrypted: str) -> bool:
        return argon2.verify(value, encrypted)
