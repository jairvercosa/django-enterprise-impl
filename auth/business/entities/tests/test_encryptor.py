import pytest

from ..encryptor import Encryptor, EncryptorExpectedTypeError


class TestEncrypt:

    def test_when_param_is_not_strinc_raise_encrypt_expected_type_error_exception(self):
        with pytest.raises(EncryptorExpectedTypeError):
            Encryptor.encrypt(None)

    def test_returns_str(self):
        assert isinstance(Encryptor.encrypt('pass'), str)

    def test_encrypt_value(self):
        expected_value = '$argon2i$v=19$m=102400,t=4,p=8$NDkyTUlqJE0$K4PWIcRV17QtJn++dv4YqA'
        assert Encryptor.encrypt('pass') == expected_value
