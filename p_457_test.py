

import unittest
from p_457_circular_array_loop import Solution


class Tests(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = Solution()

    def doAssert(self, inp, out):
        return self.assertEqual(self.solution.circularArrayLoop(inp), out)

    def test_ex1(self):
        inp = [2, -1, 1, 2, 2]
        out = True
        self.doAssert(inp, out)

    def test_ex2(self):
        inp = [-1, 2]
        out = False
        self.doAssert(inp, out)

    def test_ex3(self):
        inp = [-2, 1, -1, -2, -2]
        out = False
        self.doAssert(inp, out)

    def test_f1(self):
        self.doAssert([3, 1, 2], True)

    def test_f2(self):
        self.doAssert([2, 2, 2, 2, 2, 4, 7], False)
