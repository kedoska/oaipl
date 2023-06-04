# infra/repositories.py
import uuid
from typing import Dict
from domain.entities import Software, Client, Permission
from domain.repositories import SoftwareRepository, ClientRepository, PermissionRepository


class InMemorySoftwareRepository(SoftwareRepository):
    def __init__(self):
        self.storage: Dict[str, Software] = {}

    def get_all(self):
        return list(self.storage.values())

    def get_by_id(self, id: str):
        return self.storage.get(id)

    def save(self, software: Software):
        if not software.id:
            software.id = str(uuid.uuid4())
        self.storage[software.id] = software


class InMemoryClientRepository(ClientRepository):
    def __init__(self):
        self.storage: Dict[str, Client] = {}

    def get_all(self):
        return list(self.storage.values())

    def get_by_id(self, id: str):
        return self.storage.get(id)

    def save(self, client: Client):
        if not client.id:
            client.id = str(uuid.uuid4())
        self.storage[client.id] = client


class InMemoryPermissionRepository(PermissionRepository):
    def __init__(self):
        self.storage: Dict[str, Permission] = {}

    def get_all(self):
        return list(self.storage.values())

    def get_by_id(self, id: str):
        return self.storage.get(id)

    def save(self, permission: Permission):
        if not permission.id:
            permission.id = str(uuid.uuid4())
        self.storage[permission.id] = permission
