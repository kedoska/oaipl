# entities.py
from typing import List


class Software:
    def __init__(self, id: str, name: str, internal_code: str, product_owner: str, technical_owners: List[str],
                 permissions: List['Permission']):
        self.id = id
        self.name = name
        self.internal_code = internal_code
        self.product_owner = product_owner
        self.technical_owners = technical_owners
        self.permissions = permissions


class Client:
    def __init__(self, id: str, name: str, software: List[Software]):
        self.id = id
        self.name = name
        self.software = software


class Permission:
    def __init__(self, id: str, name: str, expiration: str, technical_owner: str):
        self.id = id
        self.name = name
        self.expiration = expiration
        self.technical_owner = technical_owner
