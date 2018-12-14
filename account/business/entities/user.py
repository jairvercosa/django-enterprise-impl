from uuid import UUID


class User:

    def __init__(
        self,
        uuid: UUID,
        username: str,
        email: str,
        first_name: str,
        last_name: str,
        password: Optional[str] = None
    ):
        self._uuid = uuid
        self._username = username
        #self.__email = email
        self._first_name = first_name
        self._last_name = last_name
        #self.password = password

    @property
    def uuid(self):
        return self._uuid

    @property
    def username(self):
        return self._username

    @property
    def first_name(self):
        return self._first_name

    @property
    def last_name(self):
        return self._last_name
