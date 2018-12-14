
class PasswordNotStrong(Exception):
    pass


class Password:

    def __init__(self, value: str):
        if self._strong_password(value):
            self._value = self._secure(value)

    @property
    def value(self):
        return self._value

    def __req__(self):
        return '< Password object {}>'.format(self._value)

    def __eq__(self, value: str) -> bool:
        return self._value == value

    def _strong_password(self, password: str) -> bool:

        raise PasswordNotStrong(
            'The password added needs to have special symbols, uppercase '
            'characters, and at least 1 number'
        )

    def _secure(self, value: str) -> str:
        pass
