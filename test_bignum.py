import unittest
import bignum

class BigNumTest(unittest.TestCase):
    def bignum_equal_to_int(self, num, i):
        i = bignum.numToBigNum(i)
        self.assertEqual(num, i)        

    def check_bignumAdd(self, n1, n2):
        bn1 = bignum.numToBigNum(n1)
        bn2 = bignum.numToBigNum(n2)
        result = bignum.bigAdd(bn1, bn2)

        self.bignum_equal_to_int(result, n1 + n2)

    def check_bignumMul(self, n1, n2):
        bn1 = bignum.numToBigNum(n1)
        bn2 = bignum.numToBigNum(n2)
        result = bignum.bigMul(bn1, bn2)

        self.bignum_equal_to_int(result, n1 * n2)

    def check_bignumSub(self, n1, n2):
        bn1 = bignum.numToBigNum(n1)
        bn2 = bignum.numToBigNum(n2)
        result = bignum.bigSub(bn1, bn2)

        if n1 < n2:
            self.assertEqual(result, [-1])
        else:
            self.bignum_equal_to_int(result, n1 - n2)

    def check_bignumDiv(self, n1, n2):
        bn1 = bignum.numToBigNum(n1)
        bn2 = bignum.numToBigNum(n2)
        result = bignum.bigDivMod(bn1, bn2)

        self.bignum_equal_to_int(result, n1 // n2)

    def check_bignumMod(self, n1, n2):
        bn1 = bignum.numToBigNum(n1)
        bn2 = bignum.numToBigNum(n2)
        result = bignum.bigDivMod(bn1, bn2, False)

        self.bignum_equal_to_int(result, n1 % n2)

    #           Tests           #

    def test_add_default(self):
        self.check_bignumAdd(123,123)

    def test_add_left(self):
        self.check_bignumAdd(12345,123)

    def test_add_right(self):
        self.check_bignumAdd(123,12345)

    def test_add_overflow(self):
        self.check_bignumAdd(9,1)

    def test_add_overflow_2(self):
        self.check_bignumAdd(99, 1)

    def test_add_zero(self):
        self.check_bignumAdd(0, 0)

    def test_add_zero_2(self):
        self.check_bignumAdd(12, 0)

    def test_add_large(self):
        self.check_bignumAdd(2**80, 2**80)


    def test_mul_default(self):
        self.check_bignumMul(123,123)

    def test_mul_zero(self):
        self.check_bignumMul(123,0)


    def test_sub_default(self):
        self.check_bignumSub(123,123)

    def test_sub_left(self):
        self.check_bignumSub(12345,123)
    
    def test_sub_right(self):
        self.check_bignumSub(123,12345)

    def test_sub_zero(self):
        self.check_bignumSub(123,0)

    def test_sub_leading_zero(self):
        self.check_bignumSub(120,30)

    def test_sub_carry(self):
        self.check_bignumSub(1003,5)

    def test_sub_slightly_larger(self):
        self.check_bignumSub(98,99)

    
    def test_div_default(self):
        self.check_bignumDiv(123,123)

    def test_div_left(self):
        self.check_bignumDiv(123,12)

    def test_div_right(self):
        self.check_bignumDiv(12,123) 

    def test_div_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            result = bignum.bigDivMod([1,2,3], [0])


    def test_mod_default(self):
        self.check_bignumMod(123,123)

    def test_mod_left(self):
        self.check_bignumMod(12345,123)

    def test_mod_right(self):
        self.check_bignumMod(123,12345)




