import unittest
from bitstuff import BitStuff

class TestBitStuff(unittest.TestCase):
    def test_max_val(self):
        b = '1111111111111111'
        sb = BitStuff.stuff(b)
        assert (len(sb) == 18 and sb == '111111011111101111')

    def test_min_val(self):
        b = '1000000000000000'
        assert BitStuff.stuff(b) == b

    def test_unstuff(self):
        b = '1111111100110011'
        sb =  BitStuff.stuff(b)
        assert BitStuff.unstuff(sb) == b
    
    def test_stuff(self):
        b = '0011111001111111'
        sb = BitStuff.stuff(b)
        assert (len(sb) == 17 and sb == '00111110011111101')

    def test_emp(self):
        assert BitStuff.stuff('') == ''
 



if __name__ == '__main__':
    unittest.main()