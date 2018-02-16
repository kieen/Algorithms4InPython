import unittest

from QuickFindUF import QuickFindUF

class QuickFindUFTest(unittest.TestCase):
    def test(self):
        uf= QuickFindUF(9)
        print(uf.id)
        uf.union(4, 3)
        uf.union(3, 8)
        uf.union(6, 5)
        uf.union(9, 4)
        uf.union(2, 1)
        self.assertFalse(uf.conncected(0, 7))
#         print(uf.id)
#         print(uf.id[8])
#         print(uf.id[9])
        self.assertTrue(uf.conncected(8, 9))
        uf.union(5, 0)
        uf.union(7, 2)
        uf.union(6, 1)
        uf.union(1, 0)
        self.assertTrue(uf.conncected(0, 7))
