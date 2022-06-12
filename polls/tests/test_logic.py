from unittest import TestCase

from polls.logic import operations, list, myfunc



class logictestcase(TestCase):
    def test_plus(self):
        result = operations(7, 12, '+')
        self.assertEqual(18, result)

    def test_minus(self):
        res = operations(6, 13, '-')
        self.assertEqual(-7, res)
    def test_multiply(self):
        res = operations(2,4,'*')
        self.assertEqual(8, res)

    def test_model(self):
        m = list(1)
        self.assertEqual(1, m)
    def testBasic(self):
        a = ['larry', 'curly', 'moe']
        self.assertEqual(myfunc(a, 0), 'larry')
        self.assertEqual(myfunc(a, 1), 'curly')