from typing_extensions import List, Any, NewType
from dataclasses import dataclass
from .context import QueryContext

QueryStr = NewType("QueryStr", str)


class AsQuery:
    def _query(self, ctx: QueryContext) -> QueryStr:
        raise NotImplementedError()
