#!/usr/bin/env python3
# @generated AUTOGENERATED file. Do not Change!

from dataclasses import dataclass
from datetime import datetime
from gql.gql.datetime_utils import DATETIME_FIELD
from gql.gql.graphql_client import GraphqlClient
from functools import partial
from numbers import Number
from typing import Any, Callable, List, Mapping, Optional

from dataclasses_json import DataClassJsonMixin

from gql.gql.enum_utils import enum_field
from .user_role_enum import UserRole
from .user_status_enum import UserStatus


QUERY: List[str] = ["""
query UserQuery($authID: String!) {
  user(authID: $authID) {
    id
    authID
    email
    status
    role
  }
}

"""]

@dataclass
class UserQuery(DataClassJsonMixin):
    @dataclass
    class UserQueryData(DataClassJsonMixin):
        @dataclass
        class User(DataClassJsonMixin):
            id: str
            authID: str
            email: str
            status: UserStatus = enum_field(UserStatus)
            role: UserRole = enum_field(UserRole)

        user: Optional[User]

    data: UserQueryData

    @classmethod
    # fmt: off
    def execute(cls, client: GraphqlClient, authID: str) -> UserQueryData:
        # fmt: off
        variables = {"authID": authID}
        response_text = client.call(''.join(set(QUERY)), variables=variables)
        return cls.from_json(response_text).data
