import pytest
from uuid import UUID, uuid4

from auth.business.entities.credential import Credential, CredentialValueError


class TestFactory:

    def test_when_has_no_uuid_adds_a_uuid(self):
        credencial = Credential.factory('username', 'p@ssworD9')
        assert  isinstance(credencial.uuid, UUID)

    def test_when_has_uuid_keeps_what_was_setted(self):
        uuid_value = uuid4()
        credencial = Credential.factory(
            'username',
            'p@ssworD9',
            uuid_value
        )
        assert credencial.uuid == uuid_value

    def test_when_has_no_username_raises_credential_value_error(self):
        with pytest.raises(CredentialValueError):
            uuid_value = uuid4()
            Credential.factory(None, 'p@ssworD9', uuid_value)

    def test_returns_credential_instance(self):
        uuid_value = uuid4()
        result = Credential.factory(
            'username',
            'p@ssworD9',
            uuid_value,
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
            self.params['username'],
            self.params['password'],
            self.params['uuid'],
        )

    def test_uuid(self):
        assert self.credential.uuid == self.params['uuid']

    def test_username(self):
        assert self.credential.username == self.params['username']

    def test_password(self):
        assert bool(self.credential.password)


class TestPasswordSetter:

    def test_set_password(self):
        uuid_value = uuid4()

        cred = Credential.factory(
            'username',
            'p@ssworD9',
            uuid_value,
        )

        old_pass = cred.password
        cred.set_password('New_p@ssw0rd')

        assert old_pass != cred.password


class TestEq:

    def test_when_username_is_different_returns_false(self):
        uuid_value = uuid4()
        crendencial_a = Credential.factory(
            'usernameA',
            'P@ssword9',
            uuid_value,
        )

        crendencial_b = Credential.factory(
            'usernameB',
            'P@ssword9',
            uuid_value,
        )

        assert bool(crendencial_a == crendencial_b) is False

    def test_when_password_is_different_returns_false(self):
        uuid_value = uuid4()
        crendencial_a = Credential.factory(
            'usernameA',
            'P@ssword8',
            uuid_value,
        )

        crendencial_b = Credential.factory(
            'usernameA',
            'P@ssword9',
            uuid_value,
        )

        assert bool(crendencial_a == crendencial_b) is False

    def test_when_username_and_password_are_equal_returns_true(self):
        uuid_value = uuid4()
        crendencial_a = Credential.factory(
            'usernameA',
            'P@ssword9',
            uuid_value,
        )

        crendencial_b = Credential.factory(
            'usernameA',
            'P@ssword9',
            uuid_value,
        )

        assert bool(crendencial_a == crendencial_b) is True


class TestVerifyPassword:

    def test_when_password_does_not_match_return_false(self):
        credential = Credential.factory(
            username='johnsmith',
            uuid=uuid4()
        )
        credential.set_password('P@ssword9')

        assert credential.verify_password('P@sssword9') is False

    def test_when_password_does_match_return_true(self):
        password = 'P@ssword9'
        credential = Credential.factory(
            username='johnsmith',
            uuid=uuid4()
        )
        credential.set_password(password)

        assert credential.verify_password(password) is True
