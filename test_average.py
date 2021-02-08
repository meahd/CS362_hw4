import unittest
import average


class TestCase(unittest.TestCase):
#calcAverage
    def test1(self):
        self.assertEqual(average.IntInputValidationForElements("\nEnter 2 to test: "),2)
    def test2(self):
        self.assertEqual(average.floatInputValidation("Enter -2 to test: "),-2)
    def test3(self):
        self.assertEqual(average.average([2.0,2.0]),2.0)

    if __name__ == '__main__':
        unittest.main(verbosity=2)
