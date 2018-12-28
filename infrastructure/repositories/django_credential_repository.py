from uuid import UUID
from django.db.models import Model
from django.core.exceptions import ObjectDoesNotExist

from auth.business.entities.credential import Credential
from auth.business.interfaces.icredential_repository import ICredentialRepository


class DjangoCredentialRepository(ICredentialRepository):

    def __init__(self, model: Model):
        self._model = model

    def find(self, uuid: UUID) -> Credential:
        try:
            instance = self._model.objects.get(uuid=uuid)
        except ObjectDoesNotExist:
            return None

        return self._factory_credential(instance)

    def find_by_username(self, username: str) -> Credential:
        try:
            instance = self._model.objects.get(username=username)
        except ObjectDoesNotExist:
            return None

        return self._factory_credential(instance)

    def update_password(self, credential: Credential) -> Credential:
        self._model.objects.filter(
            uuid=credential.uuid
        ).update(password=credential.password)
        return self.find(uuid=credential.uuid)

    def update(self, credential: Credential) -> Credential:
        self._model.objects.filter(
            uuid=credential.uuid
        ).update(
            username=credential.username,
            is_active=credential.active
        )
        return self.find(uuid=credential.uuid)

    def create(self, credential: Credential) -> Credential:
        instance = self._model.objects.create(
            username=credential.username,
            password=credential.password,
            is_active=credential.active
        )

        return self._factory_credential(instance)

    def _factory_credential(self, instance: Model) -> Credential:
        return Credential.factory(
            uuid=instance.uuid,
            username=instance.username,
            password=instance.password,
            active=instance.is_active
        )