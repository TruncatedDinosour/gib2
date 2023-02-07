import sqlalchemy
import typing
from .cfg import Cfg
from sqlalchemy.orm import Session

class SQLiteDB:
    engine: sqlalchemy.engine.base.Engine
    base: typing.Any
    session: Session
    def __init__(self, db_name: str, cfg: Cfg) -> None: ...
    def table(self, cls: typing.Any) -> typing.Any: ...
    def init(self) -> None: ...
    def commit(self) -> None: ...
    def __iadd__(self, what: typing.Any) -> SQLiteDB: ...
    def __isub__(self, what: sqlalchemy.sql.elements.BinaryExpression) -> SQLiteDB: ...