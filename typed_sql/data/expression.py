from __future__ import annotations
from typing_extensions import Generic, TypeVar, Callable, override, overload
from datetime import date, datetime, time
from ..query.as_query import AsQuery, QueryStr, QueryContext

T0 = TypeVar("T0")


class Expression(AsQuery, Generic[T0]):
    def __init__(self, q: Callable[[QueryContext], QueryStr]) -> None:
        super().__init__()
        self._q = q

    @override
    def _query(self, ctx: QueryContext) -> QueryStr:
        return self._q(ctx)

    """ Comparison """

    def __lt__(self, other: Expression) -> Expression[int]:
        def q(ctx: QueryContext) -> QueryStr:
            lhs = self._query(ctx=ctx)
            rhs = other._query(ctx=ctx)
            return QueryStr(f"({lhs}) < ({rhs})")

        return Expression[int](q=q)

    def __le__(self, other: Expression) -> Expression[int]:
        def q(ctx: QueryContext) -> QueryStr:
            lhs = self._query(ctx=ctx)
            rhs = other._query(ctx=ctx)
            return QueryStr(f"({lhs}) <= ({rhs})")

        return Expression[int](q=q)

    def __eq__(self, other: Expression) -> Expression[int]:
        def q(ctx: QueryContext) -> QueryStr:
            lhs = self._query(ctx=ctx)
            rhs = other._query(ctx=ctx)
            return QueryStr(f"({lhs}) = ({rhs})")

        return Expression[int](q=q)

    def __ne__(self, other: Expression) -> Expression[int]:
        def q(ctx: QueryContext) -> QueryStr:
            lhs = self._query(ctx=ctx)
            rhs = other._query(ctx=ctx)
            return QueryStr(f"({lhs}) != ({rhs})")

        return Expression[int](q=q)

    def __gt__(self, other: Expression) -> Expression[int]:
        def q(ctx: QueryContext) -> QueryStr:
            lhs = self._query(ctx=ctx)
            rhs = other._query(ctx=ctx)
            return QueryStr(f"({lhs}) > ({rhs})")

        return Expression[int](q=q)

    def __ge__(self, other: Expression) -> Expression[int]:
        def q(ctx: QueryContext) -> QueryStr:
            lhs = self._query(ctx=ctx)
            rhs = other._query(ctx=ctx)
            return QueryStr(f"({lhs}) >= ({rhs})")

        return Expression[int](q=q)

    """ Nullability """

    def IS_NULL(self) -> Expression[int]:
        def q(ctx: QueryContext) -> QueryStr:
            lhs = self._query(ctx=ctx)
            return QueryStr(f"({lhs}) IS NULL")

        return Expression[int](q=q)

    def IS_NOT_NULL(self) -> Expression[int]:
        def q(ctx: QueryContext) -> QueryStr:
            lhs = self._query(ctx=ctx)
            return QueryStr(f"({lhs}) IS NOT NULL")

        return Expression[int](q=q)

    """ Arithmetic """

    @overload
    def __add__(self: Expression[int], other: Expression[int]) -> Expression[int]:
        pass

    @overload
    def __add__(self: Expression[float], other: Expression[int]) -> Expression[float]:
        pass

    @overload
    def __add__(self: Expression[int], other: Expression[float]) -> Expression[float]:
        pass

    @overload
    def __add__(self: Expression[float], other: Expression[float]) -> Expression[float]:
        pass

    def __add__(self: Expression, other: Expression) -> Expression:
        def q(ctx: QueryContext) -> QueryStr:
            lhs = self._query(ctx=ctx)
            rhs = other._query(ctx=ctx)
            return QueryStr(f"({lhs}) + ({rhs})")

        return Expression(q=q)

    @overload
    def __sub__(self: Expression[int], other: Expression[int]) -> Expression[int]:
        pass

    @overload
    def __sub__(self: Expression[float], other: Expression[int]) -> Expression[float]:
        pass

    @overload
    def __sub__(self: Expression[int], other: Expression[float]) -> Expression[float]:
        pass

    @overload
    def __sub__(self: Expression[float], other: Expression[float]) -> Expression[float]:
        pass

    def __sub__(self: Expression, other: Expression) -> Expression:
        def q(ctx: QueryContext) -> QueryStr:
            lhs = self._query(ctx=ctx)
            rhs = other._query(ctx=ctx)
            return QueryStr(f"({lhs}) - ({rhs})")

        return Expression(q=q)

    @overload
    def __mul__(self: Expression[int], other: Expression[int]) -> Expression[int]:
        pass

    @overload
    def __mul__(self: Expression[float], other: Expression[int]) -> Expression[float]:
        pass

    @overload
    def __mul__(self: Expression[int], other: Expression[float]) -> Expression[float]:
        pass

    @overload
    def __mul__(self: Expression[float], other: Expression[float]) -> Expression[float]:
        pass

    def __mul__(self: Expression, other: Expression) -> Expression:
        def q(ctx: QueryContext) -> QueryStr:
            lhs = self._query(ctx=ctx)
            rhs = other._query(ctx=ctx)
            return QueryStr(f"({lhs}) * ({rhs})")

        return Expression(q=q)

    def __truediv__(self, other: Expression) -> Expression[float]:
        def q(ctx: QueryContext) -> QueryStr:
            lhs = self._query(ctx=ctx)
            rhs = other._query(ctx=ctx)
            return QueryStr(f"({lhs}) / ({rhs})")

        return Expression[float](q=q)

    def __floordiv__(self, other: Expression) -> Expression[int]:
        def q(ctx: QueryContext) -> QueryStr:
            lhs = self._query(ctx=ctx)
            rhs = other._query(ctx=ctx)
            return QueryStr(f"({lhs}) DIV ({rhs})")

        return Expression[int](q=q)
