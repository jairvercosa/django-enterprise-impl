from uuid import uuid4
from collections import namedtuple
from django_mock_queries.query import MockSet

from auth.business.entities.credential import Credential
from web.account.models import UserAccount
from repositories.django_credential_repository import DjangoCredentialRepository


class TestFind:

    def test_when_object_does_not_exist_returns_none(self, mocker):
        class FakeModel:
            objects = MockSet()

        repository = DjangoCredentialRepository(FakeModel())
        result = repository.find(uuid4())
        assert result is None

    def test_when_object_does_exist_returns_a_credential(self, mocker):
        account_uuid = uuid4()
        mockset = MockSet(
            UserAccount(
                uuid=account_uuid,
                username='johnsmith',
                password='$argon2i$v=19$m=102400,t=4,p=8$NDkyTUlqJE0$K4PWIcRV17QtJn++dv4YqA',
                is_active=True
            )
        )

        class FakeModel:
            objects = mockset

        repository = DjangoCredentialRepository(FakeModel())
        result = repository.find(account_uuid)
        assert isinstance(result, Credential)


class TestFindByUserName:
    user_name = 'johnsmith'

    def test_when_object_does_not_exist_returns_none(self, mocker):
        class FakeModel:
            objects = MockSet()

        repository = DjangoCredentialRepository(FakeModel())
        result = repository.find_by_username('johnsmith')
        assert result is None

    def test_when_object_does_exist_returns_a_credential(self, mocker):
        account_uuid = uuid4()
        username = 'johnsmith'

        mockset = MockSet(
            UserAccount(
                uuid=account_uuid,
                username=username,
                password='$argon2i$v=19$m=102400,t=4,p=8$NDkyTUlqJE0$K4PWIcRV17QtJn++dv4YqA',
                is_active=True
            )
        )

        class FakeModel:
            objects = mockset

        repository = DjangoCredentialRepository(FakeModel())
        result = repository.find_by_username(username)
        assert isinstance(result, Credential)


class TestUpdatePassword:
    user_name = 'johnsmith'

    def setup_method(self):
        uuid = uuid4()
        old_password = '$argon2i$v=19$m=102400,t=4,p=8$NDkyTUlqJE0$K4PWIcRV17QtJn++dv4YqA'

        self._instance = UserAccount(
            uuid=uuid,
            username='johnsmith',
            password=old_password,
            is_active=True
        )

        mockset = MockSet(self._instance, **{
            'model': UserAccount
        })
        class FakeModel:
            objects = mockset

        repository = DjangoCredentialRepository(FakeModel())
        self._credential = repository.find(uuid)
        self._credential.set_password('P@sssword99')

        self._result = repository.update_password(self._credential)

    def test_update_password(self):
        assert self._credential.password == self._instance.password
    
    def test_returns_credential_instance(self, mocker):
        assert isinstance(self._result, Credential)
