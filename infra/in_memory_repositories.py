# infra/repositories.py
import uuid
from typing import Dict
from domain.entities import Software, Client, Permission
from domain.repositories import SoftwareRepository, ClientRepository, PermissionRepository


class InMemorySoftwareRepository(SoftwareRepository):
    def __init__(self):
        self.storage: Dict[str, Software] = {
            "1": Software(
                id="1",
                name="The perfect Meal",
                internal_code="1",
                product_owner="Mario Bros",
                technical_owners=["Luigi Bros", "Wario Bros"],
                permissions=[],
            )
        }

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
        self.storage: Dict[str, Client] = {
            "1": Client(
                id="1",
                name="Partner XYZ",
                software=[
                    Software(
                        id="1",
                        name="The perfect Meal",
                        internal_code="1",
                        product_owner="Mario Bros",
                        technical_owners=["Luigi Bros", "Wario Bros"],
                        permissions=[
                            Permission(
                                id="1",
                                name="Access to the API",
                                expiration="2023-06-06",
                                technical_owner="Wario Bros",
                            ),
                            Permission(
                                id="2",
                                name="Access to the Database",
                                expiration="2023-06-06",
                                technical_owner="Wario Bros",
                            ),
                        ],
                    )
                ],
            )
        }

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
        self.storage: Dict[str, Permission] = {
            "1": Permission(
                id="1",
                name="Access to the API",
                expiration="2023-06-06",
                technical_owner="Wario Bros",
            ),
            "2": Permission(
                id="2",
                name="Access to the Database",
                expiration="2023-06-06",
                technical_owner="Wario Bros",
            ),
        }

    def get_all(self):
        return list(self.storage.values())

    def get_by_id(self, id: str):
        return self.storage.get(id)

    def save(self, permission: Permission):
        if not permission.id:
            permission.id = str(uuid.uuid4())
        self.storage[permission.id] = permission
