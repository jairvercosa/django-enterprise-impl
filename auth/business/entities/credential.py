from uuid import UUID
from typing import Optional


class Credential:

    def __init__(
        self,
        uuid: UUID,
        user_uuid: UUID,
        username: str,
        password: Optional[str] = None
    ):
        self._uuid = uuid
        self._user_uuid = user_uuid
        self._username = username
        #self._password = password

    @property
    def uuid(self):
        return self._uuid

    @property
    def user_uuid(self):
        return self._user_uuid

    @property
    def username(self):
        return self._username
