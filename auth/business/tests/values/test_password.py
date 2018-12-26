import pytest

from auth.business.interfaces.iencryptor import IEncryptor
from auth.business.values.password import Password, PasswordStrengthError


class FakeEncryptor(IEncryptor):

    @staticmethod
    def encrypt(value):
        return value + 'encrypt'


class TestPasswordValueSetter:

    def test_when_password_is_not_strong_raises_password_strength_error(self):
        with pytest.raises(PasswordStrengthError):
            password_value = Password(FakeEncryptor)
            password_value.value = 'pass'

    def test_when_password_is_strong_stores_it_encrypted(self):
        password = 'P@ssword9'
        password_value = Password(FakeEncryptor)
        password_value.value = password

        assert password_value.value != password


class TestValidateStrength:

    def test_when_password_length_less_than_8_returns_legth_false_on_the_dict(self):
        _, result = Password.validate_strength('pass')
        assert result.get('length') is False

    def test_when_password_length_greather_than_7_returns_legth_true_on_the_dict(self):
        _, result = Password.validate_strength('password')
        assert result.get('length') is True

    def test_when_password_has_no_digit_returns_digit_false_on_the_dict(self):
        _, result = Password.validate_strength('password')
        assert result.get('digit') is False

    def test_when_password_has_a_digit_returns_digit_true_on_the_dict(self):
        _, result = Password.validate_strength('password9')
        assert result.get('digit') is True

    def test_when_password_has_no_uppercase_returns_uppercase_false_on_the_dict(self):
        _, result = Password.validate_strength('password')
        assert result.get('uppercase') is False

    def test_when_password_has_an_uppercase_returns_uppercase_true_on_the_dict(self):
        _, result = Password.validate_strength('passworD')
        assert result.get('uppercase') is True

    def test_when_password_has_no_lowercase_returns_lowercase_false_on_the_dict(self):
        _, result = Password.validate_strength('PASSWORD')
        assert result.get('lowercase') is False

    def test_when_password_has_a_lowercase_returns_lowercase_true_on_the_dict(self):
        _, result = Password.validate_strength('PASSWORd')
        assert result.get('lowercase') is True

    def test_when_password_has_no_symbols_returns_symbol_false_on_the_dict(self):
        _, result = Password.validate_strength('password')
        assert result.get('symbol') is False

    def test_when_password_has_a_symbols_returns_symbol_true_on_the_dict(self):
        _, result = Password.validate_strength('p@ssword')
        assert result.get('symbol') is True

    def test_when_password_length_less_than_8_returns_false(self):
        result, _  = Password.validate_strength('pass')
        assert result is False
    
    def test_when_password_has_no_digit_returns_false(self):
        result, _  = Password.validate_strength('password')
        assert result is False

    def test_when_password_has_no_uppercase_returns_false(self):
        result, _  = Password.validate_strength('password9')
        assert result is False

    def test_when_password_has_no_lowercase_returns_false(self):
        result, _  = Password.validate_strength('PASSWORD9')
        assert result is False

    def test_when_password_has_no_symbols_returns_false(self):
        result, _  = Password.validate_strength('passworD9')
        assert result is False

    def test_when_password_is_strong_returns_true(self):
        result, _  = Password.validate_strength('p@ssworD9')
        assert result is True
