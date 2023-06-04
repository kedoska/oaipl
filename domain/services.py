# services.py
from .repositories import SoftwareRepository, ClientRepository, PermissionRepository


class SoftwareService:
    def __init__(self, repo: SoftwareRepository):
        self.repo = repo

    def get_all_software(self):
        return self.repo.get_all()

    def get_software_by_id(self, id: str):
        return self.repo.get_by_id(id)


class ClientService:
    def __init__(self, repo: ClientRepository):
        self.repo = repo

    def get_all_clients(self):
        return self.repo.get_all()

    def get_client_by_id(self, id: str):
        return self.repo.get_by_id(id)


class PermissionService:
    def __init__(self, repo: PermissionRepository):
        self.repo = repo

    def get_all_permissions(self):
        return self.repo.get_all()

    def get_permission_by_id(self, id: str):
        return self.repo.get_by_id(id)
