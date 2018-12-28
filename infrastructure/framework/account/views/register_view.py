from django.urls import reverse_lazy
from django.views.generic import FormView

from auth.business.values.password import PasswordStrengthError
from auth.business.use_cases.create_credential import (
    CreateCredential,
    CredentialAlreadyExistError
)

from infrastructure.repositories.django_credential_repository import (
    DjangoCredentialRepository
)
from ..forms.register_form import RegisterForm
from ..models import UserAccount


class RegisterView(FormView):
    template_name = 'account/register.html'
    form_class = RegisterForm
    success_url = reverse_lazy('summary')

    def form_valid(self, form):
        repository = DjangoCredentialRepository(UserAccount)
        usecase = CreateCredential(
            credential_repository=repository,
            username=form.data['username'],
            password=form.data['password']
        )

        try:
            usecase.execute()
        except CredentialAlreadyExistError:
            form.add_error('username', 'Username already exist.')
        except PasswordStrengthError as ex:
            form.add_error('password', str(ex))

        print(form.errors)
        if form.errors:
            return self.form_invalid(form)

        return super().form_valid(form)
