"""
A test suite for our Character class
"""
import unittest
from char_sol import *


class TestCharMethods(unittest.TestCase):

    def test_init(self):
        c = Char('c')
        assert isinstance(c, Char)
    
    def test_bad_init(self):
        with self.assertRaises(Exception):
            c = Char('--')

    def test_str(self):
        c = Char('c')
        assert str(c) == 'c'

    def test_repr(self):
        c = Char('c')
        x = Char('x')
        [c, x]

    def test_add(self):
        c = Char('c')
        x = Char('x')
        assert c + x == 'cx'
        assert type(c + x) == str

    def test_eq(self):
        b = Char('b')
        c = 'b'
        assert b == c

    def test_gt(self):
        c = Char('c')
        x = Char('x')
        assert (c > x) == False
        assert (x > c) == True

    def test_lt(self):
        c = Char('c')
        x = Char('x')
        assert (c < x) == True
        assert (x < c) == False

    def test_len(self):
        c = Char('c')
        x = Char('x')
        assert len(c) and len(x) == 1
        assert len(c) - len(x) == 0

    def test_blank(self):
        b = Char(' ')
        assert len(b) == 1

    def test_caps(self):
        c = Char('c')
        x = c.capitalize()
        assert x == 'C'

    def test_num(self):
        x = Char('1')
        assert x.isnumeric()


if __name__ == '__main__':
    unittest.main()