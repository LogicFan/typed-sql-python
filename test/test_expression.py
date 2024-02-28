from typed_sql.data.expression import Expression
from typed_sql.query.as_query import QueryStr
from typed_sql.query.context import QueryContext
import unittest

ctx = QueryContext()
e1 = Expression[int](lambda _: QueryStr("e1"))
e2 = Expression[int](lambda _: QueryStr("e2"))
e3 = Expression[float](lambda _: QueryStr("e3"))
e4 = Expression[float](lambda _: QueryStr("e4"))
e5 = Expression[str](lambda _: QueryStr("e5"))


class ExpressionText(unittest.TestCase):

    def test_single(self):
        self.assertEqual(e1._query(ctx), "e1")
        self.assertEqual(e3._query(ctx), "e3")
        self.assertEqual(e5._query(ctx), "e5")

    def test_comparison(self):
        self.assertEqual((e1 < e2)._query(ctx), "(e1) < (e2)")
        self.assertEqual((e2 > e3)._query(ctx), "(e2) > (e3)")
        self.assertEqual((e3 == e4)._query(ctx), "(e3) = (e4)")
        self.assertEqual((e4 != e5)._query(ctx), "(e4) != (e5)")
        self.assertEqual((e5 <= e1)._query(ctx), "(e5) <= (e1)")
        self.assertEqual((e1 >= e2)._query(ctx), "(e1) >= (e2)")
