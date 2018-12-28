from django.contrib.auth.models import AnonymousUser
from django.test import RequestFactory

from account.views.register_view import (
    CreateCredential,
    CredentialAlreadyExistError,
    FormView,
    PasswordStrengthError,
    RegisterView,
)


class TestFormValid:

    def test_execute_create_credential_usecase(self, mocker):
        mocker.patch.object(CreateCredential, 'execute', return_value=None)
        mocker.patch.object(FormView, 'form_valid', return_value=None)

        view = RegisterView()
        form_class = view.get_form_class()
        form = form_class(data={
            'username': 'johnsmith',
            'password': 'P@ssword99',
            'confirm_password': 'P@ssword99',
        })
        form.is_valid()

        view.form_valid(form)
        assert CreateCredential.execute.called is True

    def test_when_form_is_valid_and_credential_already_exist_call_form_invalid_method(self, mocker):
        def execute():
            raise CredentialAlreadyExistError()

        mocker.patch.object(CreateCredential, 'execute', side_effect=execute)
        mocker.patch.object(RegisterView, 'form_invalid', return_value=None)

        view = RegisterView()
        form_class = view.get_form_class()
        form = form_class(data={
            'username': 'johnsmith',
            'password': 'P@ssword99',
            'confirm_password': 'P@ssword99',
        })
        form.is_valid()

        view.form_valid(form)
        assert RegisterView.form_invalid.called is True

    def test_when_form_is_valid_and_password_is_invalid_call_form_invalid_method(self, mocker):
        def execute():
            raise PasswordStrengthError()

        mocker.patch.object(CreateCredential, 'execute', side_effect=execute)
        mocker.patch.object(RegisterView, 'form_invalid', return_value=None)

        view = RegisterView()
        form_class = view.get_form_class()
        form = form_class(data={
            'username': 'johnsmith',
            'password': 'password',
            'confirm_password': 'password',
        })
        form.is_valid()

        view.form_valid(form)
        assert RegisterView.form_invalid.called is True


class TestRequest:

    def test_when_send_a_get_request_return_200(self):
        factory = RequestFactory()
        request = factory.get('/account/register/')
        request.user = AnonymousUser()

        response = RegisterView.as_view()(request)
        assert response.status_code == 200
