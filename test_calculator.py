import unittest
from calculator import *

class TestCalculator(unittest.TestCase):
    ######### Partner 2
    def test_add(self): # 3 assertions
        self.assertEqual(add(2, 10), 12)
        self.assertEqual(add(-2, 4), 2)
        self.assertEqual(add(0, -2), -2)

    def test_subtract(self): # 3 assertions
    #     fill in code
    # ##########################
        self.assertEqual(sub(4, 2), 2)
        self.assertEqual(sub(5, 10), -5)
        self.assertEqual(sub(5, 0), 5)

    ######## Partner 1
    # def test_multiply(self): # 3 assertions
    #     fill in code

    # def test_divide(self): # 3 assertions
    #     fill in code
    # ##########################

    ######## Partner 2
    def test_divide_by_zero(self): # 1 assertion
    #     # call division function inside, example:
    #     # with self.assertRaises(<INSERT_ERROR_TYPE>):
    #     #     div(0, 5)
    #     fill in code
        with self.assertRaises(ZeroDivisionError):
            div(0,5)

    def test_logarithm(self): # 3 assertions
    #     fill in code
        self.assertAlmostEqual(log(10, 1000), 3.0)
        self.assertAlmostEqual(log(2, 8), 3.0)
        self.assertAlmostEqual(log(10, 100), 2)

    def test_log_invalid_base(self): # 1 assertion
    #     # use same technique from test_divide_by_zero
    #     fill in code
    # ##########################
        for bad_base in (-3,-1,1,0):
            with self.assertRaises(ValueError):
                log(bad_base, 10)
    
    ######## Partner 1
    def test_log_invalid_argument(self): # 1 assertion
        with self.assertRaises(ValueError):
            self.assertAlmostEqual(log(2,4), 2.0)
            self.assertAlmostEqual(log(0,8), 3.0)
            self.assertAlmostEqual(log(3,27), 3.0)
    #     # call log function inside, example:
    #     # with self.assertRaises(<INSERT_ERROR_TYPE>):
    #     #     logarithm(0, 5)
    #     fill in code

    def test_hypotenuse(self): # 3 assertions
        self.assertAlmostEqual(hypotenuse(9,12), 15.0)
        self.assertAlmostEqual(hypotenuse(5,12), 13.0)
        self.assertAlmostEqual(hypotenuse(4,3), 5.0)
    #     fill in code

    def test_sqrt(self): # 3 assertions
        self.assertEqual(square_root(4), 2.0)
        self.assertEqual(square_root(16), 4.0)
        self.assertEqual(square_root(25), 5.0)
    #     # Test for invalid argument, example:
    #     # with self.assertRaises(<INSERT_ERROR_TYPE>):
    #     #    square_root(NUM)
    #     # Test basic function
    #     fill in code

    def test_multiply(self): # 3 assertions
        self.assertEqual(mul(3,4), 12)
        self.assertEqual(mul(7,4), 28)
        self.assertEqual(mul(3,9), 27)
    #     # Test for invalid argument, example:
    #     # with self.assertRaises(<INSERT_ERROR_TYPE>):
    #     #    square_root(NUM)
    #     # Test basic function
    #     fill in code

    def test_divide(self): # 3 assertions

        # Test for invalid argument, example:
        # with self.assertRaises(<INSERT_ERROR_TYPE>):
        #    square_root(NUM)
        # Test basic function
        with self.assertRaises(ZeroDivisionError):
            self.assertAlmostEqual(div(2,5), 2.5)
            self.assertAlmostEqual(div(0,2), 2.0)
            self.assertAlmostEqual(div(5,25), 5)
    ##########################

# Do not touch this
if __name__ == "__main__":
    unittest.main()