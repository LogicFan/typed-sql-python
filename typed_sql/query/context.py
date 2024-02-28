from typing_extensions import Dict, Any


class QueryContext:
    def __init__(self) -> None:
        self.tables: Dict[str, str] = {}
        self.params: Dict[str, Any] = {}

    def insert_table(self, table_name: str) -> str:
        alias = f"t{len(self.tables)}"
        self.tables[table_name] = alias
        return alias

    def table_alias(self, table_name: str) -> str:
        if table_name not in self.tables:
            raise Exception(f"unknown table {table_name}")
        return self.tables[table_name]

    def insert_param(self, value: Any) -> str:
        alias = f":var{len(self.params)}"
        self.params[alias] = value
        return alias
