from sqlalchemy.orm import Session
from typing import Type, Any, Dict

from .methods import (
    add_record,
    save_record,
    update_record,
    delete_record,
    has_child
)


class Recorder:
    @staticmethod
    def add(session: Session, record: Type[Any]):
        add_record(session, record)

    @staticmethod
    def save(session: Session, record: Type[Any]):
        save_record(session, record)

    @staticmethod
    def update(session: Session, record: Type[Any], new_data: Dict):
        update_record(session, record, new_data)

    @staticmethod
    def delete(session: Session, record: Type[Any]):
        delete_record(session, record)

    @staticmethod
    def has_child(record: Type[Any], child_model: Type[Any]) -> bool:
        return has_child(record, child_model)
