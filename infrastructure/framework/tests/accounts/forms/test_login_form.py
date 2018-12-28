from account.forms.login_form import LoginForm


class TestRequired:

    def test_when_username_is_empty_returns_error_with_username(self):
        data = {
            'username': None,
            'password': 'P@ssword99',
        }

        form = LoginForm(data=data)
        form.is_valid()
        assert 'username' in form.errors

    def test_when_password_is_empty_returns_error_with_password(self):
        data = {
            'username': 'johnsmith',
            'password': None,
        }

        form = LoginForm(data=data)
        form.is_valid()
        assert 'password' in form.errors

    def test_when_all_fields_are_filled_up_form_is_valid(self):
        data = {
            'username': 'johnsmith',
            'password': 'P@ssword99',
        }

        form = LoginForm(data=data)
        assert form.is_valid() is True
