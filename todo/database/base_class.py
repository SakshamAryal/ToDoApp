from sqlalchemy.orm import as_declarative
from sqlalchemy import MetaData
from typing import Any, Dict

POSTGRES_NAMING_CONVENTION = {
    "ix": "%(column_0_label)s_idx",           # index names
    "uq": "%(table_name)s_%(column_0_name)s_key",  # unique constraint names
    "ck": "%(table_name)s_%(constraint_name)s_check",  # check constraint names
    "fk": "%(table_name)s_%(column_0_name)s_fkey",  # foreign key names
    "pk": "%(table_name)s_pkey",
}

metadata = MetaData(naming_convention=POSTGRES_NAMING_CONVENTION)

class_registry: Dict[str, Any] = {}

@as_declarative(class_registry=class_registry)
class Base:
    metadata = metadata
    __name__: str
    id: Any
    __abstract__: bool = True