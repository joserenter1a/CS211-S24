import unittest, time
from stack import Stack
from stack_sol import *


class TestStackReversal(unittest.TestCase):

    def test_stack_init_and_push(self):
        s = Stack()
        s.push(1)
        assert s.size() == 1

    def test_stack_pop(self):
        s = Stack()
        s.push(1)
        assert s.pop() == 1

    def test_reverse_same(self):
        inp = "1111"
        assert inp == reverse_string(inp)

    def test_reverse_empty(self):
        inp = ""
        assert inp == reverse_string(inp)

    def test_reverse_avg(self):
        inp = "101010"
        assert reverse_string(inp) == "010101"

    def test_reverse_time(self):
        inp = "1" * 50  # a thousand length str
        start = time.time()
        reverse_string(inp)
        end = time.time()
        assert (end - start) < .001  # should be easily less than 1 ms

    def test_loop(self):
        i = 500
        start = time.time()

        while i > 0:
            self.test_reverse_time()
            i -= 1
        end = time.time()
        assert (end - start) < 0.02 # less than 20 ms


        # encapsulated test case, calls another test case for more rigorous test of time

if __name__ == '__main__':
    unittest.main()