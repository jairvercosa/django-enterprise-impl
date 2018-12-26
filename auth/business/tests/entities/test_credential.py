import pytest
from uuid import uuid4

from auth.business.entities.credential import Credential, CredentialValueError


class TestFactory:

    def test_when_has_no_uuid_raises_credential_value_error(self):
        with pytest.raises(CredentialValueError):
            Credential.factory(None, uuid4(), 'username', 'p@ssworD9')

    def test_when_has_no_user_uuid_raises_credential_value_error(self):
        with pytest.raises(CredentialValueError):
            Credential.factory(uuid4(), None, 'username', 'p@ssworD9')

    def test_when_has_no_username_raises_credential_value_error(self):
        with pytest.raises(CredentialValueError):
            uuid_value = uuid4()
            Credential.factory(uuid_value, uuid_value, None, 'p@ssworD9')

    def test_when_has_no_password_raises_credential_value_error(self):
        with pytest.raises(CredentialValueError):
            uuid_value = uuid4()
            Credential.factory(uuid_value, uuid_value, 'username', None)

    def test_returns_credential_instance(self):
        uuid_value = uuid4()
        result = Credential.factory(
            uuid_value,
            uuid_value,
            'username',
            'p@ssworD9'
        )

        assert isinstance(result, Credential)



class TestCredentialProperties:

    def setup_method(self, test_method):
        uuid_value = uuid4()
        self.params = {
            "uuid": uuid_value,
            "username": "John Math",
            "password": "P@ssword9",
        }

        self.credential = Credential.factory(
            self.params['uuid'],
            self.params['uuid'],
            self.params['username'],
            self.params['password'],
        )

    def test_uuid(self):
        assert self.credential.uuid == self.params['uuid']

    def test_user_uuid(self):
        assert self.credential.user_uuid == self.params['uuid']

    def test_username(self):
        assert self.credential.username == self.params['username']

    def test_password(self):
        assert bool(self.credential.password)


class TestPasswordSetter:

    def test_set_password(self):
        uuid_value = uuid4()

        cred = Credential.factory(
            uuid_value,
            uuid_value,
            'username',
            'p@ssworD9'
        )

        old_pass = cred.password
        cred.set_password('New_p@ssw0rd')

        assert old_pass != cred.password


class TestEq:

    def test_when_username_is_different_returns_false(self):
        uuid_value = uuid4()
        crendencial_a = Credential.factory(
            uuid_value,
            uuid_value,
            'usernameA',
            'P@ssword9'
        )

        crendencial_b = Credential.factory(
            uuid_value,
            uuid_value,
            'usernameB',
            'P@ssword9'
        )

        assert bool(crendencial_a == crendencial_b) is False

    def test_when_password_is_different_returns_false(self):
        uuid_value = uuid4()
        crendencial_a = Credential.factory(
            uuid_value,
            uuid_value,
            'usernameA',
            'P@ssword8'
        )

        crendencial_b = Credential.factory(
            uuid_value,
            uuid_value,
            'usernameA',
            'P@ssword9'
        )

        assert bool(crendencial_a == crendencial_b) is False

    def test_when_username_and_password_are_equal_returns_true(self):
        uuid_value = uuid4()
        crendencial_a = Credential.factory(
            uuid_value,
            uuid_value,
            'usernameA',
            'P@ssword9'
        )

        crendencial_b = Credential.factory(
            uuid_value,
            uuid_value,
            'usernameA',
            'P@ssword9'
        )

        assert bool(crendencial_a == crendencial_b) is True
