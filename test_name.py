import unittest
import name


class TestCase(unittest.TestCase):
#calcname
    def test1(self):
        self.assertEqual(name.generateFullName('David','Meah'),"David Meah")
    #def test2(self):
    #    self.assertEqual(name.floatInputValidation("Enter -2 to test: "),-2)
    #def test3(self):
    #    self.assertEqual(name.name([2.0,2.0]),2.0)

    if __name__ == '__main__':
        unittest.main(verbosity=2)
